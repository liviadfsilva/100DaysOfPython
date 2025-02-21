from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
repetitions = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=PINK, bg=YELLOW)
    check_mark_label.config(text="")

    global repetitions
    repetitions = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global repetitions
    repetitions += 1
    work_seconds = WORK_MIN * 60
    short_break_seconds = SHORT_BREAK_MIN * 60
    long_break_seconds = LONG_BREAK_MIN * 60

    if repetitions % 8 == 0:
        timer_label.config(text="Long Break", fg=RED, bg=YELLOW, font=(FONT_NAME, 50))
        count_down(long_break_seconds)
    elif repetitions % 2 == 0:
        timer_label.config(text="Short Break", fg=PINK, bg=YELLOW, font=(FONT_NAME, 50))
        count_down(short_break_seconds)
    else:
        timer_label.config(text="Work", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
        count_down(work_seconds)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_minutes = math.floor(count / 60)
    count_seconds = count % 60
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"

    canvas.itemconfig(timer_text, text=f"{count_minutes}:{count_seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(repetitions/2)
        for _ in range(work_sessions):
            marks += "✔"
            check_mark_label.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

#TODO: start button.
start_button = Button(text="Start", command= start_timer, activebackground=YELLOW, highlightthickness=0, highlightbackground=YELLOW,
                      highlightcolor=YELLOW)
start_button.grid(column=0, row=2)

#TODO: reset button.
reset_button = Button(text="Reset", command=reset_timer, highlightthickness=0, highlightbackground=YELLOW, highlightcolor=YELLOW)
reset_button.grid(column=2, row=2)

#TODO: timer label.
timer_label = Label(text="Timer", fg=GREEN, bg= YELLOW, font=(FONT_NAME, 50))
timer_label.grid(column=1, row=0)

#TODO: check_mark.
check_mark_label = Label(bg=YELLOW, fg=GREEN)
check_mark_label.grid(column=1, row=3)

window.mainloop()