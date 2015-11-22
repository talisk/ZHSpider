# -*- coding: UTF-8 -*-

__author__ = 'sunkai'

import urllib2

from bs4 import BeautifulSoup


class Spider:

    def __init__(self):
        self.siteURL = 'http://www.zhihu.com/topic/19555404/top-answers'

    def getPage(self, page):
        url = self.siteURL + '?page=' + str(page)
        print url
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        return response.read().decode('utf8')

    def getContents(self, page):
        page = self.getPage(page)

        soup = BeautifulSoup(page, 'html.parser')

        profileList = soup.find_all(attrs={"class": "author-link"})

        for str in profileList:
            nameList = str.string
            print nameList
            urlDictionary = str.attrs
            print 'http://www.zhihu.com' + urlDictionary['href']

spider = Spider()
spider.getContents(2)