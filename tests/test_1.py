import unittest
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.insert(0, parent_dir)

from src.main import printfunc as pf

class TestPrint(unittest.TestCase):
    '''Unit test for print function'''
    def test_print(self):
        '''Test print function'''
        assert pf("String of text") == print("String of text")

if __name__ == "__main__":
    unittest.main()