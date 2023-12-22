import tkinter as tk
import copy
from PIL import Image, ImageTk

def check_winner(board, player):
    for i in range(3):
        if all([cell == player for cell in board[i]]):  # Check rows
            return True
        if all([board[j][i] == player for j in range(3)]):  # Check columns
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):  # Check diagonals
        return True
    return False

def get_empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]

def minimax(board, depth, maximizing_player):
    if check_winner(board, 'X'):
        return -10 + depth
    elif check_winner(board, 'O'):
        return 10 - depth
    elif not get_empty_cells(board):
        return 0

    if maximizing_player:
        max_eval = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = 'O'
                    eval = minimax(board, depth + 1, False)
                    board[i][j] = " "
                    max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = 'X'
                    eval = minimax(board, depth + 1, True)
                    board[i][j] = " "
                    min_eval = min(min_eval, eval)
        return min_eval

def best_move(board):
    best_eval = float('-inf')
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = 'O'
                eval = minimax(board, 0, False)
                board[i][j] = " "
                if eval > best_eval:
                    best_eval = eval
                    best_move = (i, j)
    return best_move

def make_move(row, col):
    global current_player, board, game_over

    if board[row][col] == " " and not game_over:
        board[row][col] = 'X'
        buttons[row][col].config(image=img_x, state=tk.DISABLED,width=68,height=80)
        if check_winner(board, 'X'):
            result_label.config(text="You win!")
            game_over = True
        elif not get_empty_cells(board):
            result_label.config(text="It's a tie!")
            game_over = True
        else:
            current_player = 'O'
            row, col = best_move(board)
            board[row][col] = 'O'
            buttons[row][col].config(image=img_o, state=tk.DISABLED,width=68,height=80)
            if check_winner(board, 'O'):
                result_label.config(text="Computer wins!")
                game_over = True
            elif not get_empty_cells(board):
                result_label.config(text="It's a tie!")
                game_over = True

# def restart_game():
#     global board, current_player, game_over
#     board = [[" " for _ in range(3)] for _ in range(3)]
#     current_player = 'X'
#     game_over = False
#     for i in range(3):
#         for j in range(3):
#             buttons[i][j].config(image="", state=tk.NORMAL)
       
#     result_label.config(text="")
def initialize_images():
    global img_x, img_o
    # Load your 'X' and 'O' images here
    # Example: Replace 'path_to_x_image.png' and 'path_to_o_image.png' with the actual paths of your images
    img_x = tk.PhotoImage(file='totex.png')
    # img_x=Image.open("totex.png").resize((30,30))
    img_o = tk.PhotoImage(file='odesign.png')
import tkinter as tk
import copy
from PIL import Image, ImageTk

def main():
    global root, img_x, img_o, board, current_player, game_over, buttons, result_label

    root = tk.Tk()
    root.title("Tic Tac Toe")

    initialize_images()  # Load X and O images

    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    game_over = False

    buttons = [[0 for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            buttons[i][j] = tk.Button(root, text=" ", font=('Arial', 20), width=4, height=2,
                                       command=lambda row=i, col=j: make_move(row, col))
            buttons[i][j].grid(row=i, column=j)

    result_label = tk.Label(root, text="", font=('Arial', 16))
    result_label.grid(row=3, columnspan=3)

    restart_button = tk.Button(root, text="Restart", font=('Arial', 14), command=restart)  # Solution 2
    restart_button.grid(row=4, columnspan=3)

    root.mainloop()

# ... (rest of your functions, such as check_winner, minimax, best_move, make_move, and initialize_images) ...

def restart_game():
    global board, current_player, game_over
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    game_over = False

    # Choose either Solution 1 or Solution 2:

    # ### Solution 1: Reset Window Size ###
    # root.geometry("300x400")  # Adjust dimensions as needed

    # ### Solution 2: Destroy and Recreate Window ###
    # root.destroy()
    # main()

    for i in range(3):
        for j in range(3):
            buttons[i][j].config(image="", state=tk.NORMAL)

    result_label.config(text="")

def restart():
    root.destroy()
    main()

if __name__ == "__main__":
    main()




