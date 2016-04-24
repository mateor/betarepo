# coding=utf-8
# The MIT License (MIT)
# Copyright (c) 2016 mateor

from __future__ import (absolute_import, division, generators, nested_scopes, print_function,
                        unicode_literals, with_statement)


from abc import ABCMeta, abstractmethod


class QueueException(Exception):
  """Raise when a stack method would cause the stack to reach an illegal state,."""


class Queue(object):
  __metaclass__ = ABCMeta

  @abstractmethod
  def enqueue(self, x):
    pass

  @abstractmethod
  def dequeue(self):
    pass

  @abstractmethod
  def is_empty(self):
    pass
