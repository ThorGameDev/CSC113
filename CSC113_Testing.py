# November 10, 2023

import unittest

class TestableClass:
    """Provides addition and subtraction functions with logs"""
    def __init__(self):
        self.logs = []

    def add_with_logs(self, num1, num2):
        """Adds two numbers and appends the operation to the logs"""
        self.logs.append(f"{num1} and {num2} were added!")
        return num1 + num2

    def subtract_with_logs(self, num1, num2):
        """Subtracts two numbers and appends the operation to the logs"""
        self.logs.append(f"{num1} and {num2} were subtracted!")
        return num1 - num2

class TestLogOperations(unittest.TestCase):
    """Runs unit tests for TestableClass"""
    def setUp(self):
        self.log_operations = TestableClass()

    def test_adition(self):
        """Tests the TestableClass addition function"""
        self.assertEqual(self.log_operations.add_with_logs(5,2), 7)
        self.assertEqual(self.log_operations.logs, ["5 and 2 were added!"])

    def test_subtraction(self):
        """Tests the TestableClass subtraction function"""
        self.assertEqual(self.log_operations.subtract_with_logs(5,2), 3)
        self.assertEqual(self.log_operations.logs, ["5 and 2 were subtracted!"])

# Runs the unit tests
if __name__ == '__main__':
    unittest.main()

