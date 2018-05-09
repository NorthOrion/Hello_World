# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

# Extras:

# If the number is a multiple of 4, print out a different message.
# Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

try:
    print("Hello, please submit an integer to check :")
    num = int(input())
    print("please submit an integer to divide by")
    check = int(input())
    if num % check:
        print("%d does not divide odd %d" % (check, num))
    else:
        print("%d divides odd %d" % (check, num))
except ValueError:
    print("Invalid input : Program will terminate")
