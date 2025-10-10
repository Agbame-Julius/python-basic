print("Hello, world")

def func():
    name = input("What is your name? ").strip()
    print(f"Your name is {name}")

func()

name = input("what is your full name: ").strip().capitalize()
#unpacking the user's first name and last name
first_name, last_name = name.split(" ")
print(f"Hello, {first_name}")