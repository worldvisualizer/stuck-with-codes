import sys
import math
import random
import collections
import collections.abc

def find_cheater(solutions):
    for i, i_sol in enumerate(solutions):
        est_skill = estimate_skill(i_sol)
        
    return max_ind

def readints(ff, expected=None):
    line = next(ff).strip()
    xs = [int(e) for e in list(line)]
    if expected is not None:
        assert len(xs) == expected, f'{len(xs)} != {expected}'
    return xs

def readcase(f):
    return [readints(f, 10000) for _ in range(100)]

class InputReader(collections.abc.Iterable):
    _cases = None

    def __init__(self, reader, inp=None):
        self._read(reader, inp or sys.stdin)

    def _read(self, reader, inp):
        t = int(next(inp))
        p = int(next(inp))
        self._cases = [reader(inp) for _ in range(t)]
        assert len(self._cases) == t

    def __iter__(self):
        return iter(self._cases)

def solve(c):
    return find_cheater(c)

def main():
    inp = InputReader(readcase)
    for i, c in enumerate(inp, start=1):
        print('Case #{}: {}'.format(i, solve(c)))

main()
