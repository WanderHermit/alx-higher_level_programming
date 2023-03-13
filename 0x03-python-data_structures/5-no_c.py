#!/usr/bin/python3
def no_c(my_string):
    newfun = my_string.translate({ord(t): None for t in 'cC'})
    return newfun
