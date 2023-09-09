fruits = ["apple", "jackfruit", "banana", "berry"]
print(fruits[2])   ## No error here
print(fruits[20])  ### We will get an index error ("IndexError: list index out of range") as item#20 not present 

# Nested Lits:
# List within a list

vegetables = ["cabbage", "aloo", "okra", "onion"]

basket = [fruits, vegetables]  ## This is a netsed List
print(basket)
print(basket[0])  ### See the Differnace in output
print(basket[1][1])  ### [List][item]