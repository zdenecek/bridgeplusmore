from db.db import Database
from db.sourceRepository import SourceRepository
from gui.mainWindow import MainWindow
from parse.fileParser import FileParser

print('Starting script...')

dbfile = 'boards.sqlite'
db = Database(dbfile)
parser =  FileParser()

# sr = SourceRepository(db)
# print(sr.getData())


window = MainWindow(db, parser)
window.start()

# db.connection.commit()

db.close()
print('Script ended...')
exit(0)






