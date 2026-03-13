# write your solution here
text = input("Write text: ")
text_list = text.strip()
text_list = text_list.split(" ")
word_dic = {}
with open("wordlist.txt") as f:
    for word in f:
        word = word.strip()
        word_dic[word] = word
    for word in text_list:
        if word.lower() not in word_dic:
           word = f"*{word}*"
        print(word + " ",end="") 
