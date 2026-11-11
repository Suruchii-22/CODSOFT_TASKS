"""Task 2 GUI: Interactive Tic-Tac-Toe using Tkinter and Minimax with Alpha-Beta Pruning."""
import tkinter as tk
from tkinter import messagebox
import math

WINS = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
AI, HUMAN = "O", "X"


def winner(b):
    for a, c, d in WINS:
        if b[a] != " " and b[a] == b[c] == b[d]:
            return b[a]
    return None


def minimax(b, is_ai, alpha, beta, depth):
    w = winner(b)
    if w == AI:
        return 10 - depth
    if w == HUMAN:
        return depth - 10
    if " " not in b:
        return 0

    if is_ai:
        best = -math.inf
        for i in range(9):
            if b[i] == " ":
                b[i] = AI
                score = minimax(b, False, alpha, beta, depth + 1)
                b[i] = " "
                best = max(best, score)
                alpha = max(alpha, best)
                if beta <= alpha:
                    break
        return best
    else:
        best = math.inf
        for i in range(9):
            if b[i] == " ":
                b[i] = HUMAN
                score = minimax(b, True, alpha, beta, depth + 1)
                b[i] = " "
                best = min(best, score)
                beta = min(beta, best)
                if beta <= alpha:
                    break
        return best


def best_move(b):
    best, move = -math.inf, None
    for i in range(9):
        if b[i] == " ":
            b[i] = AI
            score = minimax(b, False, -math.inf, math.inf, 1)
            b[i] = " "
            if score > best:
                best, move = score, i
    return move


class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("CodSoft AI - Tic-Tac-Toe (Unbeatable)")
        self.root.resizable(False, False)
        self.root.configure(bg="#1e1e2e")

        self.board = [" "] * 9
        self.human_score = 0
        self.ai_score = 0
        self.draw_score = 0
        self.game_over = False

        self._build_ui()

    def _build_ui(self):
        title = tk.Label(
            self.root,
            text="Tic-Tac-Toe AI",
            font=("Segoe UI", 18, "bold"),
            bg="#1e1e2e",
            fg="#cdd6f4",
            pady=8,
        )
        title.pack()

        self.score_label = tk.Label(
            self.root,
            text=self._score_text(),
            font=("Segoe UI", 11),
            bg="#1e1e2e",
            fg="#a6adc8",
        )
        self.score_label.pack(pady=2)

        self.status_label = tk.Label(
            self.root,
            text="Your turn (X)",
            font=("Segoe UI", 12, "bold"),
            bg="#1e1e2e",
            fg="#89b4fa",
            pady=6,
        )
        self.status_label.pack()

        grid_frame = tk.Frame(self.root, bg="#313244", padx=6, pady=6)
        grid_frame.pack(padx=20, pady=10)

        self.buttons = []
        for i in range(9):
            btn = tk.Button(
                grid_frame,
                text=" ",
                font=("Segoe UI", 24, "bold"),
                width=4,
                height=2,
                bg="#181825",
                fg="#cdd6f4",
                activebackground="#45475a",
                relief="flat",
                command=lambda idx=i: self.on_cell_click(idx),
            )
            r, c = divmod(i, 3)
            btn.grid(row=r, column=c, padx=3, pady=3)
            self.buttons.append(btn)

        control_frame = tk.Frame(self.root, bg="#1e1e2e")
        control_frame.pack(pady=10)

        restart_btn = tk.Button(
            control_frame,
            text="New Game",
            font=("Segoe UI", 11, "bold"),
            bg="#a6e3a1",
            fg="#11111b",
            activebackground="#94e2d5",
            padx=12,
            pady=4,
            relief="flat",
            command=self.reset_game,
        )
        restart_btn.pack(side="left", padx=5)

    def _score_text(self):
        return f"Human (X): {self.human_score}  |  AI (O): {self.ai_score}  |  Draws: {self.draw_score}"

    def on_cell_click(self, idx):
        if self.game_over or self.board[idx] != " ":
            return

        # Human move
        self.board[idx] = HUMAN
        self.buttons[idx].config(text=HUMAN, fg="#f38ba8")

        w = winner(self.board)
        if w or " " not in self.board:
            self.end_game(w)
            return

        # AI move
        self.status_label.config(text="AI is thinking...", fg="#fab387")
        self.root.update()

        ai_idx = best_move(self.board)
        if ai_idx is not None:
            self.board[ai_idx] = AI
            self.buttons[ai_idx].config(text=AI, fg="#89b4fa")

        w = winner(self.board)
        if w or " " not in self.board:
            self.end_game(w)
        else:
            self.status_label.config(text="Your turn (X)", fg="#89b4fa")

    def end_game(self, w):
        self.game_over = True
        if w == HUMAN:
            self.human_score += 1
            self.status_label.config(text="You won! (Impossible)", fg="#a6e3a1")
        elif w == AI:
            self.ai_score += 1
            self.status_label.config(text="AI wins! (Minimax is unbeatable)", fg="#f38ba8")
        else:
            self.draw_score += 1
            self.status_label.config(text="It's a draw!", fg="#f9e2af")
        self.score_label.config(text=self._score_text())

    def reset_game(self):
        self.board = [" "] * 9
        self.game_over = False
        for btn in self.buttons:
            btn.config(text=" ", bg="#181825")
        self.status_label.config(text="Your turn (X)", fg="#89b4fa")


if __name__ == "__main__":
    app_root = tk.Tk()
    gui = TicTacToeGUI(app_root)
    app_root.mainloop()
