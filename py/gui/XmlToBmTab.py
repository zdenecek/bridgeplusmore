import tkinter as tk
from tkinter import ttk, simpledialog
from gui.xmlTreeview import XmlTreeview
from db.resultRepository import ResultRepository

class XmlToBmTab:

    xmlRepository: ResultRepository

    def __init__(self, xmlRepository, bmRespository, bmParser) -> None:
        self.xmlRepository = xmlRepository
        self.bmRepository = bmRespository
        self.bmParser = bmParser

    def attach(self, root):
        self.root = root
        self.configureComponents()

    def configureComponents(self):

        self.dbFrame = XmlTreeview(self.xmlRepository, self.openXml, self.loadXml, self.root)
        self.dbFrame.pack()

        self.parseYearButton = tk.Button(self.root, pady=10, text="Ročník xml=>bm", command=self.parseWholeYear)
        self.parseYearButton.pack()

    def parseWholeYear(self):
        year = simpledialog.askinteger('Zadej ročník', 'Zadej ročník')
        yearObject = self.xmlRepository.getYear(year)

        for lesson in yearObject.lessons:
            data = self.bmParser.parseLesson(lesson)
            self.bmRepository.storeLesson(data["lessonData"], data["examplesData"])



    def loadXml(self):
        pass

    def openXml(self):
        pass
