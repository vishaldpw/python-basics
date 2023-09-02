print("Welcome to ODD EVEN Check programe: ")
# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line
# % (this is modulo - it prints the remainder)
r = number % 2
#print(r)
if r == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")