# A function to take positive number from a user and print meow that number of times

def main():
    number = get_number()
    meow(number)
    

def get_number():
    while True:
        n = int(input("What is n? ").strip())
        if n > 0:
            return n

def meow(n):
    for _ in range(n):
        print("Meow")
    
# This checks if the file is being run directly by the interpreter
if __name__ == "__main__":
    main()