"""
problem:
L = [4,2,1,3]:
i = 1, j = 3, L = [1,2,4,3] -> cost 3
i = 2, j = 2, L = [1,2,4,3] -> cost 1
i = 3, j = 4, L = [1,2,3,4] -> cost 2
- total cost: 3, 1, 2 = 6

- compute the cost of executing reversort

def min_val_position(L, i):
    # minimum value in L between L and len(L)

def reverse(sublist):
    # reverses the order of some contiguous part of the list

def reversort(L):
    for i in range(1, len(L):
        j = min_val_position(L, i)
        reverse(L[i:j+1])
"""
def find_min_position(i, L):
    # finds minimum position in L
    minval = max(L)
    minind = i
    for index in range(i, len(L)):
        if L[index] <= minval:
            minval = L[index]
            minind = index
    return minind

def reverse_list(L, i, j):
    # reverses order of the list
    while i <= j:
        temp = L[i]
        L[i] = L[j]
        L[j] = temp
        i += 1
        j -= 1

def reversort_cost_naive(L):
    total_cost = 0
    for i in range(len(L)-1):
        j = find_min_position(i, L)
        reverse_list(L, i, j)
        total_cost += max(j-i+1, 1)

        # printing cost
        # print(L)
        # print(max(j-i+1, 1))
    return total_cost

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
