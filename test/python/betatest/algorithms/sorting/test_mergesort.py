# coding=utf-8
# The MIT License (MIT)
# Copyright (c) 2016 mateor

from __future__ import (absolute_import, division, generators, nested_scopes, print_function,
                        unicode_literals, with_statement)


import unittest

from betarepo.algorithms.sorting.mergesort import mergesort
from betatest.algorithms.sorting.sorting_test_base import SortingTestBase


class TestInsertionSort(SortingTestBase, unittest.TestCase):

  @property
  def sorting_class(self):
    return mergesort
