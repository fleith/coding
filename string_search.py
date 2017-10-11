'''String search algorithms'''

_naive_iterations = 0

def naive_search(string, pattern):
    '''Naïve string search algorithm

        Pseudo code:
            string[1..n] and pattern[1..m]
            for i from 1 to n-m+1
                for j from 1 to m
                    if s[i+j-1] ≠ pattern[j]
                        jump to next iteration of outer loop
                return i
            return not found

        :param string: string
        :param pattern:  pattern to search
        :return: position in the string where the pattern start or None

        :reference: https://en.wikipedia.org/wiki/Rabin–Karp_algorithm
    '''
    for i in range(0, len(string) - len(pattern) + 1):
        global _naive_iterations
        _naive_iterations += 1
        def search():
            for j in range(0, len(pattern)):
                global _naive_iterations
                _naive_iterations += 1
                if string[i+j] != pattern[j]:
                    return None
            return i
        value = search()
        if value != None:
            return value
    return None


def test_naive_search():
    '''Naïve string search algorithm test using Py.Test'''
    global _naive_iterations
    _naive_iterations = 0
    assert naive_search("abc", "wowxyzabcnice") == None
    print(_naive_iterations)
    _naive_iterations = 0
    assert naive_search("abc", "wowxyzacbnice") == None
    print(_naive_iterations)
    _naive_iterations = 0
    assert naive_search("wowxyzabcnice", "abc") == 6
    print(_naive_iterations)
    _naive_iterations = 0
    assert naive_search("wowxyzacbnice", "abc") == None
    print(_naive_iterations)
    _naive_iterations = 0
    assert naive_search("wowxyzniceabc", "abc") == 10
    print(_naive_iterations)
    _naive_iterations = 0
    assert naive_search("abcwowxyznice", "abc") == 0
    print(_naive_iterations)
    _naive_iterations = 0
    assert naive_search("abc", "abc") == 0
    print(_naive_iterations)
    _naive_iterations = 0
    assert naive_search("abc", "") == 0
    print(_naive_iterations)
    _naive_iterations = 0
    assert naive_search("", "") == 0
    print(_naive_iterations)
    _naive_iterations = 0


def rabin_karp(string, pattern):
    '''Rabin–Karp string search algorithm

        Pseudo Code:
            function RabinKarp(string s[1..n], string pattern[1..m])
                hpattern := hash(pattern[1..m]);
                for i from 1 to n-m+1
                    hs := hash(s[i..i+m-1])
                    if hs = hpattern
                        if s[i..i+m-1] = pattern[1..m]
                            return i
                return not found
    '''
    hash_pattern = hash(pattern)
    for i in range(0, len(string) - len(pattern) + 1):
        global _rabin_iterations
        _rabin_iterations += 1
        hash_string = hash(string[i:i+len(pattern)])
        if hash_string == hash_pattern:
            if string[i:i+len(pattern)] == pattern[:len(pattern)]:
                return i

    return None

_rabin_iterations = 0

def test_rabin_karp():
    '''Naïve string search algorithm test using Py.Test'''
    print("-------------")
    global _rabin_iterations
    assert rabin_karp("abc", "wowxyzabcnice") == None
    print(_rabin_iterations)
    _rabin_iterations = 0
    assert rabin_karp("abc", "wowxyzacbnice") == None
    print(_rabin_iterations)
    _rabin_iterations = 0
    assert rabin_karp("wowxyzabcnice", "abc") == 6
    print(_rabin_iterations)
    _rabin_iterations = 0
    assert rabin_karp("wowxyzacbnice", "abc") == None
    print(_rabin_iterations)
    _rabin_iterations = 0
    assert rabin_karp("wowxyzniceabc", "abc") == 10
    print(_rabin_iterations)
    _rabin_iterations = 0
    assert rabin_karp("abcwowxyznice", "abc") == 0
    print(_rabin_iterations)
    _rabin_iterations = 0
    assert rabin_karp("abc", "abc") == 0
    print(_rabin_iterations)
    _rabin_iterations = 0
    assert rabin_karp("abc", "") == 0
    print(_rabin_iterations)
    _rabin_iterations = 0
    assert rabin_karp("", "") == 0
    print(_rabin_iterations)
    _rabin_iterations = 0


