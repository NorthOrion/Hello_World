#Take a list, say for example this one:
#  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#and write a program that prints out all the elements of the list that are less than 5.

#Extras:

#Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
#Write this in one line of Python.
#Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.

try:
    #Base + Extra 1 and 3
    in_list,out_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89], []
    print("input a number :")
    num = int(input())
    for element in in_list:
        if element < num:
            out_list.append(element)
    print(f"here is the list of elements that are less that {num} : {out_list}")

    #Extra 2
    #print([element for element in in_list if element < 5] )
except ValueError:
    print("Invalid input : program will terminate !")
