# coding=utf-8
# The MIT License (MIT)
# Copyright (c) 2016 mateor



python_library(
  name = 'stack_base',
  sources = ['stack_test_base.py'],
  dependencies = []
)

python_tests(
  name = 'stacks',
  sources = globs('test*.py'),
  dependencies = [
    ':stack_base',
    'src/python/betarepo/datastructures/linear/concrete/stacks',
  ]
)
