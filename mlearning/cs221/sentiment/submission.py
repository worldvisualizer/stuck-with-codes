#!/usr/bin/python

import random
import collections
import math
import sys
from util import *

############################################################
# Problem 3: binary classification
############################################################

############################################################
# Problem 3a: feature extraction

def extractWordFeatures(x):
    """
    Extract word features for a string x. Words are delimited by
    whitespace characters only.
    @param string x: 
    @return dict: feature vector representation of x.
    Example: "I am what I am" --> {'I': 2, 'am': 2, 'what': 1}
    """
    result = {}
    for key in x.split(' '):
        if key in result:
            result[key] += 1
        else:
            result[key] = 1
    return result

############################################################
# Problem 3b: stochastic gradient descent

def learnPredictor(trainExamples, validationExamples, featureExtractor, numIters, eta):
    '''
    Given |trainExamples| and |validationExamples| (each one is a list of (x,y)
    pairs), a |featureExtractor| to apply to x, and the number of epochs to
    train |numIters|, the step size |eta|, return the weight vector (sparse
    feature vector) learned.

    You should implement stochastic gradient descent.

    Note: only use the trainExamples for training!
    You should call evaluatePredictor() on both trainExamples and validationExamples
    to see how you're doing as you learn after each epoch. Note also that the 
    identity function may be used as the featureExtractor function during testing.
    '''
    weights = {}  # feature => weight
    # TODO
    return weights

############################################################
# Problem 3c: generate test case

def generateDataset(numExamples, weights):
    '''
    Return a set of examples (phi(x), y) randomly which are classified correctly by
    |weights|.
    '''
    random.seed(42)
    # Return a single example (phi(x), y).
    # phi(x) should be a dict whose keys are a subset of the keys in weights
    # and values can be anything (randomize!) with a nonzero score for the given weight vector.
    # y should be 1 or -1 as classified by the weight vector.

    # Note that the weight vector can be arbitrary during testing. 
    # TODO
    def generateExample():
        phi = 0
        y = 0
        return (phi, y)
    return [generateExample() for _ in range(numExamples)]

############################################################
# Problem 3e: character features

def extractCharacterFeatures(n):
    '''
    Return a function that takes a string |x| and returns a sparse feature
    vector consisting of all n-grams of |x| without spaces mapped to their n-gram counts.
    EXAMPLE: (n = 3) "I like tacos" --> {'Ili': 1, 'lik': 1, 'ike': 1, ...
    You may assume that n >= 1.
    '''
    def extract(x):
        # TODO
        pass
    return extract

############################################################
# Problem 4: k-means
############################################################

def euclideanDistance(loc1, loc2):
    """
    Return the Euclidean distance between two locations, where the locations
    are pairs of numbers (e.g., (3, 5)).
    """
    def squareTwo(num1, num2):
        return abs(num1 - num2) ** 2

    distances = {}
    for key in loc1:
        if key in loc2:
            distances[key] = squareTwo(loc1[key], loc2[key])
        else:
            distances[key] = squareTwo(loc1[key], 0)

    for key in loc2:
        if key not in distances:
            distances[key] = squareTwo(loc2[key], 0)
    
    return math.sqrt(sum(list(distances.values())))


def assignExamples(examples, assignments, centroids):
    for index, example in enumerate(examples):
        minLoss = 0
        losses = sorted(
            [
                [centIndex, euclideanDistance(example, cent)]
                for centIndex, cent in enumerate(centroids)
            ],
            key=lambda x: x[1])
        assignments[index] = losses[0][0] # centIndex of argmin
    return assignments


def setCentroids(examples, assignments, centroids):

    def sumDict(dict1, dict2):
        for key in dict2:
            dict1[key] += dict2[key]
        return dict1

    def divideDict(dictionary, count):
        for key in dictionary:
            dictionary[key] /= count
        return dictionary

    assert(len(examples) == len(assignments))
    centCalculations = [[0, collections.defaultdict(float)] for i in range(len(centroids))]
    for i, assignment in enumerate(assignments):
        example = examples[i]
        centCalculations[assignment] = [
            centCalculations[assignment][0] + 1,
            sumDict(centCalculations[assignment][1], example)
        ]

    newCentroids = []
    for container in centCalculations:
        count, sumofexample = container
        newCentroids.append(divideDict(sumofexample, count))
    return newCentroids


def calculateTotalLoss(examples, assignments, centroids):
    totalLoss = 0
    for i, example in enumerate(examples):
        cent = centroids[assignments[i]]
        totalLoss += euclideanDistance(cent, example)
    return totalLoss


def kmeans(examples, K, maxIters):
    '''
    examples: list of examples, each example is a string-to-double dict representing a sparse vector.
    K: number of desired clusters. Assume that 0 < K <= |examples|.
    maxIters: maximum number of epochs to run (you should terminate early if the algorithm converges).
    Return: (length K list of cluster centroids,
            list of assignments (i.e. if examples[i] belongs to centers[j], then assignments[i] = j)
            final reconstruction loss)
    '''

    def toDefaultDict(counterItem):
        defaultItem = collections.defaultdict(float)
        for key in counterItem.keys():
            defaultItem[key] = counterItem[key]
        return defaultItem

    def initializeCentroid(items):
        modelExample = collections.defaultdict(list)
        for item in items:
            for key, value in item.items():
                if modelExample[key]:
                    curmin, curmax = modelExample[key]
                    if curmin != None:
                        if value < curmin:
                            curmin = value
                    if curmin != None:
                        if value > curmax:
                            curmax = value
                    modelExample[key] = [curmin, curmax]
                else:
                    modelExample[key] = [0.0, 0.0]

        return modelExample

    def randomCentroid(modelExample):
        randomExample = collections.defaultdict(float)
        for key, value in modelExample.items():
            minimum, maximum = value
            randomExample[key] = random.uniform(minimum, maximum)
        return randomExample

    # assignment after creating a copy of the original works
    examples = [toDefaultDict(item) for item in examples]
    # create assignment index for each of the examples
    assignments = [0 for i in range(len(examples))]
    modelExample = initializeCentroid(examples)
    centroids = [randomCentroid(modelExample) for i in range(K)]

    for i in range(maxIters):
        assignments = assignExamples(examples, assignments, centroids)
        centroids = setCentroids(examples, assignments, centroids)

    reconstructionLoss = calculateTotalLoss(examples, assignments, centroids)

    return (centroids, assignments, reconstructionLoss)
