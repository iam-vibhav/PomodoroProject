import tkinter as tk
from pygame import mixer
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 1
CHECK_MARK = "✔"
STREAK = ""
TIMER = None
mixer.init()
mixer.music.load("AruarianDance.mp3")

# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    window.after_cancel(TIMER)
    global STREAK
    STREAK = ""
    checkmark.config(text=STREAK)
    global REPS
    REPS = 1
    timer.config(text="TIMER", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")




# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global REPS
    if (REPS % 2 == 1) and (REPS < 8):
        update_timer_text()
        count_down(WORK_MIN*60)
        mixer.music.stop()
    elif (REPS % 2 == 0) and (REPS < 8):
        update_timer_text()
        count_down(SHORT_BREAK_MIN*60)
        update_checkmark_text()
        mixer.music.play()
    elif REPS == 8:
        update_timer_text()
        count_down(LONG_BREAK_MIN*60)
        update_checkmark_text()
    else:
        pass


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def update_timer_text():
    if (REPS % 2 == 1) and (REPS < 8):
        timer.config(text="WORK!!!", fg=GREEN)
    elif (REPS % 2 == 0) and (REPS < 8):
        timer.config(text="SMALL BREAK", fg=PINK)
    else:
        timer.config(text="LONG BREAK", fg=RED)


def update_checkmark_text():
    global REPS
    if (REPS % 2 == 0) and (REPS <= 8):
        global STREAK
        STREAK += CHECK_MARK
        checkmark.config(text=STREAK)


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer = tk.Label()
timer.config(text="TIMER", fg=GREEN, bg=YELLOW, justify="center",  font=(FONT_NAME, 50, "bold"), highlightthickness=0)
timer.grid(column=1, row=1)


canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = tk.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)


def count_down(count):
    count_min = count // 60
    count_sec = count % 60
    if count_sec < 10:
        count_sec = "0" + str(count_sec)
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global TIMER
        TIMER = window.after(1000, count_down, count-1)
    if count == 0:
        global REPS
        REPS += 1
        start_timer()


timer_text = canvas.create_text(102, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=2)

start = tk.Button(text="Start", command=start_timer, highlightthickness=0)
start.grid(column=0, row=4)

reset = tk.Button(text="Reset", command=reset_timer, highlightthickness=0)
reset.grid(column=2, row=4)


checkmark = tk.Label()
checkmark.config(text=STREAK, fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"), highlightthickness=0)
checkmark.grid(column=1, row=4)

window.mainloop()

