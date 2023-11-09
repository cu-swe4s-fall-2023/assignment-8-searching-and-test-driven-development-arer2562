import matplotlib.pyplot as plt
import pandas as pd
import pandas as pd
import sys
import clean
import four_panel
import unittest
import main
import os


class TestFireGDP(unittest.TestCase):
    def test_read_and_clean(self):
        clean.read_and_clean('assn_libs/Agrofood_co2_emission.csv')
        self.assertTrue(os.path.isfile('assn_libs/Agro_NA.csv'))
        clean.read_and_clean('assn_libs/IMF_GDP.csv')
        self.assertTrue(os.path.isfile('GDP_NA.csv'))
    def test_four_panel(self):
        main.main('assn_libs/Agro_NA.csv','assn_libs/GDP_NA.csv')
        self.assertTrue(os.path.isfile('assn_libs/4_panel.png'))
    
    
   
if __name__ == '__main__':
    unittest.main()
  
 