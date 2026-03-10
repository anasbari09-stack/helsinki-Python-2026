# write your solution here
def largest():
    with open("numbers.txt") as new_file:
        return int(max(new_file))

if __name__ == "__main__":
    print(largest())