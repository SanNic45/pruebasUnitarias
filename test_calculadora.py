import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculadora = Calculator()

    def test_divide(self):
        self.assertEqual(self.calculadora.divide(10, 5), 2)
        self.assertEqual(self.calculadora.divide(-10, 5), -2)
        self.assertEqual(self.calculadora.divide(10, -5), -2)
        self.assertRaises(ZeroDivisionError, self.calculadora.divide, 10, 0)
        self.assertRaises(TypeError, self.calculadora.divide, 10, "5")
        self.assertRaises(TypeError, self.calculadora.divide, "10", 5)

    def test_multiply(self):
        self.assertEqual(self.calculadora.multiply(10, 5), 50)
        self.assertEqual(self.calculadora.multiply(-10, 5), -50)
        self.assertEqual(self.calculadora.multiply(10, -5), -50)
        self.assertRaises(TypeError, self.calculadora.multiply, 10, "5")
        self.assertRaises(TypeError, self.calculadora.multiply, "10", 5)

    def test_sum(self):
        self.assertEqual(self.calculadora.sum(10, 5), 15)
        self.assertEqual(self.calculadora.sum(-10, 5), -5)
        self.assertEqual(self.calculadora.sum(10, -5), 5)
        self.assertRaises(TypeError, self.calculadora.sum, 10, "5")
        self.assertRaises(TypeError, self.calculadora.sum, "10", 5)

    def test_subtract(self):
        self.assertEqual(self.calculadora.subtract(10, 5), 5)
        self.assertEqual(self.calculadora.subtract(-10, 5), -15)
        self.assertEqual(self.calculadora.subtract(10, -5), 15)
        self.assertRaises(TypeError, self.calculadora.subtract, 10, "5")
        self.assertRaises(TypeError, self.calculadora.subtract, "10", 5)

if __name__ == "__main__":
    unittest.main()
