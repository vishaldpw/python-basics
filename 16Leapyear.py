year = int(input("Enter  the year: "))
#print(year)
r = year % 4
x = year % 100
y = year % 400

if r == 0:
   if x == 0:
       if y == 0:
        print("Leap year. ")
       elif y != 0:
        print("not Leap year.")
   elif x != 0:
       print("Leap year. ") 
else:   
    print("not Leap year. ")


# if x == 0:
#     if y == 0:
#         print("this is a Leap Year")
# else:
#     print("Further Check required")



    


