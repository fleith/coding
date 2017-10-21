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

import dictionary

first = 'HEAD'
last = 'TAIL'

def is_valid(word):
    dict = dictionary.Dictionary()
    return dict.isInDictionary(word)


def doublets(w1, w2):
    if len(w1) != len(w2):
        return None
    words = []
    for i, c in enumerate(w1):
        if ord(c) > ord(w2[i]):
            word = w1[i:i + 1] + w2[i] + w1[i + 1:]
            if is_valid(word):
              words.append(word)
            continue
        while(c != w2[i]):
            word = w1[0:i] + c + w1[i+1:]
            if is_valid(word):
                words.append(word)
            c = chr(ord(c) + 1)




print(doublets(first,last))
