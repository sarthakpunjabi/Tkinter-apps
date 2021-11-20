from tkinter import Label,Button,Entry, Tk

window = Tk()
window.title("Grid System")
window.geometry('300x300')

label = Label(text="This is label",fg='red')
label.grid(column=0,row=0)

button = Button(window,text='Submit',highlightbackground='black')
button.grid(column=3,row=0)

button = Button(window,text='Submit',highlightbackground='blue')
button.grid(column=2,row=1)

inp = Entry(width=60 )
# inp.insert(text="this is input box")
inp.grid(column=4,row=3)


window.mainloop()