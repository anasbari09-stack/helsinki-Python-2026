# Write your solution here
from random import choice

def roll(die: str):
    if die == "A":
        return choice([3, 3, 3, 3, 3, 6])
    elif die == "B":
        return choice([2, 2, 2, 5, 5, 5])
    elif die == "C":
        return choice([1, 4, 4, 4, 4, 4])

def play(die1: str, die2: str, times: int):
    die1_wins = 0
    die2_wins = 0
    ties = 0.
    for i in range(times):
        d1 = roll(die1)
        d2 = roll(die2)
        if d1 > d2:
            die1_wins += 1
        elif d2 > d1:
            die2_wins += 1
        else:
            ties += 1

    return (die1_wins, die2_wins, ties)

if __name__ ==  "__main__":
    result = play("A", "C", 1000)
    print(result)
    result = play("B", "B", 1000)
    print(result)