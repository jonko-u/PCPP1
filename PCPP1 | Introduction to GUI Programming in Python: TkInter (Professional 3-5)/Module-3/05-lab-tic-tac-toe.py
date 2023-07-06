"""
Level of difficulty

Hard
Objectives

Learn practical skills related to:

    dealing with the grid geometry manager,
    defining and using callbacks,
    identifying and servicing GUI events.

Scenario

Write a simple GUI program which pretends to play tic-tac-toe with the user. Don't be afraid, we don't want you to implement artificial intelligence algorithms. You can do it, if you want, but we prefer to concentrate on the user interface issues. If you really want to create an actual competitor, do it on your own.

This is what the game you are about to write looks like (the beginning and sample end of the game):

ttt-start

ttt-finish

To make your task a bit easier, let's simplify the game a bit. Here are our assumptions:.

    the computer (i.e., your program) plays 'X', and Xes are always red,
    the user (e.g., you) plays 'O', and Os are always green,
    the board consists of 9 tiles, and the tile role is played by a button,
    the first move belongs to the computer - it always puts its first 'X' in the middle of the board,
    the user enters her/his move by clicking the chosen tile (clicking the tiles which are not free is ineffective)
    the program checks if the game over conditions are met, and if the game is over, a message box is displayed announcing the winner,
    otherwise the computer responds with its move and the check is repeated,
    use random to generate the computer's moves.

"""
import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")
        self.board = [None] * 9
        self.create_widgets()
        self.game_over = False
        self.computer_move()

    def create_widgets(self):
        self.buttons = []
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.master, width=10, height=5, command=lambda row=i, col=j: self.handle_click(row, col))
                button.grid(row=i, column=j)
                self.buttons.append(button)

    def handle_click(self, row, col):
        if not self.game_over and self.board[row * 3 + col] is None:
            self.board[row * 3 + col] = 'O'
            self.buttons[row * 3 + col]["text"] = 'O'
            self.buttons[row * 3 + col]["bg"] = 'light green'
            if self.check_game_over():
                return
            self.computer_move()

    def computer_move(self):
        if not self.game_over:
            while True:
                index = random.randint(0, 8)
                if self.board[index] is None:
                    self.board[index] = 'X'
                    self.buttons[index]["text"] = 'X'
                    self.buttons[index]["bg"] = 'red'
                    if self.check_game_over():
                        return
                    break

    def check_game_over(self):
        for i in range(3):
            if self.board[i * 3] is not None and self.board[i * 3] == self.board[i * 3 + 1] == self.board[i * 3 + 2]:
                self.show_winner(self.board[i * 3])
                return True
            if self.board[i] is not None and self.board[i] == self.board[i + 3] == self.board[i + 6]:
                self.show_winner(self.board[i])
                return True
        if self.board[0] is not None and self.board[0] == self.board[4] == self.board[8]:
            self.show_winner(self.board[0])
            return True
        if self.board[2] is not None and self.board[2] == self.board[4] == self.board[6]:
            self.show_winner(self.board[2])
            return True
        if all(tile is not None for tile in self.board):
            self.show_winner(None)
            return True
        return False

    def show_winner(self, winner):
        self.game_over = True
        if winner is None:
            messagebox.showinfo("Game Over", "It's a tie!")
        elif winner == 'O':
            messagebox.showinfo("Game Over", "You win!")
        else:
            messagebox.showinfo("Game Over", "You lose!")

root = tk.Tk()
game = TicTacToe(root)
root.mainloop()