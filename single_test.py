#!/usr/bin/env python3

def find_single(elements):
    single = 0
    for element in elements:
        single = single ^ element
    return single

print(find_single([1,3,1,7,9,3,9]))
print(find_single([1,3,1,7,9,3,9,8,8]))
