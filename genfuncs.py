import pandas as pd
import random
from itertools import product
import re

vowels = pd.read_csv("vowels.csv")
vowels=vowels.drop([15,17]) # drops the mid front o and mid back o

consonants = pd.read_csv("consonants.csv")

def generate_vowel_inventory(num: int):
    """Generates n amount of vowels for the conlang"""
    global vowels
    return vowels['symbol'].sample(n = num).tolist()

def generate_consonant_inventory(num: int):
    """Generates n amount of consonantss for the conlang"""
    global consonants
    return consonants['symbol'].sample(n = num).tolist()

def generate_syllable_from_pattern(pat:str, vowels=[], consonants=[], duplicates=True,num_samples_returned='all') -> list:
    """Pass a string like 'CVCV' to generate syllables in that format

    [a,e,i,o,u] * [b,d,g,t,k] -> 25 combinations of VC pairings

    [b,d,g,t,k] * [a,e,i,o,u] * [b,d,g,t,k] -> 125 combinations of VC pairings

    TODO: remember to have rules in place to remove anything that would violate said rules -> parameter?

    TODO: duplicates means that repeated symbols are prohibited (mostly used for eliminating repeated consonants that aren't sonorants.
    """

    pattern_matrix = []

    for c in pat:
        if c.upper() == "C":
            pattern_matrix.append(consonants)
        if c.upper() == "V":
            pattern_matrix.append(vowels)

    patterns = list(product(*pattern_matrix))
    str_pats = [''.join(x) for x in patterns]

    if duplicates == False:
        # this could be a one liner with the first list comp somehow
        str_pats = [re.sub(r'[^\w\s]|(.)(?=\1)', '', x) for x in str_pats]
        # problem with certain digraphs since they're two characters..
        #str_pats = [x for x in str_pats if len(x) == len(pat)]

    if num_samples_returned == 'all':
        return str_pats
    elif type(num_samples_returned) == int:
        return random.sample(str_pats,num_samples_returned)

def make_words(*word_parts):
    matrix = [p for p in word_parts]

    word_mat = list(product(*matrix))

    return [''.join(x) for x in word_mat]
