#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'spider start run.'

__author__ = 'soonfy'

# modules
import time
import random

from bs4 import BeautifulSoup

from spider_middleware.douban_spider import spider_nologin, spider_open
from douban_movie.movie_spider import MovieSpider
from douban_movie.crawl_page import get_movie, get_next, write_user_movies, write_movies

def run(userid):
  """
  start run crawl user-movies  
  @param userid  
  """
  time.sleep(random.choice(range(10)))
  
  # collect
  opener = spider_nologin()
  time.sleep(random.random())
  movie_spider = MovieSpider(userid, opener)
  soup = movie_spider.crawl_collect()
  user_movies, movies = get_movie(soup)
  write_user_movies(user_movies, userid)
  write_movies(movies)
  url_next = get_next(soup)
  while url_next:
    time.sleep(random.random())
    opener = spider_nologin()
    body = spider_open(opener, url_next)
    soup = BeautifulSoup(body, 'html.parser')
    user_movies, movies = get_movie(soup)
    write_user_movies(user_movies, userid)
    write_movies(movies)
    url_next = get_next(soup)
  
  # do
  opener = spider_nologin()
  time.sleep(random.random())
  movie_spider = MovieSpider(userid, opener)
  soup = movie_spider.crawl_do()
  user_movies, movies = get_movie(soup)
  write_user_movies(user_movies, userid)
  write_movies(movies)
  url_next = get_next(soup)
  while url_next:
    time.sleep(random.random())
    opener = spider_nologin()
    body = spider_open(opener, url_next)
    soup = BeautifulSoup(body, 'html.parser')
    user_movies, movies = get_movie(soup)
    write_user_movies(user_movies, userid)
    write_movies(movies)
    url_next = get_next(soup)

  # wish
  opener = spider_nologin()
  time.sleep(random.random())
  movie_spider = MovieSpider(userid, opener)
  soup = movie_spider.crawl_wish()
  user_movies, movies = get_movie(soup)
  write_user_movies(user_movies, userid)
  write_movies(movies)
  url_next = get_next(soup)
  while url_next:
    time.sleep(random.random())
    opener = spider_nologin()
    body = spider_open(opener, url_next)
    soup = BeautifulSoup(body, 'html.parser')
    user_movies, movies = get_movie(soup)
    write_user_movies(user_movies, userid)
    write_movies(movies)
    url_next = get_next(soup)
    