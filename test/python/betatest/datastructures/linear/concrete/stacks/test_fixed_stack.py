# coding=utf-8
# The MIT License (MIT)
# Copyright (c) 2016 mateor

from __future__ import (absolute_import, division, generators, nested_scopes, print_function,
                        unicode_literals, with_statement)


import unittest

from betarepo.datastructures.linear.concrete.stacks.fixed_array_stack import (
  DEFAULT_MAX_SIZE, FixedArrayStack, StackException)


class SortTest(unittest.TestCase):

  def setUp(self):
    self.stack = FixedArrayStack()

  def test_stack_empty(self):
    self.assertTrue(self.stack.is_empty())
    self.stack.push(6)
    self.assertFalse(self.stack.is_empty())

  def test_add_item(self):
    self.assertTrue(self.stack.is_empty())
    self.stack.push(6)
    self.assertEqual(self.stack.items, 1)

  def test_stack_overflow(self):
    self.assertTrue(self.stack.is_empty())
    for i in range(DEFAULT_MAX_SIZE):
      self.stack.push(i)
    self.assertEqual(self.stack.items, DEFAULT_MAX_SIZE)
    with self.assertRaises(StackException):
      self.stack.push(DEFAULT_MAX_SIZE + 1)

  def test_size_override(self):
    bigger_limit = 15
    bigger_stack = FixedArrayStack(bigger_limit)
    for i in range(bigger_limit):
      bigger_stack.push(i)
    self.assertEqual(bigger_stack.items, bigger_limit)

  def test_no_push_allowed(self):
    zero_size = FixedArrayStack(0)
    with self.assertRaises(StackException):
      zero_size.push(9)

  def test_pop(self):
    self.stack.push(9)
    self.assertEqual(self.stack.items, 1)
    self.assertEqual(9, self.stack.pop())
    self.assertEqual(self.stack.items, 0)

  def test_pop_but_no_items(self):
    with self.assertRaises(StackException):
      self.stack.pop()

  def test_lifo_order(self):
    int_range = [ i for i in range(DEFAULT_MAX_SIZE)]
    for i in int_range:
      self.stack.push(i)
    reverse_order = reversed(int_range)
    for i in reverse_order:
      self.assertEqual(i, self.stack.pop())
    self.assertTrue(self.stack.is_empty())

  def test_make_empty(self):
    int_range = [ i for i in range(DEFAULT_MAX_SIZE)]
    for i in int_range:
      self.stack.push(i)
    self.assertEqual(DEFAULT_MAX_SIZE, self.stack.items)
    self.stack.make_empty()
    self.assertTrue(self.stack.is_empty)
    self.assertEqual(self.stack.stack, [])
    self.assertEqual(self.stack.items, 0)