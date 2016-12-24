#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'start crawl douban.'

__author__ = 'soonfy'

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'start crawl douban.'

__author__ = 'soonfy'

# modules
import sys

from spider_middleware.ua import write_ua
from util.progress import log_bar

def ua_ready():
  userid = raw_input(' ༺༻\t who do u like ? \n ༺༻\t    155042704 or https://www.douban.com/people/155042704/ \n ༺༻\t ණ  ')
  if 'www.douban.com' in userid:
    m = re.search(r'www.douban.com/people/(\w+)/', userid)
    if m:
      userid = m.group(1)
  print ' ༺༻\t oh, you like %s' % userid
  print ' ༺༻\t ඏ  https://www.douban.com/people/%s/ ඏ  who is this...' % userid
  print ' ༺༻\t i m preparing.'
  print ' ༺༻\t ๛ ๛ ๛ ๛ ๛ ๛ ๛ ๛ ๛'
  log_bar(9)
  print ' ༺༻\t prepare to update ua...'
  write_ua()
  log_bar(11)
  print ' ༺༻\t update ua over...'
  print ' ༺༻\t ๛ ๛ ๛ ๛ ๛ ๛ ๛ ๛ ๛'
  return userid
