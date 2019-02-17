import unittest
import PyCalc

class TestPyCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(PyCalc.add(10, 5), 15)
        self.assertEqual(PyCalc.add(0, 0), 0)
        self.assertEqual(PyCalc.add(-10, 5), -5)

    def test_subtract(self):
        self.assertEqual(PyCalc.subtract(10, 5), 5)
        self.assertEqual(PyCalc.subtract(0, 0), 0)
        self.assertEqual(PyCalc.subtract(-10, 5), -15)

    def test_multiply(self):
        self.assertEqual(PyCalc.multiply(10, 5), 50)
        self.assertEqual(PyCalc.multiply(0, 0), 0)
        self.assertEqual(PyCalc.multiply(-10, 5), -50)

    def test_divide(self):
        self.assertEqual(PyCalc.divide(10, 5), 2)
        with self.assertRaises(ValueError):
            PyCalc.divide(10,0)
        self.assertEqual(PyCalc.divide(-10, 5), -2)

if __name__ == '__main__':
    unittest.main()