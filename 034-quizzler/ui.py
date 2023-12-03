from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)
        
        self.canvas = Canvas(width=300, height=250, background="white")
        self.canvas.grid(column=0, row=1, columnspan=2, padx=0, pady=50)
        
        self.question_text = self.canvas.create_text(150, 125, text="text", fill=THEME_COLOR, font=FONT, width=280)

        self.score = Label(text="score: 0", background=THEME_COLOR, fg="white")
        self.score.grid(column=1, row=0)

        self.true_button_image = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=self.true_button_image, highlightthickness=0, command=self.guess_true)
        self.true_button.grid(column=0, row=2)

        self.false_button_image = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=self.false_button_image, highlightthickness=0, command=self.guess_false)
        self.false_button.grid(column=1, row=2)


        self.get_next_question()


        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(background="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def guess_true(self):
        self.give_feedback(self.quiz.check_answer(user_answer="true"))

    def guess_false(self):
        self.give_feedback(self.quiz.check_answer(user_answer="false"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(background="green")
        else:
            self.canvas.config(background="red")
        self.window.after(1000, self.get_next_question)