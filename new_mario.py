def main():
    print_square(4)


def print_square(size):
    # for each row
    for i in range(size):
        print_row(size)
        print()
        
 # for print each brick in a row       
def print_row(width):
   for j in range(width):
       print("#", end="")
    

main()