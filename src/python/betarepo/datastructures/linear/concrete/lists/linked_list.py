# coding=utf-8
# The MIT License (MIT)
# Copyright (c) 2016 mateor

from __future__ import (absolute_import, division, generators, nested_scopes, print_function,
                        unicode_literals, with_statement)


from betarepo.datastructures.linear.abstract.list import List, ListException


class LinkedList(object):

  class Node(object):

    def __init__(self, value, next=None):
      self.value = value
      self.next = None

    def __repr__(self):
      return repr(self.value)

  def __init__(self):
    self.head = None
    self.tail = None

  def __iter__(self):
    node = self.head
    while node:
      yield node
      node = node.next

  def __len__(self):
    # Could use a 'size' attribute instead...it litters extra code into the methods but at least len could be O(1)...
    node = self.head
    length = 0
    while node:
      length += 1
      node = node.next
    return length

  def __repr__(self):
    msg = "LinkedList: "
    for node in self:
      msg += "{} -> ".format(node.value)
    return msg + "None"

  def insert(self, item):
    node = self.Node(item)
    if not self.head:
      self.head = node
      self.tail = node
    else:
      self.tail.next = node
      self.tail = node

  def remove(self):
    if self.is_empty():
      raise ListException("The linked list is empty!")
    item = self.head.value
    self.head = self.head.next
    return item

  def is_empty(self):
    return self.head == None

  def find(self, value):
    for node in self:
      if node.value == value:
        return True
    return False

  def find_at_index(self, index):
    node = self.head
    i = 0
    while node:
      if i == index:
        return node.value
      node = node.next
      i += 1
    raise ListException('The linked list does not extend to that index! (index: {})'.format(index))

  def delete_all_instances(self, value):
    """Remove all nodes from the list if their content matches value."""
    # I added this as a last-minute lark. It doesn't fit in this module.
    # TODO(mateo): Move to a better spot or delete.

    # Check the head
    node = self.head
    while node and node.value == value:
      node = node.next
    self.head = node
    tail = node

    # Check the rest.
    while node and node.next:
      if node.next.value == value:
        node.next = node.next.next
      else:
        node = node.next
        tail = node
    self.tail = tail

  # TODO (mateo) Somewhere, sometime.
  def cons(self, other):
    pass

  def car(self):
    pass
