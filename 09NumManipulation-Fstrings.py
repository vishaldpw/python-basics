#How to round off a number
a = 101
b = 3

h = round(a / b) 
print(h)
h2 = round(a / b, 3)  ### rounded to 3 decimals
print(h2)

score = 5
print(score)
score += 2 #this will increment score by 2
print(score)

score = 5
print(score)
score -= 2 #this will dec score by 2
print(score)

## you can also use *= /*  like += -=

# Fstring
name = "vishal" 
f1 = 4
f2 = 1.8
f3 = True

print(f"Your name is {name}, Your f1 score is: {f1}, Your f2 score is {f2}, You are a member: {f3}")
## In this Print statement we do not need to convert all to str to use just 1 print statement 