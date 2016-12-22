#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'start run demo.'

__author__ = 'soonfy'

##
## demo parse_movie

# from bs4 import BeautifulSoup
# from spider_middleware.douban_spider import spider_nologin
# from douban_movie.parse_movie import get_summary, get_score

# body = spider_nologin().open('https://movie.douban.com/subject/25900819/?tag=%E7%83%AD%E9%97%A8&from=gaia')
# soup = BeautifulSoup(body, 'html.parser')
# summary = get_summary(soup)
# print(summary)

# score, people, stars = get_score(soup)
# print(score)
# print(people)
# print(stars)

##
## demo ua

# from spider_middleware.ua import write_ua, read_ua
# write_ua()
# print(read_ua())

##
## demo login and crawl users

# from douban_user.user_starter import run
# userid = '67492098'
# run(userid)

##
## demo crawl douban user movies

# from douban_movie.user_movie_starter import run
# userfile = ('./crawl_douban/douban_user/users.txt')
# userids = open(userfile).read().split()
# # print(users)

# for userid in userids:
#   run(userid)
# print('all users movies saved...')


##
## demo multi-thread

# import time
# from util.thread_sf import concurrence
# def log(obj):
#   time.sleep(10)
#   print(obj[0])
#   print(obj[1])
# arr = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]]
# concurrence(log, arr, 4)
