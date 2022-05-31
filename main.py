from tkinter import *
from playsound import playsound
from tkinter import messagebox

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#f7c4c8"
RED = "#e7305b"
GREEN = "#77ad91"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER ALERT ------------------------------- #

def alert():
    playsound("pomodoro-timer-alert.mp3")

# ---------------------------- TIMER RESET ------------------------------- #

def reset():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_mark.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():

    welcome_text()

    global reps
    reps += 1
    work = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if reps % 2 != 0 and reps < 8:
        count_down(work)
        title_label.config(text="Work")
    elif reps == 8:
        count_down(long_break)
        title_label.config(text="25 min break")
    elif reps % 2 == 0:
        count_down(short_break)
        title_label.config(text="5 min break")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    min_left = int(count / 60)
    if min_left == 0:
        min_left = f"0{min_left}"
    sec_left = int(count % 60)
    if sec_left < 10:
        sec_left = f"0{sec_left}"
    canvas.itemconfig(timer_text, text=f"{min_left}:{sec_left}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count -1)
    else:
        start_timer()
        marks = ""
        work_sessions = int(reps/2)
        for _ in range(work_sessions):
            marks += "✓"
        check_mark.config(text=marks)
        alert()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro Timer")
window.config(padx=50, pady=30, bg=PINK)


canvas = Canvas(width=400, height=400, bg=PINK, highlightthickness=0)
tomato = PhotoImage(file="tomato.gif")
canvas.create_image(200, 200, image=tomato)
timer_text = canvas.create_text(200, 220, text="00:00", fill="white", font=(FONT_NAME, 30))

canvas.grid(column=1, row=1)


title_label = Label(text="TIMER", font=(FONT_NAME, 40), fg=GREEN, bg=PINK)
title_label.grid(column=1, row=0)

start_button = Button(width=5, text="Start", font=(FONT_NAME, 15), highlightbackground=PINK,
                      command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(width=5, text="Reset", font=(FONT_NAME, 15), highlightbackground=PINK,
                      command=reset)
reset_button.grid(column=2, row=2)

# ✓
check_mark = Label(font=(FONT_NAME, 40), fg=GREEN, bg=PINK)
check_mark.grid(column=1, row=3)

def welcome_text():
    messagebox.showinfo(message="Welcome to the Pomodoro Timer!"
                                "\nEach work session is 25 minutes long, then you get a quick 5 minutes break."
                                "\nAfter 4 work sessions, you get a 20 minutes break to recharge your batteries."
                                "\nAfter each work session or break, you will get a sound allert, so that it's easier"
                                " for you to keep up with the timer."
                                "\nAfter you're done, press 'Reset' and then 'Start' to start the Pomodoro Timer again!")





window.mainloop()
