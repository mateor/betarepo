# coding=utf-8
# The MIT License (MIT)
# Copyright (c) 2016 mateor

from __future__ import (absolute_import, division, generators, nested_scopes, print_function,
                        unicode_literals, with_statement)


from betarepo.datastructures.linear.concrete.stacks.fixed_array_stack import FixedArrayStack, StackException
from betarepo.datastructures.linear.abstract.stack import Stack


DEFAULT_GROWTH_FACTOR = 1.5

class DynamicArrayStack(FixedArrayStack):

  def resize(self):
    new_size = int(self.stack.capacity * self.growth_factor)
    resized_stack = FixedArrayStack(capacity=new_size)
    for i in self.stack:
      resized_stack.push(i)
    self.stack = resized_stack

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