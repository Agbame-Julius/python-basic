def main():
    name = input("What is your name? ").strip()
    hello(name)
    

def hello(to):
    print(f"Hello, {to}")

main()