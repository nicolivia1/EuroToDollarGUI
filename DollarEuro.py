#!/usr/bin/python3
import pathlib
import tkinter as tk
import pygubu
from DollarEuroui import DollarEuroUI


class DollarEuro(DollarEuroUI):
    def __init__(self, master=None):
        super().__init__(master)


if __name__ == "__main__":
    app = DollarEuro()
    app.run()
