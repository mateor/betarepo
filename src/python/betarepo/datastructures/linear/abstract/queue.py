# coding=utf-8
# The MIT License (MIT)
# Copyright (c) 2016 mateor

from __future__ import (absolute_import, division, generators, nested_scopes, print_function,
                        unicode_literals, with_statement)


from abc import ABCMeta, abstractmethod


# TODO(mateo) Maybe move these to datastructures.linear.abstract.queue instead.

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

  def make_empty(self):
    raise NotImplementedError
