import unittest

# The function we want to test
def add(a, b):
    return a + b

# Create a test case class that inherits from unittest.TestCase
class TestAddition(unittest.TestCase):

    # Define test methods starting with "test_"
    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)  # Assert that add(2, 3) is equal to 5

    def test_add_negative_numbers(self):
        self.assertEqual(add(-2, -3), -5)  # Assert that add(-2, -3) is equal to -5

    def test_add_mixed_numbers(self):
        self.assertEqual(add(2, -3), -1)  # Assert that add(2, -3) is equal to -1
        print("yugesh")

if __name__ == '__main__':
    unittest.main()