from typing import Dict, List
from model.lesson import Lesson
from model.year import Year
import simplejson as json
import db.schema as schema
import itertools


class BmRepository:

    def __init__(self, db):
        self.db = db

    def storeLesson(self, lessonData: Dict, examplesData: List):
        sql = f'''INSERT OR REPLACE INTO bm_structure ({', '.join(lessonData.keys())})
                VALUES ({ ", ".join(itertools.repeat("?", len(lessonData)))})'''
        params = list(lessonData.values())
        id = self.db.execute(sql, params).lastrowid

        for example in examplesData:
            example["StructureRowId"] = id
            sql = f'''INSERT OR REPLACE INTO bm_board ({', '.join(example.keys())})
                VALUES ({ ", ".join(itertools.repeat("?", len(example)))})'''
            params = list(example.values())
            self.db.execute(sql, params)
            



