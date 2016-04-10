# coding=utf-8
# The MIT License (MIT)
# Copyright (c) 2016 mateor

from __future__ import (absolute_import, division, generators, nested_scopes, print_function,
                        unicode_literals, with_statement)


import unittest
import random

from betarepo.datastructures.comparison_mixin import ComparisonMixin


class Heap(ComparisonMixin, object):

  class Node(object):

    # TODO(mateo): Maybe create a TreeNode superclass. Not sure what this would inherit though.
    def __init__(self, value):
      self.value = value

    @property
    def left(self):
      """Return the index number for the node's left child - does not verify or check for existance."""
      #  Known to be 2*k + 1
      return 2 * self.index + 1

    @property
    def right(self):
      """Return the index number for the node's right child - does not verify or check for existance."""
      #  Known to be 2*k + 2
      return 2 * self.index + 2

    def __repr__(self):
      # This should perhaps return the value.
      return 'Node: {}'.format(self.value)

    def __key__(self):
      return self.index


  @staticmethod
  def parent_index(index):
    return (index - 1)/2

  def __init__(self):
    self.root = None
    self.heap = []
    self.item_count = 0

  def get_value(self, index):
    return self.heap[index].value

  # def set_node(self, node, index):
  #   if index == 0:
  #     self.root = node
  #   self.item_count += 1
  #   self.heap.append(node)

  def heapify(self, value):
    node = self.Node(value)
    position = self.item_count
    self.item_count += 1
    while position > 0 and value < self.heap[(position-1)/2].value:
      import pdb; pdb.set_trace()
      self.heap[position] = self.heap[(position-1)/2]
     # self.set_node(self.heap[(position-1)/2], position)
      position = (position-1)/2
    self.heap[position] = node
    print("HERE WE ARE:", self)

  def __repr__(self):
    return '{}'.format(self.heap)