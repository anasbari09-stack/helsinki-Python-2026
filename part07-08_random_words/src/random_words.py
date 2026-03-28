# Write your solution here
from random import sample
def words(n: int, beginning: str):
    list_words = []
    with open("words.txt") as f:
        for line in f:
            word = line.strip()
            if word.startswith(beginning):
                list_words.append(word)
    
    
    if len(list_words) < n:
        raise ValueError("There are not enough words beginning with the specified string")
    else: 
        return sample(list_words, n)

if __name__ == "__main__":
    word_list = words(5, 'car')
    for word in word_list:
        print(word)
        