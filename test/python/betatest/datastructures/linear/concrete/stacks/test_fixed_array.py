# coding=utf-8
# The MIT License (MIT)
# Copyright (c) 2016 mateor

from __future__ import (absolute_import, division, generators, nested_scopes, print_function,
                        unicode_literals, with_statement)

import unittest

from betarepo.datastructures.linear.concrete.stacks.fixed_array_stack import (
  DEFAULT_CAPACITY, FixedArrayStack, StackException)

from betatest.datastructures.linear.concrete.stacks.stack_test_base import StackTestBase


class FixedArrayTest(StackTestBase, unittest.TestCase):

  @classmethod
  def stack_class(cls):
    # Used by the tests in stack_test_base.
    return FixedArrayStack

  @classmethod
  def default_capacity(cls):
    # Used by the tests in stack_test_base.
    return DEFAULT_CAPACITY

  def test_stack_overflow(self):
    self.assertTrue(self.stack.is_empty())
    for i in range(self.capacity):
      self.stack.push(i)
    self.assertEqual(self.stack.size, self.capacity)
    with self.assertRaises(StackException):
      self.stack.push(self.capacity + 1)
