# Create a program that asks the user for a number and then prints out a list of all the divisors of that number. (If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)


def integer_range(a, b):  # generator for getting all integers in [a,b]
    a = 1
    while a <= b:
        yield a
        a = a + 1


def get_divisors(n):  # returns the list of divisors, positive and negative
    div_list = []
    if n < 0:
        n = -1 * n
    for div in integer_range(1, n):
        if not n % div:
            div_list.append(div)
            div_list.append(-1 * div)
    return div_list


try:
    print("input a number :")
    number = int(input())
    divisors = get_divisors(number)
    print(f"here is the list of divisors for {number} : {divisors}")

except ValueError:
    print("Invalid input : program will terminate !")
