import random
import os

os.system("cls")

RED = "\033[91m"
BLUE = "\033[94m"
RESET = "\033[0m"
CYAN = "\033[96m"
BOLD = "\033[1m"

board = [" "]*9

def colored(cell):
    if cell == "X":
        return "  " + BLUE + "X" + RESET + "  "
    elif cell == "O":
        return "  " + RED + "O" + RESET + "  "
    else:
        return "     "       

def print_board():
  h = "\u2500"*5
  PAD = "        "
  print(f"{CYAN}{BOLD}")
  print(f"{PAD}\u250C{h}\u252C{h}\u252C{h}\u2510")
  print(f"{PAD}\u2502{colored(board[0])}\u2502{colored(board[1])}\u2502{colored(board[2])}\u2502")
  print(f"{PAD}\u251C{h}\u253C{h}\u253C{h}\u2524")
  print(f"{PAD}\u2502{colored(board[3])}\u2502{colored(board[4])}\u2502{colored(board[5])}\u2502")
  print(f"{PAD}\u251C{h}\u253C{h}\u253C{h}\u2524")
  print(f"{PAD}\u2502{colored(board[6])}\u2502{colored(board[7])}\u2502{colored(board[8])}\u2502")
  print(f"{PAD}\u2514{h}\u2534{h}\u2534{h}\u2518")
  print(f"{CYAN}{BOLD}")
  print(RESET)
   
def make_move(position, player):
    if board[position]==" ":
        board[position] = player
        return True
    else:
        print("That spot is taken, try again.")
        return False

def check_winner():
    wins =[(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    for a,b,c in wins:
        if board[a]!=" " and board[a]==board[b]==board[c]:
            return board[a]
    if" "not in board:
        return "Draw"
    return None    

def minimax(is_maximizing):
    winner=check_winner()
    if winner=="O":
        return 1
    if winner == "X":
        return-1
    if winner=="Draw":
        return 0
    scores = []
    for i in range(9):
      if board[i]==" ":
        board[i]="O" if is_maximizing else "X"
        scores.append(minimax(not is_maximizing))
        board[i]=" "
    return max(scores) if is_maximizing else min(scores)

def ai_move_minimax():
    best_score = -float("inf")
    best_move = None
    for i in range(9):
        if board[i]==" ":
            board[i]="O"
            score = minimax(False)
            board[i]=" "
            if score > best_score:
                best_score=score
                best_move=i
    return best_move

current_player = "X"

print("1)Player vs Player \n2)Player vs AI")
mode = input("Choose mode: ")

while True:
    print_board()
    if current_player == "X":
        position = int(input(f"Player {current_player},choose a position(0-8): "))
    elif mode == "1":
        position = int(input(f"Player {current_player},choose a position(0-8): "))
    else:
        position = ai_move_minimax()
        print(f"AI chooses position {position}")
    if make_move(position, current_player):
        winner=check_winner()
        if winner:
            print_board()
            if winner=="Draw":
                print("It's a draw!")
            else:
                print(f"Player {winner} wins!")
            break
        current_player= "O" if current_player=="X" else "X"

