# Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.
# Extras:
# Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
# Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)

# Initiating variables and reauesting user input
import datetime

print("Hello user, what's your name ?")
name = input()
print("That great, %s ! How old are you ?" % name)
age = int(input())

# Calculating the response
if age < 100:  # if less than 100 yrs old, print the year the user will turn 100
    print("Alright ! You will turn a 100 years old in %d" %
          (datetime.datetime.now().year - age + 100))
else:  # if 100 years old or older, no calculation necessary
    print("I see you are already over 100 years old")

# Extras 1 and 2:
print("Give me a number")
iterations = int(input())
for i in range(iterations):
    print("Alright ! You will turn a 100 years old in %d" %
          (datetime.datetime.now().year - age + 100))
