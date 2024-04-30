from tkinter import *
from quiz_brain import QuizBrain
import time
THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")
class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Trivia")
        self.window.config(pady=20,padx=20, bg=THEME_COLOR)
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column = 1)

        self.canvas = Canvas(width=300,height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, width=280, text="Question", fill=THEME_COLOR, font=FONT)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image,highlightthickness=0, command=self.check_answer_true)
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.check_answer_false)
        self.false_button.grid(row= 2, column=1)

        self.get_question()

        self.window.mainloop()

    def get_question(self):
        self.canvas.itemconfig(self.question_text, fill=THEME_COLOR)
        self.true_button.config(state="active")
        self.false_button.config(state="active")
        if self.quiz.still_has_questions():
            quiz_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=quiz_text,fill=THEME_COLOR)
        else:
            self.canvas.itemconfig(self.question_text,text="You've reached the end of the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def get_score(self):
        updated_score = self.quiz.score
        self.score_label.config(text=f"Score: {updated_score}/10")

    def check_answer_true(self):
        is_correct = self.quiz.check_answer("True")
        if is_correct:
            self.canvas.itemconfig(self.question_text,fill="green")
        else:
            self.canvas.itemconfig(self.question_text, fill="red")
        self.get_score()
        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")
        self.window.after(2000, self.get_question)

    def check_answer_false(self):
        is_correct = self.quiz.check_answer("False")
        if is_correct:
            self.canvas.itemconfig(self.question_text,fill="green")
        else:
            self.canvas.itemconfig(self.question_text, fill="red")
        self.get_score()
        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")
        self.window.after(2000, self.get_question)

