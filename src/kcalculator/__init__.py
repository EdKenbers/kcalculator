from kcalculator.kcalculatorgui import CalculatorGui
from tkinter import Tk

def main():
    root = Tk()
    calc = CalculatorGui(master=root)
    calc.mainloop()