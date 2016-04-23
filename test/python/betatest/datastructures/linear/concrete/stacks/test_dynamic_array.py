# coding=utf-8
# The MIT License (MIT)
# Copyright (c) 2016 mateor

from __future__ import (absolute_import, division, generators, nested_scopes, print_function,
                        unicode_literals, with_statement)

import unittest

from betarepo.datastructures.linear.concrete.stacks.fixed_array_stack import StackException
from betarepo.datastructures.linear.concrete.stacks.dynamic_array_stack import DynamicArrayStack

from betatest.datastructures.linear.concrete.stacks.stack_test_base import StackTestBase


class DynamicArrayTest(StackTestBase, unittest.TestCase):

  @classmethod
  def stack_class(cls):
    """Subclasses must return the Stack class the tests need to exercise."""
    return DynamicArrayStack

  @classmethod
  def capacity(cls):
    return None

  def test_pop_but_no_items(self):
    with self.assertRaises(StackException):
      self.stack.pop()

  def test_no_stack_overflow(self):
    self.assertTrue(self.stack.is_empty())
    for i in range(self.default_capacity):
      self.stack.push(i)
    self.assertEqual(self.stack.size, self.default_capacity)
    self.stack.push(100)
