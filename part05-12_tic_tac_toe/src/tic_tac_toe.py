# Write your solution here
def play_turn(game_board: list, x: int, y: int, piece: str):
    if 0 > y or y > 2 or  0 > x or x > 2 :
        return False
    
    row = game_board[y]
    if row[x] != "":
        return False 
    else:
        row = game_board[y]
        row[x] = piece
        return True
    
    
if __name__ == "__main__":
    game_board = [["", "", ""], ["", "", ""], ["", "", ""]]
    print(play_turn(game_board, 1, 0, "O"))
    print(play_turn(game_board, 0, 1, "O"))
    print(play_turn(game_board, 0, 2, "X"))
    print(play_turn(game_board, 3, 3, "O"))
    print(game_board)
