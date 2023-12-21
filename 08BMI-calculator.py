weight = input("enter your weight in KGs: \n")
Height = input("enter your height in meters: \n")
## ignore this line###
print(type(weight))
print(type(Height))
w = float(weight)
h = float(Height)
bmi = w / (h * h)
print("Your BMI is:")
print(int(bmi))  ### BMI required as whole number 
