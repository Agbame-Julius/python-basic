# a program to read from csv files
# with open("students.csv") as file:
#     for line in file:
#         name, age, region = line.rstrip().split(",")
#         print(f"{name} is in {region}")

# Reading and sorting the students from the csv file
students = []
with open("students.csv") as file:
    for line in file:
        name, region = line.rstrip().split(",")
        student = {"name": name, "region": region}
        students.append(student) #appending the student dictionary to the list

# a function to get the student's name from the dictionary
# def get_name(student):
#     return student["name"] 

#Since we are only using the get_name function once, it is better to use a lambda function instead.


#Sorting the list of students by their names
for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['region']}")
    