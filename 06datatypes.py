### Data Types
## String : collection of  
print("Hello"[4]) # This will print chracter at location 0, this method of pulling data is called subscripting
## integer : whole numbers
print(14+18)       ## Here numbers are treated as integers
print("14"+"18")   ### Here numbers are treated as strings
## Float : numbers with decimal places Ex: 3.1415
## Boolean : It is Simple  >>  True or False

print(len("456233"))   ## Here the number is considered a string 
### Type Function provides the info of data types
numchar = len(input("Enter Your Name \n"))
print(type(numchar)) 
print(type(3.17)) 
#Ex2: converting int to String   ### you can use "str" "int" or "float" to convert a data type
### float(a) ==> will convert a to float 
numchar = len(input("Enter Your Name \n"))
print(type(numchar)) 
new_numchar = str(numchar)
print(type(new_numchar))
## EX3
a = 5
print(type(a))
b = float(a)
print(type(b))

