#!/usr/bin/python3
def element_at(my_list, idx):
    size = len(my_list)

    if idx < 0:
        return (None)
    elif idx > (size - 1):
        return (None)
    else:
        for i in range(idx + 1):
            i
        return (my_list[i])
