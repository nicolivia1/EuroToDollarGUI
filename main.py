# Imports
import tkinter as tk
import tkinter.ttk as ttk
from DollarEuroui import DollarEuroUI
from Aboutui import AboutPageUI
class MainApp:
    def __init__(self, master):
        # This is needed to allow the notebook tabs to stretch.
        tk.Grid.columnconfigure(master, 0, weight=1)
        tk.Grid.rowconfigure(master, 0, weight=1)

        # build ui
        self.main_notebook = ttk.Notebook(master)
        self.main_notebook.grid(column='0', row='0', sticky='nsew')
        self.main_notebook.rowconfigure('0', weight='1')
        self.main_notebook.columnconfigure('0', weight='1')

        # Main widget
        self.mainwindow = self.main_notebook

        # Add About... tab
        # about_app = AboutApp(self.__mainwindow)
        # self.__main_notebook.add(about_app.get_top_frame(), text="About...")

        # Adding the About tab
        #about_tab = AboutPageUI(self.mainwindow)
        #self.main_notebook.add(about_tab.get_top_frame(), text="About")

        # Adding the first calculator
        dollar_to_euro_app = DollarEuroUI(self.mainwindow)
        self.main_notebook.add(dollar_to_euro_app.get_top_frame(), text="Dollars to Euros")

    def run(self):
        self.mainwindow.mainloop()

if __name__ == '__main__':
    # I probably added root = tk.TK() and the word root in MainApp(root)
    root = tk.Tk()
    app = MainApp(root)
    app.run()