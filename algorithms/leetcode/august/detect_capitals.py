
def isAllCapital(word: str) -> bool:
    for w in word:
        if w != w.capitalize():
            return False
    return True


def onlyFirstLetterCapital(word: str) -> bool:
    for i, w in enumerate(word):
        if i == 0 and w != w.capitalize():
            return False
        if i != 0 and w == w.capitalize():
            return False
    return True


def noneCapital(word: str) -> bool:
    for w in word:
        if w == w.capitalize():
            return False
    return True


def detectCapitalUse(word: str) -> bool:
    return isAllCapital(word) or onlyFirstLetterCapital(word) or noneCapital(word)


print(detectCapitalUse('USA'))
print(detectCapitalUse('FlaG'))
print(detectCapitalUse('Flag'))
print(detectCapitalUse('sdfsdfsdf'))
