while True:
    try:
        n = int(input("What is n: "))
    except ValueError:
        print("n is not an integer")
    else:
        break
print(f"n is {n}")