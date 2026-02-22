# Write your solution here
# You can test your function by calling it within the following block
def same_chars(word, char1, char2):
    if char1 >= len(word) or char2 >= len(word):
        return False
    elif word[char1] == word[char2]:
        return True
    else:
        return False
if __name__ == "__main__":
    same_chars("coder", 1, 10)