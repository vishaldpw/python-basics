# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
p = len(names)
random_integer = random.randint(0, p - 1)
K = (names[random_integer])
print(K +" is going to buy the meal today!")