# A list of students in a class
students = ["Hermione", "Ron", "Doc", "Ben"]
#Now I want to iterate over the list them

for student in students:
    print(student)
    
# I want to see their positions as well
for i in range(len(students)):
    print(i+1, students[i])