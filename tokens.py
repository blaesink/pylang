class Phoneme:
    def __init__(self,sym: str):
        self.symbol = sym

    def __str__(self):
        return f'{self.symbol}'

class Morpheme:
    def __init__(self,phonemes):
        self.phonemes = phonemes

    def __str__(self):
        return f"{''.join([x.symbol for x in self.phonemes])}"

class Word:
    def __init__(self,morphemes):
        self.morphemes = morphemes

    def __str__(self):
        return f"{''.join([x.__str__() for x in self.morphemes])}"
