import unittest 
from ToolBox.stats_tools import mean2, median2
import numpy
import pandas 


#from stats_tools import mean, median

class StatsToolsTests(unittest.TestCase):
    """Testing select stats tools"""
    def test_mean7(self):
        self.assertEqual(mean2(list(9,8,7,6,5)), 7)
    def test_median6(self):
        self.assertEqual(median2(5,6,7), 6)
class Df_Tools_Tests(unittest.TestCase):
    def test_thing(self):
        pass
if __name__ == '__main__':
    unittest.main()
