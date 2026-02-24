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

# 1.1) Is Unique.
from collections import defaultdict


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


# 1.2) Check permutation.

def is_permutation_v1(s1, s2):
    '''
    Check if s1 and s2 strings are permutations with other.

        Time complexity: O(N*log(N) + N*log(N)) = O(2N*log(N)) ~= O(N*log(N)), where N is the size
                         of len(s1) or len(s2), because if the size is different the function returns.
        Space complexity: O(1) no extra space is necessary

    :param s1:
    :param s2:
    :return:
    '''
    if len(s1) != len(s2):
        return False
    return True if sorted(s1) == sorted(s2) else False


def is_permutation_v2(s1, s2, set_size=128):
    '''Check if s1 and s2 strings are permutations with other.

        Time complexity: O(N), where N is the size of string
        Space complexity: O(K), where K is the size of char set

    :param s1:
    :param s2:
    :param set_size:
    :return:
    '''
    if len(s1) != len(s2):
        return False
    occurrences = [0] * set_size
    for c in s1:
        occurrences[ord(c)] += 1
    for c in s2:
        occurrences[ord(c)] -= 1
        if occurrences[ord(c)] < 0:
            return False
    return True if not any(occurrences) else False


def is_permutation_v3(s1, s2):
    '''Check if s1 and s2 strings are permutations with other.

        Time complexity: O(N), where N is the size of string
        Space complexity: O(K), where K is the size of char set

    :param s1:
    :param s2:
    :return:
    '''
    if len(s1) != len(s2):
        return False
    occurrences = defaultdict()
    for c in s1:
        if c not in occurrences:
            occurrences[c] = 0
        occurrences[c] += 1
    for c in s2:
        if c not in occurrences:
            occurrences[c] = 0
        occurrences[c] -= 1
        if occurrences[c] < 0:
            return False
    return True if not any(occurrences.values()) else False


def test_is_permutation_v1():
    assert is_permutation_v1('abc', 'cba') == True
    assert is_permutation_v1('abb', 'abc') == False
    assert is_permutation_v1('abcd', 'a') == False

def test_is_permutation_v2():
    assert is_permutation_v2('abc', 'cba') == True
    assert is_permutation_v2('abb', 'abc') == False
    assert is_permutation_v2('abcd', 'a') == False

def test_is_permutation_v3():
    assert is_permutation_v3('abc', 'cba') == True
    assert is_permutation_v3('abb', 'abc') == False
    assert is_permutation_v3('abcd', 'a') == False

# 1.3) URLify.

def urlfy(s):
    return s.replace(' ', '%20')

def test_urlfy():
    assert urlfy("Mr John Smith") == "Mr%20John%20Smith"


# 1.4) Palindrome Permutation.

def has_palindrome_permutation(s):
    count_valid_chars = 0
    save_chars = set()
    s = s.lower().replace(' ', '')
    for c in s:
        if c in save_chars:
            save_chars.remove(c)
        else:
            save_chars.add(c)
        count_valid_chars += 1
    if count_valid_chars % 2 == 0:
        return len(save_chars) == 0
    else:
        return len(save_chars) == 1


def test_palindrome_permutation():
    assert has_palindrome_permutation("Tact Coa") == True
    assert has_palindrome_permutation("aabbccxy") == False

# 1.5) One Away.
# 1.6) String Compression.
# 1.7) Rotate Matrix.
# 1.8) Zero Matrix.
# 1.9) String Rotation.
