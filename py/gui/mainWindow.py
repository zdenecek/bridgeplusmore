
import tkinter as tk
from tkinter import ttk

from gui.SourceManipulationTab import SourceManipulationTab
from gui.SourceLoadingTab import SourceLoadingTab

class MainWindow: 

    def __init__(self, db, fileParser):
        self.db = db
        self.fileParser = fileParser
        self.tabs = {}

    def test(self):
        self.tabs['Zdroj'].addFile([r'C:\Users\zdnek\src\bridgepuppet\data\01.docx'])
        self.tabs['Konverze'].loadSources()

    def start(self):
        self.window = tk.Tk()
        self.window.title("Načítač lekcí")
        self.window.geometry("1920x1080")
        self.window.config()
        self.configureComponents()

        # self.test()

        self.window.mainloop()

    def configureComponents(self):
        self.tabControl = ttk.Notebook(self.window)

        self.tabs['Zdroj'] = SourceLoadingTab(self.db, self.fileParser)
        self.tabs['Konverze'] = SourceManipulationTab(self.db, self.tabs['Zdroj'])

        for name, tab in self.tabs.items():
            tabRoot = ttk.Frame(self.tabControl)
            self.tabControl.add(tabRoot, text=name)
            tab.attach(tabRoot)

        self.tabControl.pack()
        
