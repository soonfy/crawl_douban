#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'douban spider class.'

__author__ = 'soonfy'

def str_num(result_str):
  nums = []
  if 'book' in result_str or '书' in result_str:
    nums.append(0)
  elif 'movie' in result_str or '电影' in result_str:
    nums.append(1)
  elif 'music' in result_str or '音乐' in result_str:
    nums.append(2)
  elif 'drama' in result_str or '舞台剧' in result_str:
    nums.append(3)
  elif 'dongxi' in result_str or '东西' in result_str:
    nums.append(4)
  elif 'item' in result_str or '条目' in result_str:
    nums.append(5)
  elif 'app' in result_str or '移动应用' in result_str:
    nums.append(6)
  elif 'game' in result_str or '游戏' in result_str:
    nums.append(7)
  elif 'doulist' in result_str or '豆列' in result_str:
    nums.append(8)
  elif 'review' in result_str or '评论' in result_str:
    nums.append(9)
  elif 'status' in result_str or '广播' in result_str:
    nums.append(10)
  elif 'contact' in result_str or '关注' in result_str:
    nums.append(11)
  elif 'rev_contact' in result_str or '被关注' in result_str:
    nums.append(12)
  elif 'photo' in result_str or '相册' in result_str:
    nums.append(13)
  elif 'join' in result_str or '小组' in result_str:
    nums.append(14)
  elif 'minisite' in result_str or '小站' in result_str:
    nums.append(15)
  elif 'market' in result_str or '市集' in result_str:
    nums.append(16)
  elif 'event' in result_str or '同城' in result_str:
    nums.append(17)
  elif 'online' in result_str or '线上' in result_str:
    nums.append(18)
  elif 'thing' in result_str or '事情' in result_str:
    nums.append(19)
  elif 'all' in result_str or '所有' in result_str:
    nums = range(20)
  return nums

def parse_people(arr, result_str):
  print(arr)
  soup = arr[1]
  h2s = soup.h2
  nums = list(str_num(result_str))
  print(nums)
  print(len(h2s))

  for index, h2 in enumerate(h2s):
    if index in nums:
      print(index)
  