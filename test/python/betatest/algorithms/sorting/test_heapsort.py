# coding=utf-8
# The MIT License (MIT)
# Copyright (c) 2016 mateor

from __future__ import (absolute_import, division, generators, nested_scopes, print_function,
                        unicode_literals, with_statement)


import unittest

from betarepo.algorithms.sorting.heapsort import heapsort
from betatest.algorithms.sorting.sorting_test_base import SortingTestBase


class TestBubbleSort(SortingTestBase, unittest.TestCase):

  @property
  def sorting_class(self):
    return heapsort
