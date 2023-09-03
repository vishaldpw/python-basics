print("Welcome to treasure island, Your Mission is to find the treasue")
dir = input("left or right: Choose one ")
if dir == "left":
    a1 = input("swim or wait: Choose one ")
    if a1 == "wait":
          door =input("which door red, yellow or blue: Choose one ")
          if door == "yellow":
                 print(" you won ")
          else:
                  print(" game over ")
    else:
           print(" game over ")                
else:
    print(" game over ")
