from tkinter import *
from tkinter import messagebox

""" Define global variables """
size_text = None
selected = None
window = None

size = None
poison_location = None


def start_window():
    global size_text
    global selected
    global window
    
    window = Tk()
    window.title("Chomp Game")
    window.geometry('1000x500')

    hello = Label(window, text="Hello!", font=("Berlin Sans FB", 30), fg="brown").grid(column=1, row=0)

    welcome = Label(window, text="Welcome to our game", font=("Berlin Sans FB", 20)).grid(column=1, row=2)

    empty1 = Label(window, font=("Berlin Sans FB", 20)).grid(column=1, row=22)

    size_que = Label(window, text='board size:   3*', font=("Calibri", 15)).grid(row=126)
    size_text = Entry(window)
    size_text.grid(row=126, column=1)

    empty2 = Label(window, font=("Berlin Sans FB", 20)).grid(column=1, row=130)

    poisons = Label(window, text="location of the poisons:", font=("Calibri", 13)).grid(column=0, row=140)

    image1 = PhotoImage(file="data\ex1.ppm")
    image2 = PhotoImage(file="data\ex2.ppm")
    image3 = PhotoImage(file="data\ex3.ppm")
    image4 = PhotoImage(file="data\ex4.ppm")

    selected = IntVar()
    rad1 = Radiobutton(window, font=("Calibri", 12), image = image1, value=1, variable=selected, compound="bottom").grid(column=0, row=141)
    rad2 = Radiobutton(window, font=("Calibri", 12), image = image2, value=2, variable=selected).grid(column=1, row=141)
    rad3 = Radiobutton(window, font=("Calibri", 12), image = image3, value=3, variable=selected).grid(column=2, row=141)
    empty3 = Label(window).grid(column=10, row=141)
    rad4 = Radiobutton(window, font=("Calibri", 12), image = image4, value=4, variable=selected).grid(column=11, row=141)

    empty4 = Label(window, font=("Berlin Sans FB", 20)).grid(column=1, row=145)

    btn = Button(window, text="start game",font=("Calibri", 12), command=clicked).grid(column=1, row=150)

    window.mainloop()


def win_window():
    window = Tk()
    window.title("Congratulations")
    window.geometry('460x600')

    Congratulations = Label(window, text="Congratulations!", font=("Berlin Sans FB", 30), fg="brown").grid(column=1, row=0)
    win = Label(window, text="You win", font=("Berlin Sans FB", 20)).grid(column=1, row=2)

    image = PhotoImage(file="data\you win.ppm")
    im = Label(window, image=image).grid(column=1, row=4)

    window.mainloop()

def lose_window(flag = False):
    window = Tk()
    window.title("lose")
    window.geometry('460x600')

    Congratulations = Label(window, text="You lose....", font=("Berlin Sans FB", 30), fg="brown").grid(column=1, row=0)
    win = Label(window, text="You can try again", font=("Berlin Sans FB", 20)).grid(column=1, row=2)

    image = PhotoImage(file="data\you lose.ppm")
    im = Label(window, image=image).grid(column=1, row=4)

    if flag:
        poison_message()
    
    window.mainloop()

def clicked():
    global window
    global size
    global poison_location
    
    size = int(size_text.get())
    poison_location = int(selected.get())

    if size > 50:
        messagebox.showinfo('Message title', 'board size is limited to 50')
    else:
        window.destroy()

def poison_message():
    global window
    messagebox.showinfo('Message title', 'Clarification: Pressing poison causes loss')

def get_size():
    return size

def get_poison_location():
    return poison_location

