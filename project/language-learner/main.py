from tkinter import Tk,Button,Canvas
from PIL import Image,ImageTk

#consonants
BACKGROUND_COLOR = "#B1DDC6"

#screen
window = Tk()
window.title("Language Learner")
window.geometry("910x750")
window.config(bg=BACKGROUND_COLOR,pady=50,padx=50)

#canvas
canvas = Canvas(height=526,width=800,bg=BACKGROUND_COLOR,highlightthickness=0)
new_image= ImageTk.PhotoImage(Image.open("project/language-learner/images/card_front.gif"))
image = canvas.create_image(400,263,image=new_image)
language = canvas.create_text(400,150,text="title",font=("Arial",40,'italic'),fill="black")
word = canvas.create_text(400,263,text="word",font=("Arial",60,'bold'),fill='black')
canvas.grid(row=0,column=0,columnspan=2)

#button
img1 = ImageTk.PhotoImage(Image.open("project/language-learner/images/right.png"))
correct = Button(image=img1,highlightthickness=0,highlightbackground=BACKGROUND_COLOR)
correct.grid(row=1,column=0)
img2 = ImageTk.PhotoImage(Image.open("project/language-learner/images/wrong.png"))
wrong = Button(image=img2,highlightthickness=0,highlightbackground=BACKGROUND_COLOR)
wrong.grid(row=1,column=1)

window.mainloop()
