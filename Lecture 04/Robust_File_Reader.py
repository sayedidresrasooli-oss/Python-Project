filename = input("Enter filename: ")

try:
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()

except FileNotFoundError:
    print("Error: File not found!")

except PermissionError:
    print("Error: Permission denied!")

except UnicodeDecodeError:
    print("Error: Cannot decode file as UTF-8!")

else:
    print("File content:")
    print(content)