sentence = input("Please type in a sentence: ")
index = 0
while index < len(sentence):
    if index == 0:
        print(sentence[0])
    if sentence[index] == " " and index + 1 < len(sentence):
        print(sentence[index + 1])
    index += 1