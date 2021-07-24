import tkinter as tk
from tkinter import ttk

class XmlTreeview(tk.Frame):

    def __init__(self, xmlRepository, openFunction, saveFunction, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.xmlRepository = xmlRepository
        self.openFunction = openFunction
        self.saveFunction = saveFunction

        self.configComponents()

    def configComponents(self):
        
        self.label = tk.Label(self, text="Objekty v databázi")
        self.label.pack()

        self.treeview = ttk.Treeview(self)
        self.treeview['columns'] = ('createdAt')
        self.treeview.column("#0", width=300, minwidth=25)
        self.treeview.column("createdAt", width=130, minwidth=25)
        self.treeview.heading("#0", text="Objekt")
        self.treeview.heading("createdAt", text="Vytvořeno")
        self.treeview.pack()

        self.loadButton = tk.Button(self, command=self.loadFromDb, text="Načíst db")
        self.loadButton.pack(side="left")
        self.selectButton = tk.Button(self, command=self.openFunction, text="Vybrat")
        self.selectButton.pack(side="left")
        self.saveButton = tk.Button(self, command=self.saveFunction, text="Uložit")
        self.saveButton.pack(side='left')

    def loadFromDb(self):
        years = self.xmlRepository.getAllYears()
        self.data = {}
        self.treeview.delete(*self.treeview.get_children())
        for year in years:
            self.treeview.insert('', 'end', iid=year.year, text=str(year))
        
        for year in years:
            for lesson in year.lessons:
                id = self.treeview.insert(year.year, 'end', text=str(lesson), values=(lesson.updatedAt,))
                self.data[id] = lesson

    def getSelectedLesson(self):
        selectedId = self.treeview.selection()[0]
        return self.data[selectedId]

    
