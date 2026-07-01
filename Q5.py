#Q5. File Reading
#Read the contents of students.txt and print each student name on a new line.
f = open("students.txt", "r")
for line in f:
    print(line.strip())
f.close()