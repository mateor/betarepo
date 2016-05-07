# coding=utf-8
# The MIT License (MIT)
# Copyright (c) 2016 mateor

from __future__ import (absolute_import, division, generators, nested_scopes, print_function,
                        unicode_literals, with_statement)


import math
import random

from betarepo.datastructures.comparison_mixin import ComparisonMixin


class ArrayHeap(ComparisonMixin):
  """An array-based implementation of a heap binary tree.


  """
  # An array is a good fit for a heap because a heap is a complete binary tree and we can use 
  # O(1) operations to jump to children instead of storing and following pointers. Very space efficient as well.

  # BinaryHeap is a binary tree with two additional constraints.
    # Shape property
    #    * A complete binary tree
    #         * all levels but possibly the last are full and levels fill from left to right.
    # Heap Property
    #     * Heaps are either:
    #         * empty
    #          or
    #         * Root has a value greater than both children or less than both children
    #       Each child is the root of heap maintaining that saem contract.

  # Heaps are useful for:
  #    * priority queues (usually with a max heap).
  #    * selection algorithms
  #       * e.g. find the kth order statistic ( the kth smallest number in a list or array)
  #         heap is obviously useful for the min or max.
  #    * Graph algorithms, like Prims and Dijkstras shortest path.
  #

  # The levels above the lowest level of a heap are always full and always have 2^h nodes
  # So a complete binary tree of height h has 2h+1 -1 nodes.

  # an n-element heap has height floor(log n) 


  @staticmethod
  def parent(index):
    return (index - 1)//2

  @staticmethod
  def left(index):
    """Return the index number for the node's left child - does not verify or check for existence."""
    return 2 * index + 1

  @staticmethod
  def right(index):
    """Return the index number for the node's right child - does not verify or check for existence."""
    return 2 * index + 2

  @staticmethod
  def height(size):
    return int(math.log(size, 2) + 1)

  def __init__(self, A, min_heap=True):
    self.root = A[0]
    self.heap = A
    self.size = len(A)



  # TODO(mateo) - enforce the heap properties with the cmp fn (return the bool as a function of min_heap=True).


  def get_value(self, index):
    return self.heap[index].value

  def build_heap(self, A):
    """Construct a heap out of an array of values.

    Linear on the number of elements in the array.
    """
    pass

  def extract_min(self):
    pass

  def extract_max(self):
    pass

  def _extract(self):
    # Extracts the min or max. Depending on the value of self.min_heap, the extract takes O(n) or O(log N).
    pass

  def bubble_up(self, index):
    """Add a node and enforce the heap properties.

    Runs in log N time.
    """

    value = self.heap[index]
    while index > 0 and value > self.heap[self.parent(index)]:

      # No need to swap - like insertion sort just add the parent value down and only do one set per loop.
      self.heap[index] = self.heap[self.parent(index)]
      index = self.parent(index)
    self.heap[index] = value


  # Since the elements in the subarray A[n/2 +1 . . n] are all leaves,
  # the procedure BUILD_HEAP goes through the remaining nodes of the tree and runs 'heapify' on each one


  def insert(self, value):
    index = self.size

    # TODO(mateo) - make a dynamicly resizing queue for this.
    self.heap.append(value)
    self.size += 1
    self.bubble_up(index)

# joey.heap[10] > joey.heap[joey.parent(10)]


# from betarepo.datastructures.trees.concrete.heaps.array_heap import ArrayHeap