class Year: 
    def __init__(self, year, lessons) -> None:
        self.year = year
        self.lessons = lessons

    def __repr__(self) -> str:
        return f"R{self.year}: { len(self.lessons)} lekcí"