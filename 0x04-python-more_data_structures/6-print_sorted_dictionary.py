#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keys = list(a_dictionary.keys())
    keys.sort()
    a_dictionary_sorted = {i: a_dictionary[i] for i in keys}

    for j in a_dictionary_sorted:
        print("{}: {}".format(j, a_dictionary_sorted[j]))
