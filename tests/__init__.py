#!usr/bin/python3
"""example"""
import unittest

# Function to be tested
def add(a, b):
    return a + b

# Test case class
class TestAddFunction(unittest.TestCase):

    
    def test_add_positive_numbers(self):
        result = add(4, 5)
        self.assertEqual(result, 9)

    
    def test_add_negative_numbers(self):
        result = add(-3, -3)
        self.assertEqual(result, -6)

    
    def test_add_mixed_numbers(self):
        result = add(3, -5)
        self.assertEqual(result, -2)

if __name__ == '__main__':
    unittest.main()
