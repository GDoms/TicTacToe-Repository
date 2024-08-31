import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk


class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.current_player = "X"
        self.buttons = []
        self.create_widgets()

    def create_widgets(self):
        frame = tk.Frame(self.root, bg="lightgray")
        frame.grid(row=0, column=0, padx=10, pady=10)

        # Load and resize images
        self.x_image = self.load_image("images/x.png")
        self.o_image = self.load_image("images/o.png")
        self.empty_image = self.load_image("images/empty.png")

        for row in range(3):
            button_row = []
            for col in range(3):
                button = tk.Button(frame, image=self.empty_image, command=lambda r=row, c=col: self.button_click(r, c))
                button.grid(row=row, column=col, padx=5, pady=5)
                button_row.append(button)
            self.buttons.append(button_row)

        # Add Restart button
        restart_button = tk.Button(self.root, text="Restart", command=self.reset_game)
        restart_button.grid(row=1, column=0, pady=10)

    def load_image(self, path, size=(100, 100)):
        """Load an image file and resize it."""
        try:
            image = Image.open(path)
            image = image.resize(size, Image.LANCZOS)  # Use LANCZOS for high-quality downsampling
            return ImageTk.PhotoImage(image)
        except Exception as e:
            print(f"Error loading image {path}: {e}")
            return None

    def button_click(self, row, col):
        button = self.buttons[row][col]
        if button.cget("image") == str(self.empty_image) and not self.check_winner():
            button.config(image=self.x_image if self.current_player == "X" else self.o_image)
            if self.check_winner():
                messagebox.showinfo("Tic Tac Toe", f"Player {self.current_player} wins!")
            elif self.check_tie():
                messagebox.showinfo("Tic Tac Toe", "It's a tie!")
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        winning_combinations = [
            [(0, 0), (0, 1), (0, 2)], [(1, 0), (1, 1), (1, 2)], [(2, 0), (2, 1), (2, 2)],  # Rows
            [(0, 0), (1, 0), (2, 0)], [(0, 1), (1, 1), (2, 1)], [(0, 2), (1, 2), (2, 2)],  # Columns
            [(0, 0), (1, 1), (2, 2)], [(2, 0), (1, 1), (0, 2)]  # Diagonals
        ]

        for combo in winning_combinations:
            if all(self.buttons[r][c].cget("image") == str(self.x_image) for r, c in combo) or \
                    all(self.buttons[r][c].cget("image") == str(self.o_image) for r, c in combo):
                return True
        return False

    def check_tie(self):
        return all(
            self.buttons[row][col].cget("image") != str(self.empty_image) for row in range(3) for col in range(3))

    def reset_game(self):
        """Reset the game to its initial state."""
        self.current_player = "X"
        for row in range(3):
            for col in range(3):
                button = self.buttons[row][col]
                button.config(image=self.empty_image)


if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToe(root)
    root.mainloop()
