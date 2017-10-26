'''
There is a common type of word puzzle(called word ladders or doublets) where
you are given two English words of the same length, say, "HEAD" and "TAIL".The
puzzle is to come up with a sequence of valid English words, starting
with "HEAD", and ending with "TAIL", such that each word is formed by changing a
single letter of the previous word.Create an algorithm to automatically solve such puzzles.

Example(altered letters capitalized):

HEAD
heaL
Teal
teLl
tAll
taIl

'''
from collections import OrderedDict

import dictionary

first = 'HEAD'
last = 'TAIL'

def is_valid(word):
    dict = dictionary.Dictionary()
    return dict.isInDictionary(word)

print(is_valid('heal'))

result = []

def doublets(w1, w2):
    if len(w1) != len(w2):
        return None
    # print("w1: ", w1, " w2: ", w2)
    if is_valid(w1):
        result.append(w1)
    # print(len(result))
    if w1 == w2:
        return result
    for i, c in enumerate(w1):
        if ord(c) < ord(w2[i]):
            doublets(w1[:i]+chr(ord(c)+1)+w1[i+1:], w2)
        elif ord(c) == ord(w2[i]):
            continue
        else:
            doublets(w1[:i] + w2[i] + w1[i + 1:], w2)

# print(doublets(first, last))