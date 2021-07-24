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

    def fetchAll(self, sql, params = []):
        print("Running fetchAll with query: " + sql)
        self.cursor.execute(sql, params)
        self.connection.commit()
        return self.cursor.fetchall()


    def execute(self, sql, params = []):
        print("Running execute with query: " + sql)
        res = self.cursor.execute(sql, params)
        self.connection.commit()
        return res
