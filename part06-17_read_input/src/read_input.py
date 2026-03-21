# Write your solution here
def read_input(sentence: str, nb1:int, nb2: int):
    while True:
        try:
            input_nb = input(sentence)
            nb = int(input_nb)
            if nb2 > nb > nb1:
                return nb
        except ValueError:
            pass
        print(f"You must type in an integer between {nb1} and {nb2}")

if __name__ == "__main__":
    number = read_input('Enter a number', 1, 5)
    print("You typed in:", number)


