# coding=utf-8
# The MIT License (MIT)
# Copyright (c) 2016 mateor

from __future__ import (absolute_import, division, generators, nested_scopes, print_function,
                        unicode_literals, with_statement)


from abc import ABCMeta, abstractmethod


class HeapException(Exception):
  """Raise when a heap method would cause the heap to reach an illegal state,."""


class Heap(object):
  __metaclass__ = ABCMeta

  @abstractmethod
  def insert(self, item):
    pass

  @abstractmethod
  def remove(self, index=None):
    pass

  @abstractmethod
  def size(self):
    pass

  @abstractmethod
  def peek(self, index):
    pass

  @abstractmethod
  def is_empty(self):
    pass

  @abstractmethod
  def make_empty(self):
    pass

  # I added this - probably has no place here.
  @abstractmethod
  def is_heap(self):
    pass