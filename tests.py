import unittest
from Brew import Brew

class TestSum(unittest.TestCase):
    def setUp(self):
      self.test_brew = Brew(ratio=17, ground_coffee=30)

    def test_calc_ratio(self):
      self.test_brew.calc()
      self.assertEqual(self.test_brew.water, 510, "Should be 510")
      self.assertEqual(self.test_brew.brewed_coffee, 450, "Should be 450")

      
if __name__ == "__main__":
    unittest.main()