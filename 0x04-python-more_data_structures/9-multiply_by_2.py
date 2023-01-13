#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    keys = list(a_dictionary.keys())
    a_dictionary_cpy = {i: a_dictionary[i] for i in keys}

    for i in a_dictionary_cpy:
        a_dictionary_cpy[i] = a_dictionary_cpy[i] * 2

    return (a_dictionary_cpy)
