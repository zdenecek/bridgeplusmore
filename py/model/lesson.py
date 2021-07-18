class Lesson:
    def __init__(self, year, number, name, paragraphs = None, sourceContent = None, resultXml = None) -> None:
        self.year = year
        self.number = number
        self.name = name
        self.content = sourceContent or "\n\n".join(paragraphs)
        self.xml = resultXml

    def paragraphCount(self):
        return self.content.split("\n\n")

    def __repr__(self) -> str:
        return f"R{self.year}L{self.number}: {self.name}"