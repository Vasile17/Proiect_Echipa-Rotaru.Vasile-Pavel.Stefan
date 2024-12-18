import tkinter as tk
import random

ROW = 5
COL = 5
MINES = 5

class Minesweeper:
    def __init__(self, master):
        self.master = master
        self.master.title("Minesweeper")
        self.refresh_button = None
        self.new_game()

    def new_game(self):
        """Initialize a new game"""
        self.board = self.initialize_board()
        self.buttons = {}
        self.revealed = [[False for _ in range(COL)] for _ in range(ROW)]
        self.game_over = False

        self.create_buttons()
        self.place_mines()
        self.calculate_numbers()

        if self.refresh_button:
            self.refresh_button.grid_forget()

    def initialize_board(self):
        return [[' ' for _ in range(COL)] for _ in range(ROW)]

    def place_mines(self):
        mines_placed = 0
        while mines_placed < MINES:
            row = random.randint(0, ROW - 1)
            col = random.randint(0, COL - 1)
            if self.board[row][col] != '*':
                self.board[row][col] = '*'
                mines_placed += 1

    def calculate_numbers(self):
        for row in range(ROW):
            for col in range(COL):
                if self.board[row][col] == '*':
                    continue
                mine_count = 0
                for r in range(row - 1, row + 2):
                    for c in range(col - 1, col + 2):
                        if 0 <= r < ROW and 0 <= c < COL and self.board[r][c] == '*':
                            mine_count += 1
                if mine_count > 0:
                    self.board[row][col] = str(mine_count)

    def create_buttons(self):
        for row in range(ROW):
            for col in range(COL):
                button = tk.Button(self.master, text=' ', width=4, height=2,
                                   command=lambda r=row, c=col: self.reveal_cell(r, c))
                button.grid(row=row, column=col)
                self.buttons[(row, col)] = button

    def reveal_cell(self, row, col):
        if self.game_over or self.revealed[row][col]:
            return
        self.revealed[row][col] = True

        if self.board[row][col] == '*':
            self.buttons[(row, col)].config(text='*', bg='red')
            self.game_over = True
            self.show_game_over_message("You lost, silly otter!")
            self.show_refresh_button()  # Show the "New game awaits" button
            return

        self.buttons[(row, col)].config(text=self.board[row][col], bg='lightgray')
        if self.board[row][col] == ' ':
            for r in range(row - 1, row + 2):
                for c in range(col - 1, col + 2):
                    if 0 <= r < ROW and 0 <= c < COL and not self.revealed[r][c]:
                        self.reveal_cell(r, c)

        if self.check_win():
            self.game_over = True
            self.show_game_over_message("Congratulations, silly otter! You won!")
            self.show_refresh_button()

    def show_game_over_message(self, message):
        message_label = tk.Label(self.master, text=message, font=("Arial", 16))
        message_label.grid(row=ROW, column=0, columnspan=COL)

    def check_win(self):
        for row in range(ROW):
            for col in range(COL):
                if self.board[row][col] != '*' and not self.revealed[row][col]:
                    return False
        return True

    def show_refresh_button(self):
        # If the button is already created, we won't create it again
        if not self.refresh_button:
            self.refresh_button = tk.Button(
                self.master, 
                text="New game awaits", 
                command=self.new_game, 
                width=20, 
                height=2, 
                font=("Arial", 14, "bold"), 
                bg="#4CAF50",   # Green background
                fg="white",     # White text
                relief="raised",  # Raised effect
                bd=5,            # Border width
                activebackground="#45a049",  # Darker green when clicked
                activeforeground="white"    # White text on click
            )
            self.refresh_button.grid(row=ROW + 1, column=0, columnspan=COL, pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    game = Minesweeper(root)
    root.mainloop()