#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'movie spider class.'

__author__ = 'soonfy'

# modules
from bs4 import BeautifulSoup

from spider_middleware.douban_spider import spider_open

class MovieSpider(object):
  """
  douban user spider class  
  @param userid  
  @param opener  
  @param category: movie, book, music
  @param timeout: 60 * 2
  """
  def __init__(self, userid, opener, category = 'movie'):
    self.userid = userid
    self.opener = opener
    self.category = category
    self.category_do = 'https://%s.douban.com/people/%s/do' % (category, userid)
    self.category_wish = 'https://%s.douban.com/people/%s/wish' % (category, userid)
    self.category_collect = 'https://%s.douban.com/people/%s/collect' % (category, userid)

  def crawl_do(self):
    """
    crawl user do  
    @return soup  
    """
    opener, category_do = self.opener, self.category_do
    body = spider_open(opener, category_do)
    soup = BeautifulSoup(body, 'html.parser')
    return soup

  def crawl_wish(self):
    """
    crawl user wish  
    @return soup  
    """
    opener, category_wish = self.opener, self.category_wish
    body = spider_open(opener, category_wish)
    soup = BeautifulSoup(body, 'html.parser')
    return soup

  def crawl_collect(self):
    """
    crawl user collect  
    @return soup  
    """
    opener, category_collect = self.opener, self.category_collect
    body = spider_open(opener, category_collect)
    soup = BeautifulSoup(body, 'html.parser')
    return soup
