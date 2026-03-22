# Write your solution here
def filter_incorrect():
    with open("lottery_numbers.csv") as f, \
     open("correct_numbers.csv", "w") as cf:
        
        for line in f:
            parts = line.strip().split(";")
            part1 = parts[0].split(" ")
            part2 = parts[1].split(",")
            try:
                part1 = int(part1[1])
                numbers = []
                error_nb = False
                for n in part2:
                    n = int(n)
                    if n > 39 or n < 1 or n in numbers:
                        error_nb = True
                    numbers.append(n)
                if error_nb  or len(numbers) != 7:
                    continue
                with open("correct_numbers.csv", "a") as nf:
                    nf.write(line)
            except:
                continue