# a function to determine if an input is an integer and print out the integer
def main():
    x = get_int()
    print(f"X is {x}")

def get_int():
    while True:
        try:
            x = int(input("Enter an integer: "))
        except ValueError:
            print("X is not an integer")
        else:
            break
    return x

main()
            