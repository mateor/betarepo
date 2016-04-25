# coding=utf-8
# The MIT License (MIT)
# Copyright (c) 2016 mateor

from __future__ import (absolute_import, division, generators, nested_scopes, print_function,
                        unicode_literals, with_statement)


import unittest

from betarepo.datastructures.linear.abstract.list import ListException
from betarepo.datastructures.linear.concrete.lists.linked_list import LinkedList


class TestLinkedList(unittest.TestCase):

  @classmethod
  def sample_list(cls, n=0):
    a_list = LinkedList()
    for i in range(n):
      a_list.insert(i)
    return a_list

  def test_is_empty(self):
    a_list = LinkedList()
    self.assertTrue(a_list.is_empty())
    a_list.insert(9)
    self.assertFalse(a_list.is_empty())

  def test_single_node(self):
    a_list = self.sample_list()
    self.assertEqual(a_list.head, None)
    self.assertEqual(a_list.tail, None)
    a_list.insert(9)
    self.assertEqual(a_list.head.value, 9)
    self.assertEqual(a_list.tail.value, 9)

  def test_list_properties(self):
    a_list = LinkedList()
    a_list.insert(9)
    self.assertEqual(a_list.head.value, 9)
    self.assertEqual(a_list.tail.value, 9)

  def test_head_and_tail(self):
    a_list = self.sample_list(9)
    self.assertEqual(a_list.head.value, 0)
    self.assertEqual(a_list.tail.value, 8)

  def test_remove_node(self):
    a_list = self.sample_list(9)
    self.assertEqual(a_list.head.value, 0)
    self.assertEqual(a_list.head.next.value, 1)
    self.assertEqual(a_list.tail.value, 8)
    a_list.remove()
    self.assertEqual(a_list.head.value, 1)
    self.assertEqual(a_list.head.next.value, 2)
    self.assertEqual(a_list.tail.value, 8)

  def test_remove_from_empty(self):
    a_list = LinkedList()
    with self.assertRaises(ListException):
      a_list.remove()

  def test_find_in_list(self):
    mexican_flag = LinkedList()
    colors = ('red', 'white', 'green')
    for color in colors:
      mexican_flag.insert(color)
    for color in colors:
      self.assertTrue(mexican_flag.find(color))
    self.assertFalse(mexican_flag.find('blue'))

  def test_find_in_empty(self):
    a_list = self.sample_list()
    self.assertFalse(a_list.find(0))

  def test_find_at_index(self):
    a_list = self.sample_list(9)
    self.assertEqual(a_list.find_at_index(6), 6)

  def test_find_at_index_overflow(self):
    a_list = self.sample_list(9)
    self.assertEqual(a_list.find_at_index(6), 6)
    with self.assertRaises(ListException):
      a_list.find_at_index(10)

  def test_find_at_index_empty(self):
    a_list = self.sample_list()
    with self.assertRaises(ListException):
      a_list.find_at_index(0)

  def test_delete_all_instances_empty(self):
    a_list = self.sample_list()
    a_list.delete_all_instances(9)

  def test_simple_delete_all_instances(self):
    a_list = self.sample_list(9)
    node_values = [ node.value for node in a_list]
    self.assertIn(3, node_values)
    a_list.delete_all_instances(3)
    node_values = [ node.value for node in a_list]
    self.assertNotIn(3, node_values)

  def test_delete_all_instances_repeated(self):
    a_list = self.sample_list()
    for i in range(10):
      a_list.insert(9)
    self.assertEqual(len(a_list), 10)
    a_list.delete_all_instances(9)
    self.assertTrue(a_list.is_empty())

  def test_delete_all_instances_repeated_at_beginning(self):
    a_list = self.sample_list()
    for i in range(3):
      a_list.insert('evil')
    for i in range(3):
      a_list.insert('good')
    self.assertEqual(len(a_list), 6)
    a_list.delete_all_instances('evil')
    self.assertEqual(len(a_list), 3)
    self.assertEqual(a_list.head.value, 'good')
    self.assertEqual(a_list.tail.value, 'good')

  def test_len_operator(self):
    a_list = LinkedList()
    self.assertEqual(len(a_list), 0)
    a_list.insert(1)
    self.assertEqual(len(a_list), 1)
    for i in range(10):
      a_list.insert(10)
    self.assertEqual(len(a_list), 11)

  def test_repr(self):
    a_list = self.sample_list(5)
    self.assertTrue(repr(a_list).endswith('None'))

  def test_iterator(self):
    nodes = []
    a_list = self.sample_list(9)
    for i in a_list:
      nodes.append(i.value)
    self.assertEqual(nodes, range(9))
