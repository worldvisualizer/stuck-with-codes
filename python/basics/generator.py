"""
learn generator and its expression, yield
and how to incorporate it into async/await
"""

def fibonacci(n):
    a, b = 1, 1
    numbers = []
    for _ in range(n):
        numbers.append(a)
        a, b = b, a + b
    return numbers

# generator works with iterator interface,
# so when iterator calls __next__ 
# generator function invokes yield statement and suspend execution.
def fibonacci_generator(n):
    a, b = 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

class Fibonacci:
    def __init__(self, n):
        self.a = 1
        self.b = 1
        self.n = n
        self.i = 0

    def __next__(self):
        if self.i == 0:
            self.i += 1
            return self.a
        elif self.i < self.n:
            self.a, self.b = self.b, self.a + self.b
            self.i += 1
            return self.a
        else:
            raise StopIteration

    def __iter__(self):
        return self


def fibonacci_iterator(n):
    return Fibonacci(n)


def test_func(n):
    print("running plain iterative fibonacci function...")
    print([elem for elem in fibonacci(n)])
    
    print("running generator fibonacci function...")
    print([elem for elem in fibonacci_generator(n)])
    
    print("running custom iterator fibonacci function...")
    print([elem for elem in fibonacci_iterator(n)])


test_func(10)
test_func(100)
