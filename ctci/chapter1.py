'''Chapter 1 - Arrays and Strings

    Questions:

    1.1) Is Unique.
    1.2) Check permutation.
    1.3) URLify.
    1.4) Palindrome Permutation.
    1.5) One Away.
    1.6) String Compression.
    1.7) Rotate Matrix.
    1.8) Zero Matrix.
    1.9) String Rotation.

'''

#1.1

def all_unique_v1(string):
    '''Check if all char are unique using a set data structure to store every char
        Time complexity = O(n) where n is the size of :string:
        Space complexity = O(n) where n is the size of :string: or the size of char set.
    '''
    existent = set()
    for c in string:
        if c in existent:
            return False
        existent.add(c)
    return True

def all_unique_v2(string, set_size=128):
    '''Check if all char are unique using an auxiliary array.

        Time complexity = O(n) where n is the size of :string:
        Space complexity = O(k) where k is the size of :set_size:

    :param string: String to check if all characters are unique
    :param set_size: Size of the set characters, by default is 128 (ASCII chars)
    :return: True if all chars are unique in the :string:
    '''
    char_set = [False] * set_size
    for c in string:
        if char_set[ord(c)]:
            return False
        char_set[ord(c)] = True
    return True

def all_unique_v3(string):
    '''Naive implementation

        Time complexity = O(n*n) where n is the size of :string:
        Space complexity = O(1), no extra space is necessary

    '''
    for i1,c1 in enumerate(string):
        for i2,c2 in enumerate(string):
            if i1 == i2:
                continue
            if c1 == c2:
                return False
    return True

def test_all_unique_v1():
    assert all_unique_v1('abcdefghijkLMn') == True
    assert all_unique_v1('aa') == False
    assert all_unique_v1('a1a') == False
    assert all_unique_v1('39tehnetn39(83oenoens0)(*()h') == False
    assert all_unique_v1('1234567890!@#$%^&*()qdrwbjfup;[]\ashtgyneoi') == True

def test_all_unique_v2():
    assert all_unique_v2('abcdefghijkLMn') == True
    assert all_unique_v2('aa') == False
    assert all_unique_v2('a1a') == False
    assert all_unique_v2('39tehnetn39(83oenoens0)(*()h') == False
    assert all_unique_v2('1234567890!@#$%^&*()qdrwbjfup;[]\ashtgyneoi') == True

def test_all_unique_v3():
    assert all_unique_v3('abcdefghijkLMn') == True
    assert all_unique_v3('aa') == False
    assert all_unique_v3('a1a') == False
    assert all_unique_v3('39tehnetn39(83oenoens0)(*()h') == False
    assert all_unique_v3('1234567890!@#$%^&*()qdrwbjfup;[]\ashtgyneoi') == True


#1.2