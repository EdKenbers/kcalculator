from functools import reduce
import operator

# CalculatorSum Class definition
class KCalc:
    # Passing a list of two numbers can make and return the sum
    '''
    Testing simple init
    >>> csum=KCalc()
    >>> csum.getResult("+", [2,0])
    2

    Testing other numbers
    >>> numbers=[4,8]
    >>> csum.getResult("+",numbers)
    12

    Testing negative numbers
    >>> numbers=[-4,-10]
    >>> csum.getResult("+",numbers)
    -14

    Testing substract numbers
    >>> numbers=[4,10]
    >>> csum.getResult("-",numbers)
    -6

    Testing multiply numbers
    >>> numbers=[4,10]
    >>> csum.getResult("x",numbers)
    40

    Testing divide numbers
    >>> numbers=[8,4]
    >>> csum.getResult("/",numbers)
    2.0
    '''

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
