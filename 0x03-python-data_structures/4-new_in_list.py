#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    size = len(my_list)
    new_list = my_list[:]

    if idx < 0:
        return (new_list)

    elif idx > (size - 1):
        return (new_list)

    else:
        for i in range(idx + 1):
            i

        new_list[i] = element
        return (new_list)
