

names = {1:"Ahmad ""Cource code 120", 2:"Ali ""Cource code 150", 3:"Sayed Kalil ""Cource code 200", 4:"Afzal ""Cource code 130", 5:"Mohammad ""Cource code 140"}
cource = ["Python", "Java", "Html","C++","C#"]
registration = {input("Register for cource: ")}

cource.append(input("Please add the cource: "))
cource.pop(int(input("Drop cource: ")))

a = int(input("Please Enter the ID: "))
if a in names:
    print(names[a])
else:
    print("Invalid ID")


print("List of cource: ", cource)
print("registred cource: ",registration)






