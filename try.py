#!/usr/bin/python
# -*- coding: UTF-8 -*-
from urllib2 import urlopen
from bs4 import BeautifulSoup
import re
import mysql.connector
html = urlopen("https://courses.students.ubc.ca/cs/main?submit=Login&serviceType=courses&studentid=27869149").read()
bsObj = BeautifulSoup(html)

tds = bsObj.find_all('td')
print tds
for td in tds:
    print td.find_all('a')
# for b in a:
#     c = "https://courses.students.ubc.ca"+b.get('href')
#     print c
#     # print b.get('href')