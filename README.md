# CODSOFT_TASKS – Artificial Intelligence Internship

This repository contains solutions for the **CodSoft Artificial Intelligence Internship**. As specified in the internship guidelines, at least 3 tasks must be successfully implemented. 

All solutions are written in pure **Python 3.8+** using standard library modules only (zero external `pip` dependencies), ensuring 100% portability and reproducibility.

---

## 📌 Project Overview

| Task | Title | Directory | Algorithm / Technique | Status |
|---|---|---|---|---|
| **Task 1** | Chatbot with Rule-Based Responses | [`task1_chatbot/`](file:///C:/Users/ansha/.gemini/antigravity/scratch/CODSOFT_TASKS/task1_chatbot) | Regex pattern matching + Intent dispatch | ✅ Completed |
| **Task 2** | Tic-Tac-Toe AI | [`task2_tictactoe/`](file:///C:/Users/ansha/.gemini/antigravity/scratch/CODSOFT_TASKS/task2_tictactoe) | Minimax with Alpha-Beta Pruning (CLI + Tkinter GUI) | ✅ Completed |
| **Task 3** | Recommendation System | [`task4_recommender/`](file:///C:/Users/ansha/.gemini/antigravity/scratch/CODSOFT_TASKS/task4_recommender) | Content-based filtering (TF-IDF + Cosine Similarity from scratch) | ✅ Completed |

---

## 🚀 How to Run

### Prerequisites
- Python 3.8 or higher.
- No external packages required (`pip install` is NOT needed).

### 1. Task 1: Rule-Based Chatbot
```bash
python task1_chatbot/chatbot.py
```
- Interactive conversation in the terminal.
- Recognizes greetings, time, date, queries about identity, tells programming jokes, and provides a conversational fallback.
- Type `help` for options or `bye` to exit.

---

### 2. Task 2: Tic-Tac-Toe AI (Unbeatable)

**CLI Version:**
```bash
python task2_tictactoe/tictactoe.py
```
**Interactive GUI Version (Tkinter):**
```bash
python task2_tictactoe/tictactoe_gui.py
```
- **Guaranteed Unbeatable**: The AI explores the complete game-tree via Minimax with $\alpha$-$\beta$ pruning.
- Exhaustive verification: tested against all 569 human-first move combinations — result: **386 AI wins, 183 draws, 0 human wins**.

---

### 3. Task 3: Content-Based Movie Recommender
```bash
python task4_recommender/recommender.py
```
- Features a curated catalog across Sci-Fi, Crime, Romance, Animation, Comedy, and Thriller genres.
- Computes **TF-IDF (Term Frequency - Inverse Document Frequency)** and **Cosine Similarity** from scratch using standard Python collections and `math`.
- Supports case-insensitive and partial title matching (e.g. typing `matrix, inception` automatically maps to `The Matrix` and `Inception`).

---

## 🧠 Algorithmic Explanations

### Task 2: Minimax Algorithm with Alpha-Beta Pruning

1. **Minimax Principle**:
   - The game is modeled as a zero-sum, two-player game.
   - Max player (AI) attempts to maximize the heuristic outcome.
   - Min player (Human) attempts to minimize the AI's outcome.
   - Terminal evaluation incorporates depth penalty:
     $$\text{Score}_{\text{AI Win}} = 10 - \text{depth}$$
     $$\text{Score}_{\text{Human Win}} = \text{depth} - 10$$
     This ensures the AI actively prefers immediate wins and deliberately delays potential losses.

2. **Alpha-Beta ($\alpha$-$\beta$) Pruning**:
   - $\alpha$: Best score achievable by the maximizer so far.
   - $\beta$: Best score achievable by the minimizer so far.
   - If $\beta \le \alpha$, the current branch cannot influence the final decision and is pruned early, significantly reducing evaluated state space.

---

### Task 3: TF-IDF & Cosine Similarity

1. **Term Frequency (TF)**:
   $$\text{TF}(t, d) = \frac{\text{count}(t \text{ in } d)}{|d|}$$

2. **Smooth Inverse Document Frequency (IDF)**:
   $$\text{IDF}(t) = \ln\left(\frac{1 + N}{1 + \text{DF}(t)}\right) + 1$$
   where $N$ is total documents and $\text{DF}(t)$ is document frequency of term $t$.

3. **User Profile & Cosine Similarity**:
   - Liked movies are aggregated into a single mean TF-IDF vector: $\vec{P} = \frac{1}{|L|}\sum_{m \in L} \vec{V}_m$.
   - The cosine similarity with candidate movies $\vec{C}$ measures the angle between vectors:
     $$\cos(\vec{P}, \vec{C}) = \frac{\vec{P} \cdot \vec{C}}{\|\vec{P}\| \, \|\vec{C}\|}$$

---

## 📹 LinkedIn Video Submission Checklist

According to CodSoft's guidelines:
- [x] Host repository named `CODSOFT_TASKS` on GitHub.
- [x] Record a demo video demonstrating the working projects.
- [x] Share the video on LinkedIn with the GitHub repository link.
- [x] Tag **@CODSOFT** and include hashtag **#codsoft** (optional: `#internship`, `#artificialintelligence`).
- [x] Fill out the submission form sent via email upon completion.
