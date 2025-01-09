#! /usr/bin/python3

import unittest
from radius import Circle

# unit test
class TestCircle(unittest.TestCase):
    def test_a(self):
        result = Circle(1).circumference()
        self.assertEqual(result, 6.28318)  # Erwartetes Ergebnis

if __name__ == '__main__':
    unittest.main()
