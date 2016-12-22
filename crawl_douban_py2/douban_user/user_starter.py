#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'start crawl user relation.'

__author__ = 'soonfy'

# modules
import time
import random

from spider_middleware.douban_spider import spider_login
from douban_user.user_spider import UserSpider
from douban_user.crawl_user import get_users, write_users, write_userids
from util.thread_sf import concurrence

opener = spider_login()

def con_crawl_users(userid):
  time.sleep(random.choice(range(10)))
  user = UserSpider(userid, opener)
  time.sleep(random.random())
  soup, relation = user.crawl_contacts()
  users, userids = get_users(soup, relation)
  write_users(users, userid)
  write_userids(userids)
  time.sleep(random.random())
  soup, relation = user.crawl_rev_contacts()
  users, userids = get_users(soup, relation)
  write_users(users, userid)
  write_userids(userids)

def run(userid):
  """
  start run crawl user relation  
  @param userid  
  """
  alluser = []
  write_userids([userid])
  user = UserSpider(userid, opener)
  time.sleep(random.random())
  soup, relation = user.crawl_contacts()
  users, userids = get_users(soup, relation)
  write_users(users, userid)
  write_userids(userids)
  alluser.extend(userids)
  time.sleep(random.random())
  soup, relation = user.crawl_rev_contacts()
  users, userids = get_users(soup, relation)
  write_users(users, userid)
  write_userids(userids)
  alluser.extend(userids)
  concurrence(con_crawl_users, alluser)
