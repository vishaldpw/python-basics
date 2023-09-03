import random
mylist = ["Heads", "Tails"]
print(random.sample(mylist, k=1))


# other way
random_integer = random.randint(1,2)
if random_integer == 1:
    print("it's Heads")
else:
    print("it's Tails")

