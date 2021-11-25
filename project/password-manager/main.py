"""
This application manages your password and profile 
"""
import random
from tkinter import Tk,Canvas,Label,Button,Entry,END,messagebox
from PIL import Image,ImageTk
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    """
    This module automatically generates password
    """
    small_letters = [chr(x) for x in range(ord('a'),ord('z')+1)]
    big_letters = [chr(x) for x in range(ord('A'),ord('Z')+1)]
    letters = small_letters + big_letters
    symbols = [chr(x) for x in range(ord('!'),ord('/')+1)]
    numbers = [chr(x) for x in range(ord('0'),ord('9')+1)]
    password = ""
    strong_password=""
    for i in range(0,10):
        password += random.choice(letters)+" "

    for i in range(0,4):
        password += random.choice(symbols)+" "

    for i in range(0,5):
        password += random.choice(numbers)+" "

    password = password.split(" ")
    password.pop()
    random.shuffle(password)
    for i in range(0,len(password)):
        strong_password += password[i]

    pyperclip.copy(strong_password)
    passwordinp.insert(0,string=f"{strong_password}")
    

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    """
    This module is to add data into database
    """
    def clean():
        """
        This module is to clean Entry after storing data
        """
        webinp.delete(0,END)
        passwordinp.delete(0,END)
        username.delete(0,END)
        messagebox.showinfo(title="save",message="Your data got saved")

    def validator():
        """
        It helps validating the Entry
        """
        if len(webinp.get())==0 or len(username.get())==0 or len(passwordinp.get())==0:
            return False
        else:
            return True
        
    with open("database.txt","a+",encoding="utf-8") as fil:
        fil.seek(0)
        read_line = fil.read()
        if webinp.get() in read_line:
            fil.seek(0)
            flag_ok = messagebox.askokcancel(title="Update",
            message="Do you want to update the profile"
            )
            for i in fil.readlines():
                if flag_ok and webinp.get() in i and validator():
                    j = f"{webinp.get()} | {username.get()} | {passwordinp.get()} \n"
                    fil.truncate(0)
                    fil.seek(0)
                    fil.write(read_line.replace(i,j))
                    clean()
                else:
                    messagebox.showerror(title="Something went wrong",
                    message="Please check your fields"
                    )
                    
        else:
            if validator():
                fil.write(f"{webinp.get()} | {username.get()} | {passwordinp.get()} \n")
                clean()
            else:
                messagebox.showerror(title="Something went wrong",
                message="Please check your fields"
                )

        

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
webid = Label(window,text="Username/email",bg="black",fg="white")
webid.grid(row=2,column=0)
passwords = Label(window,text="Password",bg="black",fg="white")
passwords.grid(row=3,column=0)

#Input
webinp = Entry(width=35,bg="black",fg="white",highlightthickness=0)
webinp.focus()
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
add = Button(highlightbackground='red',text="Add",command=save,width=36)
add.grid(row=4,column=1,columnspan=2)

window.mainloop()
