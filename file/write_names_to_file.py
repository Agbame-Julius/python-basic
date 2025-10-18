# A program to save to file
name = input("What's your name: ")

# file = open("names.txt", "a")
# file.write(f"{name}\n")
# file.close  # this closes the file after writing to it

with open("names.txt", "a") as file: # "with" will automatically close the file
    file.write(name)
    