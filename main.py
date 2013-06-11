#!/usr/bin/python
#coding:utf-8

import mechanize
import re 

br=mechanize.Browser()
br.set_handle_robots(False)
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

url=u"http://www.xiami.com/web/login"
      
br.open(url)

br.select_form(nr=0)
br["email"]="your email"
br["password"]="your password"
br.submit()

for link in br.links():
    if r"首页" in link.text:
        br.follow_link(link)

for sec_link in br.links():
    if r"每日签到" in sec_link.text:
        br.follow_link(sec_link)
