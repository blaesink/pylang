import genfuncs
import random
from tokens import *


v_inv = genfuncs.generate_vowel_inventory(5)
c_inv = genfuncs.generate_consonant_inventory(5)

morphemes = [Morpheme(x) for x in genfuncs.generate_syllable_from_pattern('CV',v_inv,c_inv,num_samples_returned=5)]
#print([x.__str__() for x in morphemes])


infix = [Morpheme(x) for x in genfuncs.generate_syllable_from_pattern('CVV',v_inv,c_inv)]

suffix = [Morpheme(x) for x in genfuncs.generate_syllable_from_pattern('CC',consonants=c_inv)]


words = genfuncs.make_words(morphemes,infix,suffix)
words = [Word(x) for x in words]
print([x.__str__() for x in random.sample(words,10)])
