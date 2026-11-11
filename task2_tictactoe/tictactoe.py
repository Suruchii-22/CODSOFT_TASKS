"""Task 2: Unbeatable Tic-Tac-Toe AI using Minimax with Alpha-Beta Pruning."""
import math

WINS = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
AI, HUMAN = "O", "X"


def winner(b):
    for a, c, d in WINS:
        if b[a] != " " and b[a] == b[c] == b[d]:
            return b[a]
    return None


def minimax(b, is_ai, alpha, beta, depth):
    w = winner(b)
    if w == AI:    return 10 - depth      # prefer faster wins
    if w == HUMAN: return depth - 10      # prefer slower losses
    if " " not in b: return 0
    if is_ai:
        best = -math.inf
        for i in range(9):
            if b[i] == " ":
                b[i] = AI
                best = max(best, minimax(b, False, alpha, beta, depth + 1))
                b[i] = " "
                alpha = max(alpha, best)
                if beta <= alpha: break   # prune
        return best
    best = math.inf
    for i in range(9):
        if b[i] == " ":
            b[i] = HUMAN
            best = min(best, minimax(b, True, alpha, beta, depth + 1))
            b[i] = " "
            beta = min(beta, best)
            if beta <= alpha: break
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


def show(b):
    for r in range(3):
        print(" " + " | ".join(b[r*3:r*3+3]))
        if r < 2: print("---+---+---")


def main():
    b = [" "] * 9
    print("You are X, AI is O. Enter a cell 1-9 (left-to-right, top-to-bottom).")
    show(b)
    while True:
        try:
            m = int(input("Your move: ")) - 1
        except ValueError:
            print("Enter a number 1-9."); continue
        if not 0 <= m <= 8 or b[m] != " ":
            print("Invalid move."); continue
        b[m] = HUMAN
        if winner(b) or " " not in b: break
        b[best_move(b)] = AI
        show(b)
        if winner(b) or " " not in b: break
    show(b)
    w = winner(b)
    print(f"{w} wins!" if w else "It's a draw!")


if __name__ == "__main__":
    main()
