# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
h2 = height * height
bmi = weight / h2
mp = round(bmi)
if mp > 18.5:
    if mp < 25:
     print("Your BMI is "+ str(mp)+ ", you have a normal weight." )
    elif mp < 30:
     print("Your BMI is "+ str(mp)+ ", you are slightly overweight." )
    elif mp < 35:
     print("Your BMI is "+ str(mp)+ ", you are obese." )
    elif mp > 35:
     print("Your BMI is "+ str(mp)+ ", you are critically obese." )
else:
    print("Your BMI is "+ str(mp)+ ", you are underweight." )
