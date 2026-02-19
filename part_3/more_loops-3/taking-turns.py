number = int(input("Please type in a number: "))
nb = 1
nb2 = number
attemps = 0
while True:
    print(nb)
    attemps += 1
    if attemps >= number:
        break
    print(nb2)
    attemps += 1
    if attemps >= number:
        break
    
    nb += 1
    nb2 -= 1
    