import random
k = input("Select rock, paper or scissors: \n") 
print("your Choice is: \n"+ k)
l1 = ["rock", "paper", "scissors"]
randoml1 = random.choice(l1)
print("Computer Choice is: \n"+ randoml1)

if k=="rock" and randoml1=="rock":
    print("Draw")
elif k=="rock" and randoml1=="paper":
    print("you Loose")
elif k=="paper" and randoml1=="paper":
    print("Draw")
elif k=="paper" and randoml1=="scissors":
    print("You Loose")
elif k=="paper" and randoml1=="rock":
    print("You Win")
elif k=="scissors" and randoml1=="paper":
    print("You Win")
elif k=="scissors" and randoml1=="scissors":
    print("Draw")
elif k=="scissors" and randoml1=="rock":
    print("You Loose")
else:
    print("you WIN")