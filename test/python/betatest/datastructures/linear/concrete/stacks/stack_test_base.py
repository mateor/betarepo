# coding=utf-8
# The MIT License (MIT)
# Copyright (c) 2016 mateor

from __future__ import (absolute_import, division, generators, nested_scopes, print_function,
                        unicode_literals, with_statement)

# TODO(mateo): Create a base exceptions module.
from betarepo.datastructures.linear.concrete.stacks.fixed_array_stack import StackException

# TODO(mateo): Enforce that this is an abstract class. Maybe scrap it entirely.
class StackTestBase(object):

  @classmethod
  def stack_class(cls):
    """Subclasses must return the Stack class the tests need to exercise."""
    raise NotImplementedError()

  @classmethod
  def default_capacity(cls):
    """Subclasses must return the Stack class the tests need to exercise."""
    return None

  @classmethod
  def fill_stack(self, stack):
    """Fill an empty stack instance up to the  declared capacity."""
    space = stack.capacity - stack.size
    for i in range(space):
      stack.push(i)

  def setUp(self):
    stack_class = self.stack_class()
    self.stack = stack_class()
    self.capacity = self.default_capacity() or 10

  def test_stack_empty(self):
    self.assertTrue(self.stack.is_empty())
    self.stack.push(6)
    self.assertFalse(self.stack.is_empty())

  def test_add_item(self):
    item = 6
    self.assertTrue(self.stack.is_empty())
    self.stack.push(item)
    self.assertEqual(self.stack.size, 1)
    self.assertIn(item, self.stack)

  def test_size_override(self):
    bigger_limit = self.capacity + 10
    stack_class = self.stack_class()
    bigger_stack = stack_class(bigger_limit)
    self.assertEqual(bigger_stack.capacity, bigger_limit)

  def test_pop(self):
    self.stack.push(9)
    self.assertEqual(self.stack.size, 1)
    self.assertEqual(9, self.stack.pop())
    self.assertEqual(self.stack.size, 0)

  def test_lifo_order(self):
    int_range = [ i for i in range(self.capacity)]
    for i in int_range:
      self.stack.push(i)
    reverse_order = reversed(int_range)
    for i in reverse_order:
      self.assertEqual(i, self.stack.pop())
    self.assertTrue(self.stack.is_empty())

  def test_make_empty(self):
    int_range = [ i for i in range(self.capacity)]
    for i in int_range:
      self.stack.push(i)
    self.assertEqual(self.capacity, self.stack.size)
    self.stack.make_empty()
    self.assertTrue(self.stack.is_empty)
    self.assertEqual(self.stack.size, 0)

  def test_pop_but_no_items(self):
    with self.assertRaises(StackException):
      self.stack.pop()