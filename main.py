from tkinter import *
import math
import winsound
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    logo.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    check_mark.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        logo.config(text="Break", fg=RED)
        count_down(long_break_sec)
        winsound.Beep(1500, 2000)
    elif reps % 2 == 0:
        logo.config(text="Break", fg=PINK)
        count_down(short_break_sec)
        winsound.Beep(1500, 2000)
    else:
        logo.config(text="Work", fg=GREEN)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    cont_sec = count % 60
    if cont_sec < 10:
        cont_sec = f"0{cont_sec}"


    canvas.itemconfig(timer_text, text=f"{count_min}:{cont_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            marks += "✔"
        check_mark.config(text=marks)



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro App")
window.config(padx=100, pady=50, bg=YELLOW)

logo = Label(text="Timer", fg=GREEN, bg=YELLOW)
logo.config(font=(FONT_NAME, 50, "bold"), anchor="center")
logo.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

button_start = Button(text="Start", font=FONT_NAME, highlightthickness=0, command=start_timer)
button_start.config(bg="white")
button_start.grid(column=0, row=2)

check_mark = Label(text="", fg=GREEN, bg=YELLOW)
check_mark.config(font=("", 18))
check_mark.grid(column=1, row=3)

button_reset = Button(text="Reset", font=FONT_NAME, highlightthickness=0, command=reset_timer)
button_reset.config(bg="white")
button_reset.grid(column=2, row=2)

window.mainloop()