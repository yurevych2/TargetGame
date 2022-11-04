'''
Nice game for people 6-106 y.o.
'''
from typing import List
from random import randint

def get_num_of_letters(word):
    '''
    Return [('h', 1), ('e', 1), ('o', 1), ('l', 2)] for word = 'hello'
    '''


def check_requirements(word, letters):
    '''
    Check is the word follow all requirements.
    '''


def generate_grid() -> List[List[str]]:
    '''
    Generates list of lists of letters - i.e. grid for the game.
    e.g. [['I', 'G', 'E'], ['P', 'I', 'S'], ['W', 'M', 'G']]
    '''


def get_words(path: str, letters: List[str]) -> List[str]:
    '''
    Reads the file f. Checks the words with rules and returns a list of words.
    '''


def get_user_words() -> List[str]:
    '''
    Gets words from user input and returns a list with these words.
    Usage: enter a word or press ctrl+d to finish for *nix or Ctrl-Z+Enter
    for Windows.
    Note: the user presses the enter key after entering each word.
    '''


def get_pure_user_words(user_words: List[str], letters: List[str],\
                        words_from_dict: List[str]) -> List[str]:
    '''
    (list, list, list) -> list

    Checks user words with the rules and returns list of those words
    that are not in dictionary.
    '''


def results():
    '''
    Body of the game.
    '''
