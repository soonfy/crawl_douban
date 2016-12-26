#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'start crawl douban.'

__author__ = 'soonfy'

# modules
import sys
import time
import random

from douban_user.user_starter import run as run_user
from douban_movie.user_movie_starter import run as run_user_movie
from util.thread_sf import concurrence
from util.progress import log_bar
from util.fs import file_ready

def crawl_user(userid):
  print ' ༺༻\t ๛ ๛ ๛ ๛ ๛ ๛ ๛ ๛ ๛'
  print ' ༺༻\t secondly, crawl user contacts...'
  run_user(userid)
  print ' ༺༻\t i m tired.'
  print ' ༺༻\t ๛ ๛ ๛ ๛ ๛ ๛ ๛ ๛ ๛'
  log_bar(59)

  print ' ༺༻\t ๛ ๛ ๛ ๛ ๛ ๛ ๛ ๛ ๛'
  print ' ༺༻\t thirdly, crawl user movies...'
  userfile = './data/douban_users/userids.txt'
  all_userids = open(userfile).read().split()
  distfile = './data/douban_users/userids_dist.txt'
  all_userids = list(set(all_userids))
  if file_ready(distfile):
    userid_str = '\n'.join(all_userids) + '\n'
    file_obj = open(distfile, 'w')
    file_obj.write(userid_str)
    file_obj.close()
  timeout = 60 * random.choice(range(1, 30))
  try:
    # concurrence(run_user_movie, userids)
    for userid in all_userids:
      run_user_movie(userid)
      print 'userid %s crawl over.' % userid
      print ' ༺༻\t i m tired. i want sleep %s.' % timeout
      time.sleep(timeout)
      print ' ༺༻\t ๛ ๛ ๛ ๛ ๛ ๛ ๛ ๛ ๛'
      log_bar(59)
  except:
    print ' ༺༻\t catch the raised error...'
    sys.exit()
  print ' ༺༻\t i m tired.'
  print ' ༺༻\t ๛ ๛ ๛ ๛ ๛ ๛ ๛ ๛ ๛'
  log_bar(59)
