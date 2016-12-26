#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'start run demo.'

__author__ = 'soonfy'

# import urllib2

# proxy=urllib2.ProxyHandler({'https': 'http://221.195.40.145:80'})
# opener=urllib2.build_opener(proxy)
# urllib2.install_opener(opener)
# body = urllib2.urlopen('https://www.douban.com').read().decode('utf-8')
# print body

import json

fd = open('./login.json', 'r')
data = fd.read()
print data
js = json.loads(data)
print js['source']
fd.close()