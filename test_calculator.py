import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
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
    # def test_multiply(self): # 3 assertions
    #     fill in code

    # def test_divide(self): # 3 assertions
    #     fill in code
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
    # def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code

    # def test_hypotenuse(self): # 3 assertions
    #     fill in code

    # def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()