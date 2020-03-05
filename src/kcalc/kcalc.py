from functools import reduce
import operator

# CalculatorSum Class definition
class KCalc:
    # Passing a list of two numbers can make and return the sum
    '''
    Testing simple init
    >>> csum=KCalc()
    >>> csum.getResult("+", [0,0])
    0

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
        if self.numbers[0] and self.numbers[1]:
            if sign == "+":
                self.result = reduce(operator.add, self.numbers)
            elif sign == "-":
                self.result = reduce(operator.sub, self.numbers)
            elif sign == "x":
                self.result = reduce(operator.mul, self.numbers)
            elif sign == "/":
                self.result = reduce(operator.truediv, self.numbers)

    # Return the sum of the two numbers
    def getResult(self, sign, numbers):
        self.setNumbers(numbers)
        self.calc(sign)
        return self.result
