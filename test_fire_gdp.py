import unittest
import fire_gdp
import random

class TestFireGDP(unittest.TestCase):
    def test_clean_str(self):
        self.assertEqual(fire_gdp.clean_str('1,000'), '1000')
        self.assertEqual(fire_gdp.clean_str('1,000,000'), '1000000')
        
        
        
if __name__ == '__main__':
    unittest.main()
  
 