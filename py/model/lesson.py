class Lesson:
    def __init__(self, year, number, name, id = None, text = None, xml = None, updatedAt = None) -> None:
        self.year = year
        self.number = number
        self.name = name
        self.id = id
        self.content = text
        self.xml = xml
        self.updatedAt = updatedAt

    def setContentFromParagraphs(self, paragraphs):

        self.content = "\n\n".join(paragraphs)

    def paragraphCount(self):
        return self.content.split("\n\n")

    def __repr__(self) -> str:
        return f"R{self.year}L{self.number}: {self.name}"