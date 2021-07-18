from model.lesson import Lesson
from model.year import Year
import simplejson as json
import db.schema as schema


class SourceRepository:

    def __init__(self, db):
        self.db = db

    def putBoard(self, data):
        sql = f'''INSERT OR REPLACE INTO boards ({','.join(schema.boards_cols)})
                VALUES ({'?,'*23 + '?'})'''
        params = [data.get('key') for key in schema.boards_cols]
        self.cursor.execute(sql, params)

    def putSet(self, data):
        sql = f'''INSERT OR REPLACE INTO sets ({','.join(schema.sets_cols)})
                VALUES (?, ?, ?, ?)'''
        params = [data[key] for key in schema.sets_cols]
        self.cursor.execute(sql, params)
    
    def putLection(self, data):
        sql = f'''INSERT OR REPLACE INTO lections ({','.join(data.keys())})
                VALUES (?, ?, ?, ?)
                '''
        params = list(data.values())
        self.cursor.execute(sql, params)

    def getLectionsForYear(self, year):
        sql = f'''SELECT * FROM lections
                WHERE Year = ?
                '''
        self.cursor.execute(sql, [year])
        return self.cursor.fetchall()
    
    def getLection(self, year, lection_number):
        sql = f'''
        SELECT * FROM lections
                WHERE Year = ?
        '''
    
    def clearLections(self):
        sql = '''
            DELETE * FROM lections
        '''
        self.cursor.execute(sql)

