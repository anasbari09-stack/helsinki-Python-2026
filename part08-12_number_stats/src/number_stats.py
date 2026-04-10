# Write your solution here!
class  NumberStats:
    def __init__(self):
        self.numbers = 0
        self.counter = 0

    def add_number(self, number:int):
        self.numbers += number
        self.counter += 1

    def count_numbers(self):
        return self.counter

    def get_sum(self):
        return self.numbers
    
    def average(self):
        if self.counter == 0:
            return 0
        return self.numbers / self.counter

print("Please type in integer numbers:")
stats  = NumberStats()
even_stats = NumberStats()
odd_stats = NumberStats()
while True:
    nb = input("")
    if int(nb) == -1:
        break
    stats.add_number(int(nb))

    if int(nb) % 2 == 0:
        even_stats.add_number(int(nb))
    else:
        odd_stats.add_number(int(nb))


print(f"Sum of numbers: {stats.get_sum()}")
print(f"Mean of numbers: {stats.average()}")
print(f"Sum of even numbers: {even_stats.get_sum()}")
print(f"Sum of odd numbers: {odd_stats.get_sum()}")

    

