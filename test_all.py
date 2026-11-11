"""Comprehensive verification test suite for all CodSoft AI Internship tasks."""
import sys
import os

# Add task paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(BASE_DIR, "task1_chatbot"))
sys.path.insert(0, os.path.join(BASE_DIR, "task2_tictactoe"))
sys.path.insert(0, os.path.join(BASE_DIR, "task4_recommender"))

import chatbot
import tictactoe
import recommender


def test_task1():
    print("[*] Testing Task 1: Chatbot...")
    assert "Hello" in chatbot.respond("hello there") or "Hey" in chatbot.respond("hello there")
    assert "CodBot" in chatbot.respond("what is your name")
    assert "Alice" in chatbot.respond("my name is Alice")
    assert "time is" in chatbot.respond("what time is it").lower()
    print("  --> Task 1 Passed! (Regex patterns & intent response verified)")


def test_task2():
    print("[*] Testing Task 2: Tic-Tac-Toe Minimax (Exhaustive Game-Tree Simulation)...")
    wins_ai = 0
    draws = 0
    wins_human = 0

    def play_all(b):
        nonlocal wins_ai, draws, wins_human
        w = tictactoe.winner(b)
        if w == tictactoe.HUMAN:
            wins_human += 1
            return
        if w == tictactoe.AI:
            wins_ai += 1
            return
        if " " not in b:
            draws += 1
            return

        # Human's turn: explore every legal move
        for i in range(9):
            if b[i] == " ":
                b[i] = tictactoe.HUMAN
                w2 = tictactoe.winner(b)
                if w2 == tictactoe.HUMAN:
                    wins_human += 1
                    b[i] = " "
                    continue
                if " " not in b:
                    draws += 1
                    b[i] = " "
                    continue

                # AI's turn: Minimax move
                ai_m = tictactoe.best_move(b)
                b[ai_m] = tictactoe.AI
                play_all(b)
                b[ai_m] = " "
                b[i] = " "

    b = [" "] * 9
    play_all(b)
    print(f"  --> AI Wins: {wins_ai}, Draws: {draws}, Human Wins: {wins_human}")
    assert wins_human == 0, "AI was beaten! Should be unbeatable."
    assert wins_ai == 386 and draws == 183, "Game-tree simulation mismatch."
    print("  --> Task 2 Passed! (AI is mathematically unbeatable)")


def test_task4():
    print("[*] Testing Task 4: Content-Based Recommender (TF-IDF + Cosine)...")
    resolved, recs = recommender.recommend(["matrix", "inception"], k=3)
    assert len(resolved) == 2
    assert len(recs) == 3
    # Check top similarity is positive
    assert recs[0][1] > 0.0
    print(f"  --> Top recommendations for {resolved}:")
    for title, score in recs:
        print(f"      - {title} (similarity: {score:.3f})")
    print("  --> Task 4 Passed! (TF-IDF and Cosine similarity verified)")


if __name__ == "__main__":
    print("=" * 60)
    print("RUNNING FULL VERIFICATION SUITE")
    print("=" * 60)
    test_task1()
    test_task2()
    test_task4()
    print("=" * 60)
    print("ALL TESTS PASSED SUCCESSFULLY! (100% Verified)")
    print("=" * 60)
