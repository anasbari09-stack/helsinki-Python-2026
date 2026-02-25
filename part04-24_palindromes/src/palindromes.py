# Write your solution here
# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!
def palindromes(word):
    palindrome = ""
    for i in range(-1, -len(word) -1, -1):
        palindrome += word[i]
    if word == palindrome:
        return True
    else :
        return False
    


while True:
    word = input("Please type in a palindrome: ")
    if palindromes(word) is True :
        print(f"{word} is a palindrome!")
        break
    else:
        print("that wasn't a palindrome")
    
