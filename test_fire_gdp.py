import unittest
import fire_gdp
import random

class TestFireGDP(unittest.TestCase):
    def test_clean_str(self):
        self.assertEqual(fire_gdp.clean_str('1,000'), '1000')
        self.assertEqual(fire_gdp.clean_str('1,000,000'), '1000000')
    
    def test_search(self):
        self.assertEqual(fire_gdp.search([1,2,3,4,5], 3), 2)
        self.assertEqual(fire_gdp.search([1,2,3,4,5], 100), None)
        self.assertEqual(fire_gdp.search([1,2,3,3,4,5], 3), 2)
        self.assertEqual(fire_gdp.search([3,1,2,3,4,5], 3), 0)
        self.assertEqual(fire_gdp.search([], 3), None)

        for i in range(100):
            random_list = [random.randint(1,100000) for x in range(1000)]
            random_value = random.choice(random_list)
            first_value = random_list[0]
            no_hit_value = 1000000
            self.assertIsNotNone(fire_gdp.search(random_list, random_value))
            self.assertIsNone(fire_gdp.search(random_list, no_hit_value))
            self.assertEqual(fire_gdp.search(random_list,first_value), 0)

    
        
        
if __name__ == '__main__':
    unittest.main()
  
 