from model.distribution import Distribution
import xml.etree.ElementTree as et
import random

class XmlParser:
    def __init__(self) -> None:
        pass

    def openXml(self, xmlText):
        return et.fromstring(xmlText)

    def parseLesson(self, lesson):

        lessonObject = self.openXml(lesson.xml)
        bmData = {}
        bmData["Year"] = lesson.year
        bmData["LessonNumber"] = lesson.number
        bmData["Name"] = lesson.__repr__()
        bmData["LessonId"] = lesson.id

        preText = ""
        postText = ""
        remainingText = ""
        start = True

        examples = []

        for node in lessonObject:
            if(node.tag == "p" and start):
                preText += f"<p>{node.text.strip()}</p>"
            elif(node.tag == "p"):
                postText += f"<p>{node.text.strip()}</p>"
            elif(node.tag == "example"):
                examples.append(node)
                start = False
                if(postText != ""):
                    remainingText += "..." + postText
                    postText = ""

        bmData["PostText"] = postText
        bmData["PreText"] = preText
        bmData["UnusedText"] = remainingText

        examplesData = []

        for example in examples:
            examplesData.append(self.parseExample(lesson, example))

        return {'lessonData': bmData, 'examplesData': examplesData}

    def parseExample(self, lesson, exampleObject: et.Element):

        bmData = {}

        bmData['ExampleNumber'] = exampleObject.attrib['number']
        bmData["BoardName"] = \
            f"R{lesson.year}L{str(lesson.number).zfill(2)}P{str(exampleObject.attrib['number']).zfill(2)} - {lesson.name}"

        auctionObject = exampleObject.find("auction")
        auction = self.parseAuction(auctionObject) if(auctionObject) else {}
        bmData["BidStr"] = auction.get("BidString", "")
        bmData["Vuln"] = auction.get("Vuln", "")
        bmData["FinalBid"] = auction.get("FinalBid", "")


        contract = exampleObject.find("contract")
        if contract != None :
            bmData["FinalBid"] = contract.attrib['value']

        bmData["SuggestedLeadCard"] = ""
        
        lead = exampleObject.find("leadcard")
        if lead != None:
            bmData["SuggestedLeadCard"] = lead.attrib["value"]

        bmData["CommentNorth"] = ""
        bmData["CommentSouth"] = ""
        bmData["CommentEast"] = ""
        bmData["CommentWest"] = ""

        bmData["CommentPlay"] = ""
        bmData["CommentBidding"] = ""
        bmData["CommentBoard"] = ""
        bmData["CommentLead"] = ""
        bmData["CommentPostMortem"] = ""

        bmData["UnusedEndText"] = ""

        # 0 before first dist, 1 between full dist, 2 after NSEW, 3 after NSEW and some other
        state = 0
        currText = ""
        dist = Distribution()

        for node in exampleObject:
            if "ignore" in node.attrib:
                continue
            if(node.tag == "distribution"):
                
                for hand in node.findall("hand"):
                    side = hand.attrib["position"]
                    if(side in ["north", "south", "east", "west"]
                            and not dist.hasHand(side)):
                        
                        for suit in ["spades", "hearts", "diamonds", "clubs"]:
                            dist.putSuit(side, suit, hand.find(suit).text.strip())

                        if state == 0:
                            # text before any distribution
                            bmData["CommentBoard"] = currText
                            currText = ""
                            state = 1
                        if dist.isComplete():
                            if state == 1:
                                bmData["CommentPlay"] = currText
                                currText = ""
                            state = 2
                    else:
                        if state == 2:
                            bmData["CommentPostMortem"] = currText
                            currText = ""
                            state = 3
            elif(node.tag == "p"):
                currText += f"<p>{node.text.strip()}</p>\n"

        bmData["DistAsText"] = dist.toFullString()


        if state == 3:
            bmData["UnusedEndText"] = currText
        else:
            bmData["CommentPostMortem"] = currText

        if state == 1:
            dist.generateRest()


        bmData["DistNorth"] = dist.getSideAsString("north")
        bmData["DistEast"] = dist.getSideAsString("east")
        bmData["DistSouth"] = dist.getSideAsString("south")
        bmData["DistWest"] = dist.getSideAsString("west")

        bmData["GeneratedHands"] = dist.generatedSides

        bmData["DistributionPlayStr"] = ""
        bmData["LeaderToEachTrick"] = ""
        bmData["SuggestedTricks"] = ""
        bmData["TeacherTags"] = ""
        bmData["WinnerOfTrick"] = ""


        return bmData

    def parseAuction(self, auctionObject: et.Element):
        start = {
            "west": 0,
            "north": 1,
            "east": 2,
            "south": 3, }
        side = {num: side[0].upper() for side, num in start}

        def convertBid(bid):
            return "P" if bid == "pass" else "D" if bid == "X" else "R" if bid == "XX" else bid

        currentContract = "P"
        bidStr = "-" * start.get(auctionObject.attrib["dealer"], 1)
        doubled = False
        redoubled = False
        currentSide = start.get(auctionObject.attrib["dealer"], 1)

        for bid in auctionObject.findall("bid"):
            b = convertBid(bid.attrib['value'])
            bidStr += b + "-"
            if(b == "P"):
                pass
            elif(b == "D"):
                doubled = True
            elif(b == "R"):
                doubled = False
                redoubled = True
            else:
                doubled = redoubled = False
                currentContract = b
            currentSide += 1

        currentSide = currentSide % 4
        bidStr = bidStr[:-1]

        finalBid = currentContract + \
            side.get(currentSide) + \
            ("D" if doubled else "R" if redoubled else "")

        vuln = auctionObject.attrib["vul"]

        return {"FinalBid": finalBid, "BidString": bidStr, "Vuln": vuln}


