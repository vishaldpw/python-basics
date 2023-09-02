### Nested if else

print("Welcome to roller coaster Ride: ")
height = int(input("what's your height in cms: "))
if height >= 120:
    print("you can use the ride")
    age = int(input("whats your age"))
    if age <= 12:
        print("You need to pay $5. ")
    elif age <18:    ### This will catch all >12 but less tha 18 ###
        print("you need topay 10$. ")
    else:
        print("pay $15 please")      
else:
    print("you cannot use the ride")
