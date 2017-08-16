#!/bin/env python

import sys

reverse_string_list = []
def is_palindrome(string):
    string_list = list(string)
    for i in range(len(string)):
        if i == 0:
            reverse_string_list.append(string_list[-1])
        else:
            reverse_string_list.append(string_list[-1 * i * - 1])
    reverse_string = "".join(reverse_string_list)
    if string == reverse_string:
        return True
    else: return False

print(is_palindrome(sys.argv[1]))
