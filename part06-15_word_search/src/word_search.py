def find_words(search_term: str):
    list_words = []
    with open("words.txt") as f:
        for line in f:
            line = line.strip()
            if search_term.startswith("*") == True:
                if line.endswith(search_term[1:]) == True:
                    list_words.append(line)
            elif search_term.endswith("*") == True:
                if line.startswith(search_term[0:-1]) == True:
                    list_words.append(line)
            elif "." in search_term:
                if len(search_term) == len(line):
                    valid = True
                    for i in range(len(search_term)):
                        if search_term[i] != ".":
                            if search_term[i] != line[i]:
                                valid = False
                    if valid == True:
                        list_words.append(line)
            elif line == search_term:
                list_words.append(line)
        return list_words

if __name__ == "__main__":
    print(find_words("cat"))


