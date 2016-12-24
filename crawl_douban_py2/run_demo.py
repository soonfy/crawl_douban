#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'start run demo.'

__author__ = 'soonfy'

num = 2
arr = range(20)

print arr[0:num]
while num <= 20:
  print arr[num:num+2]
  num = num + 2
print 'ok'
