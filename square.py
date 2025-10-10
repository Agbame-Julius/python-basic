def main():
    x = int(input("Enter the value for x: ").strip())
    print(f"The square of {x} is {square(x)}")
    

def square(number):
    return number * number

main()