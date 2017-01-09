from urllib2 import urlopen
from bs4 import BeautifulSoup
import MySQLdb

db = MySQLdb.connect(
    host='127.0.0.1',
    user='root',
    passwd='',
    db='course'
)
if db:
    print "mySQL connected"
else:
    print "connect dailed"

cur = db.cursor()

html = urlopen("https://courses.students.ubc.ca/cs/main?pname=subjarea&tname=subjareas&req=1&dept=CPSC")
bsObj = BeautifulSoup(html)
array = bsObj.table.find_all('a')

coursepages = []
for element in array:
    coursepages.append("https://courses.students.ubc.ca/"+element.get('href'))
    # print "https://courses.students.ubc.ca/"+element.get('href')
    # print element.get_text()


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
            sections.append("https://courses.students.ubc.ca/" + courselink.attrs['href'])
    combine.extend(sections)


for persection in combine:
    try:
        section = urlopen(persection)
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
        totalremain = text[p1index + p1length:p2index]
        query = "insert into info values (\"" + sectionname + "\"," + totalremain + ")"
        print query
        cur.execute(query)
        db.commit()
        info = [sectionname, totalremain]
    except Exception,e:
        print "something wrong happened"
        print str(e)
print "Parser done."
db.close()
