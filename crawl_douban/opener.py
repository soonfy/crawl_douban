#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'opener: login or nologin.'

__author__ = 'soonfy'

# modules
import time

from urllib import request
from urllib.parse import urlencode
from http import cookiejar
from urllib.request import URLError


def opener_login():
  """
  login douban opener  
  @return opener  
  """
  url_login = 'https://www.douban.com/accounts/login'
  param = {
    'source': 'None',
    'redir': 'https://www.douban.com/people/rakikikikiki/contacts',
    'form_email': 'soonfy@163.com',
    'form_password': 'soonfy163',
    'login': '登录',
    # 'captcha-id': 'twO0UmGPzATj0bF4Cf0pTD1c:en',
    # 'captcha-solution': 'young'
  }
  data = urlencode(param).encode('utf-8')
  headers = {
    'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.134 Safari/534.16',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Referer': 'https://www.douban.com/',
    'Host': 'www.douban.com',
    'Origin': 'https://www.douban.com'
  }
  req = request.Request(url_login, data, headers)
  filename = r'./crawl_douban/opener/cookie.txt'
  FileCookieJar= cookiejar.MozillaCookieJar(filename)
  FileCookieJar.save()
  handler = request.HTTPCookieProcessor(FileCookieJar)
  opener = request.build_opener(handler)
  request.install_opener(opener)
  res = request.urlopen(req)
  body = res.read().decode('utf-8')
  FileCookieJar.save()
  print('login opener success...')
  return opener

def opener_nologin():
  """
  nologin douban spider  
  @return opener  
  """
  header = {
    'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.134 Safari/534.16',
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
  print('opener success...')
  return opener

def opener_open(opener, url, timeout = 60 * 2, max = 10):
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
        return ''
      body = opener.open(url, None, timeout).read()
      return body
    except URLError as e:
      print('=== time %s error, rest 10s ===' % fail)
      print(e)
      fail += 1
      time.sleep(fail)
