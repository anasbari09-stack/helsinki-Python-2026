# Write your solution here
numbers = []
items = int(input("How many items: "))
i = 1
while i <= items:
    item = int(input(f"Item {i}: "))
    numbers.append(item)
    i += 1
print(numbers)

