import random


class Distribution:

    sides = ["north", "south", "east", "west"]
    suits = ["spades", "hearts", "diamonds", "clubs"]

    def __init__(self) -> None:
        self.cards = {side: {suit: "" for suit in self.suits}
                      for side in self.sides}
        self.generatedSides = ""

    def putSuit(self, side, suit, cards):
        self.cards[side][suit] = cards

    def hasHand(self, side):
        return any(map(lambda suit:  len(suit) > 0, self.cards[side].values()))

    def isComplete(self):
        return all([self.hasHand(side) for side in self.sides])

    def getSideAsString(self, side):
        s = self.cards[side]
        return f"{s['spades']} {s['hearts']} {s['diamonds']} {s['clubs']}"

    def toFullString(self):
        return f"     ♠{self.cards['north']['spades']}\n     ♥{self.cards['north']['hearts']}\n     ♦{self.cards['north']['diamonds']}\n     ♣{self.cards['north']['clubs']}\n" + \
        f"♠{self.cards['west']['spades'].ljust(9)}♠{self.cards['east']['spades']}\n" + \
        f"♥{self.cards['west']['hearts'].ljust(9)}♥{self.cards['east']['hearts']}\n" + \
        f"♦{self.cards['west']['diamonds'].ljust(9)}♦{self.cards['east']['diamonds']}\n" + \
        f"♣{self.cards['west']['clubs'].ljust(9)}♣{self.cards['east']['clubs']}\n" + \
        f"     ♠{self.cards['south']['spades']}\n     ♥{self.cards['south']['hearts']}\n     ♦{self.cards['south']['diamonds']}\n     ♣{self.cards['south']['clubs']}\n"


    def generateRest(self):
        unusedCards = { suit: "AKQJT98765432" for suit in self.suits} 
        newsides = [ side for side in self.sides if not self.hasHand(side)]
        stack =  [ side for x in range(13) for side in newsides]
        random.shuffle(stack)
        
        for side, suits in self.cards.items():
            for suit, cards in suits.items():
                unusedCards[suit] = unusedCards[suit].translate({ord(i):None for i in cards})

        for suit, cards in unusedCards.items():
            for card in cards:
                self.cards[stack.pop()][suit] += card

        self.generatedSides = "".join([side[0].upper() for side in newsides])

