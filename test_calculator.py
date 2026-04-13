import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######## Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(3,2),5)
        self.assertEqual(add(3,-2),1)
        self.assertEqual(add(456.568,1245.0000),1701.568)
    def test_subtract(self): # 3 assertions
        self.assertEqual(sub(10,7),3)
        self.assertEqual(subtract(-10,5),-15)
        self.assertEqual(sub(5.3156,87.32),-82.00439999999999)
    # ##########################

    ######## Partner 1
    def test_multiply(self):  # 3 assertions
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-1, 5), -5)
        self.assertEqual(multiply(0, 100), 0)

    def test_divide(self):  # 3 assertions
        self.assertEqual(div(2, 10), 5)          # 10 / 2 = 5
        self.assertAlmostEqual(div(4, 1), 0.25)  # 1 / 4 = 0.25
        self.assertEqual(div(1, 9), 9.0)          # 9 / 1 = 9
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        # call division function inside, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #     div(0, 5)
        self.assertRaises(ZeroDivisionError,div,0,5)

    def test_logarithm(self): # 3 assertions
        self.assertEqual(logarithm(10,10), 1)
        self.assertEqual(logarithm(2,4),2)
        self.assertEqual(logarithm(4,2),0.5)


    def test_log_invalid_base(self): # 1 assertion
        # use same technique from test_divide_by_zero
        self.assertRaises(ValueError, logarithm, 0,0)
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self):  # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(10, 0)  # log base 10 of 0 → undefined

    def test_hypotenuse(self):  # 3 assertions
        self.assertAlmostEqual(hypotenuse(3, 4), 5.0)    # classic 3-4-5
        self.assertAlmostEqual(hypotenuse(5, 12), 13.0)  # 5-12-13
        self.assertAlmostEqual(hypotenuse(0, 7), 7.0)    # degenerate case

    def test_sqrt(self):  # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-1)                          # negative → ValueError
        self.assertAlmostEqual(square_root(4), 2.0)
        self.assertAlmostEqual(square_root(9), 3.0)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()