# coding=utf-8
# The MIT License (MIT)
# Copyright (c) 2016 mateor

from __future__ import (absolute_import, division, generators, nested_scopes, print_function,
                        unicode_literals, with_statement)

import sys

from betarepo.algorithms.sorting.insertionsort import insertionsort
from betarepo.algorithms.sorting.bubblesort import bubblesort
from betarepo.algorithms.sorting.mergesort import mergesort


if __name__ == '__main__':
  # Just a little POC with a pex - not much of actual use here.

  sort = sys.argv[1]
  the_list = [1,  'game', "baldur's gate", 2, 'a', 9, 4, 5, -99, 99]

  if sort == "mergesort":
    print(mergesort(the_list))
  elif sort == "bubblesort":
    print(bubblesort(the_list))
  elif sort == "insertionsort":
    print(mergesort(the_list))
  else:
    print("What - you don't know how to use this thing here? You big old mess, you.\n(asked for({})".format(sort))