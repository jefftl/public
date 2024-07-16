from tkinter import *
import time
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK = "✔"
TEXT = ""
reps = 0
timer = None

def reset_pom():
    global reps
    global TEXT
    global timer
    reps = 0
    TEXT = ""
    window.after_cancel(timer)
    checkbox.config(text=TEXT)
    title_label.config(text="Timer")
    canvas.itemconfig(timer_text, text=f"00:00")


def start_timer():
    global reps
    global TEXT
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_min = LONG_BREAK_MIN*60
    if reps in [0, 2, 4, 6]:
        countdown(work_sec)
        title_label.config(text="Work")
        reps += 1
    elif reps in [1, 3, 5]:
        countdown(short_break_sec)
        title_label.config(text="Short Break")
        reps += 1
    else:
        countdown(long_break_min)
        title_label.config(text="Long Break")
        reps = 0
        TEXT = ""
        checkbox.config(text=TEXT)



window = Tk()
window.title("Pomodoro")
# window.minsize(width=500, height=500)
window.config(padx=100, pady=50, bg=YELLOW)

# Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="Pomodoro/tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


def countdown(count):
    global reps
    global TEXT
    global CHECK
    global timer
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, countdown, count - 1)
    else:
        title_label.config(text="Timer")
        if reps in [1, 3, 5, 7]:
            TEXT += CHECK
            checkbox.config(text=TEXT)


# title_label
title_label = Label(text="Timer", font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=GREEN)
title_label.grid(column=1, row=0)
title_label.config(padx=20, pady=20)

# checkbox
checkbox = Label(text=TEXT, font=(FONT_NAME, 20, "bold"), bg=YELLOW, fg=GREEN)
checkbox.grid(column=1, row=3)
checkbox.config(padx=20, pady=20)

# start_button
start_button = Button(text="Start", font=(FONT_NAME, 20, "bold"), bg=YELLOW, command=start_timer)
start_button.grid(column=0, row=4)

# reset_button
reset_button = Button(text="Reset", font=(FONT_NAME, 20, "bold"), bg=YELLOW, command=reset_pom)
reset_button.grid(column=2, row=4)

window.mainloop()
