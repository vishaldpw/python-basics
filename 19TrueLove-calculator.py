# "or" "and" , "not" operators
## adding mid Life crisis people free tickets
# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆
#Write your code below this line 👇
name1l = name1.lower()
name2l = name2.lower()
comb = name1l + name2l
tcount = comb.count("t")
rcount = comb.count("r")
ucount = comb.count("u")
ecount = comb.count("e")
lcount = comb.count("l")
ocount = comb.count("o")
vcount = comb.count("v")
m = int(tcount) + int(rcount) + int(ucount) + int(ecount)
n = int(lcount) + int(ocount) + int(vcount) + int(ecount)
print(m)
print(n)
per =  m * 10 + n
# For Love Scores less than 10 or greater than 90, the message should be:
# "Your score is **x**, you go together like coke and mentos."
if per <=10 or per >=90:
    print("Your score is " + str(per) + " you go together like coke and mentos. ")
elif per >=40 and per <=50:
    print("Your score is " + str(per) + " you are alright together. ")
else: 
    print("Your score is" + str(per) )