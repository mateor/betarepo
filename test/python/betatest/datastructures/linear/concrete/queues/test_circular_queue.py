# coding=utf-8
# The MIT License (MIT)
# Copyright (c) 2016 mateor

from __future__ import (absolute_import, division, generators, nested_scopes, print_function,
                        unicode_literals, with_statement)


import unittest

from betarepo.datastructures.linear.abstract.queue import QueueException
from betarepo.datastructures.linear.concrete.queues.circular_queue import CircularQueue, DEFAULT_CAPACITY


class TestCircularQueue(unittest.TestCase):

  @property
  def queue_class(cls):
    return CircularQueue

  @property
  def capacity(cls):
    return DEFAULT_CAPACITY

  def setUp(self):
    self.queue = self.queue_class()

  def test_create_queue_empty(self):
    self.assertTrue(self.queue.is_empty())

  def test_item_means_queue_not_empty(self):
    self.queue.enqueue(9)
    self.assertFalse(self.queue.is_empty())
    self.assertTrue(self.queue.size, 1)

  def test_front_of_queue(self):
    item = 9
    self.queue.enqueue(item)
    self.assertEqual(self.queue[self.queue.front], 9)

  def test_dequeue_from_empty_is_error(self):
    with self.assertRaises(QueueException):
      self.queue.dequeue()

  def test_queue_overflow(self):
    for i in range(self.capacity):
      self.queue.enqueue(i)
    with self.assertRaises(QueueException):
      self.queue.enqueue(DEFAULT_CAPACITY + 1)

  def test_allow_overwrite(self):
    queue = self.queue_class(capacity=self.capacity, overwrite=True)
    for i in range(self.capacity + 1):
      queue.enqueue(i)
