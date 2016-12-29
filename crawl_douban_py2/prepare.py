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
  print ' ༺༻\t i m preparing.'
  print ' ༺༻\t ๛ ๛ ๛ ๛ ๛ ๛ ๛ ๛ ๛'
  print ' ༺༻\t prepare to update ua...'
  write_ua()
  print ' ༺༻\t ๛ ๛ ๛ ๛ ๛ ๛ ๛ ๛ ๛'
  print ' ༺༻\t update ua over...'
  log_bar(11)
