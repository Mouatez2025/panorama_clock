from tkinter import *
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
reps = 0
time = None


# ---------------------------- TIMER RESET ------------------------------- # 
def rest_timer():
    window.after_cancel(time)
    timer.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")

    check_mark.config(text="")
    global reps
    reps = 0



def start_timer():
    global reps

    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    # if it's the 1th/3th/5th/7th rep:
    # count_down(work_sec)

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer.config(text="Break", fg=RED)

    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        timer.config(text="Work", fg=GREEN)



# ---------------------------- TIMER MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sic = count % 60
    if count_sic < 10:
        count_sic = f"0{count_sic}"



    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sic}")
    if count > 0:
        global time
        time = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += "✓"
            check_mark.config(text=mark)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


timer = Label(text="Timer", fg=GREEN,bg=YELLOW, font=(FONT_NAME, 50))

timer.grid(column=2, row=1)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2,row=2)


# label = canvas(text="TIMER", font=("Arial", 12, "bold"), highlightthickness=0, bg=GREEN)
# label.grid(column=1, row=0)

reset = Button(text="Reset", command=rest_timer)
reset.grid(column=3, row=3)


start = Button(text="Start", highlightthickness=0, command=start_timer)
start.grid(column=1, row=3)



check_mark = Label(fg=GREEN, bg=YELLOW, highlightthickness=0 )

check_mark.grid(column=2, row=4)









window.mainloop()