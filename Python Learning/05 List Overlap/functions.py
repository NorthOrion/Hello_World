import random as rd

# random_int_list(size) :
# generate a random list of integers
# Parameters :
#       size (int) : size of the generated list. default value is 0 for random size list
# random size is between min_size and max_size
# elements generated are between min_element and max_element


def random_int_list(size=0):
    # initializing
    list, min_size, max_size, min_element, max_element, counter = [], 5, 50, 0, 20, 0
    # setting the size of the list
    if not size:
        size = rd.randint(min_size, max_size)
    # generating random elements and appending them to the list
    while counter < size:
        list.append(rd.randint(min_element, max_element))
        counter += 1
    # returning the list
    return list
# -----------------------------------------------------------------------------
# remove_duplicates(list) :
# remove duplicate elemets from a lists
# Parameters :
#       list (list): list of elements to be modified


def remove_duplicates(list):
    for element in list:
        while list.count(element) != 1:
            list.remove(element)
    return list
# ------------------------------------------------------------------------------
# get_common_elements(list_a, list_b)
# returns a list of common elements between two input lists
# Parameters :
#       list_a, list_b (list) : input lists


def get_common_elements(list_a, list_b):
    list_out = []
    for element_a in list_a:
        for element_b in list_b:
            if element_a == element_b:
                list_out.append(element_a)
                break
    return remove_duplicates(list_out)
# -----------------------------------------------------------------------------
