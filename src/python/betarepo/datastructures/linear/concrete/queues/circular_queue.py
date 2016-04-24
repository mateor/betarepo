# coding=utf-8
# The MIT License (MIT)
# Copyright (c) 2016 mateor

from __future__ import (absolute_import, division, generators, nested_scopes, print_function,
                        unicode_literals, with_statement)

# TODO(mateo): This contains some fudging from the spec due to language implementation details.
# It's possible I will come back and tighten it up in the future.

from betarepo.datastructures.linear.abstract.queue import Queue, QueueException

DEFAULT_CAPACITY = 10


class CircularQueue(Queue):
  """
  Data structure to model a FIFO queue.

  This implementation models the classic "circular queue", tracking pointers to the front and back of the
  line instead of moving indexes or slicing/concatenating.

  The FixedCircularQueue is of a fixed and bounded size. If configured to overwrite, then the item at the
  front of the queue can be bumped from the queue without ever being returned to a consumer.
  This can be useful in networking or caching, where you can perhaps assume that the oldest item is the least relevant.

  All operations here are in constant time - there is no find method.
  """

  # TODO(mateo): These magic methods should probably be put somewhere they can be reused and not clutter the impl.
  def __iter__(self):
    i = 0
    while i < len(self.items):
      yield self.items[i]
      i += 1

  def __len__(self):
    return len(self.items)

  def __getitem__(self,index):
    return self.items[index]

  def __repr__(self):
    queued_numbers = []
    index = self.front
    for i in range(self.size):
      queued_numbers.append(self.items[index%self.capacity])
      index -= 1
    return queued_numbers

  def __init__(self, capacity=None, overwrite=False, *args, **kwargs):
    self.capacity = capacity or DEFAULT_CAPACITY
    self.overwrite = overwrite
    self.rear = self.front = self.size = 0

    # Initialize empty slots in the queue so we can not use append. Perhaps do this differently in the future.
    self.items = [ None for _ in range(DEFAULT_CAPACITY) ]

  def enqueue(self, item):
    if self.size == self.capacity and not self.overwrite:
      raise QueueException("This item would cause the queue to exceed its capacity! ({})".format(self.capacity))
    self.items[self.rear] = item
    self.size += 1
    self.rear = (self.rear % self.capacity) - 1

  def dequeue(self):
    if self.is_empty():
      raise QueueException("There are no items available to dequeue!")
    item = self.items[self.front]
    self.front = (self.front % self.capacity) - 1
    self.size -= 1
    return item

  def is_empty(self):
    return self.front == self.rear
