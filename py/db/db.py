import sqlite3
import db.schema as schema

class Database:

    def __init__(self, filename):
        self.filename = filename
        self.connection = sqlite3.connect(filename)
        self.connection.row_factory = sqlite3.Row
        self.cursor = self.connection.cursor()

    def close(self, keep = True):
        if keep:
            self.connection.commit()
        else:
            print("Changes were not commited to the database")
        self.connection.close()

    def all(self, sql, params = []):
        self.cursor.execute(sql, params)
        return self.cursor.fetchall()

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
