import unittest
import random

from insertion import insertion_sort
from bubble import bubble_sort
from selection import selection_sort
from counting import counting_sort
from merge import merge_sort
from quick import quick_sort


class TestSortingAlgorithms(unittest.TestCase):
    def setUp(self) -> None:
        self.arr = [random.randint(1, 50) for i in range(8)]

    def test_insertion_sort(self):
        sorted_arr = insertion_sort(self.arr)
        self.assertEqual(sorted_arr, sorted(self.arr))

    def test_bubble_sort(self):
        sorted_arr = bubble_sort(self.arr)
        self.assertEqual(sorted_arr, sorted(self.arr))

    def test_selection_sort(self):
        sorted_arr = selection_sort(self.arr)
        self.assertEqual(sorted_arr, sorted(self.arr))

    def test_counting_sort(self):
        sorted_arr = counting_sort(self.arr)
        self.assertEqual(sorted_arr, sorted(self.arr))

    def test_merge_sort(self):
        sorted_arr = merge_sort(self.arr)
        self.assertEqual(sorted_arr, sorted(self.arr))

    def test_quick_sort(self):
        sorted_arr = quick_sort(self.arr)
        self.assertEqual(sorted_arr, sorted(self.arr))


if __name__ == '__main__':
    unittest.main()
