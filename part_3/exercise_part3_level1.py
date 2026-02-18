string = input("Please type in a string: ")
substring = input("Please type in a substring: ")
index = 0
attemps = 0
while index  < len(string):
    if string[index:(index + len(substring))] == substring and (index + len(substring)) <= len(string):
        attemps += 1
    if attemps == 2:
        break
    if string[index:(index + len(substring))] == substring and (index + len(substring)) <= len(string):
        index += len(substring)
    else:
        index += 1
    
if attemps == 2:
    print(f"The second occurrence of the substring is at index {index}.")
else:
    print("The substring does not occur twice in the string.")



