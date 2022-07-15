from secrets import choice
from tkinter import *
from matplotlib.pyplot import fill, text
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

#------------CSV & Cards---------------#
current_card = {}
try:
    data = pd.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    data = pd.read_csv('data/english_words.csv')
finally:
    data_dict = data.to_dict(orient='records')


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(data_dict)
    canvas.itemconfig(card_title, text='Englsih', fill='black')
    canvas.itemconfig(card_word, text=current_card['English'], fill='black')
    canvas.itemconfig(card_bg, image=card_front_img)
    window.after(3000, func=flip_cards)
    
#------------Flip Cards---------------#
def flip_cards():
    global current_card
    canvas.itemconfig(card_title, text='Español', fill='white')
    canvas.itemconfig(card_word, text=current_card['Spanish'], fill='white')
    canvas.itemconfig(card_bg, image=card_back_img)

def is_know():
    global current_card
    data_dict.remove(current_card)
    to_learn = pd.DataFrame(data_dict)
    to_learn.to_csv('data/words_to_learn.csv', index=False)
    next_card()

#------------UI CONFIG---------------#
window = Tk()
window.title("Cartitas para tu English")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


flip_timer = window.after(3000, func=flip_cards)

canvas =  Canvas(width=800, height=526)
card_back_img = PhotoImage(file='images/card_back.png')
card_front_img = PhotoImage(file='images/card_front.png')
card_bg = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text='Title', font=('Ariel', 40, 'italic'))
card_word = canvas.create_text(400, 263, text='word', font=('Ariel', 60, 'bold'))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

wrong_image = PhotoImage(file='images/wrong.png')
unkwon_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
unkwon_button.grid(row=1, column=0)

check_image = PhotoImage(file='images/right.png')
right_button = Button(image=check_image, highlightthickness=0, command=is_know)
right_button.grid(row=1, column=1)

next_card()

window.mainloop()