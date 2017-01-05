#!/usr/bin/python
# -*- coding: UTF-8 -*-
from urllib2 import urlopen
from bs4 import BeautifulSoup
import MySQLdb

# #连接mysql和获取方法
# db = MySQLdb.connect(
#     host='127.0.0.1',
#     user='root',
#     passwd='root',
#     db='course'
# )
# cursor = db.cursor()
#
# #获取cpsc主页,并丢到bs里
# html = urlopen("https://courses.students.ubc.ca/cs/main?pname=subjarea&tname=subjareas&req=1&dept=CPSC")
# bsObj = BeautifulSoup(html)
#
# #在table里找到所有有a的值
# array = bsObj.table.find_all('a')
#
# #所有有a的href转成超链接
# coursepages = []
# for element in array:
#     # fout.write(element.get_text())
#     # fout.write("<br>")
#     # fout.write("https://courses.students.ubc.ca/"+element.get('href'))
#     # fout.write("<br>")
#     coursepages.append("https://courses.students.ubc.ca/"+element.get('href'))
#     # print "https://courses.students.ubc.ca/"+element.get('href')
#     # print element.get_text()
#
#
# combine = []
# for percourse in coursepages:
#     course = urlopen(percourse)
#     courseObj = BeautifulSoup(course)
#     array = courseObj.table.find_all('')
#     courses = courseObj.find_all('td')
#     sections = []
#
#     for course in courses:
#         courselink = course.a
#         if courselink != None:
#             header = "https://courses.students.ubc.ca/"
#             section = courselink.attrs['href']
#             # coursepages.append("https://courses.students.ubc.ca/" + element.get('href'))
#             sections.append("https://courses.students.ubc.ca/" + courselink.attrs['href'])
#
#     # print sections
#     combine.extend(sections)
#
#
# # course = urlopen("https://courses.students.ubc.ca/cs/main?pname=subjarea&tname=subjareas&req=3&dept=CPSC&course=320")
# # courseObj = BeautifulSoup(course)
# # array = courseObj.table.find_all('')
# # courses = courseObj.find_all('td')
# # sections = []
# #
# # for course in courses:
# #     courselink = course.a
# #     if courselink != None:
# #         header = "https://courses.students.ubc.ca/"
# #         section = courselink.attrs['href']
# #         # coursepages.append("https://courses.students.ubc.ca/" + element.get('href'))
# #         sections.append("https://courses.students.ubc.ca/" + courselink.attrs['href'])
#
# # print sections
# validsections = []
#
# for s in combine:
#     try:
#         section = urlopen(s)
#         sectionObj = BeautifulSoup(section)
#         sectiontotext = sectionObj.find('h4').get_text()
#         if sectiontotext.find('Lecture') != -1:
#             validsections.append(s)
#             # print sectionObj.find('h4')
#         else:
#             a = 1
#     except Exception:
#         a = 1
# # print validsections
#
# fout = open('output.html', 'w')
#
# fout.write("<html><meta charset=\"utf-8\" />")
# fout.write("<body>")
# fout.write("<table>")
# for persection in validsections:
#     try:
#         section = urlopen(persection)
#         sectionObj = BeautifulSoup(section)
#
#         sectionname = sectionObj.find('h4').get_text()
#
#         text = sectionObj.get_text()
#
#         p1 = 'Total Seats Remaining:'
#         p1index = text.index(p1)
#         # print p1index
#         p1length = len(p1)
#         # print p1length
#
#         p2 = 'Currently Registered:'
#         p2index = text.index(p2)
#         # print p2index
#         p2length = len(p2)
#         # print p2length
#
#         p3 = 'General Seats Remaining:'
#         p3index = text.index(p3)
#         # print p3index
#         p3length = len(p3)
#         # print p3length
#
#         p4 = 'Restricted Seats Remaining*:'
#         p4index = text.index(p4)
#         # print p4index
#         p4length = len(p4)
#         # print p3length
#
#         p5 = '*These seats are '
#         p5index = text.index(p5)
#         # print p5index
#         p5length = len(p5)
#         # print p5length
#
#         totalremain =       text[p1index + p1length:p2index]
#         # registered =        text[p2index + p2length:p3index]
#         generalremain =     text[p3index + p3length:p4index]
#         restrictedremain =  text[p4index + p4length:p5index]
#         # print totalremain
#         # print registered
#         # print generalremain
#         # print restrictedremain
#
#
#         info = [sectionname,p1,totalremain,p3,generalremain,p4,restrictedremain]
#
#         fout.write("<tr>")
#         fout.write("<td>%s</td>" % info)
#         fout.write("</tr>")
#     except Exception:
#         a = 1
#
# fout.write("</table>")
# fout.write("</body>")
# fout.write("</html>")
# fout.close()
#
# print "finished"

section = urlopen("https://courses.students.ubc.ca/cs/main?pname=subjarea&tname=subjareas&req=5&dept=CPSC&course=320&section=T2S")
sectionObj = BeautifulSoup(section)

sectionname = sectionObj.find('h4').get_text()

text = sectionObj.get_text()

p1 = 'Total Seats Remaining:'
p1index = text.index(p1)
# print p1index
p1length = len(p1)
# print p1length

p2 = 'Currently Registered:'
p2index = text.index(p2)
# print p2index
p2length = len(p2)
# print p2length

p3 = 'General Seats Remaining:'
p3index = text.index(p3)
# print p3index
p3length = len(p3)
# print p3length

p4 = 'Restricted Seats Remaining*:'
p4index = text.index(p4)
# print p4index
p4length = len(p4)
# print p3length

# p5 = '*These seats are '
# p5index = text.index(p5)
# # print p5index
# p5length = len(p5)
# # print p5length
p5 = '*These seats are'
try:
    p5index = text.index(p5)
except:
    p5index = p4index + p4length + 1

totalremain = text[p1index + p1length:p2index]
# registered =        text[p2index + p2length:p3index]
generalremain = text[p3index + p3length:p4index]
restrictedremain = text[p4index + p4length:p5index].strip().lstrip().rstrip(',')
# print totalremain
# print registered
# print generalremain
# print restrictedremain


info = [sectionname, p1, totalremain, p3, generalremain, p4, restrictedremain]
print info