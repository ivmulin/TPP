import unittest
from graphs import Dijkstra, Floyd, Tarjan

class test_graphs(unittest.TestCase):
    def setUp(self):

        self.Graph1 = [
            {1: 2, 2: 1},
            {0: 2},
            {0: 1}
        ]

        self.Graph2 = [
            {2: 1, 3: 2},
            {3: 4},
            {0: 1, 3: 1},
            {0: 4, 1: 4, 2: 1}
        ]
        
        self.Graph3 = [
            {1: 1, 4: 1}, 
            {0: 1, 2: 1, 4: 1},
            {1: 1, 3: 1},
            {2: 1, 5: 1, 4: 1},
            {0: 1, 1: 1, 3: 1},
            {3: 1}
        ]

        self.iGraph = [
            [],
            [],
            [3],
            [1],
            [0, 1],
            [0, 2]
        ]

    def test_Dijkstra(self):
        self.assertEqual( Dijkstra(self.Graph1, 0), [0, 2, 1])
        self.assertEqual( Dijkstra(self.Graph2, 0), [0, 6, 1, 2])
        self.assertEqual( Dijkstra(self.Graph3, 0), [0, 1, 2, 2, 1, 3])

    def test_Floyd(self):
        self.assertEqual( Floyd(self.Graph1), [[0, 2, 1], [2, 0, 3], [1, 3, 0]])
        self.assertEqual( Floyd(self.Graph2), [[0, 6, 1, 2], [6, 0, 5, 4], [1, 5, 0, 1], [2, 4, 1, 0]])

    def test_Tarjan(self):
        self.assertEqual( Tarjan(self.iGraph), [5, 4, 2, 3, 1, 0] )


if __name__ == "__main__":
    unittest.main(verbosity=2)
