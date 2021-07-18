from model.year import Year
from model.lesson import Lesson


class ResultRepository:
    
    def __init__(self, db) -> None:
        self.db = db

    def put(self, lesson):
        self.db.execute(''' INSERT OR REPLACE INTO result_lesson (LessonName, Year, LessonNumber, ResultXml, SourceContent)
            VALUES (?, ?, ?, ?, ?)''', [lesson.name, lesson.year, lesson.number, lesson.xml, lesson.content])

    def get(self, year, number):
        data = self.db.fetchAll(''' SELECT LessonName, ResultXml, SourceContent, UpdatedAt FROM result_lesson 
            WHERE LessonNumber = ? AND Year = ?
            LIMIT 1''', 
            [ number, year, ])[0]
        lesson = Lesson(year, number, data["LessonName"], sourceContent = data["SourceContent"], resultXml=data["ResultXml"])
        lesson.updatedAt = data["UpdatedAt"]
        return lesson

    def getAllYears(self):
        data = self.db.fetchAll(''' SELECT LessonNumber, Year, LessonName, ResultXml, SourceContent, UpdatedAt FROM result_lesson ORDER BY LessonNumber''')
        years = {}
        for row in data:
            year = row["Year"]
            if year not in years:
                years[year] = []
            lesson = Lesson(year, row["LessonNumber"], row["LessonName"], sourceContent=row["SourceContent"], resultXml=row["ResultXml"])
            lesson.updatedAt = row["UpdatedAt"]
            years[year].append(lesson)

        return [Year(year, lessons) for year, lessons in years.items()]