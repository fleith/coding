'''Find single element in a list using the XOR method,
    the result will be the single element.
'''

def find_single(elements):
    single = 0
    for element in elements:
        single = single ^ element
    return single

def test_single_element():
    assert find_single([1,3,1,7,9,3,9]) == 7
    assert find_single([1,3,1,7,9,3,9,8,8]) == 7
    assert find_single([1,1,1,1,1,1]) == 0
    assert find_single([1,1,1,1,1,1,1]) == 1
    assert find_single([1,2,3,4,5,6,7,8,9,10,1,2,3,5,6,7,8,9,10]) == 4