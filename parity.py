def main():
    x = int(input("What is x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")
        
def is_even(n):
    # if n % 2 == 0:
    #     return True
    # return False
    return n % 2 == 0  # Use this because the n % 2 == 0 will return either true or false
main()