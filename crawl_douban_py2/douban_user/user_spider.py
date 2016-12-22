#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'user spider class.'

__author__ = 'soonfy'

# modules
from bs4 import BeautifulSoup

from spider_middleware import spider_open

class UserSpider(object):
  """
  douban user spider class  
  @param userid  
  @param opener  
  relation: contacts, rev_contacts  
  @param timeout: 60 * 2
  """
  def __init__(self, userid, opener):
    self.userid = userid
    self.opener = opener
    self.contacts = 'https://www.douban.com/people/%s/contacts' % userid
    self.rev_contacts = 'https://www.douban.com/people/%s/rev_contacts' % userid

  def crawl_contacts(self):
    """
    crawl user contacts  
    @return soup, relation  
    """
    opener, contacts = self.opener, self.contacts
    print(contacts)
    body = spider_open(opener, contacts)
    soup = BeautifulSoup(body, 'html.parser')
    return soup, 'contacts'

  def crawl_rev_contacts(self):
    """
    crawl user rev_contacts  
    @return soup, relation  
    """
    opener, rev_contacts = self.opener, self.rev_contacts
    print(rev_contacts)
    body = spider_open(opener, rev_contacts)
    soup = BeautifulSoup(body, 'html.parser')
    return soup, 'rev_contacts'
