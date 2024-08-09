# Main file made by Nicole Sausville
# Due date: 8/9/24
# Description: A currency conversion calculator program


# Imports
import tkinter as tk
import tkinter.ttk as ttk

from DollarEuroui import DollarEuroUI
from Aboutui import AboutPageUI
from EuroToDollarsui import EuroToDollarsAppUI


class MainApp:
    # Constructor
    def __init__(self, master):
        tk.Grid.columnconfigure(master, 0, weight=1)
        tk.Grid.rowconfigure(master, 0, weight=1)

        # Building UI
        self.main_notebook = ttk.Notebook(master)
        self.main_notebook.grid(column=0, row=0, sticky='nsew')
        self.main_notebook.rowconfigure(0, weight=1)
        self.main_notebook.columnconfigure(0, weight=1)

        # Main widget
        self.main_window = self.main_notebook

        # Adding the About tab
        about_tab = AboutPageUI()
        self.main_notebook.add(about_tab.get_top_frame(), text="About")

        # Adding the first calculator
        dollar_to_euro_app = DollarEuroUI()
        self.main_notebook.add(dollar_to_euro_app.get_top_frame(), text="Dollars to Euros")

        # Adding the second calculator
        euro_to_dollar_app = EuroToDollarsAppUI()
        self.main_notebook.add(euro_to_dollar_app.get_top_frame(), text="Euros to Dollars")

    # Runs the window
    def run(self):
        self.main_window.mainloop()


if __name__ == '__main__':
    root = tk.Tk()
    root.title("Currency Conversion Calculator")
    app = MainApp(root)
    app.run()
