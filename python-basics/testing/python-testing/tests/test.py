import unittest
from fractions import Fraction
from my_sum import sum

class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        '''
        This code example:

        1. Imports `sum()`from the`my_sum`package you created
        2. Defines a new test case class called`TestSum`, which inherits from`unittest.TestCase`
        3. Defines a test method,`.test_list_int()`, to test a list of integers. The method `.test_list_int()` will:
            - Declare a variable `data` with a list of numbers `(1, 2, 3)`
            - Assign the result of `my_sum.sum(data)` to a `result` variable
            - Assert that the value of `result` equals `6` by using the `.assertEqual()` method on the `unittest.TestCase` class
        4. Defines a command-line entry point, which runs the `unittest` test-runner `.main()`
        '''
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

    def test_list_fraction(self):
        """
        Test that it can sum a list of fractions
        """
        data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]
        result = sum(data)
        self.assertEqual(result, 1)

    '''
    Handling Expected Failures: https://realpython.com/python-testing/#handling-expected-failures
    '''
    def test_bad_type(self):
        # This test case will now only pass if sum(data) raises a TypeError
        data = "banana"
        with self.assertRaises(TypeError): # special way to handle expected errors
            # inside the with block execute the test steps
            result = sum(data)

if __name__ == '__main__':
    unittest.main() # this executes the test runner by discovering all classes in this file that inherit from unittest.TestCase