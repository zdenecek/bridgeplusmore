from model.lesson import Lesson
from model.year import Year
import simplejson as json


class SourceRepository:

    def __init__(self, db):
        self.db = db

    def getData(self):
        
        years = {}

        lesson_data = self.db.all('SELECT year, LectionNumber, name, fullText FROM Lections ORDER BY year, lectionNumber')

        for l in lesson_data:
            lesson = Lesson(l['Year'], l['LectionNumber'], l['Name'],  json.loads(l['fullText']))
            if lesson.year not in years:
                years[lesson.year] = []
            
            years[lesson.year].append(lesson)

        return [Year(number, lessons) for (number, lessons) in years.items()]

