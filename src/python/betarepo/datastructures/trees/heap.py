# coding=utf-8
# The MIT License (MIT)
# Copyright (c) 2016 mateor

from __future__ import (absolute_import, division, generators, nested_scopes, print_function,
                        unicode_literals, with_statement)


from betarepo.datastructures.comparison_mixin import ComparisonMixin


class Heap(ComparisonMixin):
  """An array-based implementation of a heap binary tree.


  """
  # An array is a good fit for a heap because a heap is a complete binary tree and we can use 
  # O(1) operations to jump to children instead of storing and following pointers. Very space efficient as well.

  # BinaryHeap is a binary tree with two additional constraints.
    # Shape property
    #    * A complete binary tree
    #         * all levels but the last are full and levels fill from left to right.
    # Heap Property
    #     * All node values are >= or <=  each of their children
    #         * Either a min heap (all children >=) or a max heap (all all children <=)

  # Heaps are useful for:
  #    * priority queues.
  #    * selection algorithms
  #       * e.g. find the kth order statistic ( the kth smallest number in a list or array)
  #         heap is obviously useful for the min/max depending on the heap.
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

  def __init__(self, A, min_heap=True):
    self.root = A[0]
    self.heap = A
    self.count = len(A) - 1



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

  def sift_down(self, index):
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
    index = self.count

    # TODO(mateo) - make a dynamicly resizing queue for this.
    self.heap.append(value)
    self.count += 1
    self.sift_down(index)


  def __repr__(self):
    return '{}'.format(self.heap)

greg = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
joey = Heap(greg)
# joey.heap[10] > joey.heap[joey.parent(10)]