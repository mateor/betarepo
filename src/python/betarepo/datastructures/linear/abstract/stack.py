# coding=utf-8
# The MIT License (MIT)
# Copyright (c) 2016 mateor

from __future__ import (absolute_import, division, generators, nested_scopes, print_function,
                        unicode_literals, with_statement)


from abc import ABCMeta, abstractmethod


class StackException(Exception):
  """Raise when a stack method would cause the stack to reach an illegal state,."""


class Stack(object):
  __metaclass__ = ABCMeta

  @abstractmethod
  def push(self, x):
    pass

  @abstractmethod
  def pop(self):
    pass

  @abstractmethod
  def is_empty(self):
    pass

  @abstractmethod
  def make_empty(self):
    pass
