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
    gpa_tuple = {}
    for student in data:
        gpa_tuple[student.gpa()] = student
    bygpa_list = list(gpa_tuple.items())
    bygpa_list.sort()
    sorted_students = []
    for item in bygpa_list:
        sorted_students.append(item[1])
    filename = input('Enter a name for the output file: ')
    writeStudents(sorted_students, filename)
    print('The data has been written to', filename)

if __name__=='__main__': main()