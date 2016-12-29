#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'entry.'

__author__ = 'soonfy'

from prepare import ua_ready
from crawl import crawl_user

# UnicodeEncodeError: 'ascii' codec can't encode characters in position
# sys encode
import sys
reload(sys)
sys.setdefaultencoding('utf8')

print ' ༺༻\t ൠ ൠ ൠ ൠ ൠ ൠ ൠ ൠ ൠ ൠ ൠ ൠ ൠ ൠ ൠ ൠ ൠ ൠ ൠ ൠ ൠ ൠ ൠ ൠ'
userid = raw_input(' ༺༻\t who do u like ? \n ༺༻\t    55692656 or https://www.douban.com/people/50302453/ \n ༺༻\t ණ  ')
if 'www.douban.com' in userid:
  m = re.search(r'www.douban.com/people/(\w+)/', userid)
  if m:
    userid = m.group(1)
print ' ༺༻\t oh, you like %s' % userid
print ' ༺༻\t ඏ  https://www.douban.com/people/%s/ ඏ  who is this...' % userid
ua_ready()
crawl_user(userid)
print ' ༺༻\t ൠ ൠ ൠ ൠ ൠ ൠ ൠ ൠ ൠ ൠ ൠ ൠ ൠ ൠ ൠ ൠ ൠ ൠ ൠ ൠ ൠ ൠ ൠ ൠ'
