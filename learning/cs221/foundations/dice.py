import random


def roll_the_dice(score):
    number = random.choice(range(1,7))
    if number == 1:
        return score
    elif number == 2:
        score -= 10
    elif number == 6:
        score += 100
    return roll_the_dice(score)


for i in range(10):
    print(roll_the_dice(0))
