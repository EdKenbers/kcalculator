from functools import partial
from tkinter import *
import importlib.util

spec = importlib.util.spec_from_file_location("sum", "src/sum/sum.py")
summodule = importlib.util.module_from_spec(spec)
spec.loader.exec_module(summodule)



class CalculatorGui(Frame):

    numbers=[0,1,2,3,4,5,6,7,8,9]
    gridrow=[4,3,3,3,2,2,2,1,1,1]
    gridcol=[1,2,1,0,2,1,0,2,1,0]
    signgridrow=[1,2,3,4]
    signgridcol=[3,3,3,3] # Maybe not needed
    numberposition=1
    number1Text=""
    number2Text=""

    def createNumbers(self):
        for num in self.numbers:
            self.nButton = Button(self,height=5,width=33)
            self.nButton["text"] = str(num)
            self.nButton["command"] = partial( self.addNumber, str(num))
            self.nButton.grid(row=self.gridrow[num], column=self.gridcol[num])

    def createDisplay(self):
        self.display = Text(self, height = 1, width = 1)
        self.display.insert(END, "0")
        self.display.grid(row=0, column=0, sticky="we")
    
    def createSign(self, sign, gridnum):
        self.ButPlus = Button(self,height=5,width=33)
        self.ButPlus["text"] = sign
        self.ButPlus["command"] = partial( self.whichNumber, sign )
        self.ButPlus.grid(row = self.signgridrow[gridnum], column = self.signgridcol[gridnum])
    
    def createEquals(self):
        self.ButEquals = Button(self,height=5,width=33)
        self.ButEquals["text"] = "="
        self.ButEquals["command"] = self.getTotal
        self.ButEquals.grid(row=4, column=3)

    def setDisplayText(self, text):
        self.display.delete("1.0", END)
        self.display.insert(END, text)

    def whichNumber(self, sign = "+" ):
        if self.numberposition == 1:
            self.numberposition = 2
        else:
            self.numberposition = 1

    def addNumber(self,number):
        if(self.numberposition == 2):
            self.number2Text = str(self.number2Text) + str (number)
            self.setDisplayText(self.number2Text)
        else:
            self.number1Text = str(self.number1Text) + str (number)
            self.setDisplayText(self.number1Text)

    def getTotal(self):
        if(not self.number1Text == ""):
            number1=str(self.number1Text)
            number2=str(self.number2Text)
            self.cSum.setNumbers([int(number1),int(number2)])
            self.cSum.calcSum()
            self.result=self.cSum.getResult()
            self.setDisplayText(str(self.result))
            self.number1Text=""
            self.number2Text=""
            self.whichNumber()

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        
        # Initializing vars
        self.number1=None
        self.number2=None
        self.result=None

        # Creating KSum Instance
        self.cSum=summodule.KSum()

        # Creating display text box 
        self.createDisplay()

        # Creating numbers display
        self.createNumbers()

        # Creating signs display
        self.createSign("x", 0)
        self.createSign("-", 1)
        self.createSign("+", 2)

        # Creating equals display
        self.createEquals()

def main():
    from tkinter import Tk

    root = Tk()
    calc = CalculatorGui(master=root)
    calc.mainloop()
