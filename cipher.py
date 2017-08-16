#!/bin/env python

import random
import sys

source_str_upper = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
source_str_lower = list("abcdefghijklmnopqrstuvwxyz")

shuffle_upper = source_str_upper[:]
random.shuffle(shuffle_upper)
shuffle_lower = source_str_lower[:]
random.shuffle(shuffle_lower)

def cipher(words):
    words_list = list(words)
    for i in range(len(words_list)):
        word = words_list[i]
        if word.isupper() == True:
            x = source_str_upper.index(word)
            words_list[i] = shuffle_upper[x]
        if word.islower() == True:
            x = source_str_lower.index(word)
            words_list[i] = shuffle_lower[x]

    return "".join(words_list)

if sys.argv[1] == "-l":
    print(cipher(sys.argv[2]))

elif sys.argv[1] == "-f":
    f = open(sys.argv[2])
    print(cipher(f.read()))

print("key = " + "'" + "".join(shuffle_lower) + "'" + " & " + "'" + "".join(shuffle_upper) + "'")

