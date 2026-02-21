# Please write a function named print_many_times(text, times), which takes a string and an integer as arguments. The integer argument specifies how many times the string argument should be printed out:

def print_many_times(text, times):
    i=1
    while i <= times:
        print(text)
        i+=1



if __name__ == "__main__":
    print_many_times("python", 5)