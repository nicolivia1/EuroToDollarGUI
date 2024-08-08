#!/usr/bin/python3
import pathlib
import tkinter as tk
import pygubu
from Aboutui import AboutPageUI


class AboutPage(AboutPageUI):
    def __init__(self, master=None):
        super().__init__(master)


if __name__ == "__main__":
    app = AboutPage()
    app.run()
