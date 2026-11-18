student1 = [100, 68, 65, 50, 60]
student2 = [85, 83, 72, 80, 60]
student3 = [65, 93, 77, 81, 69]
student4 = [63, 55, 89, 78, 90]
student5 = [100, 78, 55, 89, 90]

sum1 = 0

for n in student1:
    sum1 += n

ave1 = sum1 / len(student1)
print("Student one score : ", end = " ")
print("Average : ",ave1, end = " ")
print("| Min score : ", min(student1), end = " ")
print("| Max score : ", max(student1))


sum2 = 0
for n in student2:
    sum2 += n

ave2 = sum2 / len(student2)
print("Student two score :", end = " ")
print("Average : ",ave2, end = " ")
print("| Min score : ", min(student2), end = " ")
print("| Max score : ", max(student2))

sum3 = 0
for n in student3:
    sum3 += n

ave3 = sum3 / len(student3)
print("Student three score :", end = " ")
print("Average : ",ave3, end = " ")
print("| Min score : ", min(student3), end = " ")
print("| Max score : ", max(student3))

sum4 = 0
for n in student4:
    sum4 += n

ave4 = sum4 / len(student4)
print("Student four score :", end = " ")
print("Average : ",ave4, end = " ")
print("| Min score : ", min(student4), end = " ")
print("| Max score : ", max(student4))

sum5 = 0
for n in student5:
    sum5 += n

ave5 = sum5 / len(student5)
print("Student five score :", end = " ")
print("Average : ",ave5, end = " ")
print("| Min score : ", min(student5), end = " ")
print("| Max score : ", max(student5))



