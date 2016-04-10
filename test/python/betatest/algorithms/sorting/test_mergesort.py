# coding=utf-8
# The MIT License (MIT)
# Copyright (c) 2016 mateor

from __future__ import (absolute_import, division, generators, nested_scopes, print_function,
                        unicode_literals, with_statement)


import unittest
import random

from betarepo.algorithms.sorting.mergesort import mergesort


class SortTest(unittest.TestCase):

  def test_empty(self):
    self.assertEqual(mergesort([]), [])

  def test_single(self):
    self.assertEquals(mergesort([1]), [1])

  def test_base_case(self):
    self.assertEqual(mergesort([1, 0]), [0, 1])

  def test_simple(self):
    self.assertEqual(mergesort([4, 5, 5, 3]), [3, 4, 5, 5])

  def test_sorted(self):
    self.assertEquals(mergesort([1, 2, 3]), [1, 2, 3])

  def test_sorts_last(self):
    self.assertEquals(mergesort([1, 1, 1, 1, 1, 1, 1, 1, 1, 0]), [0, 1, 1, 1, 1, 1, 1, 1, 1, 1] )

  def test_returns_all_elements(self):
    random_list = [ random.randint(-100, 100) for i in range(random.randint(0, 200))]
    length = len(random_list)
    self.assertEquals(len(mergesort(random_list)), length)

  def test_is_sorted(self):
    random_list = [ random.randint(-100, 100) for i in range(random.randint(0, 200))]
    self.assertEquals((mergesort(random_list)), sorted(random_list))

  def test_mixed_types(self):
    a_list = [1,  'game', "baldur's gate", 2, 'a', 9, 4, 5, -99, 99]
    self.assertEquals(mergesort(a_list), sorted(a_list))

  def test_string_input(self):
    a_string = 'a very bad memory of not remembering an ascii code'
    self.assertEquals(mergesort(a_string), sorted(list(a_string)))
