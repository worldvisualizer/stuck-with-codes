#!/usr/bin/env python3
import os
import time
from pathos.multiprocessing import ProcessingPool
from multiprocess import Pool

def multiply(x):
    print('in multiply. calculating {}...'.format(x))
    time.sleep(5)
    return x ** 3

def do_something(dd):
    print('in do something. calculating {}...'.format(dd))
    time.sleep(1)
    return dd + dd

def ready(async_obj):
    while not async_obj.ready():
        time.sleep(1)
        print(".", end=' ')

def run_amap():
    with ProcessingPool(processes=4) as pool:
        results = []
        for i in range(10):
            result = pool.amap(multiply, (i,))
            results.append(result)
        for res in results:
            if ready(res):
                res = res.get()
                another = pool.amap(do_something, (res, ))
                if ready(another):
                    y = another.get()
                    print(y)


def run_imap():
    with ProcessingPool(processes=4) as pool:
        results = []
        for i in range(10):
            result = pool.imap(multiply, (i,))
            results.append(result)
        for res in results:
            res = list(res)[0]
            another = pool.imap(do_something, (res, ))
            try:
                y = list(another)[0]
                print(y)
            except Exception as e:
                print(str(e))

def run_apipe():
    with ProcessingPool(processes=10) as pool:
        results = []
        for i in range(5):
            result = pool.apipe(multiply, i)
            results.append(result)
        for res in results:
            try:
                res = res.get(timeout = 3)
                another = pool.apipe(do_something, res)
                y = another.get()
                print(y)
            except Exception as e:
                import pdb; pdb.set_trace()
                print(str(e))
            

def multiprocess_pool():
    with Pool(processes=4) as pool:
        results = []
        for i in range(10):
            result = pool.apply_async(multiply, (i,))
            results.append(result)
        for res in results:
            try:
                res = res.get(timeout = 3)
                another = pool.apply_async(do_something, (res,))
                y = another.get()
                print(y)
            except Exception as e:
                print(str(e))
    

multiprocess_pool()
