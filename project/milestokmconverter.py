from tkinter import Label,Button,Entry,Tk,END

#defining window
window = Tk()
window.title("milestokmconverter")
window.geometry('400x400')
window.config(padx=50,pady=100)

#input miles
miles = Entry()
miles.insert(END,string="0")
miles.grid(column=1,row=0)

# label
milelabel = Label(text="Miles")
milelabel.grid(column=2,row=0)
equal = Label(text="is equal to")
equal.grid(column=0,row=1)
km = Label(text="0")
km.grid(row=1,column=1)
labkm = Label(text="km")
labkm.grid(row=1,column=2)

#conversion function
def convert():
    km.config(text=f"{int(miles.get())*1.60934}")


#button
button = Button(window,text='Submit',highlightbackground='black',command=convert)
button.grid(row=2,column=1)



window.mainloop()