# douban spider  

## spider process  

  1. [login douban](login-douban)  
  ```
  url
  https://www.douban.com/accounts/login
  data
  param = {
    "source": 'None',
    "redir": 'https://www.douban.com/people/67492098/contacts',
    "form_email": 'soonfy@163.com',
    "form_password": 'soonfy163',
    "login": '登录'
  }
  2. [crawl douban user contacts]  
  3. [crawl douban user movies]  
  4. [crawl douban movie contents]  

# modules  

  * [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html)  

  ```
  apt-get install Python-bs4
  or pip install beautifulsoup4
  parser
  apt-get install Python-html5lib
  or pip install html5lib
  ```

# methods  

