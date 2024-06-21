import unittest
from src.calculator import add, subtract, divide

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(subtract(9, 4), 5)
        self.assertEqual(subtract(6, 7), -1)
        self.assertEqual(subtract(-4, 1), -5)

    def test_divide(self):
        self.assertEqual(divide(12, 2), 6)
        self.assertEqual(divide(14, 7), 2)
        with self.assertRaises(ValueError):
            divide(2, 0)

if __name__ == '__main__':
    unittest.main()
