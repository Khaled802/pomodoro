import tkinter
import time
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
BACKGROUND = '#FFBC80'
TEXTCOLOR = '#FC4F4F'
BTNTEXTCOLOR = '#F76E11'
CHECKCOLOR = '#3E7C17'
CHECKSIGHN = '✓'

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
# window
window = tkinter.Tk()
window.title("Promodoro")
window.config(padx=50, pady=20)
window.config(background=BACKGROUND)

# canvas of tomato
canvas = tkinter.Canvas(width=200, height=224)
photo_tomato = tkinter.PhotoImage(file='tomato.png')
time_show = canvas.create_image(100, 112, image=photo_tomato)
canvas.grid(column=1, row=1)
text_canvas = canvas.create_text(100, 130, text='00:00', fill='white',
                   font=(FONT_NAME, 28, 'bold'))
canvas.config(bg=BACKGROUND, highlightthickness=0)

# label
text = tkinter.Label(text='Timer', font=('Arial', 35, 'bold')
                     , bg=BACKGROUND, fg=TEXTCOLOR)
text.config(pady=10)
text.grid(column=1, row=0)

# start button
start_btn = tkinter.Button(text='start', fg=BTNTEXTCOLOR, font=('Arial', 12, 'bold'))
start_btn.grid(column=0, row=2)

# reset button
reset_btn = tkinter.Button(text='reset', fg=BTNTEXTCOLOR, font=('Arial', 12, 'bold'))
reset_btn.grid(column=2, row=2)

# label check
check_label = tkinter.Label(text='', bg=BACKGROUND,
                            fg=CHECKCOLOR, font=('Arial', 16, 'bold'))
check_label.grid(column=1, row=3)





def increase_sec(seconds, minutes):
    seconds += 1
    if seconds >= 60:
        minutes += 1
        seconds = 0
    return minutes, seconds


def conv_to_mmss(seconds, minutes):
    return f"{str(minutes).zfill(2)}:{str(seconds).zfill(2)}"
MINUTES = 0
SECONDS = 0
MAX_MINs = 1
s = ''
RESET = False


def update_display():
    global MINUTES, SECONDS, s
    show_time = conv_to_mmss(SECONDS, MINUTES)
    print(show_time)
    canvas.itemconfig(text_canvas, text=show_time)
    check_label.config(text=s)


def reset_promo():
    global RESET
    global MINUTES, SECONDS, s
    MINUTES = 0
    SECONDS = 0
    s = ''
    update_display()
    RESET = True


def after_click_start():
    global MINUTES, SECONDS, s, RESET

    MINUTES, SECONDS = increase_sec(SECONDS, MINUTES)
    if RESET:
        reset_promo()
        RESET = False
        return
    if MINUTES >= MAX_MINs:
        s += CHECKSIGHN
        check_label.config(text=s)
        update_display()
        MINUTES = SECONDS = 0
        window.attributes('-topmost', True)
        window.attributes('-topmost', False)
        return

    update_display()
    canvas.after(1000, after_click_start)


start_btn.config(command=after_click_start)
reset_btn.config(command=reset_promo)
# window.bind('<Double-1>', )
window.mainloop()








