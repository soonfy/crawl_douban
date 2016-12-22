#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'start crawl douban.'

__author__ = 'soonfy'

# modules
import time

from spider_middleware.ua import write_ua
from douban_user.user_starter import run as run_user
from douban_movie.user_movie_starter import run as run_user_movie
from util.thread_sf import concurrence

print '>> spider ready, go...\r\n'
userid = raw_input('input douban userid --> ex(67492098)')
print '>> you want to crawl douban user %s' % userid
print '>> open > https://www.douban.com/people/%s/ < to view data...\r\n' % userid
print '==> 10s start crawl...\r\n'
time.sleep(10)

print '==> firstly, update ua...'
write_ua()
print '==> rest 10s...\r\n'
time.sleep(10)

print '==> secondly, login and crawl user contacts...'
run_user(userid)
print '==> all user contacts over...'
print '==> rest 1 min...\r\n'
time.sleep(60)

print '==> thirdly, crawl user movies...'
userfile = ('./crawl_douban/douban_user/users.txt')
userids = open(userfile).read().split()
concurrence(run_user_movie, userids, 100)
print '==> all users movies saved...'
print '==> rest 1 min...\r\n'
time.sleep(60)

print '>> spider over...\r\n'
