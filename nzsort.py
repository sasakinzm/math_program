#!/bin/env python

import sys

def words_sort(words):
    if type(words) == str:
        temp_word = ""
        temp_words_list = list(words)
        for i in range(len(temp_words_list)):
            if ord(temp_words_list[i]) == 32: pass
            else:
                for j in range(i, len(temp_words_list)):
                    if ord(temp_words_list[j]) == 32: pass
                    else:
                        if ord(temp_words_list[i]) > ord(temp_words_list[j]):
                            temp_word = temp_words_list[i]
                            temp_words_list[i] = temp_words_list[j]
                            temp_words_list[j] = temp_word
        sorted_words = "".join(temp_words_list)
        return sorted_words

    elif type(words) == list:
        new_words_int = []
        new_words_str = []
        for i in range(len(words)):
            if type(words[i]) == int or type(words[i]) == float:
                new_words_int.append(words[i])
        for i in range(len(words)):
            if type(words[i]) == str:
                new_words_str.append(words[i])

        temp_int = ""
        for i in range(len(new_words_int)):
            for j in range(i, len(new_words_int)):
                if new_words_int[i] > new_words_int[j]:
                    temp_word = new_words_int[i]
                    new_words_int[i] = new_words_int[j]
                    new_words_int[j] = temp_word
        temp_str = ""
        for i in range(len(new_words_str)):
            for j in range(i, len(new_words_str)):
                if ord(new_words_str[i][0]) > ord(new_words_str[j][0]):
                    temp_word = new_words_str[i]
                    new_words_str[i] = new_words_str[j]
                    new_words_str[j] = temp_word
        return new_words_int + new_words_str

