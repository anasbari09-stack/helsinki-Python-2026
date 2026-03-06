# Write your solution here
def dict_of_numbers():
    numbers_dic = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5:"five", 6: "six", 7: "seven", 8: "eight", 9: "nine" , 10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17:"seventeen", 18: "eighteen", 19: "nineteen", 20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90:"ninety"}
    for i in range(21, 100):
        
        if i not in numbers_dic:
            string_index = str(i)
            right_number = int(string_index[1])
            if i < 30:
                numbers_dic[i] = f"{numbers_dic[20]}-{numbers_dic[right_number]}"
            elif i < 40:
                numbers_dic[i] = f"{numbers_dic[30]}-{numbers_dic[right_number]}"
            elif i < 50:
                numbers_dic[i] = f"{numbers_dic[40]}-{numbers_dic[right_number]}"
            elif i < 60:
                numbers_dic[i] = f"{numbers_dic[50]}-{numbers_dic[right_number]}"
            elif i < 70:
                numbers_dic[i] = f"{numbers_dic[60]}-{numbers_dic[right_number]}"
            elif i < 80:
                numbers_dic[i] = f"{numbers_dic[70]}-{numbers_dic[right_number]}"
            elif i < 90:
                numbers_dic[i] = f"{numbers_dic[80]}-{numbers_dic[right_number]}"
            elif i < 100:
                numbers_dic[i] = f"{numbers_dic[90]}-{numbers_dic[right_number]}"
    return numbers_dic
if __name__ == "__main__":
    print(dict_of_numbers())
        
