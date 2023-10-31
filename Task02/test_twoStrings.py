import unittest
from twoStrings import Slave


class Test(unittest.TestCase):
    def test_slave1(self):
        self.assertEqual( Slave("vadim", "vadimovich"), True )
    def test_slave2(self):
        self.assertEqual( Slave("adolf", "nastya"), False )
    def test_slave3(self):
        self.assertEqual( Slave("", "tim"), True )
    def test_slave4(self):
        self.assertEqual( Slave("aram", "rama"), True )

if __name__ == "__main__":
    unittest.main(verbosity=2)
