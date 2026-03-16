while True:
    print("1 - add an entry, 2 - read entries, 0 - quit")
    function = int(input("Function: "))
    if function == 0:
        print("Bye now!")
        break
    elif function == 1:
        diary_entry = input("Diary entry: ")
        with open("diary.txt", "a") as f:
            f.write(f"{diary_entry}\n")
            print("Diary saved")
    else:
        print("Entries:")
        with open("diary.txt") as f:
            for line in f:
                line = line.strip()
                print(line)