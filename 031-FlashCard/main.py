from tkinter import *
from tkinter import messagebox
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

# ------------------ Open saved file/original file --------------------- #

try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

# -------------------------- Correct Answer ----------------------------- #

def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("./data/words_to_learn.csv", index=False)
    next_card()

# ---------------------------- Flip Card ------------------------------- #

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)

# ---------------------------- Next Card ------------------------------- #

def next_card():
    global current_card
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)

# ---------------------------- UI SETUP ------------------------------- #

# Window
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

# Canvas
canvas = Canvas(width=800, height=526, highlightthickness=0,  background=BACKGROUND_COLOR)
card_back_img = PhotoImage(file="./images/card_back.png")
card_front_img = PhotoImage(file="./images/card_front.png")
canvas.grid(column=0, row=0, columnspan=3)

# Populate image on canvas
card_background = canvas.create_image(400,263, image=card_back_img)

# Populate text on canvas
card_title = canvas.create_text(400, 150, text="title", fill="black", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", fill="black", font=("Ariel", 60, "bold"))

# Wrong Button
wrong_button_picture = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_button_picture, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=next_card)
wrong_button.grid(column=0, row=1)

# Flip Button
flip_button_picture = PhotoImage(file="./images/flip.png")
flip_button = Button(image=flip_button_picture, highlightthickness=0, command=flip_card)
flip_button.grid(column=1, row=1)

# Correct Button
correct_button_picture = PhotoImage(file="./images/right.png")
correct_button = Button(image=correct_button_picture, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=is_known)
correct_button.grid(column=2, row=1)

next_card()

# Run program until closed
window.mainloop()