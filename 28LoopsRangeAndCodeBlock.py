# For Loops
fruits = ["apple", "chikoo", "manago"]
for i in fruits:
    print(i)
    print(i+ " pie")
    print(fruits) ## This is Part of Loop, hence will be printed 3 times
print(fruits)     ## This is not Part of Loop, hence will be printed 3 times 
print("---------------------------")
print("---------------------------")
# Range Functions
for number in range(99, 105):
    print(number)
# Step Function  3rd number 3 is the step :: You will get table of 3 
for number in range(3, 99, 3):
    print(number)

## add all numbers for 1 to 100
sum = 0
for i in range(1, 101):
    sum = sum + i
print(f"Sum of all numbers is: {sum}")