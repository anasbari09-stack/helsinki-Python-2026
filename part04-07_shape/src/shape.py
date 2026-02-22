# Copy here code of line function from previous exercise and use it in your solution
# You can test your function by calling it within the following block
def line(number, string):
    if string == "":
        print("*" * number)
    else:
        print(string[0] * number)
if __name__ == "__main__":
    line(5, "xxx")

def shape(width, char, height, char2):
    i = 1
    while i <= width:
        line(i, char)
        i += 1
    while height > 0:
        line(width, char2)
        height -= 1


    

if __name__ == "__main__":
    shape(5, "x", 2, "o")