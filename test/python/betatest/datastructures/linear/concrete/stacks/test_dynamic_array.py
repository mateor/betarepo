# coding=utf-8
# The MIT License (MIT)
# Copyright (c) 2016 mateor

from __future__ import (absolute_import, division, generators, nested_scopes, print_function,
                        unicode_literals, with_statement)

import unittest

from betarepo.datastructures.linear.concrete.stacks.dynamic_array_stack import DynamicArrayStack, DEFAULT_GROWTH_FACTOR

from betatest.datastructures.linear.concrete.stacks.stack_test_base import StackTestBase, StackException


class DynamicArrayTest(StackTestBase, unittest.TestCase):

  @classmethod
  def stack_class(cls):
    # Used by the tests in stack_test_base.
    return DynamicArrayStack

  @classmethod
  def default_capacity(cls):
    # Used by the tests in stack_test_base.
    return None

  def test_no_stack_overflow(self):
    self.assertTrue(self.stack.is_empty())
    self.fill_stack(self.stack)
    self.assertEqual(self.stack.size, self.capacity)
    self.stack.push(100)

  def test_resizing(self):
    self.fill_stack(self.stack)
    self.assertEqual(self.stack.size, self.capacity)
    self.stack.push(99)
    self.assertEqual(self.stack.capacity, self.capacity * DEFAULT_GROWTH_FACTOR)

