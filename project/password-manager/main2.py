""" This application manages your password and profile """
import random
import json
from tkinter import Tk,Canvas,Label,Button,Entry,END,messagebox
from PIL import Image,ImageTk
import pyperclip

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
    new_data = {
                f"{webinp.get().lower()}":{
                    "email":f"{username.get().lower()}",
                    "password":f"{passwordinp.get().lower()}"
                }
            }
    try:
        if validator():
            print("trying")
            with open("database.json",mode="r",encoding='utf-8') as fil:
                data = json.load(fil)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        print("Exception")
        messagebox.showwarning(title="warning message",message="This is exceptional case")
        with open("database.json",mode="w",encoding="utf-8") as fill:
            if validator():
                fill.seek(0)
                json.dump(new_data,fill,indent=4)
                clean()
    else:
        print("in else")
        data.update(new_data)
        with open("database.json",mode="w",encoding='utf-8') as fil:
            if validator():
                json.dump(data,fil,indent=4)
                clean()

def search_func():
    """
    This is for the search functionality
    """
    try:
        with open("database.json",mode="r",encoding="utf-8") as fil:
            data = json.load(fil)
            temp = webinp.get()

    except FileNotFoundError as message:
        messagebox.showerror(title="not found",message=f"{message}")
    else:
        if temp in data:
            messagebox.showinfo(title="showing password",
            message=f"Provider:{temp} \n"+
            f"email:{data[temp]['email']} \n"+
            f"password:{data[temp]['password']}"
            )
        else:
            messagebox.showwarning(title="No provider like that",
            message=f"There is no provider like {temp}"
            )

#screen
window = Tk()
window.title("Password manager")
window.geometry('500x500')
window.config(padx=50,pady=50,bg="black")

#cavas
canvas = Canvas(width=200,height=200,highlightthickness=0,bg='black')
img = ImageTk.PhotoImage(Image.open("logo.gif"))
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
webinp = Entry(width=22,bg="black",fg="white",highlightthickness=0)
webinp.focus()
webinp.grid(row=1,column=1,pady=20)
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
search = Button(highlightbackground='red',text='Search',command=search_func)
search.grid(row=1,column=2)

window.mainloop()
