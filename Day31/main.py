from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

#Canvas
canvas = Canvas(width=800, height=526, highlightthickness=0)
front_card_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=front_card_img)
canvas.config(bg=BACKGROUND_COLOR)
canvas.create_text(390, 150, text="Spanish", fill="black", font=("Arial", 40, "italic"))
canvas.create_text(400, 275, text="palabra", fill="black", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

#X button
x_button_img = PhotoImage(file="images/wrong.png")
x_button = Button(image=x_button_img, highlightthickness=0, activebackground=BACKGROUND_COLOR,
                  highlightbackground=BACKGROUND_COLOR, highlightcolor=BACKGROUND_COLOR)
x_button.grid(row=1, column=0)

#Yes button
yes_button_img = PhotoImage(file="images/right.png")
yes_button = Button(image=yes_button_img, highlightthickness=0, activebackground=BACKGROUND_COLOR,
                  highlightbackground=BACKGROUND_COLOR, highlightcolor=BACKGROUND_COLOR)
yes_button.grid(row=1, column=1)

window.mainloop()
