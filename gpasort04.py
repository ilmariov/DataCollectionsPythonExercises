from gpa import Student, makeStudent
from graphics import *
from button import Button

def readStudents(filename):
    infile = open(filename, 'r')
    students = []
    for line in infile:
        students.append(makeStudent(line))
    infile.close()
    return students

def writeStudents(students, filename):
    outfile = open(filename, 'w')
    for s in students:
        print('{0}\t{1}\t{2}'.format(s.getName(), s.getHours(), s.getQPoints()), file=outfile)
    outfile.close()

def gpaWindow():
    win = GraphWin('GPA Sorting', 400, 300)
    win.setCoords(0,0,40,30)
    Text(Point(20,27), 'This program sorts student grade information by GPA').draw(win)

    Text(Point(5,23), 'Input File').draw(win)
    Text(Point(24,23), 'Output File').draw(win)
    infile = Entry(Point(14,23),10).draw(win)
    infile.setText('students.dat')
    outfile = Entry(Point(34,23),10).draw(win)
    outfile.setText('out.dat')

    Text(Point(5,16), 'Sort by:').draw(win)
    Text(Point(14,19), 'Asc. Order').draw(win)
    gpa_asc = Button(win, Point(14,16), 8, 3, 'GPA')
    gpa_asc.activate()
    name_asc = Button(win, Point(14,12), 8, 3, 'Name')
    name_asc.activate()
    credits_asc = Button(win, Point(14,8), 8, 3, 'Credits')
    credits_asc.activate()

    Text(Point(27,19), 'Desc. Order').draw(win)
    gpa_desc = Button(win, Point(27,16), 8, 3, 'GPA')
    gpa_desc.activate()
    name_desc = Button(win, Point(27,12), 8, 3, 'Name')
    name_desc.activate()
    credits_desc = Button(win, Point(27,8), 8, 3, 'Credits')
    credits_desc.activate()

    outmsg = Text(Point(15,3), 'No file generated so far').draw(win)
    quit_button = Button(win, Point(32,3), 6, 3, 'Quit')
    quit_button.activate()

    pt = win.getMouse()

    while not(quit_button.clicked(pt)):
        pressed_button = [gpa_asc.clicked(pt), name_asc.clicked(pt), credits_asc.clicked(pt), 
            gpa_desc.clicked(pt), name_desc.clicked(pt), credits_desc.clicked(pt)]
        data = readStudents(infile.getText())
        sort_field = [Student.gpa, Student.getName, Student.getHours]
        for i in range(6):
            if pressed_button[i]:
                if i < 3:
                    data.sort(key=sort_field[i])
                else:
                    data.sort(key=sort_field[i-3], reverse=True)
                writeStudents(data, outfile.getText())
                outmsg.setText('{0} file generated'.format(outfile.getText()))
        pt = win.getMouse()
    win.close()

def main():
    filename = input('Enter the name of the data file: ')
    data = readStudents(filename)
    field = int(input('''Enter '1' to sort by gpa, '2' by name, '3' by credits: '''))
    while field!=1 and field!=2 and field!=3:
        field = int(input('Enter a valid option to sort on: '))
    order = int(input('''Enter '1' to sort in ascending order, '2' otherwise: '''))
    while order!=1 and order!=2:
        order = int(input('''Enter '1' to sort in ascending order, '2' otherwise: '''))

    sort_field = [Student.gpa, Student.getName, Student.getHours]
    sort_order = [False, True]
    for i in range(3):
        if field==i+1:
            data.sort(key=sort_field[i], reverse=sort_order[order-1])
    filename = input('Enter a name for the output file: ')
    writeStudents(data, filename)
    print('The data has been written to', filename)


if __name__=='__main__': gpaWindow()