"""
This application is for enhancing productivity
"""
import math
from tkinter import Button,Label,Canvas,Tk
from PIL import ImageTk,Image

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
CALCTIME = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    """
    This module is for reseting the timer
    """
    global REPS
    window.after_cancel(CALCTIME)
    timer.config(text="Timer")
    canvas.itemconfig(timer_text,text="00:00")
    REPS = 0
    check_mark.config(text="")
    start.config(state='active')


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    """
    This module is for deciding the state and mode
    """
    start.config(state='disabled')
    global REPS
    REPS +=1
    check_mark.config(text="",fg=GREEN)
    if REPS == 8:
        timer.config(text="Long break Enjoy ☕️",fg="red",bg='black',font=(FONT_NAME,26,'bold'))
        check_mark.config(text="✔",fg='white')
        count_down(LONG_BREAK_MIN*60)
    elif REPS%2==0:
        timer.config(text="Short-break Relax 🧘🏻 ",fg="pink",bg='black',font=(FONT_NAME,26,'bold'))
        check_mark.config(text="✔",fg='white')
        count_down(SHORT_BREAK_MIN *60)
    else:
        timer.config(text="WORK",fg=GREEN,bg='black',font=(FONT_NAME,46,'bold'))
        count_down(WORK_MIN * 60)
    

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    """
    This module is for count down
    """
    count_min = str(math.floor(count/60) )
    count_sec = str(count % 60)

    canvas.itemconfig(timer_text,text=f"{count_min.zfill(2)}:{count_sec.zfill(2)}")
    if count > 0:
        global CALCTIME
        CALCTIME = window.after(1000,count_down,count-1)
    else:
        window.attributes('-topmost', True)
        window.attributes('-topmost', False)
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("pomodoro")
window.config(padx=100,pady=50,bg='black')

#Labels
timer = Label(text="WORK",fg=GREEN,bg='black',font=(FONT_NAME,46,'bold'))
timer.grid(row=0,column=1)

#canvas
canvas = Canvas(width=200,height=224,highlightthickness=0,bg='black')
tomato_img = ImageTk.PhotoImage(Image.open('tomato.gif'))
canvas.create_image(100,112,image=tomato_img)
timer_text = canvas.create_text(100,130,text="00:00",fill="black",font=(FONT_NAME,35,'bold'))
canvas.grid(row=1,column=1)

#button
start = Button(window,text="Start",highlightbackground='#FF5151',
highlightthickness=0,command=start_timer
)
start.grid(row=2,column=0)

reset = Button(window,text="Reset",highlightbackground='#FF5151',
highlightthickness=0,command=reset_timer
)
reset.grid(row=2,column=2)

#checkmark
check_mark = Label(fg=GREEN,bg='black')
check_mark.grid(row=3,column=1)

window.mainloop()
