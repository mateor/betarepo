# coding=utf-8
# The MIT License (MIT)
# Copyright (c) 2016 mateor

from __future__ import (absolute_import, division, generators, nested_scopes, print_function,
                        unicode_literals, with_statement)


# TODO(mateo): Enforce that this is an abstract class. Maybe scrap it entirely.
class StackTestBase(object):

  @classmethod
  def stack_class(cls):
    """Subclasses must return the Stack class the tests need to exercise."""
    raise NotImplementedError()

  @classmethod
  def capacity(cls):
    """Subclasses must return the Stack class the tests need to exercise."""
    return None

  def setUp(self):
    stack = self.stack_class()
    self.stack = stack()
    self.default_capacity = self.capacity() or 10

  def test_stack_empty(self):
    self.assertTrue(self.stack.is_empty())
    self.stack.push(6)
    self.assertFalse(self.stack.is_empty())

  def test_add_item(self):
    self.assertTrue(self.stack.is_empty())
    self.stack.push(6)
    self.assertEqual(self.stack.size, 1)

  def test_size_override(self):
    bigger_limit = 15
    stack_class = self.stack_class()
    bigger_stack = stack_class(bigger_limit)
    for i in range(bigger_limit):
      bigger_stack.push(i)
    self.assertEqual(bigger_stack.size, bigger_limit)

  def test_pop(self):
    self.stack.push(9)
    self.assertEqual(self.stack.size, 1)
    self.assertEqual(9, self.stack.pop())
    self.assertEqual(self.stack.size, 0)


  def test_lifo_order(self):
    int_range = [ i for i in range(self.default_capacity)]
    for i in int_range:
      self.stack.push(i)
    reverse_order = reversed(int_range)
    for i in reverse_order:
      self.assertEqual(i, self.stack.pop())
    self.assertTrue(self.stack.is_empty())

  def test_make_empty(self):
    int_range = [ i for i in range(self.default_capacity)]
    for i in int_range:
      self.stack.push(i)
    self.assertEqual(self.default_capacity, self.stack.size)
    self.stack.make_empty()
    self.assertTrue(self.stack.is_empty)
    self.assertEqual(self.stack.size, 0)
