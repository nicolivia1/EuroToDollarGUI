#!/usr/bin/python3
import pathlib
import tkinter as tk
import pygubu
import tkinter.ttk as ttk

PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "About.ui"
RESOURCE_PATHS = [PROJECT_PATH]


class AboutPageUI:
    def __init__(self, master=None):
        self.builder = pygubu.Builder()
        self.builder.add_resource_paths(RESOURCE_PATHS)
        self.builder.add_from_file(PROJECT_UI)
        # Main widget
        self.main_window = self.builder.get_object(
            "topLabel", master)
        self.builder.connect_callbacks(self)

    # I added this trying to get About tab to work
    def get_top_frame(self):
        # Return the top frame for the app so that it can be displayed in a tabbed notebook.
        return self.main_window

    def run(self):
        self.main_window.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    app = AboutPageUI(root)
    app.run()
