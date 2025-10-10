name = input("What's your name: ")

match name:
    case "Harry" | "Ron" | "Hermione": # The pipe is equivalent to or
        print("Gryffindor")
    
    case "Julius":
        print("Accra")
    case _: # the underscore(_) is the default case 
        print("Who?")