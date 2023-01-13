#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_list_cpy = []
    sum = 0

    for i in my_list:
        if i not in my_list_cpy:
            my_list_cpy.append(i)

    for j in my_list_cpy:
        sum += j
    return (sum)
