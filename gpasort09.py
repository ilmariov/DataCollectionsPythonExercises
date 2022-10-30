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
    gpas = {}
    for student in data:
        gpas[student.gpa()] = student
    gpa_list = list(gpas.keys())
    sorted_gpa = gpa_list.sort()
    # enter code to finish
    filename = input('Enter a name for the output file: ')
    writeStudents(sorted_gpa, filename)
    print('The data has been written to', filename)

if __name__=='__main__': main()