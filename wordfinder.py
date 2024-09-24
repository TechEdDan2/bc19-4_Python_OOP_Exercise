"""Word Finder: finds random words from a dictionary."""
import random


class WordFinder:
    """ Finds words in a list of words 
    >>> wf = WordFinder("words.txt") 
    3 words read 
    
    >>> wf.random() 
    'cat' 
    
    >>> wf.random() 
    'cat' 
    
    >>> wf.random() 
    'porcupine' 
    
    >>> wf.random() 
    'dog'
    """

    def __init__(self, file_path):
        """ Read the file and notes number of items """
        file_content = open(file_path)

        self.words = self.parse(file_content)

        print(f"{len(self.words)} words read")

    def parse(self, dict_file):
        """Parse dict_file -> list of words."""

        return [w.strip() for w in dict_file]
    
    def random(self):
        """Return random word."""

        return random.choice(self.words)