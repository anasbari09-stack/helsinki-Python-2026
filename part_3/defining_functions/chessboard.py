# write a function named chessboard, which prints out a chessboard made out of ones and zeroes.
#  The function takes an integer argument, which specifies the length of the side of the board. 
def chessboard(repeat_time):
    i = 0
    switch = 0
    while i < repeat_time:
        r = 0 
        if switch == 0:
            pr = 0
            while r < repeat_time:
                if pr == 0:
                    print(1,end="")
                    pr = 1
                else:
                    print(0,end="")
                    pr = 0
                r += 1
            switch = 1
            print()
        else:
            pr = 1
            while r < repeat_time:
                if pr == 0:
                    print(1,end="")
                    pr = 1
                else:
                    print(0,end="")
                    pr = 0
                r += 1
            switch = 0
            print()
        i+= 1

        


# Testing the function
if __name__ == "__main__":
    chessboard(3)
