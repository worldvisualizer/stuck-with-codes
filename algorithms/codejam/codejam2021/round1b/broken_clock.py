"""
"""
def broken_clock(t1, t2, t3):
    print(t1, t2, t3)
    if t3 % (720 * 1000) == 0:
        # seconds type of question
        print("seconds")
    else:
        print("nanoseconds")
    return [0, 0, 0, 0]

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
    input_list = readints(f, sep=' ')
    assert 3 == len(input_list)
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

def solve(c):
    t1, t2, t3 = c
    hour_numbers = broken_clock(t1, t2, t3)
    return ' '.join([str(e) for e in hour_numbers])

def main():
    inp = InputReader(readcase)
    for i, c in enumerate(inp, start=1):
        print('Case #{}: {}'.format(i, solve(c)))

main()
