"""
@File: train.py
@author: Jonathan Baxley
Main train function
"""
import math
import pickle
import random
import sys

from AIlab2.features import *

"""
Node class used by decision tree
key is the value of the node
"""
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

"""
Ensemble class used by Adaboost
attribute is the specific feature
weight is the weight for that feature
"""
class Ensemble:
    def __init__(self, attribute, weight):
        self.attribute = attribute
        self.weight = weight

"""
Picks the most common language in a list of sentences either dutch or english.
@:param: Parent - list of features with a description of length
@:return: Returns english if english is the most common language, returns dutch if dutch is the most common language
"""
def pluralityValues(parent):
    num_en = 0
    num_nl = 0
    for x in parent:
        if x[-1] == "en":
            num_en += 1
        else:
            num_nl += 1
    if num_en > num_nl:
        return "en"
    elif num_nl == num_en:
        num = random.randint(0,1)
        if num == 0:
            return "nl"
        return "en"
    return "nl"

"""
Function to calculate the best attribute given a list of examples
@:param: a - list of attributes
@:param: examples - list of features from sentences
@:return: Returns the most important feature in a
"""
def importance(a, examples):
    sum = 0
    highest = a[0]
    for x in a:
        if x == "nl" or x == "en":
            continue
        b = []
        for y in examples:
            b.append([y[x], y[-1]])
        num = information_gain(examples, b)
        if num > sum:
            sum = num
            highest = x
    return highest

"""
Calculates information gain for an attribute
@:param: examples - list of features from sentences
@:param: b - list that contains a list with a feature and language
"""
def information_gain(example, b):
    parent = entropy(example)
    parent_len = len(example)
    truth = []
    false = []
    for x in b:
        if x[0]:
            truth.append(x)
        else:
            false.append(x)
    truth_entropy = entropy(truth)
    truth_len = len(truth)
    false_entropy = entropy(false)
    false_len = len(false)

    child = (truth_len/parent_len) * truth_entropy + (false_len/parent_len) * false_entropy

    return parent - child

"""
Function to calculate entropy of an attribute
@:param: a - list of features
@:return: Returns a number representing entropy, less entropy = more information gain
"""
def entropy(a):
    if len(a) == 0:
        return 0
    eng = 0
    dutch = 0
    for x in a:
        if x[-1] == "en":
            eng += 1
        elif x[-1] == "nl":
            dutch += 1
    eng = eng/len(a)
    dutch = dutch/len(a)
    entropy = 0
    if eng != 0:
        entropy += eng * math.log(eng, 2) * -1
    elif dutch != 0:
        entropy += dutch * math.log(dutch, 2) * -1
    return entropy

"""
Function to see if all languages are the same in examples
@:param: examples - list of features from sentences
@:return: Returns true if all are the same, false else
"""
def all_classifications(examples):
    same = True
    prev = examples[0]
    for x in examples:
        if x != prev:
            same = False
    return same

"""
Main train function that preprocess's data and decides what kind of learning type to be used.
Writes a model to hypothesisisOut file
"""
def train(examples, hypothesisOut, learningType):
    f = open(examples, "r", encoding=("UTF-8"))
    usage = []
    attributes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for x in f:
        y = x.split("|")
        lang = y[0]
        words = y[1]
        booleans = []
        booleans.append(containsFor(words) == "en")
        booleans.append(containsYou(words) == "en")
        booleans.append(containsAn(words) == "en")
        booleans.append(containsThe(words) == "en")
        booleans.append(containsBe(words) == "en")
        booleans.append(containsOf(words) == "en")
        booleans.append(containsAnd(words) == "en")
        booleans.append(containsThis(words) == "en")
        booleans.append(containsThat(words) == "en")
        booleans.append(containsWith(words) == "en")
        booleans.append(containsAs(words) == "en")
        booleans.append(lang)
        usage.append(booleans)
    if learningType == "dt":
        tree = train_dt(usage, attributes, usage)
        pickled_tree = pickle.dumps(tree)
        f = open(hypothesisOut+".dt", "wb")
        f.write(pickled_tree)
    else:
        ensemble = train_ada(usage, attributes)
        pickled_ensemble = pickle.dumps(ensemble)
        f = open(hypothesisOut+".ada", "wb")
        f.write(pickled_ensemble)
    return

"""
Function for training using decision trees
@:param: examples - list of features from sentences
@:param: attributes - list of features
@:param: parent - original examples file
@:return: Returns a Node which is a BST
"""
def train_dt(examples, attributes, parent):
    if examples == []:
        return Node(pluralityValues(parent))
    elif all_classifications(examples):
        return Node(examples[0][9])
    elif attributes == []:
        return Node(pluralityValues(examples))
    else:
        A = importance(attributes, examples)
        attributes.remove(A)
        tree = Node(A)

        exs = []
        for x in examples:
            if not x[A]:
                exs.append(x)
        subtree = train_dt(exs, attributes, parent)
        tree.left = "en"
        tree.right = subtree
        return tree

"""
Function for training using Adaboost
@:param: examples - list of features from sentences
@:param: attributes - list of features
@:return: Returns a list of ensembles
"""
def train_ada(examples, attributes):
    h = []
    z = []
    for a in attributes:
        h.append(get_weight(a, examples))
    h = normalize(h)
    for i in range(len(attributes)):
        z.append(Ensemble(attributes[i], h[i]))
    return z

"""
Function to normalize a list of numbers
@:param: h - list of numbers to be normalized
@:return: Returns a normalized list
"""
def normalize(h):
    normal = [float(i)/sum(h) for i in h]
    return normal

"""
Function to get the weight of an attribute
@:param: a - attribute/feature
@:param: examples - list of features from sentences
@:return: a number representing the weight
"""
def get_weight(a, examples):
    correct = 0
    for x in examples:
        if x[a] and x[-1] == "en":
            correct += 1
        elif not x[a] and x[-1] == "nl":
            correct += 1

    weight = correct/len(examples)
    return weight


"""
Main function for train.py
Takes 3 parameters <examples> <hypothesisOut> <learning-type> as arguments where
examples is the name of a file that examples should be taken from,
hypothesisisOut is the name of a file that the model should be written to,
and learning-type is either "dt" or "ada" to decide which learning type should be used
"""
def main():
    n = len(sys.argv)
    if n != 4:
        print("Incorrect arguments")
        return

    f = open(sys.argv[1], "r", encoding=("UTF-8"))
    lst = []
    for x in f:
        lst.append(x)

    train(sys.argv[1], sys.argv[2], sys.argv[3])

if __name__ == '__main__':
    main()