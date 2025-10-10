# it stores a key value pair
students = {
    "Hermione": "Gryffindor",
    "Ron": "Gryffindor",
    "Josh":"Slytherin",
    "Draco": "Accra"
}

new_students = [
    
     {"name":"Hermione", "House": "Gryffindor","Patronus": "Otter"},
     {"name": "Harry", "House": "Gryffindor", "Patronus": "Otag"},    
     {"name" : "Ron", "House": "Gryffindor", "Patronus": "Jack Russel"},
     {"name" : "Draco", "House": "Slytherin", "Patronus": None}
    
]

print(students["Draco"])

for student in new_students:
    print(student["name"], student["House"], student["Patronus"], sep=", ")