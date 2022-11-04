'''
Nice game for people 6-106 y.o.
'''
from typing import List
from random import randint

def get_num_of_letters(word):
    '''
    Return [('h', 1), ('e', 1), ('o', 1), ('l', 2)] for word = 'hello'
    '''
    word = word.lower()
    letters_of_word = list(set([element for element in word]))
    num_of_repetition = []
    for letter in letters_of_word:
        num_of_repetition.append(word.count(letter))

    letter_repetition = []
    for index in range(0,len(letters_of_word)):
        letter_repetition.append((letters_of_word[index],num_of_repetition[index]))
    
    return letter_repetition


def check_requirements(word, letters):
    '''
    Check is the word follow all requirements.
    '''
    num_of_letters = get_num_of_letters(word)
    if (len(word) < 4) or (letters[4] not in word):
        return False
    letters_str = ''
    for letter in letters:
        letters_str += letter
    for pair in num_of_letters:
        if (letters_str.count(pair[0])) < pair[1]:
            return False
    
    return True


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
