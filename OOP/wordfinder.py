import random
"""Word Finder: finds random words from a dictionary."""


class WordFinder:
    ...
def __init__(self, path):
    dict_file = open(path)
    self.words = self.parse(dict_file)
def parse(self, dict_file):
    return[w.strip() for w in dict_file]
def random(self):
    return random.choice(self.words)

class SpecialWordFinder(WordFinder):
    def parse(self, dict_file):
        return [w.strip() for w in dict_file
                if w.strip() and not w.startswith("#")]