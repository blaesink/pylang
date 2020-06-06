import genfuncs

v_inv = genfuncs.generate_vowel_inventory(5)
c_inv = genfuncs.generate_consonant_inventory(5)
#print(v_inv,c_inv)

morphemes = genfuncs.generate_syllable_from_pattern(v_inv,c_inv,'CV')
