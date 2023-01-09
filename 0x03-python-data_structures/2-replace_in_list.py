#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    size = len(my_list)
    if idx < 0:
       return (my_list)
    elif idx > (size - 1):
        return (my_list)
    else:
        for i in range(idx + 1):
            i
        my_list[i] = element
        return (my_list)
