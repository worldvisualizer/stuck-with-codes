STRINGDIGIT = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

DIGITSTRING = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
}


def stringToDigit(numberString):
    """
    decode string to digit

    numberString: (str) string representation of a digit

    returns: (int) digit
    """
    return STRINGDIGIT.get(numberString, 0)


def encodeNumberToString(wholeInt):
    """
    encode whole number into string
    consider negative number as well

    wholeInt: (int) whole number

    returns: (str) string representation of a wholeInt
    """
    if wholeInt == 0:
        return "zero"
    string = "" if abs(wholeInt) == wholeInt else "negative"
    wholeInt = abs(wholeInt)
    digitlist = []
    
    while wholeInt:
        digitlist.append(wholeInt % 10)
        wholeInt //= 10
    digitlist.reverse()
    string += "".join([DIGITSTRING.get(i, "") for i in digitlist])
    return string


def tokenizeString(strParam):
    """
    tokenize a series of string
    assumes the strParm can be tokenized into a list of
    length 2n + 1 where n >= 0

    strParam: (str) number/plus/minus

    returns: (list) list of numbers, plus, minus
    """


def compute(expression):
    """
    computes a list of arithmetic expression,
    e.g.) [46, "minus", 22, "plus", 10]
    and returns an integer

    assumes the strParm can be tokenized into a list of
    length 2n + 1 where n >= 0

    expression: (list) e.g. [46, "minus", 22, "plus", 10]

    returns: (int) result
    """
    if len(expression) == 1:
        return expression[0]
    result = 0
    firstnum, side, secondnum = expression[0], expression[1], expression[2]
    

def StringChallenge(strParam):
    """
    tokenizes string into a list of things,
    computes a list of arithmetic expressions,
    e.g.) [46, "minus", 22, "plus", 10]
    and returns string encoded integer
    without the use of eval() since it's always a source of attack

    strParam: (str) arithmetic expression in string

    returns: (int) result
    """
    expressionList = tokenizeString(strParam)
    resultInt = compute(expressionList)
    return encodeNumberToString(resultInt)


# keep this function call here 
