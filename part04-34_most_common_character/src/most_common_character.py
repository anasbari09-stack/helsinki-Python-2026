def most_common_character(string):
    big_count = 0
    big_char = ""
    for i in string:
        if string.count(i) > big_count:
            big_count = string.count(i)
            big_char = i
        elif string.count(i) == big_count:
            if string.find(i) < string.find(big_char):
                big_char = i
    return big_char

if __name__ == "__main__":
    first_string = "abcdbde"
    print(most_common_character(first_string))
    
    second_string = "exemplaryelementary"
    print(most_common_character(second_string))
