import unittest
import ugen

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual(ugen.generateFromTxtFile(),'1234:jmhurban:Jozef:Miloslav:Hurban:Legal')

if __name__ == '__main__':
    unittest.main()