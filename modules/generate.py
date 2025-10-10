# This is about library
import random
coin = random.choice(["Head", "tails"])
# print(coin)

number = random.randint(1, 10) # generate a random number between 1 and 10
# print(number)

names = ["Julius", "Ben", "Mola"]
random.shuffle(names)

for name in names:
    print(name)