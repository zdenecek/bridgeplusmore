import sqlite3

class Database:

    def __init__(self, filename):
        self.filename = filename
        self.connection = sqlite3.connect(filename)
        self.cursor = self.connection.cursor()

    def close(self):
        self.connection.close()