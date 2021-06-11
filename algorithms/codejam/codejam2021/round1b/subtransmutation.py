"""
"""
def compare(sol, metals):
    ls = len(sol)
    um = len(metals)
    if ls < um:
        return False
    for i in range(1, len(metals)):
        if sol[i] < metals[i]:
            return False
    return True

def transmute(elem, a, b):
    smallers = []
    sa = elem - a
    sb = elem - b
    if sa > 0:
        smallers.append(sa)
    if sb > 0:
        smallers.append(sb)
    return smallers

def branch_down(metal_list, a, b, um):
    if compare(metal_list, um):
        return True
    for i, elem in enumerate(metal_list[::-1]):
        copy_metals = metal_list[:i] + metal_list[i+1:]
        smallers = transmute(elem, a, b)
        for item in smallers:
            copy_metals[item] += 1
            print(copy_metals)
            if branch_down(copy_metals, a, b, um):
                return True
    return False


def transmute_naive(a, b, units_of_metals):
    for i in range(len(units_of_metals) + 1, 21):
        root_list = [0 for j in range(len(units_of_metals))]
        root_list += [1]
        if branch_down(root_list, a, b, units_of_metals):
            return i
    return "IMPOSSIBLE"


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
    available_spells = readints(f, sep=' ')
    n, a, b = available_spells
    assert 3 == len(available_spells)
    units_of_metals = readints(f, sep=' ')
    assert n == len(units_of_metals)
    return (n, a, b, units_of_metals)

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
    n, a, b, units_of_metals = c
    units_of_metals = [0] + units_of_metals
    return transmute_naive(a, b, units_of_metals)

def main():
    inp = InputReader(readcase)
    for i, c in enumerate(inp, start=1):
        print('Case #{}: {}'.format(i, solve(c)))

main()
