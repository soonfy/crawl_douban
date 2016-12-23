#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'douban spider: login or nologin.'

__author__ = 'soonfy'

# modules
import os
import time
import sys

import urllib2 as request
import urllib
import cookielib as cookiejar

from util.fs import file_ready

from spider_middleware.ua import read_ua

def spider_login():
  """
  login douban spider  
  @return opener  
  """
  url_login = 'https://www.douban.com/accounts/login'
  param = {
    'source': 'None',
    'redir': 'https://www.douban.com/people/rakikikikiki/contacts',
    'form_email': 'soonfy@163.com',
    'form_password': 'soonfy163',
    'login': '登录',
    # 'captcha-id': 'TqpZLxJyLAFWZXATpb637tDR:en',
    # 'captcha-solution': 'broken'
  }
  data = urllib.urlencode(param).encode('utf-8')
  headers = {
    # 'User-Agent': read_ua(),
    'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.134 Safari/534.16',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Referer': 'https://www.douban.com',
    'Host': 'www.douban.com',
    'Origin': 'https://www.douban.com'
  }
  req = request.Request(url_login, data, headers)
  filename = os.path.abspath(r'./data/spider/cookie.txt')
  if file_ready(filename):
    FileCookieJar= cookiejar.MozillaCookieJar(filename)
    FileCookieJar.save()
    handler = request.HTTPCookieProcessor(FileCookieJar)
    opener = request.build_opener(handler)
    request.install_opener(opener)
    res = request.urlopen(req)
    body = res.read().decode('utf-8')
    if u'验证码不正确' in body:
      print body
      print ' ༺༻\t login error, need input captcha-id and captcha-solution...'
      sys.exit()
    FileCookieJar.save()
    return opener

def spider_nologin():
  """
  nologin douban spider  
  @return opener  
  """
  header = {
    'User-Agent': read_ua(),
    'Referer': 'https://www.douban.com/',
    'Host': 'www.douban.com',
    'Origin': 'https://www.douban.com'
  }
  headers = []
  for key, value in header.items():
    elem = (key, value)
    headers.append(elem)
  cj = cookiejar.CookieJar()
  handler = request.HTTPCookieProcessor(cj)
  opener = request.build_opener(handler)
  request.install_opener(opener)
  opener.addheaders = headers
  return opener

def spider_open(opener, url, timeout = 60 * 2, max = 10):
  """
  open url  
  @param opener  
  @param url  
  @param timeout  
  @param max - max times reopen  
  @return body/''  
  """
  fail = 1
  while True:
    try:
      if fail > max:
        print ' ༺༻\t he not like u...'
        sys.exit()
      body = opener.open(url, None, timeout).read()
      return body
    except request.URLError:
      print url
      print '=== time %s error, rest 10s ===' % fail
      fail += 1
      time.sleep(10)
