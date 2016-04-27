# coding=utf-8
# The MIT License (MIT)
# Copyright (c) 2016 mateor

from __future__ import (absolute_import, division, generators, nested_scopes, print_function,
                        unicode_literals, with_statement)


from betarepo.datastructures.linear.concrete.stacks.fixed_array_stack import FixedArrayStack
from betarepo.datastructures.linear.abstract.stack import Stack, StackException


DEFAULT_GROWTH_FACTOR = 1.5

class DynamicArrayStack(Stack):
  """
  Overallocate the array if pushing an item to an already full stack.

  The array size grows by a factor of a, and inserting n elements takes O(n) time overall - so each insertion is
  constant amortized time.
   """

  # TOD)(mateo): Refactor in a major way. This is too much code for this idea.
  # The issue is that this models best if the DynamicArray implements a a wrapper around the FixedArray.
  # BUt then it requires all these method wrapper - there is a better way.

  # Maybe a decorator - although I don't want it adding noise perf analysis.

  # TODO(deallocate - must be a threshold less than 1/a to proovide hysteresis)

  def __init__(self, capacity=None, growth_factor=None):
    self.growth_factor = growth_factor or DEFAULT_GROWTH_FACTOR
    self.stack = FixedArrayStack(capacity)

  def __len__(self):
    return len(self.stack)

  def __repr__(self):
    return repr(self.stack)

  def __getitem__(self,index):
    return self.stack[index]

  def __iter__(self):
    i = 0
    while i < len(self.stack):
      yield self.stack[i]
      i += 1

  @property
  def size(self):
    return self.stack.size

  @property
  def capacity(self):
    return self.stack.capacity

  def push(self, value):
    try:
      self.stack.push(value)
    except StackException:
      self.resize()
      self.push(value)

  def pop(self):
    return self.stack.pop()

  def is_empty(self):
    return self.stack.is_empty()

  def make_empty(self):
    return self.stack.make_empty()

  def resize(self):
    new_size = int(self.stack.capacity * self.growth_factor)
    resized_stack = FixedArrayStack(capacity=new_size)
    for i in self.stack:
      resized_stack.push(i)
    self.stack = resized_stack
