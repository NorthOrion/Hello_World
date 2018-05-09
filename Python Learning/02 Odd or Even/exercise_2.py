# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

# Extras:

# If the number is a multiple of 4, print out a different message.
# Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

print("Hello, please submit an integer :")
try:
    num = int(input())
    if num % 2:
        print("%d is an odd number" % num)
    else:
        # Extra 1
        if num % 4:
            print("%d is a pair number" % num)
        else:
            print("%d is a multiple of 4" % num)
except ValueError :
    print("Invalid input : Program will terminate")
