class Lesson:
    def __init__(self, year, number, name, content) -> None:
        self.year = year
        self.number = number
        self.name = name
        self.content = content

    def __repr__(self) -> str:
        return f"R{self.year}L{self.number}: {self.name}"