import genfuncs
import random


v_inv = genfuncs.generate_vowel_inventory(5)
c_inv = genfuncs.generate_consonant_inventory(5)

morphemes = genfuncs.generate_syllable_from_pattern('CV',v_inv,c_inv,duplicates=False)

print(len(morphemes))

infix = genfuncs.generate_syllable_from_pattern('CVV',v_inv,c_inv,False,num_samples_returned=10)

suffix = genfuncs.generate_syllable_from_pattern('CC',consonants=c_inv,duplicates=False,num_samples_returned=5)

words = genfuncs.make_words(morphemes,infix,suffix)
print(random.sample(words,30))
