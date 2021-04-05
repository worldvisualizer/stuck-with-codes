import math
import random

def sigmoid(x):
    return 1.0 / (1 + math.exp(-x)) 

def prob_correct(s_i, q_j):
    x = s_i - q_j
    return sigmoid(x)

def prob_solve(cheater):
    f = random.uniform
    s_d = f(-3.0, 3.0)
    
    total = 0
    for _ in range(10000):
        q_i = f(-3.0, 3.0)
        if cheater:
            if random.uniform(0, 1.0) < 0.5:
                total += 1
                continue
        total += prob_correct(s_d, q_i)
    return total / 10000


def prob_solve_sampled(tries=100, cheater=False):
    print(sum([prob_solve(cheater) for _ in range(tries)]) / float(tries))

prob_solve_sampled(tries=100, cheater=False)
prob_solve_sampled(tries=100, cheater=True)
prob_solve_sampled(tries=1000, cheater=False)
prob_solve_sampled(tries=1000, cheater=True)
