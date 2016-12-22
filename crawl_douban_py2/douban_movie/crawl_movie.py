#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'parse douban movie content data.'

__author__ = 'soonfy'

# modules
from bs4 import NavigableString

def get_summary(soup):
  """
  get content from douban movie html  
  ex: https://movie.douban.com/subject/25900819/?tag=%E7%83%AD%E9%97%A8&from=gaia  
  """
  summary = ''
  tag_span = soup.find('span', class_='all hidden')
  tag_short = soup.find(id='link-report').select_one('span[property="v:summary"]')
  if tag_span:
    for child in tag_span.children:
      if isinstance(child, NavigableString):
        summary = summary + child
  elif tag_short:
    for child in tag_short.children:
      if isinstance(child, NavigableString):
        summary = summary + child
  else:
    pass
  return ''.join(summary.split())

def get_score(soup):
  """
  get score from douban movie html  
  ex: https://movie.douban.com/subject/25900819/?tag=%E7%83%AD%E9%97%A8&from=gaia  
  """
  rating_num, rating_people = None, None
  rating_stars = []
  tag_strong = soup.find('strong', class_='rating_num')
  if tag_strong:
    rating_num = tag_strong.string
  tag_a = soup.find('a', class_='rating_people').select_one('span[property="v:votes"]')
  if tag_a:
    rating_people = tag_a.string
  tag_spans = soup.findAll('span', class_='rating_per')
  for tag in tag_spans:
    rate = tag.string
    rating_stars.append(rate)
  return rating_num, rating_people, rating_stars

