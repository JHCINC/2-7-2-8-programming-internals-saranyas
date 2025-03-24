'''Book Recommender'''
# Date: 24/3/2025
#                  Imports
# used to create a custom window for age calculator
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# MAIN

# creating custom window
window = tk.Tk()
window.geometry("300x300")
window.config(bg="#F7DC6F")
window.resizable(width=False, height=False)
window.title('Book Recommender!')

# Entry boxes for date, month and year
e_genre = tk.Entry(window, width=5)

# Labels for heading and subheading of GUI
lb_heading = tk.Label(window, text="Book Recommender!", font=("Arial", 20), fg="black", bg="#F7DC6F")
lb_subheading = tk.Label(window, font=("Arial", 12), text="Enter your favourite genre.",
                         fg="black", bg="#F7DC6F")

# Labels for date, month and year
lb_genre = tk.Label(window, text="Genre: ", font=('Arial', 12, "bold"), fg="darkgreen", bg="#F7DC6F")

# Label for text box that will display the calculated age
lb_rbook = tk.Label(window, text="The recommended book for your is: ", font=('Arial', 12, "bold"), fg="darkgreen",
                             bg="#F7DC6F")
tbox_genre = tk.Text(window, width=5, height=0, state="disabled")


# Functions
def rec_book():
    # get the genre input
    g = (e_genre.get())

  #  rec_book = randomise generator book
    #display_calc_age(calc_age) # display recommended book


#def find_book(g):
   #find book for reader
    #book = randomise genrator thingie


def display_rec_book(book):
    tbox_genre.config(state='normal')
    ##book info is dispayed in the text boz after clearning the previous info in the textbox
    tbox_genre.delete('1.0', tk.END)
    tbox_genre.insert(tk.END, rec_book)
    tbox_genre.config(state='disabled')


# Button to calculate age
btn_calculate_age = tk.Button(window, text="Recommend Book!", font=("Arial", 13), command=rec_book)

# Button to exit application
btn_exit = tk.Button(window, text="Exit Application!", font=("Arial", 13), command=exit)


def exit():
    window.destroy()


# Placing the elements on the screen
lb_heading.place(x=70, y=5)
lb_subheading.place(x=10, y=40)
lb_genre.place(x=100, y=70)
e_genre.place(x=180, y=70)
btn_calculate_age.place(x=100, y=150)
lb_rbook.place(x=50, y=200)
tbox_genre.place(x=240, y=203)
btn_exit.place(x=100, y=230)

tk.mainloop()