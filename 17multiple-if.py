### Nested if else
### Here we added a condition of asking pic for additional 3 USD
bill = 0
print("Welcome to roller coaster Ride: ")
height = int(input("what's your height in cms: "))
if height >= 120:
    age = int(input("whats your age: "))
    if age <= 12:
        bill = 5
        #print("You need to pay $5. ")
    elif age <18:    ### This will catch all >12 but less tha 18 ###
        bill = 10
        #print("you need topay 10$. ")
    else:
        bill = 15
        #print("pay $15 please")
    pic = input("Do you need a pic: Y or N ")
    if pic == "Y":
        bill = bill + 3
    print("you need to pay $"+str(bill))
               
else:
    print("you cannot use the ride")
