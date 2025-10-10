def add(x, y):
    return x + y
sum = add(2, 3)
print(sum)

# x = int(input("Enter the first number to add: ").strip())
# y = int(input("Enter the second number to add: ").strip())

# x = float(input("Enter the first number:").strip())
# y = float(input("Enter the second number: ").strip())
# sum = round(x + y)
# formating the result to be more readable
# print(f"{sum:,}")

x = float(input("Enter the first number: ").strip())
y = float(input("Enter the second number: ").strip())
# z = round(x / y, 2) # rounding to 2 decimal places
z = x / y
print(f"{z:.2f}")