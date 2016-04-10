# coding=utf-8
# The MIT License (MIT)
# Copyright (c) 2016 mateor

from __future__ import (absolute_import, division, generators, nested_scopes, print_function,
                        unicode_literals, with_statement)


class ComparisonMixin(object):
  """Allow datastructures to define common comparison functions."""

  def __eq__(self, other):
    return not self.__key__() < other.__key__() and not other.__key__() < self.__key__()

  def __ne__(self, other):
    return self.__key__() < other.__key__() or other.__key__() < self.__key__()

  def __gt__(self, other):
    return other.__key__() < self.__key__()

  def __ge__(self, other):
    return not self.__key__() < other.__key__()

  def __le__(self, other):
    return not other.__key__() < self.__key__()

  def __key__(self, other):
    raise NotImplementedError('Implementing classes must define a __key__ method to use as the basis for comparison.')
