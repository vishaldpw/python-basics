# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
# print(student_heights)
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
total_height = 0
for i in student_heights:
    total_height = total_height + i
print(total_height)

number = 0
for i in student_heights:
    number = number + 1
print(number)

average = total_height / number
av = int(average)
print(f"average Height of students is: {av}" )