import unittest
from sortirovka import Sortirovka

class TestSortirovka(unittest.TestCase):
    def setUp(self):
        self.sortirovka = Sortirovka

    def test_insertion(self):
        self.assertEqual(self.sortirovka.Insertion([3]), [3])
        self.assertEqual(self.sortirovka.Insertion([0, -2, 15, 7]), [-2, 0, 7, 15])

    def test_selection(self):
        self.assertEqual(self.sortirovka.Selection([]), [])
        self.assertEqual(self.sortirovka.Selection([3, 1, 4, 2, 5, 8, 5]), [1, 2, 3, 4, 5, 5, 8])

    def test_bubble(self):
        self.assertEqual(self.sortirovka.Bubble([1, 2]), [1, 2])
        self.assertEqual(self.sortirovka.Bubble([3, 2, 7, 5, 92]), [2, 3, 5, 7, 92])

if __name__ == "__main__":
    unittest.main()
