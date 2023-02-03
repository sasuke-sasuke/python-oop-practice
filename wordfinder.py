"""Word Finder: finds random words from a dictionary."""
from random import choice

class WordFinder:
    """Creates an object that chooses a random word from a word text file that contains one word per line"""
    def __init__(self, path):
        file = open(path, 'r')
        self.word_list = file.readlines()
        self.cleaned_words = []
        self.count = len(self.word_list)

        self.num_of_words()
        self.clean_up()
        file.close()

    def num_of_words(self):
        """ Displays number of words read"""
        print(f'{self.count} words were read.')

    def clean_up(self):
        """Removes 'junk' from word"""
        for word in self.word_list:
            self.cleaned_words.append(word.strip())

    def random_word(self):
        """Returns random word from list"""
        return choice(self.cleaned_words)


class SpecialWordFinder(WordFinder):
    
    def __init__(self, path):
        super().__init__(path)


