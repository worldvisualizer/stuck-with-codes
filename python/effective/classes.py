"""
Effective Python, so these books are all inspired
by Effective C++. Impressive.

Pythonic Way of thinking is one clear way to do it.
"""

# Classes and Interfaces - Back to Basics
"""
Classses in python provide:
- inheritance
- polymorphism
- encapsulation

express a program's intended behaviors with objects
makes it easy to improve and expand functionality over time
"""

# Item 37: Compose classes instead of nesting many
# levels of built-in types

# simple dictionary: easy to use, easy to be brittle
# case in point: when requirements change (feature addition)

# requirement:
# -> all grades for all students, by subject (1st), 
# -> and track weight of each score towards overall grade (2nd)

# implementing this is a fucking pain:
def average_grade(self, name):
    by_subject = self._grades[name]

    score_sum, score_count = 0, 0
    for subject, scores in by_subject.items():
        subject_avg, total_weight = 0,0
        for score, weight in scores:
            subject_avg += score * weight
            total_weight += weight

        score_sum += subject_avg / total_weight
        score_count += 1

    return score_sum / score_count
    # now.

book.add_student('mmm')
book.report_grade('mmm', 'mmth', 75, 0.05)
# ...
# this goes on.
print(book.average_grade('mmm'))

# let's rewrite this: dependency could be in:
# student -> weight, subject -> grade,
# gradebook -> student....?

# Book had other ideas:
# average grade of the subject
# subjects a student is taking
# grade has its weights with it

# simple grade: class is too heavy, how about namedtuple?
from collections import namedtuple

Grade = namedtuple('Grade', ('score', 'weight'))

class Subject:
    def __init__(self):
        self._grades = []

    def report_grade(self, score, weight):
        self._grades.append(Grade(score, weight))

    def average_grade(self):
        total, total_weight = 0, 0
        for grade in self._grades:
            total += grade.score * grade.weight
            total_weight += grade.weight
        return total / total_weight

class Student:
    def __init__(self):
        self._subjects = defaultdict(Subject)

    def get_subject(self, name):
        return self._subjects[name]

    def average_grade(self):
        total, count = 0, 0
        for subject in self._subjects.values():
            total += subject.average_grade()
            count += 1
        return total / count

class Gradebook:
    def __init__(self):
        self._students = defaultdict(Student)

    def get_student(self, name):
        return self._students[name]

# Item 39: Use @classmethod polymorphism to
# construct objects generically
"""
Polymorphism enableds multiple classes in a hierarchy
to implement their own unique versions of a method.

So, same inheritance, different behavior.
Animal -> (Dog, Cats, Horses) -> fulfills Animal stuff
"""
class InputData:
    def read(self):
        raise NotImplementedError

class PathInputData(InputData):
    def __init__(self, path):
        super().__init__()
        self.path = path

    def read(self):
        # ...

# I got the idea.
# what about MapReduce workers?
class Worker:
    def __init__(self, input_data):
        self.input_data = input_data
        self.result = None

    def map(self):
        raise NotImplementedError

    def reduce(self, other):
        raise NotImplementedError

class LineCountWorker(Worker):
    def map(self):
        data = self.input_data.read()
        self.result = data.count('\n')

    def reduce(self, other):
        self.result += other.result

# the user (orchestrator of MapReduce) that will 
# use these workers

import os

def generate_inputs(data_dir):
    for name in os.listdir(data_dir):
        yield PathInputData(os.path.join(data_dir, name))

def create_workers(input_list):
    workers = []
    for input_data in input_list:
        workers.append(LineCountWorker(input_data))
    return workers

from threading import Thread

def execute(workers):
    threads = [Thread(target=w.map) for w in workers]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    first, *rest = workers
    for worker in rest:
        first.reduce(worker)
    return first.result

# this is not generic. 
# we need different kinds of workers for different 
# kinds of work.
def mapreduce(data_dir):
    inputs = generate_inputs(data_dir)
    workers = create_workers(inputs)
    return execute(workers)

# in order to support different workers
# we could introduce constructor polymorphism
# except that it's not possible in python's case.

# so let's use classmethod polymorphism
class GenericInputData:
    def read(self):
        raise NotImplementedError

    @classmethod
    def generate_inputs(cls, config):
        raise NotImplementedError

class PathInputData(GenericInputData):
    @classmethod
    def generate_inputs(cls, config):
        data_dir = config['data_dir']
        for name in os.listdir(data_dir):
            yield cls(os.path.join(data_dir, name))

class GenericWorker:
    def __init__(self, input_data):
        self.input_data = input_data
        self.result = None

    def map(self):
        raise NotImplementedError

    def reduce(self, other):
        raise NotImplementedError

    @classmethod
    def create_workers(cls, input_class, config):
        workers = []
        # this is the fuck yeah part
        for input_data in input_class.generate_inputs(config):
            workers.append(cls(input_data))
        return workers

def mapreduce(worker_class, input_class, config):
    workers = worker_class.create_workers(input_class, config)
    return execute(workers)

# who knew @classmethod could be alternative constructors

# Item 40: Initialize Parent Classes with super





























