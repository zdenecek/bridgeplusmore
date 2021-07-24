
from os import close
from gui.xmlTreeview import XmlTreeview
import tkinter as tk
from tkinter import PhotoImage, StringVar, ttk
from tkinter import scrolledtext
from tkinter import simpledialog, messagebox
import re


class SourceManipulationTab: 

    def __init__(self, resultRepository, sourcePanel):
        self.state = {}
        self.sourceTab = sourcePanel
        self.resultRepository = resultRepository

 
    def attach(self, root):
        self.root = root
        self.configureComponents()

    def configureComponents(self):

        # options | source
        # srcs  | db | xml

        rows = [tk.Frame(self.root) for i in range(3)]
        for row in rows:
            row.pack()
        
        self.sourceFrame = tk.Frame(rows[0])
        self.optionsFrame = tk.Frame(rows[0])

        self.sourcesFrame = tk.Frame(rows[2])
        self.dbFrame = XmlTreeview(self.resultRepository, self.openXml, self.saveXml, rows[2])
        self.dbFrame.grid(row=1, column=2, padx=10)
        
        self.resultXmlFrame = tk.Frame(rows[2])

    

        def configSource():
            fr = self.sourceFrame
            fr.grid(column=2, row=1)  

            fr.topPane = tk.Frame(fr)
            fr.topPane.pack()   

            fr.text = scrolledtext.ScrolledText(fr, width=150, undo=True)
            fr.text.pack()     

            fr.topPane.label = tk.Label(fr.topPane, text="Zdrojový text")
            fr.topPane.label.pack(side='left')

            fr.topPane.label = tk.Button(fr.topPane, text="Zpět", command=fr.text.edit_undo)
            fr.topPane.label.pack(side='left')            

        configSource()


        def configOptions():
            fr = self.optionsFrame
            fr.grid(column=1, row=1)

            fr.label = tk.Label(fr, text="Manipulace")
            fr.label.grid(columnspan=10)


            fr.endExample = tk.Button(fr, text="Nový příklad", command=self.startExample)
            fr.endExample.grid(row=3,columnspan=2)
            fr.startExample = tk.Button(fr, text="Ukončit příklad", command=self.endExample)
            fr.startExample.grid(row=3, column=2,columnspan=2)
            fr.startExample = tk.Button(fr, text="Začít lekci", command=self.startLesson)
            fr.startExample.grid(row=4,columnspan=2)
            fr.startExample = tk.Button(fr, text="Ukončit lekci", command=self.endLesson)
            fr.startExample.grid(row=4,column=2,columnspan=2)

            fr.basicText = tk.Button(fr, text="Text", command=self.convertText)
            fr.basicText.grid(row=12)
            fr.literature = tk.Button(fr, text="Literatura", command=self.convertLiterature)
            fr.literature.grid(row=12, column=1)

            ####

            fr.label = tk.Label(fr, text="Nástroje")
            fr.label.grid(row=14,columnspan=10)

            fr.twoColumns = tk.Button(fr, text="Dva sloupce", command=self.splitColumns)
            fr.twoColumns.grid(row=15,columnspan=2)
            fr.moreColumns = tk.Button(fr, text="Více sloupců", command=self.splitMoreColumns)
            fr.moreColumns.grid(row=15, column=2,columnspan=2)

            ###########

            fr.distlabel = tk.Label(fr, text="Rozdání")
            fr.distlabel.grid(row=21,columnspan=10)
            
            fr.nsew1image = PhotoImage(file = r"C:\Users\zdnek\src\bridgepuppet\img\pybuttons\NSEWOneTop.png")
            fr.nsew1 = tk.Button(fr, command=self.nsewOneTop, image=fr.nsew1image)
            fr.nsew1.grid(row=22)

            fr.nsew2image = PhotoImage(file = r"C:\Users\zdnek\src\bridgepuppet\img\pybuttons\NSEWTwoTop.png")
            fr.nsew2 = tk.Button(fr, image=fr.nsew2image, command=self.nsewTwoTop)
            fr.nsew2.grid(row=22, column=1)

            fr.nsew3image = PhotoImage(file = r"C:\Users\zdnek\src\bridgepuppet\img\pybuttons\NSEWOneBoth.png")
            fr.nsew3 = tk.Button(fr, image=fr.nsew3image, command=self.nsewOneBoth)
            fr.nsew3.grid(row=22, column=2)

            fr.ewimage = PhotoImage(file = r"C:\Users\zdnek\src\bridgepuppet\img\pybuttons\EW.png")
            fr.ew = tk.Button(fr, image=fr.ewimage, command=self.ew)
            fr.ew.grid(row=22, column=3)

            fr.onedistimage = PhotoImage(file = r"C:\Users\zdnek\src\bridgepuppet\img\pybuttons\OneDistribution.png")
            fr.onedist = tk.Button(fr,  image=fr.onedistimage, command=self.oneDistribution)
            fr.onedist.grid(row=23)

            fr.onesuitimage = PhotoImage(file = r"C:\Users\zdnek\src\bridgepuppet\img\pybuttons\OneSuit.png")
            fr.onesuit = tk.Button(fr, image=fr.onesuitimage, command=self.oneSuit)
            fr.onesuit.grid(row=23, column=1)

            fr.suitcombimage = PhotoImage(file = r"C:\Users\zdnek\src\bridgepuppet\img\pybuttons\SuitCombination.png")
            fr.suitcomb = tk.Button(fr, image=fr.suitcombimage, command=self.suitCombination)
            fr.suitcomb.grid(row=23, column=2)

            fr.nsimage = PhotoImage(file = r"C:\Users\zdnek\src\bridgepuppet\img\pybuttons\NS.png")
            fr.ns = tk.Button(fr, image=fr.nsimage, command=self.ns)
            fr.ns.grid(row=23, column=3)

            fr.nsewsquareimage = PhotoImage(file = r"C:\Users\zdnek\src\bridgepuppet\img\pybuttons\NSEWSquare.png")
            fr.nsewsquare = tk.Button(fr, image=fr.nsewsquareimage, command=self.NSEWSquare)
            fr.nsewsquare.grid(row=24, column=0)

            fr.nshorizontalimage = PhotoImage(file = r"C:\Users\zdnek\src\bridgepuppet\img\pybuttons\NSHorizontal.png")
            fr.nshorizontal = tk.Button(fr, image=fr.nshorizontalimage, command=self.NSHorizontal)
            fr.nshorizontal.grid(row=24, column=1)

            fr.bidlabel = tk.Label(fr, text="Dražba a výnos")
            fr.bidlabel.grid(row=31,columnspan=10)

            fr.bidPair = tk.Button(fr, text="Dražba páru", command=lambda: self.parseBidding(True))
            fr.bidPair.grid(row=32,columnspan=2)
            fr.bidAll = tk.Button(fr, text="Dražba NSEW",  command=lambda: self.parseBidding(False))
            fr.bidAll.grid(row=32, column=2,columnspan=2)
            
            fr.finalContract = tk.Button(fr, text="Závazek", command=self.contract)
            fr.finalContract.grid(row=33,columnspan=2)
            fr.lead = tk.Button(fr, text="Výnos",  command=self.leadCard)
            fr.lead.grid(row=33, column=2,columnspan=2)

            fr.biddingAnswer = tk.Button(fr, text="Řešení dražby\n(hláška místo ?)", command=self.biddingAnswer)
            fr.biddingAnswer.grid(row=34,columnspan=2)

        configOptions()
        

        def configSources():
            fr = self.sourcesFrame
            fr.grid(row=1, column=1, padx=10)

            self.lessonLabel = StringVar(value="Lekce")
            fr.lessonLabel = tk.Label(fr, textvariable=self.lessonLabel)
            fr.lessonLabel.pack()

            fr.label = tk.Label(fr, text="Zdroje z .docx")
            fr.label.pack()

            fr.treeview = ttk.Treeview(fr)
            fr.treeview.column("#0", width=350)
            fr.treeview.heading("#0", text="Objekt")
            fr.treeview.pack()

            fr.loadButton = tk.Button(fr, command=self.loadSources, text="Zobrazit načtené")
            fr.loadButton.pack(side="left")
            fr.openSourceButton = tk.Button(fr, command=self.openSource, text="Vybrat")
            fr.openSourceButton.pack(side="left")



        configSources()

        def configResultXml():
            fr = self.resultXmlFrame
            fr.grid(row=1, column=3, padx=10)

            fr.topPane = tk.Frame(fr,)
            fr.topPane.pack()   

            fr.text = scrolledtext.ScrolledText(fr, height=20, undo=True)
            fr.text.pack()     

            fr.topPane.label = tk.Label(fr.topPane, text="Výsledné xml")
            fr.topPane.label.pack(side='left')

            fr.topPane.label = tk.Button(fr.topPane, text="Zpět", command=fr.text.edit_undo)
            fr.topPane.label.pack(side='left')


        
        configResultXml()



    ### helper methods
    def addXml(self, tag, attributes = None, content = None, pair = True, close = False): 
        attributeText = (" " + " ".join([f"{name}=\"{val}\"" for name, val in attributes.items()])) if attributes else ""

        self.resultXmlFrame.text.insert("end", 
             "<" +  ("/" if close else "") + tag +  attributeText+ ("/" if not pair else "") + ">\n" + ((content + "\n") if content else ""))
        self.resultXmlFrame.text.see("end")

    def selectedSourceText(self):
        return self.sourceFrame.text.selection_get()
    
    def loadSources(self):
        years = self.sourceTab.currentData.values()
        self.sourcesFrame.data = {}
        self.sourcesFrame.treeview.delete(*self.sourcesFrame.treeview.get_children())
        for year in years:
            self.sourcesFrame.treeview.insert('', 'end', iid=year.year, text=str(year))
        
        for year in years:
            for lesson in year.lessons:
                id = self.sourcesFrame.treeview.insert(year.year, 'end', text=str(lesson), values=(len(lesson.content)))
                self.sourcesFrame.data[id] = lesson

    def openSource(self): 
        self.state = {}

        selectedId = self.sourcesFrame.treeview.selection()[0]
        self.setLesson(self.sourcesFrame.data[selectedId])

        self.sourceFrame.text.delete('1.0', 'end')
        self.sourceFrame.text.insert('1.0', self.lesson.content)

        
    def openXml(self):
        self.state = {}
        self.setLesson(self.dbFrame.getSelectedLesson())

        self.resultXmlFrame.text.delete('1.0', 'end')
        self.resultXmlFrame.text.insert('1.0', self.lesson.xml)
        
    def saveXml(self):
        self.lesson.xml = self.resultXmlFrame.text.get('1.0', 'end')
        self.resultRepository.put(self.lesson)

    def setLesson(self, lesson):
        self.lesson = lesson
        self.lessonLabel.set( lesson.__repr__())


    ######################################### MANIPULATIONS

    def startLesson(self):
        # self.resultXmlFrame.text.delete('1.0', 'end')
        self.resultXmlFrame.text.insert("end", '<?xml version="1.0" encoding="UTF-8"?>\n')
        self.addXml(tag="lesson", attributes={"year": self.lesson.year, "title": self.lesson.name,"number": self.lesson.number })

    def endLesson(self):
        self.addXml(tag="lesson", close=True)


    def startExample(self):
        self.state["exampleNumber"] = 1 if "exampleNumber" not in self.state else (self.state["exampleNumber"]  + 1)
        self.addXml(tag="example", attributes={"number": self.state["exampleNumber"]})

    def endExample(self):
        self.addXml(tag="example", close=True)

    ### Convert actions

    def convertLiterature(self):
        text = self.selectedSourceText()    
        text = re.sub("literatura:*\s", "", text , flags=re.IGNORECASE)
        text = re.sub("\t+", "\t", text)
        lines = [line.strip() for line in text.split("\n")]
        lines = [line for line in lines if len(line) > 0]

        self.addXml("literature")
        for line in lines:
            self.addXml("li", content=line)
            self.addXml("li", close=True)
        self.addXml("literature", close=True)
            

    def convertText(self):
        text = self.selectedSourceText()
        text = re.sub("\n+", "\n", text)
        text = re.sub("\t+", " ", text)
        text = re.sub(" +", " ", text)
        
        for para in [p for p in text.split("\n") if len(p) > 0]:
            self.addXml("p", content=para.strip())
            self.addXml("p", close=True)

    def evalSeparator(self, sep):
        if("\|" in sep):
            print("Yes")
            return 1000
        elif("\t" in sep):
            return len([char for char in sep if char == "\t"])
        else:
            return len([char for char in sep if char == " "])      

    def splitMoreColumns(self):
        answer = simpledialog.askinteger('Zadej počet sloupců', 'Zadej počet sloupců')
        return self.splitColumns(answer)

    def splitColumns(self, cols = 2):
        text = self.sourceFrame.text.selection_get()
        lines = [line.strip() for line in text.split("\n")]
        columns = []
        for c in range(cols):   # comprehension doesnt work ??
            columns.append([]) 
        
        for line in lines:
            remainingText = line
            for col in range(cols-1):
                possibleSeparators = re.findall(r"\||\t+| +", remainingText)
                possibleSeparators.sort(key=self.evalSeparator)
                try:
                    separator = possibleSeparators[0]
                    index = remainingText.index(separator)
                    
                    ctext = remainingText[:index].strip()
                    remainingText = remainingText[index + len(separator):]

                    columns[col].append(ctext)

                except IndexError:
                    columns[col].append("")
            columns[cols-1].append(remainingText)

        newText = "\n\n".join(["\n".join([line for line in column]) for column in columns])
        
        start = self.sourceFrame.text.tag_ranges(tk.SEL)[0]
        self.sourceFrame.text.delete(tk.SEL_FIRST, tk.SEL_LAST)
        self.sourceFrame.text.insert(start, newText)
        

    # distribution

    def getSelectedAsDistributionLines(self):
        text = re.sub("10", "T", self.selectedSourceText())
        lines = re.sub("[^\s23456789TJQKAXx-]", "", text, flags=re.IGNORECASE).split("\n")
        return [re.sub("\s+", "\t", str.strip()).split("\t") for str in lines if len(str) > 0]
      
    def parseDistribution(self, format, lines):

        data = {side:{ suit: "" for suit in range(4)} for side in ['N', 'S', 'E', 'W', 'H', "D"]}
        counters = {side: 0 for side in ['N', 'S', 'E', 'W', 'H', 'D']}

        lineFormats = format.split(" ")
        for lineFormat, line in zip(lineFormats, lines):
            for index in range(len(lineFormat)):
                side = lineFormat[index]
                data[side][counters[side]] = line[index]
                counters[side] += 1

        self.addDistributionXml(data)

    def addDistributionXml(self, data):
        transformSide = {
            "N": "north",
            "S": "south",
            "E": "east",
            "W": "west",
            "D": "dummy",
            "H": "hand",
        }
        transformSuit = ['spades', 'hearts', 'diamonds', 'clubs']

        self.addXml("distribution")
        for side,suits in data.items():
            if(not any([len(cards) for cards in suits.values()])):
                continue
            else:
                self.addXml("hand", attributes={"position": transformSide.get(side)})
                for suit, cards in suits.items():
                    if bool(cards):
                        self.addXml(transformSuit[suit], content=cards)
                        self.addXml(transformSuit[suit], close=True)
                self.addXml("hand", close=True)
        self.addXml("distribution", close=True)   
    #

    def nsewOneTop(self):
        self.parseDistribution( "N N N WNE WE WSE WSE S S", self.getSelectedAsDistributionLines())

    def nsewOneBoth(self):
        self.parseDistribution( "N N N WNE WE WE WSE S S S", self.getSelectedAsDistributionLines())

    def nsewTwoTop(self):
        self.parseDistribution( "N N WNE WNE WE WSE S S S", self.getSelectedAsDistributionLines())

    def ns(self):
        self.parseDistribution( "N N N N S S S S", self.getSelectedAsDistributionLines())

    def ew(self):
        self.parseDistribution( "WE WE WE WE", self.getSelectedAsDistributionLines())

    def oneDistribution(self):
        self.parseDistribution( "H H H H", self.getSelectedAsDistributionLines())

    def oneSuit(self):
        self.parseDistribution( "H", self.getSelectedAsDistributionLines())

    def suitCombination(self):
        self.parseDistribution( "D H", self.getSelectedAsDistributionLines())

    def NSEWSquare(self):
        self.parseDistribution( "NNNN WE WE WE WE SSSS", self.getSelectedAsDistributionLines())
    
    def NSHorizontal(self):
        self.parseDistribution( "NNNN SSSS", self.getSelectedAsDistributionLines())

    ### bidding

    transformBid = {"t": "c", "k": "d", "s": "H", "p": "S", "b": "NT", "n": "NT",
                     "♣": "c", "♦": "d", "♥": "H", "♠": "S", "ʘ": "NT"}


    def parseBid(self, text):
        if("pas" in text):
            return "pass"
        elif("rekontra" in text):
            return "XX"
        elif("kontra" in text):
            return "X"
        else:
            bidtext = text.strip()[:2].lower()
            print("bid:" + bidtext)

            if(bidtext[0].isalnum() and bidtext[1] in self.transformBid):
                return bidtext[0] + self.transformBid[bidtext[1]]
            else:
                return "?"

    def parseBidding(self, onlyPairBidding = False):
        text = self.selectedSourceText()
        lines = [line for line in text.split('\n') if len(line) > 0]
        auction = []
        for line in lines:
            bids = line.strip().split('-') if onlyPairBidding else re.sub("\t+", "\t", line.strip()).split('\t')
            for bid in bids:
                auction.append(self.parseBid(bid))
        
        self.addXml("auction", attributes= {"onesided": "true"} if onlyPairBidding else {"dealer": "", "vul":""})
        for bid in auction:
            self.addXml("bid", {"value": bid}, pair=False)
        self.addXml("auction", close=True)

    transformSuit = {"t": "c", "k": "d", "s": "H", "p": "S",
                    "♣": "c", "♦": "d", "♥": "H", "♠": "S"}

    def leadCard(self):
        originalText = re.sub("výnos:*", "", self.selectedSourceText(), flags= re.IGNORECASE)
        text = re.sub("10", "T", originalText)
        match = re.search("[AKQJT98765432]", text)
        if(match.start() != 0 and text[match.start() -1] in self.transformSuit):
            suitchar = self.transformSuit[text[match.start() -1]]
        elif(match.end() < len(text) and text[match.end() ] in self.transformSuit):
            suitchar = self.transformSuit[text[match.end()]]
        elif(match.end() + 1 < len(text) and text[match.end()  +1] in self.transformSuit):
            suitchar = self.transformSuit[text[match.end() + 1]]
        else:
            suitchar = "?"
        card = match.group() + suitchar
        self.addXml("leadcard", {"value": card}, content=originalText)
        self.addXml("leadcard", close=True)

    def contract(self):
        text = re.sub("závazek:*", "", self.selectedSourceText(), flags= re.IGNORECASE).lower()
        match = re.match("[1-7]", text)
        if(match.end() < len(text) and text[match.end()  + 0] in self.transformBid):
            suitchar = self.transformBid[text[match.end() + 0]]
        elif(match.end() + 1 < len(text) and text[match.end()  + 1] in self.transformBid):
            suitchar = self.transformBid[text[match.end() + 1]]
        else:
            suitchar = "?"
        self.addXml("contract", {"value": match.group() + suitchar + "S"}, pair=False)


    def biddingAnswer(self):
        text = re.sub("odpověď:*|řešení:*", "", self.selectedSourceText(), flags= re.IGNORECASE).lower()
        match = re.match("[1-7]", text)
        if(match.end() < len(text) and text[match.end()  + 0] in self.transformBid):
            suitchar = self.transformBid[text[match.end() + 0]]
        elif(match.end() + 1 < len(text) and text[match.end()  + 1] in self.transformBid):
            suitchar = self.transformBid[text[match.end() + 1]]
        else:
            suitchar = "?"
        self.addXml("bidding-solution", {"value": match.group() + suitchar}, pair=False)