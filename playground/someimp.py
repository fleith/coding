#!/usr/bin/env python3

import threading
from time import sleep

def mymap(func, elements):
    return [func(ele) for ele in elements]

assert mymap(lambda x: x*x, [1, 2, 3, 5]) == [1, 4, 9, 25]


def dbounce(func, wait):
    timeout = None
    def exec():
        nonlocal timeout
        if timeout:
            timeout.cancel()
        timeout = threading.Timer(wait, func)
        timeout.start()
    return exec

def log():
    print("log called")

f = dbounce(log, 5)
f()
f()
sleep(4)
f()
f()
sleep(8)
