'''Book Recommender'''
# Date: 24/3/2025
#                  Imports
# used to create a custom window for age calculator
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

#import book_data
import book_data

#import random for random selection of books
import random



# MAIN

# creating custom window
window = tk.Tk()
window.geometry("350x350")
window.config(bg="#F7DC6F")
window.resizable(width=False, height=False)
window.title('Book Recommender!')

# Entry boxes for fav genre
e_genre = tk.Entry(window, width=18)

# Labels for heading and subheading of GUI
lb_heading = tk.Label(window, text="Book Recommender!", font=("Arial", 20), fg="black", bg="#F7DC6F")
lb_subheading = tk.Label(window, font=("Arial", 12), text="Enter your favourite genre.",
                         fg="black", bg="#F7DC6F")

# Labels for date, month and year
lb_genre = tk.Label(window, text="Genre: ", font=('Arial', 12, "bold"), fg="darkgreen", bg="#F7DC6F")

# Label for text box that will display the book
lb_rbook = tk.Label(window, text="The recommended book for your is: ", font=('Arial', 12, "bold"), fg="darkgreen",
                             bg="#F7DC6F")
tbox_genre = tk.Text(window, width=30, height=6, state="disabled")


# Functions
def rec_book():
    # get the genre input
    g = e_genre.get()

    #choose random book in genres
    if g == "romance":
        rom = random.choice(list(book_data.romance.items()))
        print(rom)
        display_rbook(rom)
        g.pop(rom)

    elif g == "dystopian":
        dys = random.choice(list(book_data.dystopian.items()))
        print(dys)
        display_rbook(dys)

    def rbook():
        rbook = rec_book
        tbox_book.config(state='normal')


#def find_book(g):
   #find book for reader
    #book = randomise genrator thingie


def display_rbook(book):
    tbox_genre.config(state='normal')
    ##book info is dispayed in the text boz after clearning the previous info in the textbox
    tbox_genre.delete('1.0', tk.END)
    tbox_genre.insert(tk.END, book)
    tbox_genre.config(state='disabled')


# Button to recomend book
btn_recomend_book = tk.Button(window, text="Recommend Book!", font=("Arial", 13), command=rec_book)

# Button to exit application
btn_exit = tk.Button(window, text="Exit Application!", font=("Arial", 13), command=exit)

#button to re-recomend book
btn_read = tk.Button(window, text="Read Already", font=("Arial", 13), command=rec_book)
                     #if pressed, then take out current book from list to be chosen


def exit():
    window.destroy()


# Placing the elements on the screen
lb_heading.place(x=70, y=5)
lb_subheading.place(x=50, y=40)
lb_genre.place(x=100, y=70)
e_genre.place(x=180, y=70)
btn_recomend_book.place(x=100, y=100)
btn_read.place(x=120, y=140)
lb_rbook.place(x=50, y=170)
tbox_genre.place(x=50, y=200)
btn_exit.place(x=100, y=310)

tk.mainloop()