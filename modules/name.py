# command line module
import sys

if len(sys.argv) < 2:
    sys.exit("Too few argument") # This causes the program to exit prematurely
    
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")
    
# else:
#     print("Hello, my name is", sys.argv[1])  # We don't have to hide the  main idea in the else statement
print(sys.argv[1])