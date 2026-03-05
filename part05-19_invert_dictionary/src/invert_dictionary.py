# Write your solution here
def invert(dictionary: dict):
    new_dic = {}
    key_list = []
    values_list = []
    for key, value in dictionary.items():
        key_list.append(value)
        values_list.append(key)
    dictionary.clear()
    for i in range(0, len(values_list)):
        dictionary[key_list[i]] = values_list[i]
    

if __name__ == "__main__":
    s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
    invert(s)
    print(s)