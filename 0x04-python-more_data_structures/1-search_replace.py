#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_1 = []
    for x in my_list:
        if x == search:
            new_1.append(replace)
        else:
            new_1.append(x)
    return new_1
