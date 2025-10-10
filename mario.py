def main():
    n = int(input("what is n? "))
    draw_square(n)
    

def draw_square(number):
    # for each row in square
    for i in range(number):
        # for each brick in row
        for j in range(number):
            #print brick on the same line
            print("#", end="")
        #start a new line for the next row
        print()
main()