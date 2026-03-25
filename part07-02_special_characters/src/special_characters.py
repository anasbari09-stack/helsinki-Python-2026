# Write your solution here
import string
def separate_characters(my_string: str):
    ascii_letters = ""
    punctuation = ""
    others = ""
    for l in my_string:
        if l in string.ascii_lowercase or l in string.ascii_uppercase:
          ascii_letters += l
        elif l in string.punctuation:
            punctuation += l
        else :
            others += l
    return (ascii_letters, punctuation, others)


