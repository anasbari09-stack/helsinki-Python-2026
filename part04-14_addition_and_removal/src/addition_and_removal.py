# Write your solution here
numbers = []
while True:
    print(f"The list is now {numbers}")
    choise = input("a(d)d, (r)emove or e(x)it: ")
    if choise == "d":
        if numbers == []:
            numbers.append(1)
        else:
            numbers.append(numbers[-1] + 1)

    elif choise == "r" and numbers != []:
        numbers.pop(-1)
    elif choise == "x":
        print("Bye!")
        break