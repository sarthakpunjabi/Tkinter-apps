from tkinter import Tk,Button,Canvas
from PIL import Image,ImageTk
from random import choice
import pandas as pd


#global characters
ind=0
try:
    data = pd.read_csv("project/language-learner/data/words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("project/language-learner/data/french_words.csv")
temp = data


def next_card():
    """
    This function chooses random selection from the list
    """
    global ind
    ind = choice(temp["French"].index)
    question = temp.iloc[ind].French
    canvas.itemconfig(word,text=question,fill="black")
    canvas.itemconfig(language,text=temp.columns[0],fill="black")
    canvas.itemconfig(image,image=new_image)
    
def flip_card(): 
    canvas.itemconfig(language,text=temp.columns[1],fill="white")
    canvas.itemconfig(word,text=temp.iloc[ind].English,fill="white")
    canvas.itemconfig(image,image=old_image)

def is_known():
    temp.drop(ind,inplace=True)
    temp.to_csv("project/language-learner/data/words_to_learn.csv")
    next_card()

#consonants
BACKGROUND_COLOR = "#B1DDC6"

#screen
window = Tk()
window.title("Language Learner")
window.geometry("910x750")
window.config(bg=BACKGROUND_COLOR,pady=50,padx=50)
window.after(5000,func=flip_card)

#canvas
canvas = Canvas(height=526,width=800,bg=BACKGROUND_COLOR,highlightthickness=0)
old_image = ImageTk.PhotoImage(Image.open("project/language-learner/images/card_back.gif"))
new_image = ImageTk.PhotoImage(Image.open("project/language-learner/images/card_front.gif"))
image = canvas.create_image(400,263,image=new_image)
language = canvas.create_text(400,150,text=temp.columns[0],font=("Arial",40,'italic'),fill="black")
word = canvas.create_text(400,263,text="word",font=("Arial",60,'bold'),fill='black')
canvas.grid(row=0,column=0,columnspan=2)

#button
img1 = ImageTk.PhotoImage(Image.open("project/language-learner/images/right.png"))
correct = Button(image=img1,highlightthickness=0,highlightbackground=BACKGROUND_COLOR,command=is_known)
correct.grid(row=1,column=0)
img2 = ImageTk.PhotoImage(Image.open("project/language-learner/images/wrong.png"))
wrong = Button(image=img2,highlightthickness=0,highlightbackground=BACKGROUND_COLOR)
wrong.grid(row=1,column=1)

next_card()

window.mainloop()
