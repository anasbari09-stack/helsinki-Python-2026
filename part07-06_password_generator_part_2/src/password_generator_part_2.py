from random import choice
import string

def generate_strong_password(len_word: int, numbers:bool , char: bool):
    lowercase = string.ascii_lowercase
    digits = string.digits
    charachters = "!?=+-()#"
    all_words = lowercase
    word = choice(lowercase)
    if numbers:
       word += choice(digits)
       all_words += digits
       
    if char:
        word += choice(charachters)
        all_words += charachters
    
    while len(word) < len_word:
        word += choice(all_words)
    return word


if __name__ == "__main__":

    for i in range(10):
        print(generate_strong_password(8, True, True))

