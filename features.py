"""
@File: features.py
@author: Jonathan Baxley
File for determining if features exists in sentences
"""

"""
Checks if sentence contains The
@:param: words - list of words
@:return: Returns "en" if it contains The else otherwise
"""
def containsThe(words):
    word = words.split()
    for x in word:
        lower = x.lower()
        if lower == "the":
            return "en"
    return "nl"
"""
Checks if sentence contains You
@:param: words - list of words
@:return: Returns "en" if it contains You else otherwise
"""
def containsYou(words):
    word = words.split()
    for x in word:
        lower = x.lower()
        if lower == "you":
            return "en"
    return "nl"

"""
Checks if sentence contains An
@:param: words - list of words
@:return: Returns "en" if it contains An else otherwise
"""
def containsAn(words):
    word = words.split()
    for x in word:
        lower = x.lower()
        if lower == "an":
            return "en"
    return "nl"

"""
Checks if sentence contains Be
@:param: words - list of words
@:return: Returns "en" if it contains Be else otherwise
"""
def containsBe(words):
    word = words.split()
    for x in word:
        lower = x.lower()
        if lower == "be":
            return "en"
    return "nl"

"""
Checks if sentence contains Of
@:param: words - list of words
@:return: Returns "en" if it contains Of else otherwise
"""
def containsOf(words):
    word = words.split()
    for x in word:
        lower = x.lower()
        if lower == "of":
            return "en"
    return "nl"

"""
Checks if sentence contains And
@:param: words - list of words
@:return: Returns "en" if it contains And else otherwise
"""
def containsAnd(words):
    word = words.split()
    for x in word:
        lower = x.lower()
        if lower == "and":
            return "en"
    return "nl"

"""
Checks if sentence contains This
@:param: words - list of words
@:return: Returns "en" if it contains This else otherwise
"""
def containsThis(words):
    word = words.split()
    for x in word:
        lower = x.lower()
        if lower == "this":
            return "en"
    return "nl"

"""
Checks if sentence contains That
@:param: words - list of words
@:return: Returns "en" if it contains That else otherwise
"""
def containsThat(words):
    word = words.split()
    for x in word:
        lower = x.lower()
        if lower == "that":
            return "en"
    return "nl"

"""
Checks if sentence contains With
@:param: words - list of words
@:return: Returns "en" if it contains With else otherwise
"""
def containsWith(words):
    word = words.split()
    for x in word:
        lower = x.lower()
        if lower == "with":
            return "en"
    return "nl"

"""
Checks if sentence contains As
@:param: words - list of words
@:return: Returns "en" if it contains As else otherwise
"""
def containsAs(words):
    word = words.split()
    for x in word:
        lower = x.lower()
        if lower == "as":
            return "en"
    return "nl"

"""
Checks if sentence contains For
@:param: words - list of words
@:return: Returns "en" if it contains For else otherwise
"""
def containsFor(words):
    word = words.split()
    for x in word:
        lower = x.lower()
        if lower == "for":
            return "en"
    return "nl"