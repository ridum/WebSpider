from urllib2 import urlopen
from bs4 import BeautifulSoup

htmlarray = []
htmlarray.append(urlopen("https://courses.students.ubc.ca/cs/main?pname=subjarea&tname=subjareas&req=1&dept=CPSC"))
htmlarray.append(urlopen("https://courses.students.ubc.ca/cs/main?pname=subjarea&tname=subjareas&req=1&dept=MATH"))

coursepages = []
for html in htmlarray:
    bsObj = BeautifulSoup(html)
    # print bsObj
    array = bsObj.table.find_all('a')

    for element in array:
        coursepages.append("https://courses.students.ubc.ca/" + element.get('href'))
# print coursepages

combine = []
for percourse in coursepages:
    course = urlopen(percourse)
    courseObj = BeautifulSoup(course)
    array = courseObj.table.find_all('')
    courses = courseObj.find_all('td')
    sections = []

    for course in courses:
        courselink = course.a
        if courselink != None:
            header = "https://courses.students.ubc.ca/"
            section = courselink.attrs['href']
            # coursepages.append("https://courses.students.ubc.ca/" + element.get('href'))
            sections.append("https://courses.students.ubc.ca/" + courselink.attrs['href'])

    print sections
    combine.extend(sections)