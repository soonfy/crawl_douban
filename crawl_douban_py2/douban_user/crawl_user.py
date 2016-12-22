#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'parse user contacts.'

__author__ = 'soonfy'

# modules
import re

from util.fs import file_ready

def get_users(soup, relation):
  """
  parse users from douban user contacts  
  @param soup  
  @param relation: contacts, rev_contacts  
  @return users, userids  
  """
  tag_dls = soup.find_all('dl')
  users = []
  userids = []
  for tag in tag_dls:
    tag_a = tag.dd.a
    user_url = tag_a['href']
    user_name = tag_a.string
    user = '%s\t%s\t%s' % (relation, user_name, user_url)
    users.append(user)
    m = re.search(r'/people/(\w+)/', user_url)
    if m:
      userids.append(m.group(1))
  return users, userids

def write_users(users, userid, user_dir = r'./crawl_douban/douban_user/users'):
  """
  write users into file  
  @param users  
  @param userid  
  @param user_dir  
  """
  user_file = r'%s/users/%s.txt' % (user_dir, userid)
  if file_ready(user_file):
    user_str = '\r\n'.join(users) + '\r\n'
    file_obj = open(user_file, 'a')
    file_obj.write(user_str)
    file_obj.close()

def write_userids(userids, userid_file = r'./crawl_douban/douban_user/users.txt'):
  """
  write userids into file  
  @param userids  
  @param userid_file  
  """
  if file_ready(userid_file):
    user_str = '\r\n'.join(userids) + '\r\n'
    file_obj = open(user_file, 'a')
    file_obj.write(userid_str)
    file_obj.close()
