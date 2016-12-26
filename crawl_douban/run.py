#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'opener: login or nologin.'

__author__ = 'soonfy'

from spider import spider_douban

spd = spider_douban()
mt = spd.crawl('https://music.douban.com/people/xzyzsk7/collect')
print(mt)
for v in mt:
  print(v)