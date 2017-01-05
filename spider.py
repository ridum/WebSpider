from urllib2 import urlopen
from bs4 import BeautifulSoup

htmlarray = []
htmlarray.append(urlopen("https://courses.students.ubc.ca/cs/main?pname=subjarea&tname=subjareas&req=1&dept=CPSC"))
coursepages = []
for html in htmlarray:
    bsObj = BeautifulSoup(html, "html.parser")
    array = bsObj.table.find_all('a')

    for element in array:
        coursepages.append("https://courses.students.ubc.ca/" + element.get('href'))



combine = []
for percourse in coursepages:
    course = urlopen(percourse)
    courseObj = BeautifulSoup(course, "html.parser")
    array = courseObj.table.find_all('')
    courses = courseObj.find_all('td')
    sections = []

    for course in courses:
        courselink = course.a
        if courselink != None:
            header = "https://courses.students.ubc.ca/"
            section = courselink.attrs['href']
            sections.append("https://courses.students.ubc.ca/" + courselink.attrs['href'])


    combine.extend(sections)


fout = open('output.html', 'w')

fout.write("<html><meta charset=\"utf-8\" />")
fout.write("<body>")
fout.write("<table>")
for persection in combine:
    try:
        section = urlopen(persection)
        sectionObj = BeautifulSoup(section, "html.parser")
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

