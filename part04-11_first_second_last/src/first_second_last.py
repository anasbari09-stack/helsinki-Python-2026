# Write your solution here
# You can test your function by calling it within the following block
def first_word(sentence):
    find1 = sentence.find(" ")
    return sentence[:find1]
def second_word(sentence):
    find1 = sentence.find(" ")
    find2 = sentence[(find1 +1):].find(" ")
    if find2 == -1:
        return sentence[find1 + 1:]
    else:
        return sentence[find1 + 1 : find2 + find1 + 1]
def last_word(sentence):
    index = (-1)
    while True:
        if sentence[index] == " " :
            return sentence[index + 1:]
        index -= 1

if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))
    