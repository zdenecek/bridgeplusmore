
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

class SourceManipulationTab: 

    def __init__(self, db, sourcePanel):
        self.sourceTab = sourcePanel
        self.db = db
 
    def attach(self, root):
        self.root = root
        self.configureComponents()

    def configureComponents(self):
        
        self.sourceFrame = tk.Frame(self.root)
        self.resultFrame = tk.Frame(self.root)
        self.optionsFrame = tk.Frame(self.root)

        self.sourceTreeviewLabel = tk.Label(self.sourceFrame, text="Zdroje z .docx")
        self.resultTreeviewLabel = tk.Label(self.resultFrame, text="Objekty v databázi")

        self.loadButton = tk.Button(self.sourceFrame, command=self.load, text="Načíst", pady=10)

        self.sourceTreeview = ttk.Treeview(self.sourceFrame)
        self.sourceTreeview.column("#0", width=350)
        self.sourceTreeview.heading("#0", text="Objekt")

        self.resultTreeview = ttk.Treeview(self.resultFrame)
        self.resultTreeview['columns'] = ('createdAt')
        self.resultTreeview.column("#0", width=120, minwidth=25)
        self.resultTreeview.column("createdAt", width=60, minwidth=25)
        self.resultTreeview.heading("#0", text="Objekt")
        self.resultTreeview.heading("createdAt", text="Vytvořeno")

        self.sourceAreaLabel = tk.Label(self.root, text="Zdrojový text")
        self.workspaceAreaLabel = tk.Label(self.root, text="Pracovní plocha")
        self.resultAreaLabel = tk.Label(self.root, text="Výsledné xml")
        self.optionsFrameLabel = tk.Label(self.root, text="Akce")

        self.sourceArea = scrolledtext.ScrolledText(self.root)
        self.workspaceArea = scrolledtext.ScrolledText(self.root)
        self.resultArea = scrolledtext.ScrolledText(self.root)

        self.sourceTreeviewLabel.pack()
        self.sourceTreeview.pack()
        self.loadButton.pack()

        self.resultTreeviewLabel.pack()
        self.resultTreeview.pack()

        self.sourceFrame.grid(column=1, row=1, rowspan=2)
        self.resultFrame.grid(column=1, row=3, rowspan=2)

        self.sourceAreaLabel.grid(column=2, row=1)
        self.sourceArea.grid(column=2, row=2)

        self.resultAreaLabel.grid(column=2, row=3)
        self.resultArea.grid(column=2, row=4)

        self.workspaceAreaLabel.grid(column=3, row=1)
        self.workspaceArea.grid(column=3, row=2)

        self.optionsFrameLabel.grid(column=3, row=3)
        self.optionsFrame.grid(column=3, row=4)


    
    def load(self):
        self.sourceData = self.sourceTab.currentData
        self.sourceTreeview.delete(*self.sourceTreeview.get_children())
        for year in self.sourceData.values():
            self.sourceTreeview.insert('', 'end', iid=year.year, text=str(year))
        
        for year in self.sourceData.values():
            for lesson in year.lessons:
                self.sourceTreeview.insert(year.year, 'end', text=str(lesson), values=(len(lesson.content)))
