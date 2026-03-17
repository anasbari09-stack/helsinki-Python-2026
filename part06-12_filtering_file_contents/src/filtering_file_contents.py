# Write your solution here
def filter_solutions():
    with open("correct.csv", "w") as f:
        pass
    with open("incorrect.csv", "w") as f:
        pass
    with open("solutions.csv") as f:
        for line in f:
            parts = line.strip().split(";")
            operation = parts[1]
            operation.find("-")
            operation.find("+")

            if operation.find("+") > operation.find("-"):
                find = operation.find("+")
                result = int(operation[0:find]) + int(operation[find+1:])
            else:
                find = operation.find("-")
                result = int(operation[0:find]) - int(operation[find+1:])

            if result == int(parts[2]):
                
                with open("correct.csv", "a") as f:
                    f.write(line)
            else:
               
                with open("incorrect.csv", "a") as f:
                    f.write(line)
            

            


if __name__ == "__main__":
    filter_solutions()