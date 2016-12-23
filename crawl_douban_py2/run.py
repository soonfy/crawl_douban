#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'start crawl douban.'

__author__ = 'soonfy'

# modules
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

print ' ༺༻\t ൠ ൠ ൠ ൠ ൠ ൠ ൠ ൠ ൠ ൠ ൠ ൠ ൠ ൠ ൠ ൠ ൠ ൠ ൠ ൠ ൠ ൠ ൠ ൠ'
userid = raw_input(' ༺༻\t who do u like ? \n ༺༻\t    55692656 or https://www.douban.com/people/rakikikikiki/ \n ༺༻\t ණ  ')
if 'www.douban.com' in userid:
  m = re.search(r'www.douban.com/people/(\w+)/', userid)
  if m:
    userid = m.group(1)
print ' ༺༻\t oh, you like %s' % userid
print ' ༺༻\t ඏ https://www.douban.com/people/%s/ ඏ who is this...' % userid
print ' ༺༻\t i m preparing.'
log_bar(11)

print ' ༺༻\t ൠ ൠ ൠ ൠ ൠ ൠ ൠ ൠ ൠ ൠ ൠ'
print ' ༺༻\t firstly, update ua...'
write_ua()
print ' ༺༻\t ൠ ൠ ൠ ൠ ൠ ൠ ൠ ൠ ൠ ൠ ൠ'
print ' ༺༻\t i m tired.'
log_bar(9)

print ' ༺༻\t ๛ ๛ ๛ ๛ ๛ ๛ ๛ ๛ ๛'
print ' ༺༻\t secondly, crawl user contacts...'
run_user(userid)
print ' ༺༻\t ๛ ๛ ๛ ๛ ๛ ๛ ๛ ๛ ๛'
print ' ༺༻\t i m tired.'
log_bar(59)

print ' ༺༻\t thirdly, crawl user movies...'
userfile = ('./data/douban_users/userids.txt')
userids = open(userfile).read().split()
userids = set(userids)
concurrence(run_user_movie, userids, 10)
print ' ༺༻\t i m tired.'
log_bar(61)

print ' ༺༻\t ൠ ൠ ൠ ൠ ൠ ൠ ൠ ൠ ൠ ൠ ൠ ൠ ൠ ൠ ൠ ൠ ൠ ൠ ൠ ൠ ൠ ൠ ൠ ൠ'
