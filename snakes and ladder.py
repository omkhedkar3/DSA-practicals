import tkinter as tk
import random

# Updated snake and ladder positions
snakes = {17: 7, 54: 34, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 99: 78}
ladders = {3: 22, 6: 25, 11: 49, 20: 59, 27: 84, 36: 44, 51: 67, 71: 91, 80: 100}

class SnakeLadderGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake and Ladder Game")
        self.canvas = tk.Canvas(root, width=480, height=480, bg="#f0e6d6")
        self.canvas.pack()

        self.player_names = ["Player 1", "Player 2"]
        self.player_turns = [0, 0]

        self.board = {}
        self.draw_board()
        self.draw_snakes_and_ladders()

        self.players = [0, 0]
        self.tokens = [self.canvas.create_oval(5, 430, 25, 450, fill="blue"),
                       self.canvas.create_oval(5, 400, 25, 420, fill="red")]

        self.turn = 0

        self.info = tk.Label(root, text="Player 1's Turn (Blue)", font=('Arial', 12))
        self.info.pack()

        self.roll_btn = tk.Button(root, text="🎲 Roll Dice", command=self.play_turn, font=('Arial', 12))
        self.roll_btn.pack()

        self.dice_label = tk.Label(root, text="", font=('Arial', 20))
        self.dice_label.pack(pady=10)

        self.restart_btn = tk.Button(root, text="🔄 Restart Game", command=self.restart_game)
        self.restart_btn.pack()

        self.name_frame = tk.Frame(root)
        self.name_frame.pack(pady=10)
        tk.Label(self.name_frame, text="Player 1 Name:").grid(row=0, column=0)
        self.name1_entry = tk.Entry(self.name_frame)
        self.name1_entry.grid(row=0, column=1)
        tk.Label(self.name_frame, text="Player 2 Name:").grid(row=1, column=0)
        self.name2_entry = tk.Entry(self.name_frame)
        self.name2_entry.grid(row=1, column=1)

        self.set_names_btn = tk.Button(self.name_frame, text="✅ Set Names", command=self.set_names)
        self.set_names_btn.grid(row=2, column=0, columnspan=2, pady=5)

    def set_names(self):
        name1 = self.name1_entry.get().strip()
        name2 = self.name2_entry.get().strip()
        if name1:
            self.player_names[0] = name1
        if name2:
            self.player_names[1] = name2
        self.update_info()

    def draw_board(self):
        size = 48
        num = 100
        for row in range(10):
            for col in range(10):
                x = col * size if row % 2 == 0 else (9 - col) * size
                y = row * size
                self.canvas.create_rectangle(x, y, x + size, y + size, fill="white", outline="black")
                self.canvas.create_text(x + size // 2, y + size // 2, text=str(num), font=("Arial", 8, "bold"))
                self.board[num] = (x + 4, y + 4)
                num -= 1

    def draw_snakes_and_ladders(self):
        for start, end in ladders.items():
            x1, y1 = self.get_center(start)
            x2, y2 = self.get_center(end)
            self.canvas.create_line(x1, y1, x2, y2, fill="green", width=3, arrow=tk.LAST)

        for start, end in snakes.items():
            x1, y1 = self.get_center(start)
            x2, y2 = self.get_center(end)
            self.canvas.create_line(x1, y1, x2, y2, fill="red", width=3, arrow=tk.LAST)

    def get_center(self, position):
        x, y = self.board[position]
        return (x + 8, y + 8)

    def get_coords(self, position):
        if position == 0:
            return (5, 430)
        return self.board[position]

    def move_token(self, player):
        x, y = self.get_coords(self.players[player])
        self.canvas.coords(self.tokens[player], x, y, x + 20, y + 20)

    def play_turn(self):
        dice = random.randint(1, 6)
        self.dice_label.config(text=f"🎲 {dice}")

        curr = self.players[self.turn]
        next_pos = curr + dice

        if next_pos > 100:
            next_pos = curr

        msg = f"{self.player_names[self.turn]} rolled a {dice}"

        if next_pos in snakes:
            msg += f"\n🐍 Snake from {next_pos} to {snakes[next_pos]}"
            next_pos = snakes[next_pos]
        elif next_pos in ladders:
            msg += f"\n🪜 Ladder from {next_pos} to {ladders[next_pos]}"
            next_pos = ladders[next_pos]

        self.players[self.turn] = next_pos
        self.player_turns[self.turn] += 1
        self.move_token(self.turn)

        if next_pos == 100:
            self.info.config(
                text=f"🏆 {self.player_names[self.turn]} wins in {self.player_turns[self.turn]} turns!"
            )
            self.roll_btn.config(state='disabled')
        else:
            self.turn = 1 - self.turn
            self.update_info(prefix=msg)

    def update_info(self, prefix=""):
        msg = f"{prefix}\n{self.player_names[self.turn]}'s Turn"
        self.info.config(text=msg)

    def restart_game(self):
        self.players = [0, 0]
        self.player_turns = [0, 0]
        for i in range(2):
            self.move_token(i)
        self.turn = 0
        self.dice_label.config(text="")
        self.info.config(text=f"{self.player_names[0]}'s Turn (Blue)")
        self.roll_btn.config(state='normal')

# Run the game
root = tk.Tk()
game = SnakeLadderGame(root)
root.mainloop()
