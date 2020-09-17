def compute(expression):
    def computeSide(firstnum, side, secondnum):
        if side == '-':
            return int(firstnum) - int(secondnum)
        if side == '+':
            return int(firstnum) + int(secondnum)
    """
    computes a list of arithmetic expression,
    e.g.) ["46", "-", "22", "+", "10"]
    and returns an integer

    assumes the strParm can be tokenized into a list of
    length 2n + 1 where n >= 0

    expression: (list) list of strings

    returns: (int) result
    """
    if len(expression) == 1:
        return expression[0]
    result = computeSide(expression[0], expression[1], expression[2])

    for side, other in list(zip(expression[3::2], expression[4::2])):
        result = computeSide(result, side, other)
    return result


print(compute(["46", "-", "22", "+", "10"]))
print(compute(["44"]))
