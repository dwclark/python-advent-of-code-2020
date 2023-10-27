plays = [2,20,0,4,1,17]

def speak(board, num, turn):
    prev = board.get(num, -1)
    board[num] = turn
    return (turn - prev) if prev != -1 else 0

def new_board():
    board = {}
    for i, play in enumerate(plays):
        speak(board, play, i)
    return board

def play(max_turns):
    board = new_board()
    prev = 0
    for turn in range(len(plays), (max_turns-1)):
        prev = speak(board, prev, turn)
    return prev

print("Part 1:", play(2020))
print("Part 2:", play(30000000))
