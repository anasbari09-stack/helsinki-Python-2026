# Write your solution here

while True:
    print("1 - Add word, 2 - Search, 3 - Quit")
    function = int(input("Function: "))
    if function == 1:
        word_finnish = input("The word in Finnish: ")
        word_english = input("The word in English: ")
        with open("dictionary.txt", "a") as f:
            f.write(f"{word_finnish} - {word_english}\n")
        print("Dictionary entry added")
    elif function == 2:
        search_term = input("Search term: ") 
        with open("dictionary.txt") as f:
            for line in f:
                parts = line.strip().split("-")
                if parts[0].find(search_term) != -1 or parts[1].find(search_term) != -1 :
                    print(line.strip())
    else:       
        print("Bye!")
        break
