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


  # Allow mixed types? (python and all) or implement at least one that enforces a BaseType.

  @abstractmethod
  def push(self, x):
    raise NotImplementedError

  @abstractmethod
  def pop(self):
    raise NotImplementedError

  def is_empty(self):
    raise NotImplementedError

  def make_empty(self):
    raise NotImplementedError
