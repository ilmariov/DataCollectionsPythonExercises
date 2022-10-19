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
    print('''\nFields to sort on:
    1: By GPA
    2: By Name
    3: By Credits''')
    field = input('Enter a valid option to sort on: ')
    while field!='1' and field!='2' and field!='3':
        field = input('Enter a valid option to sort on: ')
    if field == '1':
        data.sort(key=Student.gpa)
    elif field == '2':
        data.sort(key=Student.getName)
    else:
        data.sort(key=Student.getHours)
    filename = input('Enter a name for the output file: ')
    writeStudents(data, filename)
    print('The data has been written to', filename)

if __name__=='__main__': main()