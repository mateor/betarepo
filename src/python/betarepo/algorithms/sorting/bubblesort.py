# coding=utf-8
# The MIT License (MIT)
# Copyright (c) 2016 mateor

from __future__ import (absolute_import, division, generators, nested_scopes, print_function,
                        unicode_literals, with_statement)


import unittest
import random


# best/average = O(n^2)
# very slow - minimal to zero production value.
# O(1) space - sorts in place

# Only thing it is good for is when list is already sorted
# but insertion sort has that as well.

# Keeps track of the last swapped element for every pass - everything after that
# last swap is already known to be sorted.

def bubblesort(A):
  try:
    A[:-1] = A[:-1]
  except TypeError:
    raise TypeError('This insertion sort requires that the input support indexing. Try a list instead! (was: {})'.format(type(A)))

  unsorted = len(A)
  while unsorted != 0:
    last_swapped = 0
    for i in range(1, unsorted):
      if A[i - 1] > A[i]:
        A[i - 1], A[i] = A[i], A[i - 1]
        last_swapped = i
    unsorted = last_swapped
  return A

