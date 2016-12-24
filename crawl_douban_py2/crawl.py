#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'start crawl douban.'

__author__ = 'soonfy'

# modules
import sys
import time

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
  all_userids = open(userfile).read().split()
  amount = len(all_userids)
  step = counter = 4000
  part = all_userids[0:counter]
  print part
  userids = set(part)
  try:
    concurrence(run_user_movie, userids)
  except:
    print ' ༺༻\t catch the raised error...'
    sys.exit()
  print ' ༺༻\t i m tired.'
  print ' ༺༻\t i want sleep 2h.'
  print ' ༺༻\t ๛ ๛ ๛ ๛ ๛ ๛ ๛ ๛ ๛'
  time.sleep(60 * 60 * 2)
  log_bar(59)

  while counter < amount:
    part = all_userids[counter:counter + step]
    userids = set(part)
    try:
      concurrence(run_user_movie, userids)
    except:
      print ' ༺༻\t catch the raised error...'
      sys.exit()
    counter = counter + step
    print ' ༺༻\t i m tired.'
    print ' ༺༻\t i want sleep 2h.'
    print ' ༺༻\t ๛ ๛ ๛ ๛ ๛ ๛ ๛ ๛ ๛'
    time.sleep(60 * 60 * 2)
    log_bar(59)
