number = 1
while True:
    number = int(input("Please type in a number: "))
    if number <= 0:
        break
    nb = 1
    factorial = 1
    while nb <= number:
        factorial *= nb
        nb += 1
    
    print(f"The factorial of the number {number} is {factorial}")

print("Thanks and bye!")