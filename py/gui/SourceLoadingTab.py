
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import scrolledtext


class SourceLoadingTab: 

    def __init__(self, db, fileParser):
        self.db = db
        self.fileParser = fileParser
        self.currentData = {}
        
 
    def attach(self, root):
        self.root = root
        
        self.configureComponents()

    def configureComponents(self):

        self.cols = []
        for i in range(2):
            self.cols.append(tk.Frame(self.root))

        self.addFileButton = tk.Button(self.cols[0], text="Otevřít soubor", command=self.addFile)

        self.previewTreeview = ttk.Treeview(self.cols[0])
        self.previewTreeview['columns'] = ('count')
        self.previewTreeview.column("#0", width=500, minwidth=25)
        self.previewTreeview.column("count", width=60, minwidth=25)
        self.previewTreeview.heading("#0", text="Objekt")
        self.previewTreeview.heading("count", text="Počet odstavců")

        self.previewAreaLabel = tk.Label(self.cols[1], text="Náhled lekce")
        self.previewArea = scrolledtext.ScrolledText(self.cols[1])

        for index, col in enumerate(self.cols):
            col.grid(row=1, column=index, padx=10)
        
        self.addFileButton.pack(pady=10)
        self.previewTreeview.pack(pady=10)

        self.previewAreaLabel.pack()
        self.previewArea.pack()


    
    def addFile(self):
        data = {}
        filepaths = filedialog.askopenfilenames(title="vyberte soubory s lekcemi")
        if len(filepaths) == 0:
            return
        for path in filepaths:
            year = self.fileParser.parseDocumentGetYearFromFilename(path)
            data[year.year] = year
        
        self.putData(data)

    def putData(self, data):
        self.previewTreeview.delete(*self.previewTreeview.get_children())
        self.currentData = data
        for year in data.values():
            self.previewTreeview.insert('', 'end', iid=year.year, text=str(year))
        
        for year in data.values():
            for lesson in year.lessons:
                self.previewTreeview.insert(year.year, 'end', text=str(lesson), values=(len(lesson.content)))

    def saveData(self):
        pass
