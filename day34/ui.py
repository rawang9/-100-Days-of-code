THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain
class QuizInterface():
    def __init__(self,quiz:QuizBrain):
        self.quiz=quiz
        self.screen=Tk()
        self.screen.title("Quizzle")
        self.screen.config(bg=THEME_COLOR,padx=20,pady=20)

        self.lebal=Label(text="Score : 0",fg="white",bg=THEME_COLOR,font=("Arial",20))
        self.lebal.grid(row=0,column=1)

        self.canvas=Canvas(width=300,height=250,bg="white")
        self.text= self.canvas.create_text(150,125,text = "Some q text",width=280,fill=THEME_COLOR,font=("Arial",20))
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)
        #buttons
        true=PhotoImage(file="images/true.png")
        false=PhotoImage(file="images/false.png")
        self.true_button=Button(image=true,highlightthickness=0,command=self.true)
        self.false_button=Button(image=false,highlightthickness=0,command=self.false)
        self.true_button.grid(row=3,column=0)
        self.false_button.grid(row=3,column=1)
        self.newtQ()
        self.screen.mainloop()
    def newtQ(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            nextques=self.quiz.next_question()
            self.canvas.itemconfig(self.text,text=nextques)
        else:
            self.canvas.itemconfig(self.text,text="You have reached to the End!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
    def true(self):
        self.feedback(self.quiz.check_answer("True"))

    def false(self):
        ans=self.quiz.check_answer("False")
        self.feedback(ans)
    def feedback(self,ans):
        if ans:
            self.canvas.config(bg="green")
            self.lebal.config(text=f"Score : {self.quiz.score}")
        else:
            self.canvas.config(bg="red")
        self.screen.after(1000,self.newtQ)