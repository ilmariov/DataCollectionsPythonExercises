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
    name_asc = Button(win, Point(14,12), 8, 3, 'Name')
    credits_asc = Button(win, Point(14,8), 8, 3, 'Credits')
    Text(Point(27,19), 'Desc. Order').draw(win)
    gpa_desc = Button(win, Point(27,16), 8, 3, 'GPA')
    name_desc = Button(win, Point(27,12), 8, 3, 'Name')
    credits_desc = Button(win, Point(27,8), 8, 3, 'Credits')
    outmsg = Text(Point(15,3), 'No file generated so far').draw(win)
    quit_button = Button(win, Point(32,3), 6, 3, 'Quit')
    entry_list = [infile, outfile]
    buttons = [gpa_asc, name_asc, credits_asc, gpa_desc, name_desc, credits_desc, quit_button]
    return win, entry_list, buttons, outmsg    

def main():
    win, entries, buttons, outmsg = gpaWindow()
    for i in range(7):
        buttons[i].activate()
    pt = win.getMouse()
    while not(buttons[6].clicked(pt)):
        pressed_button = []
        for i in range(6):
            pressed_button.append(buttons[i].clicked(pt))
        data = readStudents(entries[0].getText())
        sort_field = [Student.gpa, Student.getName, Student.getHours]
        for i in range(6):
            if pressed_button[i]:
                if i < 3:
                    data.sort(key=sort_field[i])
                else:
                    data.sort(key=sort_field[i-3], reverse=True)
                writeStudents(data, entries[1].getText())
                outmsg.setText('** {0} file generated **'.format(entries[1].getText()))
        pt = win.getMouse()
    win.close()


if __name__=='__main__': main()