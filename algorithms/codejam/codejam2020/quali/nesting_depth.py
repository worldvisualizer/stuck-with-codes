"""
problem:
- given S, make S' s.t.

221 -> ((22)1)
312 -> (((3))1(2))

intuition:
- decision to put parens or not at each slot (recursive)
    - stack for each number to check if solution is correct
- dividing the numberscape into sum-patterns

- strategy to make tree-like order for each number

3 - 1
  - 2
"""

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
