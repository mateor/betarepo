# coding=utf-8
# The MIT License (MIT)
# Copyright (c) 2016 mateor

python_library(
  name = 'sorting_test_base',
  sources = [
    'sorting_test_base.py',
  ],
)


python_tests(
  name = 'sorting',
  sources = globs('test*.py'),
  dependencies = [
    ':sorting_test_base',
    'src/python/betarepo/algorithms/sorting',
  ]
)