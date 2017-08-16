#!/bin/env python

import sys

def shiritori(filename):
    words = []
    first_words = []
    last_words = []
    f = open(filename)
    for line in f:
        words.append(line)
        first_words.append(line[0])
        last_words.append(line[-2])
    f.close()

    for i in range(len(first_words)):
        x = first_words.count(first_words[i])
        
        counter = 0
        
        if :
            pass
        else: counter += 1

    if counter > 2: return NO!

    elif counter = 0:
        initial_vector = [first_words[0], last_words[0]]
        








    elif counter = 1:
        





print shiritori(sys.argv[1])
