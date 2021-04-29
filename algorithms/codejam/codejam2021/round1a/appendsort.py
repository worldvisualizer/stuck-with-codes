"""
list of integers x1, ..., xn.
want strictly increasing order, but we cannot reorder them.
only way is to append the number to the right.

naive:
- keep context of number of digits
"""
def digit_list(num):
    return [int(i) for i in list(str(num))]

def list_to_num(num_list):
    return int(''.join([str(i) for i in num_list]))

"""
def get_min_larger(prev, now):
    num_append = 0
    prev_list, now_list = digit_list(prev), digit_list(now)
    max_len = max(len(prev_list), len(now_list))
    i = 0
    while i < max_len:
        if i < len(prev_list):
            if prev_list[i]
    now = int(''.join([str(i) for i in now_list]))
    return (now, num_append)
"""
def get_min_larger(prev, now):
    num_append = 0
    prev_list, now_list = digit_list(prev), digit_list(now)
    while len(prev_list) > len(now_list):
        now_list.append(0)
        num_append += 0

    prev = list_to_num(prev_list)

    while prev >= list_to_num(now_list):
        index = -1
        for i in range(10):
            now_list[i] = pre
            if 
        now = now * 10 + 

def appendsort(arr):
    total_ops = 0
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            num, ops = get_min_larger(arr[i-1], arr[i])
            arr[i] = num
            total_ops += ops
    return total_ops

import sys
import collections
import collections.abc

def readint(f):
    return int(readline(f))

def readints(f, expected=None, sep=None):
    line = readline(f)
    xs = [int(e) for e in line.split(sep)]
    if expected is not None:
        assert len(xs) == expected, '{} != {}'.format(len(xs), expected)
    return xs

def readline(f):
    return next(f).strip()

def readcase(f):
    len_ints = readint(f)
    input_list = readints(f, sep=' ')
    assert len_ints == len(input_list)
    return input_list

class InputReader(collections.abc.Iterable):
    _cases = None

    def __init__(self, reader, inp=None):
        self._read(reader, inp or sys.stdin)

    def _read(self, reader, inp):
        t = int(next(inp))
        self._cases = [reader(inp) for _ in range(t)]
        assert len(self._cases) == t

    def __iter__(self):
        return iter(self._cases)

def reversort_cost(L):
    return reversort_cost_naive(L)

def solve(c):
    return reversort_cost(c)

def main():
    inp = InputReader(readcase)
    for i, c in enumerate(inp, start=1):
        print('Case #{}: {}'.format(i, solve(c)))

main()
