#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'start crawl douban.'

__author__ = 'soonfy'

# modules
import sys

from douban_user.user_starter import run as run_user
from douban_movie.user_movie_starter import run as run_user_movie
from util.thread_sf import concurrence
from util.progress import log_bar

def crawl_user(userid):
  print ' ༺༻\t ๛ ๛ ๛ ๛ ๛ ๛ ๛ ๛ ๛'
  print ' ༺༻\t secondly, crawl user contacts...'
  run_user(userid)
  print ' ༺༻\t i m tired.'
  print ' ༺༻\t ๛ ๛ ๛ ๛ ๛ ๛ ๛ ๛ ๛'
  log_bar(59)

  print ' ༺༻\t ๛ ๛ ๛ ๛ ๛ ๛ ๛ ๛ ๛'
  print ' ༺༻\t thirdly, crawl user movies...'
  userfile = ('./data/douban_users/userids.txt')
  userids = open(userfile).read().split()
  userids = set(userids)
  try:
    concurrence(run_user_movie, userids, 10)
  except:
    print ' ༺༻\t catch the raised error...'
    sys.exit()
  print ' ༺༻\t i m tired.'
  print ' ༺༻\t ๛ ๛ ๛ ๛ ๛ ๛ ๛ ๛ ๛'
