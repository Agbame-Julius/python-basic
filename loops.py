i = 0
# While loop does something when a condition is met
while i < 3:
    print("meow")
    i += 1 # we don't have i++
    
# for loop works with a list
for _ in range(3): # since we are not using the i variable, we can use underscore instead
    print("Bark!!")
    
    
#I want take an input from a user and it should be positive

while True:
    n = int(input("what's n: "))
    if n > 0:
        break #This breaks the infinite loop when n is positive 
    
    
# I want to meow the number of n times
for _ in range(n):
    print("meow")

    

