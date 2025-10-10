# this program is to read names types in the command line
import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:]: #this is to start iterating from the first index
    print("Hello, my name is", arg) 