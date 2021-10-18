"""Word Finder: finds random words from a dictionary."""

import random


class WordFinder:
    """Machine for finding random words from dictionary.
    
    >>> wf = WordFinder("dogs.txt")
    3 words read

    >>> wf.random() in ["Fido", "Whiskey", "Dr.Sniffle"]
    True

    >>> wf.random() in ["Fido", "Whiskey", "Dr.Sniffle"]
    True

    >>> wf.random() in ["Fido", "Whiskey", "Dr.Sniffle"]
    True
    """

    def __init__(self, path):
        """Read dictionary and reports # items read."""

        file_path = open(path)

        self.words = self.read_file_list(file_path)

        print(f"{len(self.words)} words read")

    def read_file_list(self, file_path):
        """Read through each line in txt file -> list of words."""

        return [line.strip() for line in file_path]

    def random(self):
        """Return random word."""

        return random.choice(self.words)

class SpecialWordFinder(WordFinder):
    """Specialized WordFinder that excludes blank lines/comments.
    
    >>> swf = SpecialWordFinder("cats.txt")
    4 words read

    >>> swf.random() in ["Auden", "Ezra", "Fluffy", "Meowsley"]
    True

    >>> swf.random() in ["Auden", "Ezra", "Fluffy", "Meowsley"]
    True

    >>> swf.random() in ["Auden", "Ezra", "Fluffy", "Meowsley"]
    True
    """

    def read_file_list(self, file_path):
        """Read through each line in txt file -> list of words, skipping blanks/comments."""

        return [line.strip() for line in file_path
                if line.strip() and not line.startswith("#")]


        
