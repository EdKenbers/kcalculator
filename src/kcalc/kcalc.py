from functools import reduce
import operator

# KCalc Class definition
class KCalc:
    # Passing a list of two numbers can make and return the sum, substract, multiply and divide

    def __init__(self):
        self.numbers = [ 0, 0 ]
        self.result = 0
    
    # Change numbers to sum
    def setNumbers(self, numbers):
        self.numbers=numbers

    # Make the sum of two numbers
    def calc(self, sign):
        if sign == "+":
            self.result = operator.add(self.numbers[0],self.numbers[1])
        elif sign == "-":
            self.result = operator.sub(self.numbers[0],self.numbers[1])
        elif sign == "x":
            self.result = operator.mul(self.numbers[0],self.numbers[1])
        elif sign == "/":
            self.result = operator.truediv(self.numbers[0],self.numbers[1])

    # Return the sum of the two numbers
    def getResult(self, sign, numbers):
        self.setNumbers(numbers)
        self.calc(sign)
        return self.result
