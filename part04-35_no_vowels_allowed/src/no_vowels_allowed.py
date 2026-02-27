# Write your solution here
def no_vowels(string):
    new_string = ""
    voels = "aeiou"
    for char in string:
        if char not in voels:
            new_string += char
    return new_string

if __name__ == "__main__":
    my_string = "this is an example"
    print(no_vowels(my_string))