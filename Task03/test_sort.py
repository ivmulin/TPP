import unittest
import sort


class Test(unittest.TestCase):
    def test_mergeSort(self):
        self.assertEqual( sort.mergeSort([]), [])
        self.assertEqual( sort.mergeSort([4]), [4] )
        self.assertEqual( sort.mergeSort([2, -8]), [-8, 2] )
        self.assertEqual( sort.mergeSort([9, -3, 2, 17, 1, 2]), [-3, 1, 2, 2, 9, 17] )
        
    def test_fastSort(self):
        self.assertEqual( sort.fastSort([]), [])
        self.assertEqual( sort.fastSort([4]), [4] )
        self.assertEqual( sort.fastSort([2, -8]), [-8, 2] )
        self.assertEqual( sort.fastSort([9, -3, 2, 17, 1, 2]), [-3, 1, 2, 2, 9, 17] )

    def test_heapSort(self):
        self.assertEqual( sort.heapSort([]), [])
        self.assertEqual( sort.heapSort([4]), [4] )
        self.assertEqual( sort.heapSort([2, -8]), [-8, 2] )
        self.assertEqual( sort.heapSort([9, -3, 2, 17, 1, 2]), [-3, 1, 2, 2, 9, 17] )


if __name__ == "__main__":
    unittest.main()
