# coding=utf-8
# The MIT License (MIT)
# Copyright (c) 2016 mateor

from __future__ import (absolute_import, division, generators, nested_scopes, print_function,
                        unicode_literals, with_statement)


import unittest
import random

from betarepo.algorithms.sorting.bubblesort import bubblesort


# TODO(mateo): Since we are making this a repo - break this into a test library
# - there is little to no reason for the duplication between these various sorting tests.

# TODO(mateo): Write some tests that validates runtime - integration tests.

class SortTest(unittest.TestCase):

  def test_empty(self):
    self.assertEqual(bubblesort([]), [])

  def test_single(self):
    self.assertEquals(bubblesort([1]), [1])

  def test_base_case(self):
    self.assertEqual(bubblesort([1, 0]), [0, 1])

  def test_simple(self):
    self.assertEqual(bubblesort([4, 5, 5, 3]), [3, 4, 5, 5])

  def test_sorted(self):
    self.assertEquals(bubblesort([1, 2, 3]), [1, 2, 3])

  def test_sorts_last(self):
    self.assertEquals(bubblesort([1, 1, 1, 1, 1, 1, 1, 1, 1, 0]), [0, 1, 1, 1, 1, 1, 1, 1, 1, 1] )

  def test_returns_all_elements(self):
    random_list = [ random.randint(-100, 100) for i in range(random.randint(0, 200))]
    length = len(random_list)
    self.assertEquals(len(bubblesort(random_list)), length)

  def test_is_sorted(self):
    random_list = [ random.randint(-100, 100) for i in range(random.randint(0, 200))]
    self.assertEquals((bubblesort(random_list)), sorted(random_list))

  def test_mixed_types(self):
    a_list = [1,  'game', "baldur's gate", 2, 'a', 9, 4, 5, -99, 99]
    self.assertEquals(bubblesort(a_list), sorted(a_list))

  def test_bad_input(self):
    with self.assertRaises(TypeError):
      bubblesort(    a_string = 'a very bad memory of ascii codes lost')
