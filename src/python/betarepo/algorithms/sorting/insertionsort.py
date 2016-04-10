# coding=utf-8
# The MIT License (MIT)
# Copyright (c) 2016 mateor

from __future__ import (absolute_import, division, generators, nested_scopes, print_function,
                        unicode_literals, with_statement)


import unittest
import random


# Insertion sort is often modeled as sorting playing cards in hand.

# O(n^2) but on the fast side
# O(1) space - sorts in place
# can be useful in mostly sorted sets - O(nk) with  (k) the largest distance between an element (n) and its index.
# a stable sort (maintains order between equal keys)

def insertionsort(A):
  try:
    A[:-1] = A[:-1]
  except TypeError:
    raise TypeError('This insertion sort requires that the input support indexing. '
      'Try a list instead! (was: {})'.format(type(A)))

  for i in range(1, len(A)):
    num = A[i]

    j = i
    while j > 0 and A[j - 1] > num:
      A[j] = A[j -1]
      j -= 1
    A[j] = num

  return A
