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


import random

from betarepo.datastructures.comparison_mixin import ComparisonMixin
from betarepo.datastructures.trees.heap import Heap


def heapsort(A):
  # HEAPSORT procedure takes time O(n lg n), since the call to BUILD_HEAP takes time O(n) and
  #  each of the n -1 calls to Heapify takes time O(lg n).


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
