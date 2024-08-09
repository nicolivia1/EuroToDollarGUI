# Made by Nicole Sausville


#!/usr/bin/python3
import pathlib
import tkinter as tk
import pygubu
import tkinter.ttk as ttk
import tkinter.messagebox as mb


PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "DollarEuroCalculator.ui"
RESOURCE_PATHS = [PROJECT_PATH]


class DollarEuroUI:
    EURO_CONVERSION_RATE = 0.91468602

    def __init__(self, master=None):
        self.builder = pygubu.Builder()
        self.builder.add_resource_paths(RESOURCE_PATHS)
        self.builder.add_from_file(PROJECT_UI)
        # Main widget
        self.main_window = self.builder.get_object(
            "topLabel", master)
        self.builder.connect_callbacks(self)

        self.dollar_input = self.builder.get_object("dollarEntry", master)
        self.euro_output = self.builder.get_variable("euro_entry_variable")

    def run(self):
        self.main_window.mainloop()

    def get_top_frame(self):
        # Return the top frame for the app so that it can be displayed in a tabbed notebook.
        return self.main_window

    def calculate(self):
        try:
            dollars = float(self.dollar_input.get())
            euros = dollars * DollarEuroUI.EURO_CONVERSION_RATE
            self.euro_output.set(f"{euros:.2f}")
        except ValueError:
            mb.showerror(title="Error Calculating Euros!",
                         message="Dollar amount must be a decimal number. Please try again.")


if __name__ == "__main__":
    root = tk.Tk()
    app = DollarEuroUI(root)
    app.run()
