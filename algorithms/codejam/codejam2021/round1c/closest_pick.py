import sys
import collections
import collections.abc

def win_condition(luck, num1, num2, ps, k):
    min_abs = k
    for e in ps:
        v = abs(luck - e)
        if min_abs > v:
            min_abs = v
    my_luck = [abs(luck - num1), abs(luck - num2)]
    return my_luck[0] < min_abs or my_luck[1] < min_abs

def closest_pick(n, k, ps):
    max_prob = 0
    # x = lucky number
    for y in range(1, k+1):
        for z in range(y, k+1):
            is_win = 0
            for x in range(1, k+1):
                if win_condition(x, y, z, ps, k):
                    is_win += 1
            win_prob = is_win / float(k)
            if max_prob < win_prob:
                max_prob = win_prob
    return max_prob

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
    input_list = readints(f, sep=' ')
    assert n == len(input_list)
    return (n, k, input_list)

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
    n, k, ps = c
    return closest_pick(n, k, ps)

def main():
    inp = InputReader(readcase)
    for i, c in enumerate(inp, start=1):
        print('Case #{}: {}'.format(i, solve(c)))

main()
