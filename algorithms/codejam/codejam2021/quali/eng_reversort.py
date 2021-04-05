"""
problem:
L = [4,2,1,3]:
i = 1, j = 3, L = [1,2,4,3] -> cost 3
i = 2, j = 2, L = [1,2,4,3] -> cost 1
i = 3, j = 4, L = [1,2,3,4] -> cost 2
- total cost: 3, 1, 2 = 6

- come up with a list that can achieve cost C

def min_val_position(L, i):
    # minimum value in L between L and len(L)

def reverse(sublist):
    # reverses the order of some contiguous part of the list

def reversort(L):
    for i in range(1, len(L):
        j = min_val_position(L, i)
        reverse(L[i:j+1])
"""
import itertools

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
    return total_cost

def eng_reversort(length, cost):
    if length - 1 > cost:
        return "IMPOSSIBLE"
    cands = list(itertools.permutations([i for i in range(1, length + 1)]))
    cands = [list(t) for t in cands]
    for candidate in cands:
        ref = candidate[:]
        if reversort_cost_naive(candidate) == cost:
            return ' '.join([str(e) for e in ref])
    return "IMPOSSIBLE"

import sys
import collections
import collections.abc

def readcase(f):
    l, c = next(f).strip().split(' ')
    return (int(l), int(c))

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

def solve(c):
    length, cost = c
    return eng_reversort(length, cost)

def main():
    inp = InputReader(readcase)
    for i, c in enumerate(inp, start=1):
        print('Case #{}: {}'.format(i, solve(c)))

main()


