# coding=utf-8
# The MIT License (MIT)
# Copyright (c) 2016 mateor

from __future__ import (absolute_import, division, generators, nested_scopes, print_function,
                        unicode_literals, with_statement)


def mergesort(A):
  try:
    A = list(A)
  except Exception:
    raise TypeError("This type is not supported by this implementation. Try a list! (was {})".format(type(A)))

  if A and len(A) > 1:
    mid = len(A)//2
    left = mergesort(A[:mid])
    right = mergesort(A[mid:])

    sorted = []
    while left and right:
      next_elem = left.pop(0) if left[0] <= right[0] else right.pop(0)
      sorted.append(next_elem)
    return sorted + left + right
  return A
