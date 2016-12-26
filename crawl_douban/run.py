#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'opener: login or nologin.'

__author__ = 'soonfy'

from spider import spider_douban
from parser import parse_people

spd = spider_douban()
mt = spd.parse_params('https://www.douban.com/people/xzyzsk7/')
print(mt)
for v in mt:
  print(v)

parse_people(mt, 'all')
