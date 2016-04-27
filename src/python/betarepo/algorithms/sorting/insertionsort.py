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

  # Validate the input. TODO(mateor): delete the type checking. Let's validate by the caller or something.
  try:
    A[:-1] = A[:-1]
  except TypeError:
    raise TypeError('This insertion sort requires that the input support indexing. '
      'Try a list instead! (was: {})'.format(type(A)))

  # Compare numbers with those to the left. (Compare A[1] to A[0]. Next, A[2] to A[1]. If A[2] < A[1], then try A[0]...
  for i in range(1, len(A)):
    num = A[i]
    j = i

    # The invariant is nums to the left of A[i] are sorted. Once A[i] > A[j], there is no need to check more numbers.
    # This does not swap - each comparison results in setting one number in its final position for that sweep.
    while j > 0 and A[j - 1] > num:
      A[j] = A[j -1]
      j -= 1
    A[j] = num

  return A
