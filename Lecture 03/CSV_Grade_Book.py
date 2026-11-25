import csv

# Create students.csv
students = [
    ["101", "Ali Ahmad", 80, 90],
    ["102", "Mohammad Afzal", 70, 85],
    ["103", "Sara Khan", 40, 50],
    ["104", "John Smith", 90, 95],
    ["105", "Abdul Rahman", 60, 70]
]

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["student_id", "name", "midterm", "final"])
    writer.writerows(students)

# Read and calculate results
results = []

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        total = int(row["midterm"]) + int(row["final"])
        average = total / 2

        row["total"] = total
        row["average"] = average
        results.append(row)

        if average >= 50:
            print(row["name"], "Passed")

# Write results.csv
with open("results.csv", "w", newline="") as file:
    fields = ["student_id", "name", "midterm", "final", "total", "average"]
    writer = csv.DictWriter(file, fieldnames=fields)
    writer.writeheader()
    writer.writerows(results)

print("Results saved successfully!")