from tkinter import Tk,Canvas,Label,Button,Entry,END
from PIL import Image,ImageTk

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    pass

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    pass

# ---------------------------- UI SETUP ------------------------------- #

#screen
window = Tk()
window.title("Password manager")
window.geometry('500x500')
window.config(padx=50,pady=50,bg="black")

#cavas
canvas = Canvas(width=200,height=200,highlightthickness=0,bg='black')
img = ImageTk.PhotoImage(Image.open("project/password-manager/logo.gif"))
image = canvas.create_image(100,100,image=img)
canvas.grid(row=0,column=1)

#Labels
website = Label(window,text="Website:",bg="black",fg="white")
website.grid(row=1,column=0)
website.focus()
webid = Label(window,text="Username/email",bg="black",fg="white")
webid.grid(row=2,column=0)
password = Label(window,text="Password",bg="black",fg="white")
password.grid(row=3,column=0)

#Input
webinp = Entry(width=35,bg="black",fg="white",highlightthickness=0)
webinp.insert(END,string="Enter website name")
webinp.grid(row=1,column=1,columnspan=2,pady=10)
username = Entry(width=35,bg="black",fg="white",highlightthickness=0)
username.insert(END,string="Enter User Id")
username.grid(row=2,column=1,columnspan=2,pady=10)
passwordinp = Entry(width=22,bg="black",fg="white",highlightthickness=0)
passwordinp.insert(END,string="Enter Password")
passwordinp.grid(row=3,column=1,pady=20)

#button
generate = Button(width=8,highlightbackground='red',text='Generate',command=generate_password)
generate.grid(row=3,column=2)
add = Button(highlightbackground='red',text="Add",command=add,width=36)
add.grid(row=4,column=1,columnspan=2)

window.mainloop()
