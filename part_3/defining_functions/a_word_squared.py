# Write your solution here
def squared(text, repeat_time):
    i = 0
    index = 0
    while i < repeat_time:
        r = 0
        while r < repeat_time:
            if index >= len(text):
                index = 0
            print(text[index],end = "")
            index += 1
            r += 1
        print()
        i += 1
if __name__ == "__main__" :
    squared("ab", 3)
    print()
    squared("aybabtu", 5)
