# Q4. File Creation
#Create a file named students.txt and write 5 student names into it.
f = open("students.txt", "w")
f.write("Aarav\n")
f.write("Priya\n")
f.write("Rohan\n")
f.write("Sneha\n")
f.write("Karan\n")
f.close()
print("students.txt created")
f = open("students.txt", "r")
a = f.read()
print(a)
f.close()



