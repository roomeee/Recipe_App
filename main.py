import tkinter as tk
from PIL import ImageTk
import sqlite3
from numpy import random
YELLOW = "#edc861"
DARK = '#e6a330'


def fetch_db():
    connection = sqlite3.connect("recipes (1).db")
    cursor = connection.cursor()
    # fetch all the table names
    cursor.execute("SELECT * FROM sqlite_schema WHERE type='table';")
    all_tables = cursor.fetchall()

    # choose random table idx
    idx = random.randint(0, len(all_tables) - 1)


    # fetch records from table
    table_name = all_tables[idx][1]
    cursor.execute("SELECT * FROM " + table_name + ";")
    table_records = cursor.fetchall()

    connection.close()

    return table_name, table_records


def load_frame1():
    frame1.pack_propagate(False)

    logo = ImageTk.PhotoImage(file="RRecipe_logo.png")
    log_wid = tk.Label(frame1, image=logo, bg="#edc861")
    log_wid.image = logo
    log_wid.pack()

    bel1 = tk.Label(frame1, text="Random recipe ",
                    bg=YELLOW,
                    fg="white",
                    font=("TkMenuFont", 14)
                    )
    bel1.pack()

    button = tk.Button(frame1,
                       text="SHUFFLE",
                       font=("TkHeadingFont", 20),
                       bg=DARK,
                       fg="white",
                       cursor="hand2",
                       activebackground=YELLOW,
                       activeforeground='black',
                       command=lambda: load_frame()
                       )
    button.pack(pady=20)


def load_frame():
    fetch_db()
    print('djdjd')


root = tk.Tk()

root.title('recipe picker')
root.eval("tk::PlaceWindow . center")

frame1 = tk.Frame(root, width=500, height=600, bg="#edc861")
frame2 = tk.Frame(root, bg="#edc861")

for frame in (frame1, frame2):
    frame.grid(row=0, column=0)
load_frame1()
root.mainloop()
