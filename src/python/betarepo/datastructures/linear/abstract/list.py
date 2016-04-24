# coding=utf-8
# The MIT License (MIT)
# Copyright (c) 2016 mateor

from __future__ import (absolute_import, division, generators, nested_scopes, print_function,
                        unicode_literals, with_statement)


from abc import ABCMeta, abstractmethod


class ListError(Exception):
  """Raise when a stack method would cause the stack to reach an illegal state,."""


class List(object):
  __metaclass__ = ABCMeta

  @abstractmethod
  def insert(self, item):
    pass

  @abstractmethod
  def remove(self, index):
    pass

  @abstractmethod
  def find(self, item):
    pass

  @abstractmethod
  def find_at_index(self, index):
    pass

  @abstractmethod
  def is_empty(self):
    pass
