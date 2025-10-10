# a function to determine if an input is an integer and print out the integer
def main():
    x = get_int()
    print(f"X is {x}")

def get_int():
    while True:
        try:
            return int(input("Enter an integer: ")) # use the return statement over here since we are not using the variable 
        except ValueError:
            print("X is not an integer") # can use pass keyword over here if we don't to tell the user what it is we are handling

main()
            