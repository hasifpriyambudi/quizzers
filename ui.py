from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")

class QuizInterface:

    def __init__(self, quizBrain: QuizBrain):
        self.quizBrain = quizBrain
        self.window = Tk()
        self.window.title("Quizzer")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.scoreLabel = Label(text="Score: 0", foreground="white", bg=THEME_COLOR)
        self.scoreLabel.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question = self.canvas.create_text(150, 125, width=280, text="question Text", fill=THEME_COLOR, font=FONT)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        trueImage = PhotoImage(file="images/true.png")
        self.trueButton = Button(image=trueImage, highlightthickness=0, command=lambda: self.checkAnswer("true"))
        self.trueButton.grid(row=2, column=0)

        falseImage = PhotoImage(file="images/false.png")
        self.falseButton = Button(image=falseImage, highlightthickness=0, command=lambda: self.checkAnswer("false"))
        self.falseButton.grid(row=2, column=1)

        self.getNextQuestions()

        self.window.mainloop()

    def getNextQuestions(self):
        self.canvas.config(bg="white")
        if self.quizBrain.still_has_questions():
            self.canvas.itemconfig(self.question, fill=THEME_COLOR)
            self.scoreLabel.config(text=f"Score: {self.quizBrain.score}")
            quizText = self.quizBrain.next_question()
            self.canvas.itemconfig(self.question, text=quizText)
        else:
            self.canvas.itemconfig(self.question, text="You've reached the end of the quiz", fill=THEME_COLOR)
            self.trueButton.config(state="disabled")
            self.falseButton.config(state="disabled")

    def checkAnswer(self, answer: str):
        self.giveFeedback(self.quizBrain.check_answer(answer))

    def giveFeedback(self, isRight):
        if isRight:
            self.canvas.configure(bg="green")
        else:
            self.canvas.configure(bg="red")
        self.canvas.itemconfig(self.question, fill="white")
        self.window.after(1000, self.getNextQuestions)
