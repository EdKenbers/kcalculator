# CalculatorSum Class definition
class CalculatorSum:
    # Passing a list of two numbers can make and return the sum
    '''
    Testing simple init
    >>> csum=CalculatorSum()
    >>> csum.calcSum()
    >>> csum.getResult()
    0

    Testing other numbers
    >>> numbers=[ 4, 8 ]
    >>> csum.setNumbers(numbers)
    >>> csum.calcSum()
    >>> csum.getResult()
    12

    Testing negative numbers
    >>> numbers=[ -4, -10 ]
    >>> csum.setNumbers(numbers)
    >>> csum.calcSum()
    >>> csum.getResult()
    -14
    '''

    def __init__(self):
        self.numbers = [ 0, 0 ]
        self.result = 0
    
    # Change numbers to sum
    def setNumbers(self, numbers):
        self.numbers=numbers

    # Make the sum of two numbers
    def calcSum(self):
        if self.numbers[0] and self.numbers[1]:
            self.result = sum(self.numbers)

    # Return the sum of the two numbers
    def getResult(self):
        return self.result
