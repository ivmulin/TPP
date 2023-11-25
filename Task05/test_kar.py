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


    def test_Fleury(self):
        self.assertEqual( kar.Fleury( self.f ), [0, 3, 2, 1, 3, 4, 1, 5, 2, 4, 5, 0] )
    
    def test_CycleAlgorithm(self):
        self.assertEqual( kar.CycleAlgorithm( self.w ), [0, 3, 2, 1, 3, 4, 1, 5, 2, 4, 5, 0] )
    
    def test_Kosaraju(self):
        self.assertEqual( kar.Kosaraju( self.t ), [0, 3, 2, 1, 5, 4] )

if __name__ == "__main__":
    unittest.main(verbosity=2)
