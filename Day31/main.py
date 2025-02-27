from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
# ---------------------------- NEXT CARD ------------------------------- #
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/spanish_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="Español", fill="black")
    canvas.itemconfig(card_word, text=current_card["Spanish"], fill="black")
    canvas.itemconfig(front_card_bg, image=front_card_img)
    flip_timer = window.after(3000, flip_card)

# ---------------------------- IS KNOWN ------------------------------- #
def is_known():
    to_learn.remove(current_card)
    data_file = pandas.DataFrame(to_learn)
    data_file.to_csv("data/words_to_learn.csv", index=False)
    next_card()

# ---------------------------- FLIP CARD ------------------------------- #
back_card_img = PhotoImage(file="images/card_back.png")

def flip_card():
    canvas.itemconfig(front_card_bg, image=back_card_img)
    canvas.itemconfig(card_title, text="Português", fill="white")
    canvas.itemconfig(card_word, text=current_card["Portuguese"], fill="white")

flip_timer = window.after(3000, flip_card)

# ---------------------------- CANVAS ------------------------------- #
canvas = Canvas(width=800, height=526, highlightthickness=0)
front_card_img = PhotoImage(file="images/card_front.png")
front_card_bg = canvas.create_image(400, 263, image=front_card_img)
canvas.config(bg=BACKGROUND_COLOR)
card_title = canvas.create_text(390, 150, text="Language", fill="black", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 275, text="word", fill="black", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# ---------------------------- BUTTONS ------------------------------- #
#X button
x_button_img = PhotoImage(file="images/wrong.png")
x_button = Button(image=x_button_img, highlightthickness=0, activebackground=BACKGROUND_COLOR,
                  highlightbackground=BACKGROUND_COLOR, highlightcolor=BACKGROUND_COLOR, command=next_card)
x_button.grid(row=1, column=0)

#Yes button
yes_button_img = PhotoImage(file="images/right.png")
yes_button = Button(image=yes_button_img, highlightthickness=0, activebackground=BACKGROUND_COLOR,
                  highlightbackground=BACKGROUND_COLOR, highlightcolor=BACKGROUND_COLOR, command=is_known)
yes_button.grid(row=1, column=1)

next_card()

window.mainloop()
