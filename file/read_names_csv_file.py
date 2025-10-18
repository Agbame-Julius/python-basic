import csv

students = []
with open("students.csv") as csvfile:
    reader = csv.reader(csvfile)
    for name, region in reader:
        students.append({"name": name, "region": region})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['region']}")