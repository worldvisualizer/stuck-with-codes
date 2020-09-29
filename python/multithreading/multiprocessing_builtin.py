#!/usr/bin/env python3
import os
import time
from multiprocessing import Pool, TimeoutError

def multiply(x):
    print('in multiply. calculating {}...'.format(x))
    time.sleep(float(x) + 3)
    return x ** 3

def do_something(dd):
    print('in do something. calculating {}...'.format(dd))
    return dd + dd

def save_result(y):
    time.sleep(1)
    return

if __name__ == '__main__':
    with Pool(processes=4) as pool:
        results = []
        for i in range(10):
            result = pool.apply_async(multiply, (i,))
            results.append(result)
        for res in results:
            another = pool.apply_async(do_something, (res.get(), ))
            try:
                y = another.get()
                print(y)
            except Exception as e:
                print(str(e))
