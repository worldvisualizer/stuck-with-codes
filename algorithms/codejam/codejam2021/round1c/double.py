import sys
import collections
import collections.abc

def not_ops(numstr):
    ret = ''
    for e in numstr:
        ee = '0' if e == '1' else '1'
        ret += ee
    
    return ret.lstrip('0')

def double_ops(numstr):
    numstr += '0'
    return numstr

def double_or_noting(num1, num2):
    ret = double_or_noting_helper(str(num1), str(num2))
    if ret == -1:
        return 'IMPOSSIBLE'
    return ret

def double_or_noting_helper(num1, num2):
    thelist = [(num1, 0)]
    while thelist:
        numstr, step = thelist.pop(0)
        if numstr == num2:
            return step
        if step > 10:
            return -1
        thelist.append((double_ops(numstr), step +1))
        thelist.append((not_ops(numstr), step + 1))
    

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
    n, k = readints(f, sep=' ')
    return (n, k)

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
    n1, n2 = c
    return double_or_noting(n1, n2)

def main():
    inp = InputReader(readcase)
    for i, c in enumerate(inp, start=1):
        print('Case #{}: {}'.format(i, solve(c)))

main()
