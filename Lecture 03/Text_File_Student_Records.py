# Create students.txt and write 5 records
with open("students.txt", "w") as file:
    file.write("101,Ali,Computer Science\n")
    file.write("102,Ahmad,IT\n")
    file.write("103,Sara,Software Engineering\n")
    file.write("104,Omar,Networking\n")
    file.write("105,Zahra,Database\n")

# Read and display all records
try:
    with open("students.txt", "r") as file:
        records = file.readlines()
        for record in records:
            print(record.strip())
except FileNotFoundError:
    print("File does not exist!")

# Search student by ID
sid = input("Enter student ID to search: ")

found = False
for record in records:
    if record.split(",")[0] == sid:
        print("Student Found:", record.strip())
        found = True

if not found:
    print("Student not found!")

# Append a new student
with open("students.txt", "a") as file:
    new_student = input("Enter ID, Name, Department: ")
    file.write(new_student + "\n")

# Count total records
with open("students.txt", "r") as file:
    print("Total Students:", len(file.readlines()))