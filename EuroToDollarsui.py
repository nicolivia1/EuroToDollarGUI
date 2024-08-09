# Made by Evan Vu


import pathlib
import tkinter as tk
import pygubu
import tkinter.messagebox as mb

PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "EuroToDollar.ui"
RESOURCE_PATHS = [PROJECT_PATH]


class EuroToDollarsAppUI:
    # Function lets you use a calculator to convert euros to dollars.
    def __init__(self, master=None, on_first_object_cb=None):
        self.builder = pygubu.Builder(
            on_first_object=on_first_object_cb)
        self.builder.add_resource_paths(RESOURCE_PATHS)
        self.builder.add_from_file(PROJECT_UI)
        # Main widget
        self.mainwindow: tk.Frame = self.builder.get_object("frame1", master)

        self.dollar_entry_variable: tk.StringVar = None
        self.builder.import_variables(self)

        self.builder.connect_callbacks(self)
        self.euro_entry = self.builder.get_object("euro_entry", self)
        self.dollar_entry_variable = self.builder.get_variable("dollar_entry_variable")


    # Starts the loops of the app
    def run(self):
        self.mainwindow.mainloop()


    # Calculates euros to dollars
    def calculate(self):
        conversion_rate = 1.10
        dollar = 0.0
        print("Calculate", self.euro_entry.get())
        try:
            euro = float(self.euro_entry.get())
            dollar = euro * conversion_rate
            self.dollar_entry_variable.set(f"{dollar:.2f}")
        except:
            mb.showerror(title="Error please type in numbers!",
                         message="Entry must be a number.")

    # Return the top frame for the app so that it can be displayed in a tabbed notebook.
    def get_top_frame(self):
        return self.mainwindow


if __name__ == "__main__":
    root = tk.Tk()
    app = EuroToDollarsAppUI(root)
    app.run()
