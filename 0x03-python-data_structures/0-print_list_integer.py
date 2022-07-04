#!/usr/bin/python3


def print_list_integer(my_list=[]):
    """ prints integer of a list """
    for i in range(len(my_list)):
        print("{:d}".format(my_list[i]))
