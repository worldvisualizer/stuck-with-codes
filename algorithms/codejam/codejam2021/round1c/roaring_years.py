import sys
import collections
import collections.abc

def initial_year_list(curr):
    retlist = []
    yearlen = len(str(curr))
    for i in range(0, 10):
        times = 2
        while (i+1) * times <= 18:
            init_int = 10 ** i
            init_list = [init_int + ind for ind in range(0, times)]
            # if curr > int(''.join([str(e) for e in init_list])):
            retlist.append(init_list)
            times += 1
    return retlist

def get_next_elem(elem):
    last_num = elem[-1]
    elem.pop(0)
    elem.append(last_num + 1)
    return elem

def wrapper_generator(elem, curr):
    year = int(''.join([str(e) for e in elem]))
    while year <= curr:
        elem = get_next_elem(elem)
        year = int(''.join([str(e) for e in elem]))
    yield int(''.join([str(e) for e in elem]))

def roaring_years(curr):
    ll = [wrapper_generator(e, curr) for e in initial_year_list(curr)]
    retlist = []
    for fun in ll:
        for item in fun:
            retlist.append(item)
    retlist.sort()
    return retlist[0]

def readint(f):
    return int(readline(f))

def readline(f):
    return next(f).strip()

def readcase(f):
    return readint(f)

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
    return roaring_years(c)

def main():
    inp = InputReader(readcase)
    for i, c in enumerate(inp, start=1):
        print('Case #{}: {}'.format(i, solve(c)))

main()
