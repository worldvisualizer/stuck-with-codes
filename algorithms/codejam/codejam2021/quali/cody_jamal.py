"""
problem:

CJ?CC? -> CJCCCC, CJCCCJ, CJJCCC, or CJJCCJ

- find ax + by that minimizes such cost
"""
def cost(x, y, cod_ja):
    # CJCCCJ -> x + y + x
    costs = {
        'CJ': x,
        'JC': y,
    }
    cost_map = collections.defaultdict(int, costs)
    total_cost = 0
    for i in range(len(cod_ja)-1):
        total_cost += cost_map[cod_ja[i:i+2]]
    return total_cost

"""
# past code
def cjh(x, y, cod_ja, index):
    if index == len(cod_ja) - 1:
        return cost(x, y, cod_ja)
    if cod_ja[index] == '?':
        cod_ja_c = cod_ja[:index] + 'C' + cod_ja[index+1:]
        cod_ja_j = cod_ja[:index] + 'J' + cod_ja[index+1:]
        return min(
            cjh(x, y, cod_ja_c, index+1),
            cjh(x, y, cod_ja_j, index+1)
        )
    else:
        return cjh(x, y, cod_ja, index+1)
"""

def cody_jamal_list(x, y, cod_ja, i, cod_ja_list):
    if i == len(cod_ja):
        return cod_ja_list
    for ch in cod_ja:
        templist = []
        for string in cod_ja_list:
            if ch == '?':
                if string == '':
                    templist.append(string + 'C')
                    templist.append(string + 'J')
                elif string[-1] == 'C':
                    templist.append(string + 'C')
                elif string[-1] == 'J':
                    templist.append(string + 'J')
            else:
                templist.append(string + ch)
        cod_ja_list = templist
    return cod_ja_list

def cody_jamal(x, y, cod_ja):
    results = cody_jamal_list(x, y, cod_ja, 0, [''])
    return min([cost(x, y, res) for res in results])


import sys
import collections
import collections.abc

def readcase(f):
    line = f.readline().strip().split(' ')
    x = int(line[0])
    y = int(line[1])
    assert len(line) == 3
    return (x,y,line[2])

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
    x, y, cod_ja = c
    return cody_jamal(x, y, cod_ja)

def main():
    inp = InputReader(readcase)
    for i, c in enumerate(inp, start=1):
        print('Case #{}: {}'.format(i, solve(c)))

main()
