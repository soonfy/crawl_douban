#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'page spider class.'

__author__ = 'soonfy'

# modules
import re

from bs4 import BeautifulSoup

class PageSpider(object):
  """
  douban page spider class  
  @param opener  
  """
  def __init__(self, opener):
    self.opener = opener
    self.page_people = re.compile(r'https://www.douban.com/people/(\w+)/?')

  def crawl_page(self, page):
    """
    crawl page  
    @return soup  
    ex:
      https://www.douban.com/people/xzyzsk7/

      https://movie.douban.com/people/xzyzsk7/do
      https://movie.douban.com/people/xzyzsk7/wish
      https://movie.douban.com/people/xzyzsk7/collect
      https://music.douban.com/people/xzyzsk7/do
      https://music.douban.com/people/xzyzsk7/wish
      https://music.douban.com/people/xzyzsk7/collect
      https://book.douban.com/people/xzyzsk7/do
      https://book.douban.com/people/xzyzsk7/wish
      https://book.douban.com/people/xzyzsk7/collect

      https://www.douban.com/people/xzyzsk7/games?action=do
      https://www.douban.com/people/xzyzsk7/games?action=wish
      https://www.douban.com/people/xzyzsk7/games?action=collect

      https://www.douban.com/location/people/xzyzsk7/drama/wish

      https://www.douban.com/people/xzyzsk7/notes
      https://www.douban.com/people/xzyzsk7/reviews
      https://www.douban.com/people/xzyzsk7/things

      https://movie.douban.com/subject/25900819/
      https://movie.douban.com/subject/25900819/comments?status=P
      https://movie.douban.com/subject/25900819/comments?status=F
      https://movie.douban.com/subject/25900819/reviews
      https://movie.douban.com/review/8112498/
      https://book.douban.com/subject/26919519/
      https://book.douban.com/subject/26919519/comments/
      https://book.douban.com/subject/26919519/reviews
      https://book.douban.com/review/8239252/
    """
    opener, page_people = self.opener, self.page_people
    if re.search(page_people, page):
      print(1)
    else:
      print(0)
