from gpa import Student, makeStudent

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

def main():
    print('This program sorts student grade information by GPA')
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


if __name__=='__main__': main()