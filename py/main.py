from parse.xmlParser import XmlParser
from db.resultRepository import ResultRepository
from db.db import Database
from db.bmRepository import BmRepository
from gui.mainWindow import MainWindow
from parse.fileParser import FileParser

print('Starting script...')

dbfile = 'boards.sqlite'
db = Database(dbfile)
resultRepo = ResultRepository(db)
bmRepo = BmRepository(db)

parser =  FileParser()
bmParser = XmlParser()


window = MainWindow(resultRepository=resultRepo, bmRepository=bmRepo, fileParser=parser, bmParser=bmParser)
window.start()


db.close()
print('Script ended...')
exit(0)






