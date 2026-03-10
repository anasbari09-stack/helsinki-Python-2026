# write your solution here
def read_fruits():
    with open("fruits.csv") as new_file:
        fruits_dic = {}
        for fruit in new_file:
            fruit = fruit.replace("\n", "")
            parts = fruit.split(";")
            key = parts[0]
            value = parts[1]
            fruits_dic[key] = float(value)
    return fruits_dic

if __name__ == "__main__":
    print(read_fruits())