from model.year import Year
from model.lesson import Lesson


class ResultRepository:

    def __init__(self, db) -> None:
        self.db = db

    def put(self, lesson):
        self.db.execute(''' INSERT OR REPLACE INTO result_lesson (LessonName, Year, LessonNumber, ResultXml, SourceContent)
            VALUES (?, ?, ?, ?, ?)''', [lesson.name, lesson.year, lesson.number, lesson.xml, lesson.content])

    def get(self, year, number):
        data = self.db.fetchAll(''' SELECT Id, LessonName, ResultXml, SourceContent, UpdatedAt FROM result_lesson 
            WHERE LessonNumber = ? AND Year = ?
            LIMIT 1''', [number, year, ])[0]
        return self.__constructLessonFromData(data)

    def getAllYears(self):
        data = self.db.fetchAll(
            ''' SELECT Id, LessonNumber, Year, LessonName, ResultXml, SourceContent, UpdatedAt FROM result_lesson ORDER BY LessonNumber''')
        years = {}
        for row in data:
            year = row["Year"]
            if year not in years:
                years[year] = []
            years[year].append(self.__constructLessonFromData(row))

        return [Year(year, lessons) for year, lessons in years.items()]

    def getYear(self, year):
        data = self.db.fetchAll(''' SELECT Id, LessonNumber, Year, LessonName, ResultXml, SourceContent, UpdatedAt FROM result_lesson
        WHERE Year = ? ORDER BY LessonNumber''', [year])
        lessons = []
        for row in data:
            lessons.append(self.__constructLessonFromData(row))
        return Year(year, lessons)

    def __constructLessonFromData(self, data):
        return Lesson(data["Year"],
                data["LessonNumber"],
                data["LessonName"],
                id=data["Id"],
                text=data["SourceContent"],
                xml=data["ResultXml"],
                updatedAt=data["UpdatedAt"])
