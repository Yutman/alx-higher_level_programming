#!/usr/bin/python3
def search_replace(my_list, search, replace):
    my_list_cpy = my_list[:]
    for i in range(0, len(my_list_cpy)):
        if my_list_cpy[i] == search:
            my_list_cpy[i] = replace
    return (my_list_cpy)
