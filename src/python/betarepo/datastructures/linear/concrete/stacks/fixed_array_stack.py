# coding=utf-8
# The MIT License (MIT)
# Copyright (c) 2016 mateor

from __future__ import (absolute_import, division, generators, nested_scopes, print_function,
                        unicode_literals, with_statement)


from betarepo.datastructures.linear.abstract.stack import Stack, StackException


DEFAULT_CAPACITY = 10

class FixedArrayStack(Stack):
  """A list-based LIFO stack that raises a StackException on overflow/underflow."""

  def __init__(self, capacity=None):
    # Explicitly check for None because a zero-size stack would fail the falsey check.
    self.capacity = capacity if capacity is not None else DEFAULT_CAPACITY
    self.size = 0
    self.items = []

  # TODO(mateo): These magic methods should probably be put somewhere they can be reused, since I am now compposing this
  # class instead of inheriting from it.
  def __iter__(self):
    i = 0
    while i < len(self.items):
      yield self.items[i]
      i += 1

  def __getitem__(self,index):
    return self.items[index]

  def __len__(self):
    return len(self.items)

  def __repr__(self):
    return 'Stack[{}] = {}'.format(self.capacity, self.items)

  def push(self, x):
    # TODO(mateo): A mxin that validates BaseType? Can be constant time but will it cause runtime analysis issues?
    # Does no validation of type
    if self.size != self.capacity:
      self.items.append(x)
      self.size += 1
    else:
      raise StackException("This stack of size {} is full!".format(self.capacity))

  def pop(self):
    if self.items:
      elem, self.items = self.items[-1], self.items[:-1]
      self.size -= 1
      return elem
    else:
      raise StackException('Tried to pop() from an empty stack!')

  def is_empty(self):
    return not self.items

  def make_empty(self):
    self.items = []
    self.size = 0
