import collections
import math

############################################################
# Problem 3a

def findAlphabeticallyLastWord(text):
    """
    Given a string |text|, return the word in |text| that comes last
    alphabetically (that is, the word that would appear last in a dictionary).
    A word is defined by a maximal sequence of characters without whitespaces.
    You might find max() and list comprehensions handy here.
    """
    return sorted(text.split(' '), reverse=True)[0]

############################################################
# Problem 3b

def euclideanDistance(loc1, loc2):
    """
    Return the Euclidean distance between two locations, where the locations
    are pairs of numbers (e.g., (3, 5)).
    """
    def squareTwo(num1, num2):
        return abs(num1 - num2) ** 2
    
    return math.sqrt(squareTwo(loc1[0], loc2[0]) + squareTwo(loc1[1], loc2[1]))

############################################################
# Problem 3c

def mutateSentences(sentence):
    """
    Given a sentence (sequence of words), return a list of all "similar"
    sentences.
    We define a sentence to be similar to the original sentence if
      - it as the same number of words, and
      - each pair of adjacent words in the new sentence also occurs in the original sentence
        (the words within each pair should appear in the same order in the output sentence
         as they did in the orignal sentence.)
    Notes:
      - The order of the sentences you output doesn't matter.
      - You must not output duplicates.
      - Your generated sentence can use a word in the original sentence more than
        once.
    Example:
      - Input: 'the cat and the mouse'
      - Output: ['and the cat and the', 'the cat and the mouse', 'the cat and the cat', 'cat and the cat and']
                (reordered versions of this list are allowed)
    """
    def mutateSentencesRecurse(lensentence, adjacentWords, midsentence, sentences):
        if lensentence == len(midsentence):
            sentences.append(' '.join(midsentence))
            return
        for adjword in adjacentWords[midsentence[-1]]:
            mutateSentencesRecurse(lensentence, adjacentWords, midsentence + [adjword], sentences)

    from collections import defaultdict
    sentence = sentence.split(' ')
    adjacentWords = defaultdict(list)

    for i, word in enumerate(sentence[:-1]):
        if sentence[i+1] not in adjacentWords[word]:
            adjacentWords[word].append(sentence[i+1])
    
    sentences = []
    # keyset gives glimpse into dict (maybe getting mid-iteration cursor)
    # for dict class. therefore, making copy is important
    for word in list(adjacentWords):
        mutateSentencesRecurse(len(sentence), adjacentWords, [word], sentences)
    return sentences
    
############################################################
# Problem 3d

def sparseVectorDotProduct(v1, v2):
    """
    Given two sparse vectors |v1| and |v2|, each represented as collections.defaultdict(float), return
    their dot product.
    You might find it useful to use sum() and a list comprehension.
    This function will be useful later for linear classifiers.
    Note: A sparse vector has most of its entries as 0
    The keys of the sparse vector can be any type. For example, an input could be {'a': 1.0, 'b': 2.0}
    """
    return sum([v1[key] * v2[key] for key in list(v1)])
    

############################################################
# Problem 3e

def incrementSparseVector(v1, scale, v2):
    """
    Given two sparse vectors |v1| and |v2|, perform v1 += scale * v2.
    Do not modify v2 in your implementation.
    This function will be useful later for linear classifiers.
    """
    for key in list(v2):
        if key in list(v1):
            v1[key] += v2[key] * scale
        else:
            v1[key] = v2[key] * scale
    return v1

############################################################
# Problem 3f

def findSingletonWords(text):
    """
    Splits the string |text| by whitespace and returns the set of words that
    occur exactly once.
    You might find it useful to use collections.defaultdict(int).
    """
    from collections import defaultdict
    wordcount = defaultdict(int)
    for word in text.split(' '):
        wordcount[word] += 1
    return set([w for w, count in wordcount.items() if count == 1])

############################################################
# Problem 3g

def longestCommonSubsequenceLength(text1, text2, scoreMat):
    for i in range(1, len(text2)+1):
        for j in range(1, len(text1)+1):
            if text1[j-1] == text2[i-1]:
                score = 1
            else:
                score = 0
            scoreMat[i][j] = max(
                score + scoreMat[i-1][j-1], scoreMat[i-1][j], scoreMat[i][j-1]
            )
    return scoreMat[len(text2)][len(text1)]

def computeLongestPalindromeLength(text):
    """
    A palindrome is a string that is equal to its reverse (e.g., 'ana').
    Compute the length of the longest palindrome that can be obtained by deleting
    letters from |text|.
    For example: the longest palindrome in 'animal' is 'ama' and it's length is 3.
    Your algorithm should run in O(len(text)^2) time.
    You should first define a recurrence before you start coding.
    """
    textReversed = ''.join(reversed(list(text)))
    scoreMat = [[0 for i in range(len(text) + 1)] for j in range(len(textReversed) + 1)]
    return longestCommonSubsequenceLength(text, textReversed, scoreMat)

