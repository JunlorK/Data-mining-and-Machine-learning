# -*- coding: utf8 -*-
'''
Created on Mar 29, 2016

@author: JuniorK
'''
import feedparser
import urllib
from bs4 import  BeautifulSoup
def get_link(rss):
    feed = feedparser.parse(rss)
    list_link=[]
    for item in feed['entries']:
        list_link.append(str(item['link']))
    return list_link
def get_title(rss):
    feed = feedparser.parse(rss)
    list_title=[]
    for item in feed['entries']:
        list_title.append(str(item['title']))
    return list_title
def get_content(link):
    html=urllib.urlopen(link).read()
    soup = BeautifulSoup(html, 'html.parser')
    result = soup.select("#divNewsContent")
    soup = BeautifulSoup(str(result[0]), 'html.parser') 
    content=''
    for ptag in soup.find_all("p"):
        if str(ptag).find("p style=\"text-align: justify;\"")!=-1:
            tmp=str(ptag).replace("<p style=\"text-align: justify;\">","").replace("</p>", "")+'\n'
            if tmp!=" \n" and tmp!=" ": content+=tmp+'\n'
        if str(ptag).find("<p>")!=-1:
            tmp=str(ptag).replace("<p>","").replace("</p>","")+'\n'
            if tmp!=" \n" and tmp!=" ": content+=tmp+'\n'
    return content
#get_content('http://dantri.com.vn/giai-tri/linh-nga-pham-huong-va-ho-ngoc-ha-ghi-dau-an-vao-top-sao-mac-dep-20160329120918197.htm')