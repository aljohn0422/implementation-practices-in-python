import unittest
import random
from unittest.case import TestCase

from sorting.insertion import insertion_sort
from sorting.bubble import bubble_sort
from sorting.selection import selection_sort
from sorting.counting import counting_sort
from sorting.merge import merge_sort
from sorting.quick import quick_sort
from structure.hash_table import HashTable


class TestSortingAlgorithms(unittest.TestCase):
    def setUp(self) -> None:
        self.arr = [random.randint(1, 50) for i in range(20)]

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


class TestDataStructures(unittest.TestCase):
    def test_hash_table(self):
        ht = HashTable()
        ht.put(2, 5)
        ht.put(2, 3)
        ht.put(10, 28)
        ht.put(20, 3)
        self.assertEqual(ht.get(2), 3)
        self.assertEqual(ht.get(10), 28)


if __name__ == '__main__':
    unittest.main()
