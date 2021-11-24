from tkinter import Button,Label,Entry, Tk

window = Tk()
window.title("Changing on input")
window.minsize(width=500,height=500)

def my_func():
    my_label.config(text=inp.get())


my_label = Label(text="this is label",font=('Arial',24,'bold'))
my_label.pack()

button = Button(window,text = 'Submit',command=my_func)
button.pack()

inp = Entry(width=10)
inp.pack()

window.mainloop()