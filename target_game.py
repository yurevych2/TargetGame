'''
Nice game for people 6-106 y.o.
'''
from typing import List
from random import choice
from string import ascii_lowercase

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
    length = 3
    grid = [[choice(ascii_lowercase) for _ in range(length)] for _ in range(length)]
    
    return grid


def get_words(path: str, letters: List[str]) -> List[str]:
    '''
    Reads the file f. Checks the words with rules and returns a list of words.
    '''
    with open(path, 'r')as file:
        file.readline()
        file.readline()
        file.readline()
        words = file.readlines()
    answers = []
    for word in words:
        word = word.strip().lower()
        if check_requirements(word, letters):
            answers.append(word)

    return answers


def get_user_words() -> List[str]:
    '''
    Gets words from user input and returns a list with these words.
    Usage: enter a word or press ctrl+d to finish for *nix or Ctrl-Z+Enter
    for Windows.
    Note: the user presses the enter key after entering each word.
    '''
    user_words = []
    while True:
        try:
            word = input('>>> ')
            user_words.append(word)
        except EOFError:
            break

    return user_words


def get_pure_user_words(user_words: List[str], letters: List[str],\
                        words_from_dict: List[str]) -> List[str]:
    '''
    (list, list, list) -> list

    Checks user words with the rules and returns list of those words
    that are not in dictionary.
    '''
    pure_user_words = []
    for word in user_words:
        if check_requirements(word, letters) and word not in words_from_dict:
            pure_user_words.append(word)

    return pure_user_words


def results():
    '''
    Body of the game.
    '''
    possible_answers = []
    while not possible_answers:
        grid = generate_grid()
        possible_answers = get_words('en.txt', [[element for element in row] for row in grid])
    print(grid)
    user_words = get_user_words()
    pure_words = get_pure_user_words(user_words,grid,possible_answers)
    num_guessed_words = 0
    guessed_words = []
    for word in user_words:
        if check_requirements(word,grid) and (word not in guessed_words):
            if word in possible_answers:
                possible_answers.remove(word)
            guessed_words.append(word)
            num_guessed_words += 1

    return num_guessed_words, possible_answers, pure_words
