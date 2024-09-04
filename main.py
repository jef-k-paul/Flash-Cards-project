from tkinter import *
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"
current_wrd = {}
to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except:
    orignal_data = pandas.read_csv("data/french_words.csv")
    to_learn = orignal_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_crd():
    global current_wrd, flip_timer
    window.after_cancel(flip_timer)
    current_wrd = random.choice(to_learn)
    canvas.itemconfig(canvas_title, text="French", fill="black")
    canvas.itemconfig(canvas_word, text=current_wrd["French"], fill="black")
    canvas.itemconfig(canvas_bg, image=card_front)
    window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(canvas_title, text="English", fill="white")
    canvas.itemconfig(canvas_word, text=current_wrd["English"], fill="white")
    canvas.itemconfig(canvas_bg, image=canvas_bac_img)


def known_wrd():
    to_learn.remove(current_wrd)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)

    next_crd()


window = Tk()
window.title("Flash Card Application")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


flip_timer = window.after(3000, func=flip_card)


canvas = Canvas(width=800, height=526)
card_front = PhotoImage(file="images/card_front.png")
canvas_bac_img = PhotoImage(file="images/card_back.png")
canvas_bg = canvas.create_image(400, 263, image=card_front)
canvas_title = canvas.create_text(400, 150, text="", font=('Arial', 40, "italic"))
canvas_word = canvas.create_text(400, 263, text="", font=("Arial", 40, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)


cross_img = PhotoImage(file="images/wrong.png")
unknown_btn = Button(image=cross_img, highlightthickness=0, command=next_crd)
unknown_btn.grid(row=1, column=0)


tick_img = PhotoImage(file="images/right.png")
known_btn = Button(image=tick_img, highlightthickness=0, command=known_wrd)
known_btn.grid(row=1, column=1)


next_crd()

window.mainloop()
