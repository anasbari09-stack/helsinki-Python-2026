

def run(program):
    print_list = []
    variables_dic = {chr(i): 0 for i in range(65, 91)}
    def print_programe(value):
        print_list.append(value)

    def mov_programe(variable , value):
        variables_dic[variable] = value
        return variables_dic
    def add_programe(variable , value):
        if variable in variables_dic:
            variables_dic[variable] += value
        else:
            variables_dic[variable] = value

    def sub_programe(variable , value):
        if variable in variables_dic:
            variables_dic[variable] -= value
        else:
            variables_dic[variable] = -(value)

    def mul_programe(variable , value):
        if variable in variables_dic:
            variables_dic[variable] *= value
        else:
            variables_dic[variable] = 0    
    
    locations = {}
    
    for index, line in enumerate(program):
        if ":" in line:
            # "begin:" -> "begin"
            label_name = line.strip().split(":")[0]
            locations[label_name] = index
    i = 0
    while i < len(program):
        parts = program[i].strip().split(" ")
        if parts[0] == "PRINT":
            if parts[1] not in variables_dic:
                print_programe(int(parts[1]))
            else:
                print_programe(variables_dic[parts[1]])
        elif parts[0] == "MOV":
            if parts[2] not in variables_dic:
                mov_programe(parts[1] , int(parts[2]))
            else:
                mov_programe(parts[1] , variables_dic[parts[2]])
        elif parts[0] == "ADD":
            if parts[2] not in variables_dic:
                add_programe(parts[1] , int(parts[2]))
            else:
                add_programe(parts[1] , variables_dic[parts[2]])
        elif parts[0] == "SUB":
            if parts[2] not in variables_dic:
                sub_programe(parts[1] , int(parts[2]))
            else:
                sub_programe(parts[1] , variables_dic[parts[2]])
        elif parts[0] == "MUL":
            if parts[2] not in variables_dic:
                mul_programe(parts[1] , int(parts[2]))
            else:
                mul_programe(parts[1] , variables_dic[parts[2]])

        elif parts[0] == "JUMP":
            i = locations[parts[1]]
            continue

        elif parts[0] == "IF":
            if parts[3] in variables_dic:
                if parts[2] == ">":
                    if variables_dic[parts[1]] > variables_dic[parts[3]]:
                        i = locations[parts[5]]
                        continue
                elif parts[2] == ">=":
                    if variables_dic[parts[1]] >= variables_dic[parts[3]]:
                        i = locations[parts[5]]
                        continue
                elif parts[2] == "<":
                    if variables_dic[parts[1]] < variables_dic[parts[3]]:
                        i = locations[parts[5]]
                        continue
                elif parts[2] == "<=":
                    if variables_dic[parts[1]] <= variables_dic[parts[3]]:
                        i = locations[parts[5]]
                        continue 
                elif parts[2] == "==":
                    if variables_dic[parts[1]] == variables_dic[parts[3]]:
                        i = locations[parts[5]]
                        continue 
                elif parts[2] == "!=":
                    if variables_dic[parts[1]] != variables_dic[parts[3]]:
                        i = locations[parts[5]]
                        continue 
            else:
                if parts[2] == ">":
                    if variables_dic[parts[1]] > int(parts[3]):
                        i = locations[parts[5]] 
                        continue
                elif parts[2] == ">=":
                    if variables_dic[parts[1]] >= int(parts[3]):
                        i = locations[parts[5]] 
                        continue
                elif parts[2] == "<":
                    if variables_dic[parts[1]] < int(parts[3]):
                        i = locations[parts[5]] 
                        continue
                elif parts[2] == "<=":
                    if variables_dic[parts[1]] <= int(parts[3]):
                        i = locations[parts[5]]
                        continue
                elif parts[2] == "==":
                    if variables_dic[parts[1]] == int(parts[3]):
                        i = locations[parts[5]] 
                        continue
                elif parts[2] == "!=":
                    if variables_dic[parts[1]] != int(parts[3]):
                        i = locations[parts[5]] 
                        continue
        elif parts[0] == "END":
            break
        i += 1
    return print_list

        

if __name__ == "__main__":
    program2 = []
    program2.append("MOV A 1")
    program2.append("MOV B 10")
    program2.append("begin:")
    program2.append("IF A >= B JUMP quit")
    program2.append("PRINT A")
    program2.append("PRINT B")
    program2.append("ADD A 1")
    program2.append("SUB B 1")
    program2.append("JUMP begin")
    program2.append("quit:")
    program2.append("END")
    result = run(program2)
    print(result)
        
