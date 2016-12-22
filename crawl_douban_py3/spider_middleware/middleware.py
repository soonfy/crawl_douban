#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'spider middleware.'

__author__ = 'soonfy'

from bs4 import BeautifulSoup
from urllib.parse import urlencode
from urllib import request
import http.cookiejar
import os

url_ua = 'http://www.useragentstring.com/pages/useragentstring.php?name=All'
url_login = 'https://www.douban.com/accounts/login'
_user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/54.0.2840.100 Safari/537.36'

def get_ua():
  """
  get ua list from web  
  ex:
    'http://www.useragentstring.com/pages/useragentstring.php?name=All'
  """
  print('get ua list from web...')
  req = request.Request(url_ua)
  try:
    res = request.urlopen(req)
  except urllib.URLError as e:
    print(e)
  body = res.read()
  soup = BeautifulSoup(body, 'html.parser')
  tag_lis = soup.find_all('li')
  uas = []
  for tag in tag_lis:
    tag_a = tag.find('a')
    uas.append(tag.string)
  return uas

def write_ua():
  """
  write ua list to file
  """
  pass

def read_ua():
  """
  read ua list from file
  """
  pass

def get_cookie():
  """
  get cookie from douban
  """
  print('get cookie...')
  param = {
    "source": 'None',
    "redir": 'https://www.douban.com/people/67492098/contacts',
    "form_email": 'soonfy@163.com',
    "form_password": 'soonfy163',
    "login": '登录'
  }
  data = urlencode(param).encode('utf-8')
  header = {
    'User-Agent': _user_agent,
    'Content-Type': 'application/x-www-form-urlencoded',
    'Referer': 'https://www.douban.com/people/67492098/contacts',
    'Host': 'www.douban.com',
    'Origin': 'https://www.douban.com'
  }

  filename = os.path.abspath(r'./spider_douban/cookie.txt')
  FileCookieJar= http.cookiejar.MozillaCookieJar(filename)
  FileCookieJar.save()
  handler = request.HTTPCookieProcessor(FileCookieJar)

  req = request.Request(url_login, data, header)

  # cookie = http.cookiejar.CookieJar()
  # handler = request.HTTPCookieProcessor(cookie)
  # proxy_support = request.ProxyHandler({'https': '114.231.242.248:8088'})
  opener = request.build_opener(handler)
  request.install_opener(opener)
  res = request.urlopen(req)

  body = res.read()
  print(body.decode('utf-8'))
  FileCookieJar.save()

  # print('next page...')
  # print(request.urlopen('https://www.douban.com/people/TORTURE/contacts').read().decode('utf-8'))

def use_cookie():
  """
  use cookie file
  """
  cookie = http.cookiejar.MozillaCookieJar()
  filename = os.path.abspath(r'./spider_douban/cookie.txt')
  cookie.load(filename)
  header = {
    'User-Agent': _user_agent,
    'Referer': 'https://www.douban.com/people/67492098/contacts',
    'Content-Type': 'text/html; charset=utf-8',
    'Host': 'www.douban.com',
    'Origin': 'https://www.douban.com'
  }
  url = 'https://www.douban.com/people/TORTURE/contacts'
  req = request.Request(url, ''.encode('utf-8'), header)
  handler = request.HTTPCookieProcessor(cookie)
  opener = request.build_opener(handler)
  request.install_opener(opener)
  res = request.urlopen(req)
  body = res.read()
  print(body.decode('utf-8'))
