#  Name of variable should be one Unit
#  user_name = vishal is OK  
#  user name = vishal not OK
# length1 = len() is OK
# 1length = len() is not OK   {No number at start of variable}
# name of inbuild function should not be used as variables ex: print, len


print("Welcome to Band Name genrator\n")
name = input("whats your pet name: \n")
city = input("which city you did schooling: \n")
print("Band name can be " + city + " ka " + name)
