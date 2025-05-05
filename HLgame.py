# Higher Lower Game using Tkinter

import tkinter as tk
import random
from data import data

# --- Game Logic ---
def format_data(account):
    return account["name"], account["description"], account["country"]

def check_answer(guess, a_followers, b_followers):
    return (a_followers > b_followers and guess == 'A') or (b_followers > a_followers and guess == 'B')

def next_round():
    global account_a, account_b
    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)
    update_ui()

def handle_guess(guess):
    global score
    a_followers = account_a["follower_count"]
    b_followers = account_b["follower_count"]
    if check_answer(guess, a_followers, b_followers):
        score += 1
        next_round()
    else:
        show_game_over()

def show_game_over():
    for widget in window.winfo_children():
        widget.destroy()
    tk.Label(window, text="Game Over!", font=("Segoe UI", 28, "bold"), fg="#ff4d4d", bg="#f8f9fa").pack(pady=30)
    tk.Label(window, text=f"Your Final Score: {score}", font=("Segoe UI", 18), bg="#f8f9fa").pack(pady=10)
    tk.Button(window, text="Play Again", font=("Segoe UI", 14), bg="#007bff", fg="white", width=15, command=start_game).pack(pady=20)

# --- UI Updates ---
def update_ui():
    label_score.config(text=f"Score: {score}")
    
    a_name, a_desc, a_country = format_data(account_a)
    b_name, b_desc, b_country = format_data(account_b)

    label_name_a.config(text=f"{a_name}")
    label_desc_a.config(text=f"{a_desc}\nFrom {a_country}")

    label_name_b.config(text=f"{b_name}")
    label_desc_b.config(text=f"{b_desc}\nFrom {b_country}")

# --- Game Initialization ---
def start_game():
    global score, account_a, account_b

    # Reset screen
    for widget in window.winfo_children():
        widget.destroy()

    # Title
    tk.Label(window, text="Higher Lower Game", font=("Segoe UI", 26, "bold"), fg="#343a40", bg="#f8f9fa").pack(pady=20)

    # Score Label
    global label_score
    label_score = tk.Label(window, text="Score: 0", font=("Segoe UI", 16), bg="#f8f9fa", fg="#0069d9")
    label_score.pack()

    # Comparison Frame
    frame = tk.Frame(window, bg="#f8f9fa")
    frame.pack(pady=30)

    # Dimensions
    card_width = 250
    card_height = 120

    # Left Card
    left_card = tk.Frame(frame, bg="white", bd=1, relief="solid", width=card_width, height=card_height)
    left_card.grid(row=0, column=0, padx=40)
    left_card.grid_propagate(False)  # Fix size

    global label_name_a, label_desc_a
    label_name_a = tk.Label(left_card, text="", font=("Segoe UI", 14, "bold"), bg="white", fg="#17a2b8", wraplength=220)
    label_name_a.pack(pady=(10, 0))
    label_desc_a = tk.Label(left_card, text="", font=("Segoe UI", 10), bg="white", fg="#212529", wraplength=220, justify="center")
    label_desc_a.pack()

    # VS Label
    tk.Label(frame, text="VS", font=("Segoe UI", 20, "bold"), bg="#f8f9fa", fg="#6c757d").grid(row=0, column=1)

    # Right Card
    right_card = tk.Frame(frame, bg="white", bd=1, relief="solid", width=card_width, height=card_height)
    right_card.grid(row=0, column=2, padx=40)
    right_card.grid_propagate(False)  # Fix size

    global label_name_b, label_desc_b
    label_name_b = tk.Label(right_card, text="", font=("Segoe UI", 14, "bold"), bg="white", fg="#17a2b8", wraplength=220)
    label_name_b.pack(pady=(10, 0))
    label_desc_b = tk.Label(right_card, text="", font=("Segoe UI", 10), bg="white", fg="#212529", wraplength=220, justify="center")
    label_desc_b.pack()

    # Buttons
    btn_frame = tk.Frame(window, bg="#f8f9fa")
    btn_frame.pack(pady=20)

    tk.Button(btn_frame, text="Choose A", font=("Segoe UI", 13), bg="#007bff", fg="white", width=12,
              command=lambda: handle_guess("A")).grid(row=0, column=0, padx=25)

    tk.Button(btn_frame, text="Choose B", font=("Segoe UI", 13), bg="#28a745", fg="white", width=12,
              command=lambda: handle_guess("B")).grid(row=0, column=1, padx=25)

    # Start Round
    score = 0
    account_b = random.choice(data)
    next_round()

# --- Main Window ---
window = tk.Tk()
window.title("Higher Lower Game")
window.geometry("800x600")
window.config(bg="#f8f9fa")

start_game()
window.mainloop()
