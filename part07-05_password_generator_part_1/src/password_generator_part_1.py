# Write your solution here
from random import choice
import string

def generate_password(len_word: int):
    word = ""
    for i in range(len_word):
        word  += choice(string.ascii_lowercase)
    return word

