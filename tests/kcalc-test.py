import unittest
from kcalc.kcalc import KCalc

class TestKCalcMethods(unittest.TestCase):

    # Test contruction of Class KCalc()
    def test_construct(self):
        kcalcTestClass = KCalc()
        self.assertEqual(kcalcTestClass.numbers , [0,0])
        self.assertEqual(kcalcTestClass.result , 0)

    # Test for setNumbers(self, numbers)
    def test_setNumbers(self):
        kcalcTestClass = KCalc()
        numbers = [2,2]
        kcalcTestClass.setNumbers(numbers)
        self.assertEqual(kcalcTestClass.numbers , [2,2])

    # Test for calc(self, sign)
    def test_calc(self):
        kcalcTestClass = KCalc()
        kcalcTestClass.setNumbers([6,3])
        
        # Sum
        kcalcTestClass.calc('+')
        self.assertEqual(kcalcTestClass.result , 9)

        # Substract
        kcalcTestClass.calc('-')
        self.assertEqual(kcalcTestClass.result , 3)

        # Multiply
        kcalcTestClass.calc('x')
        self.assertEqual(kcalcTestClass.result , 18)

        # Multiply
        kcalcTestClass.calc('/')
        self.assertEqual(kcalcTestClass.result , 2.0)
        
    def test_getResult(self):
        kcalcTestClass = KCalc()
        kcalcTestClass.getResult('+',[0,2])
        self.assertEqual(kcalcTestClass.result , 2)



if __name__ == '__main__':
    unittest.main()