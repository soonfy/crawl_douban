#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'parse douban page data.'

__author__ = 'soonfy'

# modules
import re

from util.fs import file_ready

def get_movie(soup):
  """
  get user-movies from douban user-movie html  
  @param soup  
  @return user_movies, movie_urls  
  """
  tag_divs = soup.find_all('div', class_='item')
  user_movies = []
  user_movie = None
  movie_urls = []
  tag_h = soup.h1
  if tag_h:
    user_movie = tag_h.string
  for tag in tag_divs:
    tag_a = tag.find('li', class_='title').find('a')
    movie_url = tag_a['href']
    movie_name = tag_a.find('em').string
    tag_span = tag.find('span', class_='date')
    movie_date = None
    movie_rate = None
    if tag_span:
      movie_date = tag_span.string
    tag_rate = tag.find('span', class_=re.compile('rating\d-t'))
    if tag_rate:
      movie_rate = str(tag_rate['class'])
      m = re.search(r'rating(\w)', movie_rate)
      if m:
        movie_rate = m.group(1)
    movie = '%s\t%s\t%s\t%s\t%s' % (user_movie, movie_name, movie_url, movie_date, movie_rate)
    user_movies.append(movie)
    movie_urls.append(movie_url)
  return user_movies, movie_urls

def get_next(soup):
  """
  get next url from douban user-movie html  
  @param soup  
  @return next_url
  """
  tag_span = soup.find('span', class_='next')
  tag_a = None
  if tag_span:
    tag_a = tag_span.find('a')
  url = None
  if tag_a:
    url = tag_a['href']
  return url

def write_user_movies(user_movies, userid):
  """
  write user_movies into file  
  @param user_movies  
  @param userid  
  """
  user_movie_file = r'./crawl_douban/douban_movie/user_movies/%s.txt' % (userid)
  if file_ready(user_movie_file):
    user_movie_str = '\r\n'.join(user_movies) + '\r\n'
    file_obj = open(user_movie_file, 'a')
    file_obj.write(user_movie_str)
    file_obj.close()

def write_movies(movies, movie_file = r'./crawl_douban/douban_movie/movies.txt'):
  """
  write movies into file  
  @param movies  
  @param movie_file  
  """
  if file_ready(movie_file):
    movie_str = '\r\n'.join(movies) + '\r\n'
    file_obj = open(movie_file, 'a')
    file_obj.write(movie_str)
    file_obj.close()
