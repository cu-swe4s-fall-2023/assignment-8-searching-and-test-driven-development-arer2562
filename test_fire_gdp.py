import unittest
import fire_gdp
import random
import numpy as np
import matplotlib.pyplot as plt
from io import StringIO
import os

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

    def test_get_data_fire_and_year(self):
        fire_file_name = 'Agrofood_co2_emission.csv'
        target_country = 'Albania'
        
        data = fire_gdp.get_data(fire_file_name, 
                                 query_value=target_country, 
                                 query_col=0)
        
        self.assertEqual(data[0][0], 'Albania')
        self.assertEqual(data[0][1], '1990')
        self.assertEqual(data[1][2], '5.5561')
    
    def test_get_gdpr(self):
        gdp_file_name = 'IMF_GDP.csv'
        target_country = 'Albania'
        
        data = fire_gdp.get_data(gdp_file_name, 
                                 query_value=target_country, 
                                 query_col=0)
        
        self.assertEqual(data[0][2], '...')
        self.assertEqual(data[0][47],'334,359.13')
    
    def test_get_fire_gdp_year_data(self):
        fire_file_name = 'Agrofood_co2_emission.csv'
        gdp_file_name = 'IMF_GDP.csv'

        fire_year_col = 1
        fire_savanna_col = 2
        fire_forest_col = 3
        fire_Co2_col = 29
        
        # 1: [ [fire], [gdp], [year] ]
        
        country = 'Albania'
        
        data = fire_gdp.get_fire_gdp_year_data(fire_file_name,
                                               gdp_file_name,
                                               country,
                                               fire_year_col,
                                               fire_savanna_col,
                                               fire_forest_col,
                                               fire_Co2_col)

        fire = data[0]
        gdp = data[1]
        year = data[2]
        co2 = data[3]
        
        self.assertEqual(1.3469 + 13.3278, fire[0])
        self.assertEqual(334359.13, gdp[0])
        self.assertEqual(1996, year[0])
        self.assertEqual(3231.9567474710607, co2[0])
    
    def test_scat(self):
        # Create random data for testing
        data = np.random.rand(10, 2)

        # Call the scat function with the random data
        country = 'test'
        infile = 'test_data.txt'
        out_file = 'test_scatter.png'

        with open(infile, 'w') as f:
            for row in data:
                f.write(f'{row[0]}\t{row[1]}\n')

        fire_gdp.scat(country, infile, out_file)

        # Check if the output file was created
        self.assertTrue(os.path.isfile(out_file))

    def tearDown(self):
        # Clean up by removing the output file and the test data file
        if os.path.isfile('test_scatter.png'):
            os.remove('test_scatter.png')
        if os.path.isfile('test_data.txt'):
            os.remove('test_data.txt')
        
if __name__ == '__main__':
    unittest.main()
  
 