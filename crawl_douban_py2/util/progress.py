#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'file system.'

__author__ = 'soonfy'

# modules
import sys
import time

def log_bar(amount):
  for counter in range(amount):
    sys.stdout.write(' ༺༻\t [ ' + 'ෆ ' * (counter + 1) + ' ]' + ' %.2f' % (float(counter + 1) / amount * 100) + '%' + '\r')
    sys.stdout.flush()
    time.sleep(1)