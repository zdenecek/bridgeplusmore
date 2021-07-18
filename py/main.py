from db.resultRepository import ResultRepository
from db.db import Database
from gui.mainWindow import MainWindow
from parse.fileParser import FileParser

print('Starting script...')

dbfile = 'boards.sqlite'
db = Database(dbfile)
resultRepo = ResultRepository(db)
parser =  FileParser()


window = MainWindow(resultRepo, parser)
window.start()


db.close()
print('Script ended...')
exit(0)






