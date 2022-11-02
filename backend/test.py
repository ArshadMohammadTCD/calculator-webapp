import unittest
from Calculator import calc, errorCheck, calc_api

class TestCalc(unittest.TestCase):
    def test_correct_expr(self):
        """
        Test if correct expression returns True
        """
        self.assertTrue(errorCheck("1 + 2 - 3 + log(4)"), "Should be True")
        self.assertTrue(errorCheck("1 - 5 * 7^8-exp(9)"), "Should be True")

    def test_incorrect_expr(self):
        """
        Test if incorrect expression returns False
        """
        self.assertFalse(errorCheck("1++24-log(2"), "Should be False")
        self.assertFalse(errorCheck("1 - 38 ^- log(3) + 32*2)"), "Should be False")
        self.assertFalse(errorCheck(""), "Should be False")
        self.assertFalse(errorCheck("1.2 - 6"), "Should be False")
        self.assertFalse(errorCheck("(5 * 4 + 2"), "Should be False")
        self.assertFalse(errorCheck("249 + log()"), "Should be False")

    def test_api_correct(self):
        """
        Test if valid expression returns correct answer
        """
        self.assertEqual(calc_api("4 + 6"), "10", "Should be 10")
        self.assertEqual(calc_api("25-9"), "16", "Should be 16")

    def test_api_incorrect(self):
        """
        Test if invalid expression returns error String
        """
        self.assertEqual(calc_api("4-+ 6"), "error: invalid input", "Should be invalid input")
        self.assertEqual(calc_api("log()"), "error: invalid input", "Should be invalid input")
        self.assertEqual(calc_api(""), "error: invalid input", "Should be invalid input")


if __name__ == "__main__":
    unittest.main()
    print("All tests Passed")