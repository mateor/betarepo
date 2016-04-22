# coding=utf-8
# The MIT License (MIT)
# Copyright (c) 2016 mateor

from __future__ import (absolute_import, division, generators, nested_scopes, print_function,
                        unicode_literals, with_statement)


from betarepo.datastructures.linear.abstract.stack import Stack

DEFAULT_MAX_SIZE = 10

class StackException(Exception):
  """Raise when a stack method would cause the stack to reach an illegal state,."""

class FixedArrayStack(Stack):
  """A list-based LIFO stack that raises a StackException on overflow/underflow."""

  def __init__(self, size=None):
    # Explicitely check for None because a zero-sized stack would fail the falsey check.
    self.max_size = size if size is not None else DEFAULT_MAX_SIZE
    self.items = 0
    self.stack = []

  def push(self, x):
    # TODO(mateo): A mxin that validates BaseType? Can be constant time but will it cause runtime analysis issues?
    # Does no validation of type
    if self.items != self.max_size:
      self.stack.append(x)
      self.items += 1
    else:
      raise StackException("This stack of size {} is full!".format(self.max_size))

  def pop(self):
    if self.stack:
      elem, self.stack = self.stack[-1], self.stack[:-1]
      self.items -= 1
      return elem
    else:
      raise StackException('Tried to pop() from an empty stack!')

  def is_empty(self):
    return not self.stack

  def make_empty(self):
    self.stack = []
    self.items = 0
