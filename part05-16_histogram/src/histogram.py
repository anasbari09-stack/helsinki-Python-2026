def histogram(string):
    histogram_dic = {}
    for s in string:
        if s not in histogram_dic:
            histogram_dic[s] = 0
        histogram_dic[s] += 1
    for key, value in histogram_dic.items():
        print(f"{key} {"*" * value}")

if __name__ == "__main__":
    histogram("statistically")