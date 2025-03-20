from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas.grid(row=1, columnspan=2, column=0, pady=50)
        self.canvas_question = self.canvas.create_text(150, 125, width=280, text="question here",
                                                       font=("Arial", 20, "italic"), fill="black")

        self.true_button_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=self.true_button_img, highlightthickness=0, command=self.true_click)
        self.true_button.grid(row=2, column=0)

        self.false_button_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=self.false_button_img, highlightthickness=0, command=self.false_click)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        question_text = self.quiz.next_question()
        self.canvas.itemconfig(self.canvas_question, text=question_text)

    def true_click(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_click(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
            self.window.after(1000, self.get_next_question)
        else:
            self.canvas.config(bg="red")
            self.window.after(1000, self.get_next_question)