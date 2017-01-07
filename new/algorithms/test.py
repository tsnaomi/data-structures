# coding='utf-8'

import unittest

from insertion_sort import insertion_sort
from merge_sort import merge_sort
from quicksort import hoare_quicksort, lumoto_quicksort
from radix_sort import radix_sort


class TestInsertionSort(unittest.TestCase):

    def setUp(self):
        self.sort = insertion_sort
        self.unsorted_list = [3, 1, 4, 5, 9, 2, 6, 5, 3, 8, 9, 7, 9]
        self.sorted_list = sorted(self.unsorted_list)
        self.reversed_list = list(reversed(self.sorted_list))

    def test_insertSort(self):
        self.assertEqual(self.sort(self.unsorted_list), self.sorted_list)

    def test_insertSort_empty(self):
        self.assertEqual(self.sort([]), [])

    def test_insertSort_singleton(self):
        self.assertEqual(self.sort([3]), [3])

    def test_insertSort_sorted(self):
        self.assertEqual(self.sort(self.sorted_list), self.sorted_list)

    def test_insertSort_reversed(self):
        self.assertEqual(self.sort(self.reversed_list), self.sorted_list)


class TestMergeSort(unittest.TestCase):

    def setUp(self):
        self.sort = merge_sort
        self.unsorted_list = [3, 1, 4, 5, 9, 2, 6, 5, 3, 8, 9, 7, 9]
        self.sorted_list = sorted(self.unsorted_list)
        self.reversed_list = list(reversed(self.sorted_list))

    def test_mergeSort(self):
        self.assertEqual(self.sort(self.unsorted_list), self.sorted_list)

    def test_mergeSort_empty(self):
        self.assertEqual(self.sort([]), [])

    def test_mergeSort_singleton(self):
        self.assertEqual(self.sort([3]), [3])

    def test_mergeSort_sorted(self):
        self.assertEqual(self.sort(self.sorted_list), self.sorted_list)

    def test_mergeSort_reversed(self):
        self.assertEqual(self.sort(self.reversed_list), self.sorted_list)


class TestQuicksort(unittest.TestCase):

    def setUp(self):
        self.hoareSort = hoare_quicksort
        self.lumotoSort = lumoto_quicksort
        self.unsorted1 = [3, 1, 4, 5, 9, 2, 6, 5, 3, 8, 9, 7, 9]
        self.unsorted2 = [3, 1, 4, 5, 9, 2, 6, 5, 3, 8, 9, 7, 9]
        self.sorted_list = sorted(self.unsorted1)
        self.reversed_list = list(reversed(self.sorted_list))

    def test_quicksort(self):
        # hoare partition
        self.assertEqual(self.hoareSort(self.unsorted1), self.sorted_list)

        # lumoto partition
        self.assertEqual(self.lumotoSort(self.unsorted2), self.sorted_list)

    def test_quicksort_empty(self):
        # hoare partition
        self.assertEqual(self.hoareSort([]), [])

        # lumoto partition
        self.assertEqual(self.lumotoSort([]), [])

    def test_quicksort_singleton(self):
        # hoare partition
        self.assertEqual(self.hoareSort([3]), [3])

        # lumoto partition
        self.assertEqual(self.lumotoSort([3]), [3])

    def test_quicksort_sorted(self):
        # hoare partition
        self.assertEqual(self.hoareSort(self.sorted_list), self.sorted_list)

        # lumoto partition
        self.assertEqual(self.lumotoSort(self.sorted_list), self.sorted_list)

    def test_quicksort_reversed(self):
        # lumoto partition
        self.assertEqual(self.hoareSort(self.reversed_list), self.sorted_list)

        # hoare partition
        self.assertEqual(self.lumotoSort(self.reversed_list), self.sorted_list)


class TestRadixSort(unittest.TestCase):

    def setUp(self):
        self.sort = radix_sort
        self.unsorted_list = [3, 1, 4, 5, 9, 2, 6, 5, 3, 8, 9, 2400, 24, 240]
        self.sorted_list = sorted(self.unsorted_list)
        self.reversed_list = list(reversed(self.sorted_list))

    def test_mergeSort(self):
        self.assertEqual(self.sort(self.unsorted_list), self.sorted_list)

    def test_mergeSort_empty(self):
        self.assertEqual(self.sort([]), [])

    def test_mergeSort_singleton(self):
        self.assertEqual(self.sort([3]), [3])

    def test_mergeSort_sorted(self):
        self.assertEqual(self.sort(self.sorted_list), self.sorted_list)

    def test_mergeSort_reversed(self):
        self.assertEqual(self.sort(self.reversed_list), self.sorted_list)


if __name__ == '__main__':
    unittest.main()
