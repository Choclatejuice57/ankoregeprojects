# Adds an input command so you can enter your age
age = int(input("Enter Age"))

# This line determines whether it is even or odd by dividing the age by 2 and. If the reminder.
#If the reminder is 0, it's even. If it's 1, it's odd.
# Start is the 1st number you want to print.
if (age % 2) == 0:
    start = 0
else:
    start = 1

# The magic happens here, a while loop repeats the print command.
# The way it does it is by printing start and adding 2 every time till it hits the age.
# Or it becomes just greater than age.
while start <= age:
    print(start)
    start = start + 2
