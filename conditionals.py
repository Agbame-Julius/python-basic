grade = int(input("What your grade for math? "))

match grade:
    case 90:
        print("A")
    case 80:
        print("B")
    case _:
        print("F")