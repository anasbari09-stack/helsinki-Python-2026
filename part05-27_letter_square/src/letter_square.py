# Write your solution here
letteres_dic = {1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6:"F", 7: "G", 8: "H", 9:"I", 10: "J", 11: "K", 12: "L", 13: "M", 14: "N", 15: "O", 16: "P", 17: "Q", 18: "R", 19: "S", 20: "T", 21: "U", 22: "V", 23: "W", 24: "X", 25: "Y", 26: "Z"}
layer = int(input("Layers:"))
repetition = layer * 2 - 1
list_ligne = []
lettre = layer
for i in range(repetition):
    list_ligne.append(letteres_dic[layer])

s = 0
f = repetition
switch = repetition // 2 
for i in range(repetition):
    for d in range(s , f):
        list_ligne[d] = letteres_dic[lettre]
    for r in range(0, repetition):
        print(list_ligne[r], end="")
    print()
    if i < switch:
        s += 1
        f -= 1
        lettre -= 1
    else:
        s -= 1
        f += 1
        lettre += 1

