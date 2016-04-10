# coding=utf-8
# The MIT License (MIT)
# Copyright (c) 2016 mateor

from __future__ import (absolute_import, division, generators, nested_scopes, print_function,
                        unicode_literals, with_statement)


# ComplexityTheta(n log n)
# A bit slower in practice than quicksort - but has a better
# worst-case runtime.

# It can be slower than quicksort in practice because the worst-case
# of quicksort in most impls is very rare. And in heapsort
# there are a lot of element swaps, even if the data is already
# ordred.

# Not stable!

# Put the data in a min/max heap. The root is then the min/max.

# When an element is removed from the heap, it self balances
# so the next element will "bubble up" to the root. The
# heap operations are all superlinear - putting the elements
# in the list is dstrictly linear and is dominated by the heap operations.


# Heap properties
# Use a min-heap with the heap property of: A[PARENT (i)] <= A[i]
# Height of tree with n nodes is floor(lg n)
# nodes to height bounds: 2^h <= n <= 2^(h+1)-1  -- i.e. the last level must be between empty and full - 1.

# heapify - add an element and bubble it up to its proper position in the heap. O(lg n) - the heigth of the tree
# build_heap - linear time
# heap sort - O(n lg n)
# extract-min = remove the root rebalance= - O(lg n)

# Heap is a full binary tree (no empty spaces in interior levels) - so it can be represented as an array,
# which is space efficient.


import unittest
import random

from betarepo.datastructures.comparison_mixin import ComparisonMixin
from betarepo.datastructures.trees.heap import Heap


def heapsort(A):
  # implement when the heap is done.
  pass


### Test Suite ###


if __name__ == '__main__':
  #unittest.main()
  greg = Heap()
  nums = [2, 3, 6, 7, 8, 5, 90, 11, 78, 1, ]
  for num in nums:
    greg.heapify(num)

  import pdb; pdb.set_trace()


 # Not yet ready to break into its own test yet.

class SortTest(unittest.TestCase):

  def test_empty(self):
    self.assertEqual(insertionsort([]), [])

  def test_single(self):
    self.assertEquals(insertionsort([1]), [1])

  def test_base_case(self):
    self.assertEqual(insertionsort([1, 0]), [0, 1])

  def test_simple(self):
    self.assertEqual(insertionsort([4, 5, 5, 3]), [3, 4, 5, 5])

  def test_sorted(self):
    self.assertEquals(insertionsort([1, 2, 3]), [1, 2, 3])

  def test_sorts_last(self):
    self.assertEquals(insertionsort([1, 1, 1, 1, 1, 1, 1, 1, 1, 0]), [0, 1, 1, 1, 1, 1, 1, 1, 1, 1] )

  def test_returns_all_elements(self):
    random_list = [ random.randint(-100, 100) for i in range(random.randint(0, 200))]
    length = len(random_list)
    self.assertEquals(len(insertionsort(random_list)), length)

  def test_is_sorted(self):
    random_list = [ random.randint(-100, 100) for i in range(random.randint(0, 200))]
    self.assertEquals((insertionsort(random_list)), sorted(random_list))

  def test_mixed_types(self):
    a_list = [1,  'game', "baldur's gate", 2, 'a', 9, 4, 5, -99, 99]
    self.assertEquals(insertionsort(a_list), sorted(a_list))

  def test_bad_input(self):
    with self.assertRaises(TypeError):
      insertionsort('a very bad memory of not remembering an ascii code')

### Test Suite ###

