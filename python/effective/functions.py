"""
Effective Python, so these books are all inspired
by Effective C++. Impressive.

Pythonic Way of thinking is one clear way to do it.
"""

# Functions - Interesting Stuff

# Item 20: Prefer Raising Exceptions to Returning None

# take advantage of try/except/else/finally
x, y = 2, 5
try:
    result = careful_divide(x, y)
except ValueError:
    raise
else:
    return result 

# Item 21: Know How Closures Interact with Variable Scope

def sort_priority(value, group):
    def helper(x):
        if x in group:
            return (0, x)
        return (1, x)
    values.sort(key=helper)
"""
    1) Python supports closures
    
    2) functions are first-class objects
    - you can refer to them directly, assign them to vars,
    - pass them as arguments to other functions,
    - compare them in expressions and if statements,
"""

# example about closure
def sort_priority2(numbers, group):
    found = False
    def helper(x):
        if x in group:
            found = True
            return (0, x)
        return (1, x)
    numbers.sort(key=helper)
    return found

# sort_priority2 -> found = False
"""
When you reference a variable in an expression,
Python interpreter traverses the scope in order:

    1) current function's scope
    2) enclosing scopes (other containing functions)
    3) scope of the module
    4) built-in scope

If nothing can be found from those 4, then
NameError exception is raised
"""

# this is the sucky part about the python
found = False # variable declaration
def inner_function():
    found = True # this is also variable declaration!
    # WTF python. 
    # variable reassignment using closure is impossible
    # and this is because there's no declaration expression.

# okay, I didn't know this: nonlocal
def sort_priority3(numbers, group):
    found = False
    def helper(x):
        nonlocal found # yessss
        if x in group:
            found = True
            return (0, x)
        return (1, x)
    numbers.sort(key=helper)
    return found

# Caution: nonlocal scope should be directly enclosing function
# as with global scope, you don't know what's gonna happen

# Helper class might be better
class Sorter:
    def __init__(self, group):
        self.group = group
        self.found = False

    def __call__(self, x):
        if x in self.group:
            self.found = True
            return (0, x)
        return (1, x)

numbers.sort(key=Sorter(group))

# Item 24: Use None and Docstrings to specify
# Dynamic Default Arguments

def decode(data, default={}):
    try:
        return json.loads(data)
    except ValueError:
        return default

foo = decode('bad_data')
foo['key1'] = 5
bar = decode('also bad')
bar['key2'] = 1
print(foo, bar)
# they both have {key1: 5, key2: 1}, fuck!
# both have references to default parameter.
# and because it's dynamic, it's mutable.

from datetime import datetime

def log(message, when=datetime.now()):
    print(f'{when}: {message}')

log('System error')
time.sleep(0.1)
log('System reboot')
# when is the same.
# understandable because code executes 
# when module loads. then never looked back.

# Item 26: Define Function Decorators with
# functools.wrap

# decorators: has ability to run additional code
# before and after each call to a function it wraps
# it means it can access args, retvals, exceptions

# are decorators proxies?
# https://stackoverflow.com/questions/18618779/differences-between-proxy-and-decorator-pattern

# what if I want to print the arguments and retvals
# of a function call?
def trace(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'{func.__name__} {args!r} {kwargs!r}')
        return result
    return wrapper

# 1) *args even when passing arguments into function?
# 2) !r ?!
# 3) decorator only has @ symbol? shit you are right
@trace
def fibonacci(n):
    """ Returns n-th Fibonacci number """
    if n in (0, 1):
        return n
    return (fibonacci(n-2) + fibonacci(n-1))

fibonacci = trace(fibonacci)
fibonacci(4)

print(fibonacci)
# <function trace.<locals>.wrapper at ...>

# problem is that this is really a wrapper function
# and original function cannot be located

# solution: use functools.wraps
from functools import wraps

def trace(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # ...
    return wrapper

@trace
def fibonacci(n):
    # ...
    pass



















































