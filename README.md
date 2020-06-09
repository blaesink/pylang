# Pylang generator
The purpose of this generator is to generate (hopefully) coherent-sounding conlangs used in fantasy settings.

# How it (should) work
## Vowel and Consonant Generation
Both `generate_vowel_inventory` and `generate_consonant_inventory` take in `n` arguments and generate a list of consonants and vowels.

## Morpheme Generation
Once basic vowels and consonants are generated, they can be used to create morphemes via `generate_syllable_from_pattern`.
`generate_syllable_from_pattern` parses a string of `'C'` and `'V'` characters to create a matrix of the phonemes, and returns the products of all elements in the matrix.


`Example`: your vowels are `['a','e','i']` with consonants `['b','d','g']`.
Passing them into `generate_syllable_from_pattern` with the pattern of `CV` will generate the following matrix:
```
[ ['a','e','i'], ['b','d','g'] ]
```
and will return:
`['ab','ad','ag','eb','ed','eg','ib','id','ig']`, which is as stated, the product of all characters passed in using the supplied pattern.

Please note that the number of morphemes generated increases _multiplicatively_ and can and will generate a number of morphemes that will exceed your need.
To avoid being overloaded, change `num_samples_returned` to a number _less than the product of the lengths of the vowel and consonant inventories for the time being._

### Infixes, Suffixes
`generate_syllable_from_pattern` is supplied with optional empty list arguments in the event you'd like to create consonant clusters, long vowels, or dipthongs.
If you'd like to have no repeating characters, setting `duplicates` to `False` will remove them (_see below_).

`Note` It's planned to have the `duplicates: bool=False` reworked due to multi-characters consonants,

## Word Generation
`make_words` takes in any number of arguments and creates a matrix of the supplied samples the same as `generate_syllable_from_pattern`.
As you can have any amount of prefixes,infixes and suffixes, do make sure to add them _in order_ to avoid getting samples you don't expect!
(This is useful if you're looking to emulate agglutinative languages like Hungarian.)


# Next Steps
- Add language families for the vowels and consonants to add to the `generate_*_inventory` functions to tailor the generators towards a certain 'feel'
- `In Progress` Redo the duplicate logic with tokenizing the phonemes due to multi-character consonants.
	- Working on it via using new Phoneme/Morpheme/Word classes.
- `TODO` have a dedupe logic for arguments passed to the `make_words` in the case of potential agglutinatives?
