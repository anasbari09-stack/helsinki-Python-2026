# Write your solution here
# You can test your function by calling it within the following block
def spruce(number):
    print("a spruce!")
    space = (number -1)
    space2 = (number -1)
    nb_char = 1
    while space >= 0:
        print(f"{" " * space}{nb_char * "*"}")
        space -= 1
        nb_char += 2
    print(f"{" " * space2}*")
if __name__ == "__main__":
    spruce(5)