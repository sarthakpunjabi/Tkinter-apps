from tkinter import *

# function for changing text in the label
def change_label():
    my_label.config(text="Button got clicked")

#defining screen
window = Tk()
window.title("Changing label on click")
window.minsize(width=500,height=300)

#defining components
my_label = Label(text="this is my label",font=('Arial',24,'bold'))
my_button = Button(text="click me", command=change_label,bg="black")

#packing the components or showing it on screen
my_label.pack()
my_button.pack()


#for showing the screen continously
window.mainloop()