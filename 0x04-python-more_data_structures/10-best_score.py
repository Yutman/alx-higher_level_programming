#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return (None)
    if isinstance(a_dictionary, dict):
        my_list = []
        for i in a_dictionary:
            my_list.append(a_dictionary[i])
        if len(my_list) == 0:
            return (None)
        max_value = my_list[0]

        for j in my_list[1:]:
            if j > max_value:
                max_value = j

        for k in a_dictionary:
            if a_dictionary[k] == max_value:
                return (k)
    return (None)
