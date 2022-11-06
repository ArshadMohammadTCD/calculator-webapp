import unittest
from Calculator import calc, errorCheck, calc_api

class TestCalc(unittest.TestCase):
    def test_correct_expr(self):
        """
        Test if correct expression returns True
        """
        self.assertTrue(errorCheck("1 + 2 - 3 + log(4)"), "Should be True")
        self.assertTrue(errorCheck("1 - 5 * 7^8-exp(9)"), "Should be True")
        self.assertTrue(errorCheck("54 + -3 * 6"), "Should be True")
        self.assertTrue(errorCheck("6.453 - 24 ^ 42"), "Should be True")

    def test_incorrect_expr(self):
        """
        Test if incorrect expression returns False
        """
        self.assertFalse(errorCheck("1++24-log(2"), "Should be False")
        self.assertFalse(errorCheck("1 - 38 ^- log(3) + 32*2)"), "Should be False")
        self.assertFalse(errorCheck(""), "Should be False")
        self.assertFalse(errorCheck("(5 * 4 + 2"), "Should be False")
        self.assertFalse(errorCheck("249 + log()"), "Should be False")

    def test_api_correct(self):
        """
        Test if valid expression returns correct answer
        """
        self.assertEqual(calc_api("4 + 6"), "10.000", "Should be 10")
        self.assertEqual(calc_api("25-9"), "16.000", "Should be 16")
        self.assertEqual(calc_api("exp(4)"), "54.598", "Should be 54.598")
        self.assertEqual(calc_api("3+5*exp(4.2)/(5+7)"), "30.786", "Should be 30.786")

    def test_api_incorrect(self):
        """
        Test if invalid expression returns error String
        """
        self.assertEqual(calc_api("4-+ 6"), "error: invalid input", "Should be invalid input")
        self.assertEqual(calc_api("log()"), "error: invalid input", "Should be invalid input")
        self.assertEqual(calc_api(""), "error: invalid input", "Should be invalid input")
        self.assertEqual(calc_api("3+**8"), "error: invalid input", "Should be invalid input")

    def test_basic_operations(self):
        """
        Test add, minus, multiply and division function
        """
        self.assertEqual(calc_api("1+1"), "2.000")
        self.assertEqual(calc_api("2+5-3"), "4.000")
        self.assertEqual(calc_api("4+8-1*2"), "10.000")
        self.assertEqual(calc_api("5*4+6-2/3*5"), "22.667")
        self.assertEqual(calc_api("0*0+1-4/5-145"), "-144.800")
        self.assertEqual(calc_api("100-64921/210+357*2357"), "841239.852")

    def test_power(self):
        """
        Test power
        """
        self.assertEqual(calc_api("0^0"), "1.000")
        self.assertEqual(calc_api("55^4"), "9150625.000")
        self.assertEqual(calc_api("1+8^6-5*7/10^8"), "262145.000")

    def test_log(self):
        """
        Test log
        """
        self.assertEqual(calc_api("log(4)"), "0.602")
        self.assertEqual(calc_api("log(11)"), "1.041")
        self.assertEqual(calc_api("log(102)"), "2.009")

    def test_exp(self):
        """
        Test exp
        """
        self.assertEqual(calc_api("exp(0)"), "1.000")
        self.assertEqual(calc_api("exp(4)"), "54.598")
        self.assertEqual(calc_api("exp(11)"), "59874.142")

    def test_bracket(self):
        """
        Test bracket
        """
        self.assertEqual(calc_api("(5+1)"), "6.000")
        self.assertEqual(calc_api("6*(1-1)"), "0.000")
        self.assertEqual(calc_api("(1+1)/(2-1)"), "2.000")
        self.assertEqual(calc_api("(1+5-2)*(2-1)"), "4.000")
        self.assertEqual(calc_api("(1+(2-(5+7)))"), "-9.000")
        self.assertEqual(calc_api("13+(1+(2-(5+7)))"), "4.000")

    def test_neg(self):
        """
        Test neg
        """
        self.assertEqual(calc_api("-1-1"), "-2.000")
        self.assertEqual(calc_api("1-(-1)"), "2.000")
        self.assertEqual(calc_api("311+(-4)*(-22)-10"), "389.000")
        self.assertEqual(calc_api("-log(4)"), "-0.602")
        self.assertEqual(calc_api("-exp(5)"), "-148.413")
        self.assertEqual(calc_api("exp(-2)"), "0.135")
        self.assertEqual(calc_api("exp(-(-2))"), "7.389")

    def test_dec(self):
        """
        Test dec
        """
        self.assertEqual(calc_api("1.5+3.1"), "4.600")
        self.assertEqual(calc_api("8.000+9.000"), "17.000")
        self.assertEqual(calc_api("5.7655+1.47-5.6547*(8.11111-5.9)+4.269"), "-0.999")

if __name__ == "__main__":
    unittest.main()
    print("All tests Passed")
