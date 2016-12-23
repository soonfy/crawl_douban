#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'start crawl douban.'

__author__ = 'soonfy'

# modules
import time
import sys
import re

from spider_middleware.ua import write_ua
from douban_user.user_starter import run as run_user
from douban_movie.user_movie_starter import run as run_user_movie
from util.thread_sf import concurrence
from util.progress import log_bar

# UnicodeEncodeError: 'ascii' codec can't encode characters in position
# sys encode
import sys
reload(sys)
sys.setdefaultencoding('utf8')

print '>> spider ready, go...\n'
userid = raw_input('>> input douban userid or userurl: \n ex: \n    155042704 or https://www.douban.com/people/rakikikikiki/ \n==> ')
if 'www.douban.com' in userid:
  m = re.search(r'www.douban.com/people/(\w+)/', userid)
  if m:
    userid = m.group(1)
print '>> you want to crawl douban user %s' % userid
print '>> open [ https://www.douban.com/people/%s/ ] to view data...\n' % userid
print '==> 10s start crawl...\n'
log_bar(10)

print '==> firstly, update ua...'
write_ua()
print '==> ua update over...\n'
print '==> rest 10s...\n'
log_bar(10)

print '==> secondly, login and crawl user contacts...'
run_user(userid)
print '==> all user contacts over...'
print '==> rest 1 min...\n'
log_bar(60)

print '==> thirdly, crawl user movies...'
userfile = ('./data/douban_users/userids.txt')
userids = open(userfile).read().split()
userids = set(userids)
concurrence(run_user_movie, userids)
print '==> all users movies saved...'
print '==> rest 1 min...\n'
log_bar(60)

print '>> spider over...\n'
