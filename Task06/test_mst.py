""" Unittest MST algorithms """

import unittest
import mst


class TestMst(unittest.TestCase):
    """ Tester """

    def setUp(self):
        self.graph1 = [
            {1: 5, 5: 3},
            {0: 5, 2: 4, 3: 3, 4: 7},
            {1: 4, 3: 6},
            {1: 3, 2: 6, 4: 5},
            {1: 7, 3: 5, 5: 2},
            {0: 3, 4: 2}
        ]

        self.graph2 = [
            {1: 3, 2: 4, 4: 1},
            {0: 3, 2: 5},
            {0: 4, 1: 5, 3: 2, 4: 6},
            {2: 2, 4: 7},
            {0: 1, 2: 6, 3: 7}
        ]

        self.result1 = [(0, 5), (5, 4), (0, 1), (1, 3), (1, 2)]
        self.result2 = [(0, 4), (0, 1), (0, 2), (2, 3)]

    def test_prim(self):
        """ Unittesting Prim's algorithm """
        self.assertEqual(mst.prim(self.graph1), self.result1)
        self.assertEqual(mst.prim(self.graph2), self.result2)

    def test_kruskal(self):
        """ Unittesting Kruskal's algorithm """
        self.assertEqual(mst.kruskal(self.graph1), [
                         [4, 5], [0, 5], [1, 3], [1, 2], [0, 1]])
        self.assertEqual(mst.kruskal(self.graph2), [
                         [0, 4], [2, 3], [0, 1], [0, 2]])


if __name__ == "__main__":
    unittest.main(verbosity=2)
