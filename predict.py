"""
@File: predict.py
@author: Jonathan Baxley
Main predict function
"""
from AIlab2.train import *


"""
Main predict function, determines whether or not it is a .dt or .ada and predicts based on that
@:param: hypothesis - file containing the model
@:param: file - file containing the sentences to be analyzed
"""
def predict(hypothesis, file):
    model_file = open(hypothesis, "rb")
    model = pickle.load(model_file)
    f = open(file, "r", encoding=("UTF-8"))
    sentences = []
    type = hypothesis.split(".")
    type = type[-1]
    for x in f:
        y = x.replace("\n", "")
        sentences.append(y)
    if type == "dt":
        predict_dt(model, sentences)
    elif type == "ada":
        predict_ada(model, sentences)

"""
Predict function for ada boost, it adds up an estimate and if the estimate is close to 0 it is dutch else english
@:param: model - model to be used for adaboost (list of ensembles)
@:param: sentences - list of sentences
"""
def predict_ada(model, sentences):
    for x in sentences:
        estimate = 0
        for z in model:
            y = z.attribute
            if y == 0:
                if containsFor(x) == "en":
                    estimate += z.weight
            elif y == 1:
                if containsYou(x) == "en":
                    estimate += z.weight
            elif y == 2:
                if containsAn(x) == "en":
                    estimate += z.weight
            elif y == 3:
                if containsThe(x) == "en":
                    estimate += z.weight
            elif y == 4:
                if containsBe(x) == "en":
                    estimate += z.weight
            elif y == 5:
                if containsOf(x) == "en":
                    estimate += z.weight
            elif y == 6:
                if containsAnd(x) == "en":
                    estimate += z.weight
            elif y == 7:
                if containsThis(x) == "en":
                    estimate += z.weight
            elif y == 8:
                if containsThat(x) == "en":
                    estimate += z.weight
            elif y == 9:
                if containsWith(x) == "en":
                    estimate += z.weight
            elif y == 10:
                if containsAs(x) == "en":
                    estimate += z.weight
        if estimate <= .1:
            print("nl")
        else:
            print("en")

"""
Predict function for decision trees, it adds up an estimate and if the estimate is close to 0 it is dutch else english
@:param: model - model to be used for adaboost (list of ensembles)
@:param: sentences - list of sentences
"""
def predict_dt(model, sentences):
    if model == None:
        return None
    for x in sentences:
        tree = model
        while tree != None:
            attribute = tree.val
            if attribute == 0:
                if containsFor(x) == "en":
                    print("en")
                    break
            elif attribute == 1:
                if containsYou(x) == "en":
                    print("en")
                    break
            elif attribute == 2:
                if containsAn(x) == "en":
                    print("en")
                    break
            elif attribute == 3:
                if containsThe(x) == "en":
                    print("en")
                    break
            elif attribute == 4:
                if containsBe(x) == "en":
                    print("en")
                    break
            elif attribute == 5:
                if containsOf(x) == "en":
                    print("en")
                    break
            elif attribute == 6:
                if containsAnd(x) == "en":
                    print("en")
                    break
            elif attribute == 7:
                if containsThis(x) == "en":
                    print("en")
                    break
            elif attribute == 8:
                if containsThat(x) == "en":
                    print("en")
                    break
            elif attribute == 9:
                if containsWith(x) == "en":
                    print("en")
                    break
            elif attribute == 10:
                if containsAs(x) == "en":
                    print("en")
                    break
            elif tree.right == None:
                print("nl")
                break
            tree = tree.right

"""
Main function for predict.py
Takes 2 parameters <hypothesis> <file>  as arguments where
hypothesis is the model being used, 
file is the file of sentences to be predicted
"""
def main():
    n = len(sys.argv)
    if n != 3:
        print("Incorrect arguments")
    predict(sys.argv[1], sys.argv[2])

if __name__ == '__main__':
    main()