import unittest
import kar


class test_kar(unittest.TestCase):
    def setUp(self):
        G1 = [
            {3},
            {3, 5},
            {1, 4},
            {2, 4},
            {1, 5},
            {0, 2}
        ]
        self.f = G1.copy()
        self.w = G1.copy()
        self.t = G1.copy()


    def test_F(self):
        self.assertEqual( kar.F( self.f ), [0, 3, 2, 1, 3, 4, 1, 5, 2, 4, 5, 0] )
    
    def test_W(self):
        self.assertEqual( kar.W( self.w ), [0, 3, 2, 1, 3, 4, 1, 5, 2, 4, 5, 0] )
    
    def test_T(self):
        self.assertEqual( kar.T( self.t ), [0, 3, 2, 1, 5, 4] )

if __name__ == "__main__":
    unittest.main(verbosity=2)
