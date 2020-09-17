STRINGDIGIT = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

def stringToDigit(numberString):
    """
    decode string to digit

    numberString: (str) string representation of a digit

    returns: (int) digit
    """
    return STRINGDIGIT.get(numberString, None)

def tokenizeString(strParam):
    """
    tokenize a series of string
    assumes the strParm can be tokenized into a list of
    length 2n + 1 where n >= 0

    strParam: (str) number/plus/minus

    returns: (list) list of numbers, plus, minus
    """
    number, expression = "", []
    while len(strParam) > 0:
        for i in range(3,6):
            digit = stringToDigit(strParam[:i])
            if digit:
                number += digit
                strParam = strParam[i:]
                break
        if strParam[:5] == "minus":
            expression.append(number)
            expression.append("-")
            strParam = strParam[5:]
            number = ""
        if strParam[:4] == "plus":
            expression.append(number)
            expression.append("+")
            strParam = strParam[4:]
            number = ""
    expression.append(number)
    return expression

print(tokenizeString("foursixminustwotwoplusonezero"))
print(tokenizeString("onezeropluseight"))
print(tokenizeString("oneminusoneone"))
print(tokenizeString("foursixfoursixfoursix"))
