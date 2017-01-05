from urllib2 import urlopen
from bs4 import BeautifulSoup


html = urlopen("https://courses.students.ubc.ca/cs/main?pname=subjarea&tname=subjareas&req=1&dept=CPSC")
bsObj = BeautifulSoup(html)
array = bsObj.table.find_all('a')


coursepages = []
for element in array:
    # fout.write(element.get_text())
    # fout.write("<br>")
    # fout.write("https://courses.students.ubc.ca/"+element.get('href'))
    # fout.write("<br>")
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
            header = "https://courses.students.ubc.ca/"
            section = courselink.attrs['href']
            # coursepages.append("https://courses.students.ubc.ca/" + element.get('href'))
            sections.append("https://courses.students.ubc.ca/" + courselink.attrs['href'])

    # print sections
    combine.extend(sections)


fout = open('output.html', 'w')

fout.write("<html><meta charset=\"utf-8\" />")
fout.write("<body>")
fout.write("<table>")
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
        print sectionname
        print totalremain
        # print(element)

        info = [sectionname, totalremain]

        fout.write("<tr>")
        fout.write("<td>%s</td>" % info)
        fout.write("</tr>")
    except Exception:
        a = 1

fout.write("</table>")
fout.write("</body>")
fout.write("</html>")
fout.close()

print(coursepages)

