BACKGROUND_COLOR = "#B1DDC6"
import pandas
import tkinter as tk
import random
current={}
to_learn={}
#dectionary
try:
    data=pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data=pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

#front
def nextw():
    global current,flip_timer
    screen.after_cancel(flip_timer)
    current=random.choice(to_learn)
    canvas.itemconfig(tit,text="French",fill="black")
    canvas.itemconfig(word,text=current["French"],fill="black")
    canvas.itemconfig(card_bg,image=front)
    flip_timer=screen.after(3000,func=flip_card)
def flip_card():
    canvas.itemconfig(tit,text="English",fill="white")
    canvas.itemconfig(word,text=current["English"],fill="white")
    canvas.itemconfig(card_bg,image=back)

def is_known():
    to_learn.remove(current)
    data=pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv",index=False)

    nextw()
screen=tk.Tk()
screen.title="Flashy"
screen.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

flip_timer=screen.after(3000,func=flip_card)

canvas=tk.Canvas(width=800,height=526)
back=tk.PhotoImage(file="images/card_back.png")
front=tk.PhotoImage(file="images/card_front.png")
right=tk.PhotoImage(file="images/right.png")
wrong=tk.PhotoImage(file="images/wrong.png")
card_bg=canvas.create_image(400,263,image=front)
tit=canvas.create_text(400,150,text="",font=("Ariel",40))
word=canvas.create_text(400,263,text="",font=("Ariel",60,"bold"))
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row=0,column=0,columnspan=2)
nextw()

#Button
unknow=tk.Button(image=wrong,highlightthickness=0,command=nextw)
right_b=tk.Button(image=right,highlightthickness=0,command=is_known)
right_b.grid(row=1,column=1)
unknow.grid(row=1,column=0)
screen.mainloop()