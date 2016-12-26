#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'douban spider class.'

__author__ = 'soonfy'

# modules
import re

from opener import opener_nologin, opener_login

class spider_douban(object):
  """
  douban spider class.  
  crawl urls  
  """

  # private attr
  __reg_people = re.compile('^https\://www\.douban\.com/(people)/(\w+)/?$', re.I)
  __reg_movie_pages = re.compile('^https\://(movie|book|music)\.douban\.com/people/(\w+)/(do|wish|collect)/?$', re.I)
  __reg_subject = re.compile('^https\://(movie|book|music)\.douban\.com/(subject)/(\w+)/?$', re.I)
  __reg_review_pages = re.compile('^https\://(movie|book|music)\.douban\.com/subject/(\w+)/(reviews)?$', re.I)
  __reg_reviews = re.compile('^https\://(movie|book|music)\.douban\.com/(review)/(\w+)/?$', re.I)
  __reg_comment_pages = re.compile('^https\://(movie|book|music)\.douban\.com/subject/(\w+)/(comments)', re.I)
  __reg_urls = [__reg_people, __reg_movie_pages, __reg_subject, __reg_review_pages, __reg_reviews, __reg_comment_pages]

  def __init__(self, login = False):
    if login:
      self.opener = opener_login()
    else:
      self.opener = opener_nologin()

  def crawl(self, url):
    for _reg in self.__reg_urls:
      _mt = re.search(_reg, url)
      if _mt:
        print(_reg)
        return _mt.groups()
      else:
        continue
    return ()

# https://www.douban.com/people/xzyzsk7/

# https://movie.douban.com/people/xzyzsk7/do
# https://movie.douban.com/people/xzyzsk7/wish
# https://movie.douban.com/people/xzyzsk7/collect
# https://music.douban.com/people/xzyzsk7/do
# https://music.douban.com/people/xzyzsk7/wish
# https://music.douban.com/people/xzyzsk7/collect
# https://book.douban.com/people/xzyzsk7/do
# https://book.douban.com/people/xzyzsk7/wish
# https://book.douban.com/people/xzyzsk7/collect

# https://www.douban.com/people/xzyzsk7/games?action=do
# https://www.douban.com/people/xzyzsk7/games?action=wish
# https://www.douban.com/people/xzyzsk7/games?action=collect

# https://www.douban.com/location/people/xzyzsk7/drama/wish

# https://www.douban.com/people/xzyzsk7/notes
# https://www.douban.com/people/xzyzsk7/reviews
# https://www.douban.com/people/xzyzsk7/things

# https://movie.douban.com/subject/25900819/
# https://movie.douban.com/subject/25900819/comments?status=P
# https://movie.douban.com/subject/25900819/comments?status=F
# https://movie.douban.com/subject/25900819/reviews
# https://movie.douban.com/review/8112498/
# https://book.douban.com/subject/26919519/
# https://book.douban.com/subject/26919519/comments/
# https://book.douban.com/subject/26919519/reviews
# https://book.douban.com/review/8239252/