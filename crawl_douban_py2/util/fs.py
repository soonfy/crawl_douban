#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'file system.'

__author__ = 'soonfy'

# modules
import os

def file_ready(filepath):
  """
  judge filepath exists, append mode  
  @param filepath  
  @return boolean  
  """
  try:
    if os.path.exists(os.path.split(filepath)[0]):
      if os.path.isfile(filepath):
        pass
      else:
        fd = open(filepath, 'w')
        fd.write('')
        fd.close()
    else:
      os.makedirs(os.path.split(filepath)[0])
      fd = open(filepath, 'w')
      fd.write('')
      fd.close()
    return True
  except Exception as e:
    print(e)
    return False

def file_write(filepath):
  """
  judge filepath exists, write mode  
  @param filepath  
  @return boolean  
  """
  try:
    if os.path.exists(os.path.split(filepath)[0]):
      if os.path.isfile(filepath):
        os.remove(filepath)
      else:
        pass
      fd = open(filepath, 'w')
      fd.write('')
      fd.close()
    else:
      os.makedirs(os.path.split(filepath)[0])
      fd = open(filepath, 'w')
      fd.write('')
      fd.close()
    return True
  except Exception as e:
    print(e)
    return False