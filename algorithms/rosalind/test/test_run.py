"""
testing harness for testing example dataset from rosalind
this class parses input, runs the function, and displays result.
copying and pasting answer submission to rosalind textbox will be enough

when running entirety of the test, separate class called TestFramework is in charge
"""
import unittest


class TestRun(unittest.TestCase):
    

    def __init__(self, datapath, func, debug = False):
        """
	receives dataset filepath, testing function itself, and expected results
        """
        self.datapath = datapath
        self.func = func
        self.debug = debug

    def print_results(results):
        print("------- test run for {} -------".format(self.func.__name__))
        print("------------------------------------------")
        print("------- results ---------------")
        for item in results:
            print(item)


    def test_run(self):
        with open(self.datapath, 'r') as datafile:
            inputs = [line for line in datafile.read()]
            results = self.func(inputs)
            if self.debug:
                self.print_results(results)
                



