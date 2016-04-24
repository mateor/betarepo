# coding=utf-8
# The MIT License (MIT)
# Copyright (c) 2016 mateor

from __future__ import (absolute_import, division, generators, nested_scopes, print_function,
                        unicode_literals, with_statement)


from abc import ABCMeta, abstractmethod


# TODO(mateo): Define a LinearException in some betarepo base exception class? Would that be useful in perf testing?
class QueueException(Exception):
  """Raise when a stack method would cause the stack to reach an illegal state,."""


class Queue(object):
  __metaclass__ = ABCMeta

  @abstractmethod
  def enqueue(self, x):
    raise NotImplementedError

  @abstractmethod
  def dequeue(self):
    raise NotImplementedError

  def is_empty(self):
    raise NotImplementedError
