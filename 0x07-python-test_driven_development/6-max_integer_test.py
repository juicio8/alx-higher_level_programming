import unittest
from max_integer import max_integer

class TestMax(unittest.TestCase):
    def test_none(self):
        self.assertAlmostEqual(max_integer([]), None)
        self.assertAlmostEqual(max_integer(), None)
        self.assertAlmostEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertAlmostEqual(max_integer([1, 4, 3, 2]), 4)
