import importlib.util

from tkinter import Frame,Button,Text,DISABLED,END  
from functools import partial
from kcalc.kcalc import KCalc


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

    def createPoint(self):
        self.butPoint = Button(self,height=5,width=33,state=DISABLED)
        self.butPoint["text"] = ","
        self.butPoint.grid(row=4, column=2)

    def createDisplay(self):
        self.display = Text(self, height = 1, width = 1)
        self.display.insert(END, "0")
        self.display.grid(row=0, column=0, sticky="we")

    def createClear(self):
        self.butClear = Button(self,height=5,width=33)
        self.butClear["text"] = "Clear"
        self.butClear["command"] = partial( self.clear )
        self.butClear.grid(row=4, column=0)
    
    def createSign(self, sign, gridnum):
        self.butSign = Button(self,height=5,width=33)
        self.butSign["text"] = sign
        self.butSign["command"] = partial( self.whichNumber, sign )
        self.butSign.grid(row = self.signgridrow[gridnum], column = self.signgridcol[gridnum])
    
    def createEquals(self):
        self.butEquals = Button(self,height=5,width=33)
        self.butEquals["text"] = "="
        self.butEquals["command"] = partial( self.getTotal, True )
        self.butEquals.grid(row=4, column=3)

    def setDisplayText(self, text):
        self.display.delete("1.0", END)
        self.display.insert(END, text)

    def whichNumber(self, sign = "+" ):
        if self.numberposition == 1:
            self.numberposition = 2
        else:
            self.getTotal(False)
            # Changing number[0] to last result
            self.number1Text = str(self.result)
            self.number2Text = ""
        self.sign = sign

    def addNumber(self,number):
        if(self.numberposition == 2):
            self.number2Text = str(self.number2Text) + str (number)
            self.setDisplayText(self.number2Text)
        else:
            self.number1Text = str(self.number1Text) + str (number)
            self.setDisplayText(self.number1Text)

    def clear(self):
        self.resetVars()
        self.setDisplayText("0")

    def getTotal(self, isEquals):
        if(not self.number1Text == ""):
            number1=str(self.number1Text)
            number2=str(self.number2Text)
            self.result=self.kCalc.getResult(self.sign,[int(number1),int(number2)])

            # Showing Result
            self.setDisplayText(str(self.result))

            # if you click on Equals sign, reset number position and Text
            if isEquals == True:
                # Reset numbers text
               self.resetVars()

    def resetVars(self):
            # Reset numbers text
            self.number1Text=""
            self.number2Text=""
            self.numberposition = 1

    def showingGui(self):
        # Creating display text box 
        self.createDisplay()

        # Creating numbers and point display
        self.createNumbers()
        self.createPoint()

        # Creating signs display
        self.createSign("x", 0)
        self.createSign("-", 1)
        self.createSign("+", 2)

        # Creating Clear Button
        self.createClear()

        # Creating equals display
        self.createEquals()


    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        
        # Initializing vars
        self.number1=None
        self.number2=None
        self.result=None
        self.sign="+"

        # Creating KCalc Instance
        self.kCalc=KCalc()

        # Showing all gui elements
        self.showingGui()

