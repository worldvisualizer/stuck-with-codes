
def increasing_substring(string):
    """
    candidates array
    maxlen array
    """
    maxlens, maxlen, curr = [1], 1, string[0]
    for i in range(1, len(string)):
        if curr[-1] < string[i]:
            curr += string[i]
            maxlen += 1
        else:
            maxlen = 1
            curr = string[i]
        maxlens.append(maxlen)
    return maxlens

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
    input_list = readline(f)
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

def solve(c):
    lengths = increasing_substring(c)
    return ' '.join([str(e) for e in lengths])

def main():
    inp = InputReader(readcase)
    for i, c in enumerate(inp, start=1):
        print('Case #{}: {}'.format(i, solve(c)))

main()
