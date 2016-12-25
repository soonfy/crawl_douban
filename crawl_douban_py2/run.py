#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'entry.'

__author__ = 'soonfy'

from prepare import ua_ready
# from crawl import crawl_user

# UnicodeEncodeError: 'ascii' codec can't encode characters in position
# sys encode
import sys
reload(sys)
sys.setdefaultencoding('utf8')

print ' ༺༻\t ༒ ༒ ༒ ༒ ༒ ༒ ༒ ༒ ༒ ༒ ༒ ༒ ༒ ༒ ༒'
userid = ua_ready()
# crawl_user(userid)
print ' ༺༻\t ༒ ༒ ༒ ༒ ༒ ༒ ༒ ༒ ༒ ༒ ༒ ༒ ༒ ༒ ༒'
