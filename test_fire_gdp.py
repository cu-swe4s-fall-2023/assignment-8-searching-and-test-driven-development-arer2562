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
    
    def test_get_data_open_file(self):
        fire_file_name = 'Agrofood_co2_emission.csv'
        gdp_file_name = 'IMF_GDP.csv'
        dne_file_name = 'fire_gdp.txt'
        empty_file_name = 'empty.txt'
        
        with open(empty_file_name, 'w') as empty_file:
            pass
        
        self.assertEqual(fire_gdp.get_data(empty_file_name), [])
        self.assertRaises(FileNotFoundError, fire_gdp.get_data, dne_file_name)
    
    def test_get_data_read_lines(self):
        fire_file_name = 'Agrofood_co2_emission.csv'
        gdp_file_name = 'IMF_GDP.csv'
        empty_file_name = 'empty.txt'

        self.assertEqual(len(fire_gdp.get_data(fire_file_name)), 6966)
        self.assertEqual(len(fire_gdp.get_data(gdp_file_name)), 199)
        self.assertEqual(len(fire_gdp.get_data(empty_file_name)), 0)
            
    def test_get_get_header(self):
        fire_file_name = 'Agrofood_co2_emission.csv'
        gdp_file_name = 'IMF_GDP.csv'
        empty_file_name = 'empty.txt'
        
        target_country = 'Zimbabwe'
        
        data, header = fire_gdp.get_data(fire_file_name, 
                                         query_value=target_country, 
                                         query_col=0,
                                         get_header=True)
        self.assertEqual(len(data), 31)
        self.assertEqual(len(header), 31)
        
        data,header = fire_gdp.get_data(gdp_file_name,
                                        query_value=target_country,
                                        query_col=0,
                                        get_header=True)
        
        self.assertEqual(len(data), 1)
        self.assertEqual(len(header), 74)
        
        data, header = fire_gdp.get_data(empty_file_name,
                                         query_value=target_country,
                                         query_col=0,
                                         get_header=True)
         
        self.assertEqual(len(data), 0)
        self.assertEqual(len(header), 0)       
        
        data, header = fire_gdp.get_data(gdp_file_name,
                                         query_value=target_country,
                                         query_col=1,
                                         get_header=True) 
        
        self.assertEqual(len(data), 0)
        self.assertEqual(len(header), 74)
        
        self.assertRaises(IndexError,
                          fire_gdp.get_data,
                          gdp_file_name,
                          query_value=target_country,
                          query_col=10000,
                          get_header=True)
    def test_get_data_query_lines(self):
        fire_file_name = 'Agrofood_co2_emission.csv'
        gdp_file_name = 'IMF_GDP.csv'
        empty_file_name = 'empty.txt'
        
        target_country = 'Zimbabwe'
        
        self.assertEqual(len(fire_gdp.get_data(fire_file_name, 
                                               query_value=target_country, 
                                               query_col=0)), 
                        31)
        
        self.assertEqual(len(fire_gdp.get_data(gdp_file_name,
                                               query_value=target_country,
                                               query_col=0)), 
                         1)
        
        self.assertEqual(len(fire_gdp.get_data(empty_file_name,
                                               query_value=target_country,
                                               query_col=0)),
                         0)
        
        self.assertEqual(len(fire_gdp.get_data(gdp_file_name,
                                               query_value=target_country,
                                               query_col=1)), 
                         0)
        
        self.assertRaises(IndexError,
                          fire_gdp.get_data,
                          gdp_file_name,
                          query_value=target_country,
                          query_col=10000)

        
        
if __name__ == '__main__':
    unittest.main()
  
 