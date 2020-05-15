"""
Effective Python, so these books are all inspired
by Effective C++. Impressive.

Pythonic Way of thinking is one clear way to do it.
"""

# Metaclasses and Attributes - Interesting Stuff

"""
Metaclasses let you intercept Python's class statement
and provide special behavior each time a class is defined

There's also dynamically customizing attribute access
enables you to override objects and cause side effects

Follow RULE OF LEAST SURPRISE
"""

# Item 44: Use Plain Attributes instead of Setter/Getter

class Resistor:
    def __init__(self, ohms):
        # convention, to make property setting possible
        self._ohms = ohms

    def get_ohms(self):
        return self._ohms

    def set_ohms(ohms):
        self._ohms = ohms

# quite bulky. attrs could be a solution
class Resistor2(Resistor):
    def __init__(self, ohms):
        super().__init__(ohms)
        self._voltage = 0

    @property
    def voltage(self):
        return self._voltage
    
    # this makes decoration on object attribute
    # possible, with custom methods to further 
    # validate input and take additional actions
    @voltage.setter
    def voltage(self, voltage):
        self._voltage = voltage
        self.current = self._voltage / self.ohms

    @ohms.setter
    def ohms(self, ohms):
        if hasattr(self, '_ohms'):
            raise AttributeError('Ohms immutable')
        self._ohms = ohms

# define new class interfaces using simple public attrs
# and avoid defining setter/getter

# also use @property to define behavior 

# Item 45: consider @property instead of refactoring
from datetime import datetime, timedelta

class Bucket:
    def __init__(self, period):
        self.period_delta = timedelta(seconds=period)
        self.reset_time = datetime.now()
        self.quota = 0

    def __repr__(self):
        return f'Bucket(quota={self.quota})'

    def fill(bucket, amount):
        now = datetime.now()
        if now - bucket.reset_time > bucket.period_delta:
            bucket.quota = 0
            bucket.reset_time = now
        bucket.quota += amount

    def deduct(bucket, amount):
        now = datetime.now()
        if now - bucket.reset_time > bucket.period_delta:
            return False
        if bucket.quota - amount < 0:
            return False
        bucket.quota -= amount
        return True

    @quota.setter
    def quota(self, amount):
        delta = self.max_quota - amount
        if amount == 0:
            self.quota_consumed = 0
            self.max_quota = 0
        elif delta < 0:
            assert self.quota_consumed == 0
            self.max_quota = amount
        else:
            assert self.max_quota >= self.quota_consumed
            self.quota_consumed += delta


# Item 46: Use Descriptors for reusable @property methods

# methods @property cannot be reused for mulitple attrs
class Homework:
    def __init__(self):
        self._grade = 0

    @property
    def grade(self):
        return self._grade
    
    @grade.setter
    def grade(self, value):
        if not 0<= value <= 100:
            raise ValueError
        self._grade = value

    @exam.setter
    def exam_grade(self, value):
        # ... same kind of validation goes
        # what if we just make a common method?
        # that could work. but there might be a better way
        # because we could be talking about different classes
    # ...

# solution: use descriptor.
# descriptor class can provide __get__ and __set__ methods
# lets you reuse same logic for multiple attributes 
# in a single class
class Grade:
    def __init__(self):
        self._value = 0

    def __get__(self, instance, instance_type):
        # ...
        return self._value 

    def __set__(self, instance, value):
        # ...
        if not (O <= value <= 100):
            raise ValueError
        self._value = value


class Exam:
    math_grade = Grade()
    writing_grade = Grade()
    # ...

# now, this is becoming as same as:
exam = Exam()
exam.writing_grade = 40
# ->>
Exam.__dict__['writing_grade'].__set__(exam, 40)

# this becomes as same as this:
exam.writing_grade
# ->>
Exam.__dict__['writing_grade'].__get__(exam, Exam)
# this has something to do with __getattribute__
# method of object

# this becomes problematic, because of global Grade
# for every Exam class

# need to keep track of each instance of the Exam class
# and its values

class Grade:
    def __init__(self):
        self._value = {}

    def __get__(self, instance, instance_type):
        if instance is None:
            return self
        return self._values.get(instance, 0)

    def __set__(self, instance, value):
        if not (0 <= value <= 100):
            raise ValueError
        self_values[instance] = value
        # this causes memory leak, where 
        # exam instance never running out of references
        # solution: use weakref built-in module

from weakref import WeakKeyDictionary

class Grade:
    def __init__(self):
        self._values = WeakKeyDictionary()

    def __get__(self, instance, instance_type):
        # ...

    def __set__(self, instance, value):
        # ....

# fuck yeah.












