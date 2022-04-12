from tkinter import *
from time import sleep
# ---------------------------- CONSTANTS ------------------------------- #
#Colors association picked on colorhunt.co
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25*60
SHORT_BREAK_MIN = 5*60
LONG_BREAK_MIN = 20*60
reps = 0
allowed_to_start = True
check = '✔'
TICK = 1000
time = "00:00"

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global time
    global reps
    global allowed_to_start
    global check
    window.after_cancel(time)
    reps = 0
    check = '✔'
    canvas.itemconfig(timer, text="00:00")
    title.config(text='Timer', fg=GREEN)
    check_l.config(text="")
    allowed_to_start = True


# ---------------------------- TIMER MECHANISM ------------------------------- #
def check_start():
    global allowed_to_start
    if allowed_to_start:
        start_timer()
        allowed_to_start = False

def start_timer():
    global reps
    if reps < 7:
        if reps % 2 == 0:
            title.config(text="Work", fg=GREEN)
            count_down(WORK_MIN)
        else:
            title.config(text='Break', fg=PINK)
            count_down(SHORT_BREAK_MIN)
    elif reps == 7:
        title.config(text='Break', fg=RED)
        count_down(LONG_BREAK_MIN)
    reps += 1


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global check
    global time
    m = str(count // 60)
    s = str(count % 60)
    if len(m) == 1:
        m = "0" + m
    if len(s) == 1:
        s = "0" + s
    fcount = m + ":" + s
    canvas.itemconfig(timer, text=fcount)
    if count > 0:
        time = window.after(TICK, count_down, count - 1)
    else:
        if reps % 2 != 0:
            check_l.config(text=check)
            check += '✔'
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

#Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
#Background img
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
#Timer
timer = canvas.create_text(100, 130, text=time, fill="white", font=(FONT_NAME, 35, "bold"))
#Buttons
start_b = Button(text="Start", highlightthickness=0, command=check_start)
reset_b = Button(text="Reset", highlightthickness=0, command=reset_timer)
#Text elements
title = Label(text="Timer", font=(FONT_NAME, 40, "bold"), anchor="center", fg=GREEN, bg=YELLOW)
check_l = Label(font=(FONT_NAME, 15), fg=GREEN, bg=YELLOW)


#Layout
title.grid(row=0, column=1)
canvas.grid(row=1, column=1)
start_b.grid(row=2, column=0)
reset_b.grid(row=2, column=2)
check_l.grid(row=3, column=1)


window.mainloop()