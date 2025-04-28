'''Book Recommender'''
# Date: 24/3/2025
#                  Imports
# used to create a custom window for age calculator
import tkinter as tk
import tkinter as tk2
from tkinter import messagebox
from tkinter import ttk

#import book_data
import book_data
#import window2

#import random for random selection of books
import random

#global counter
global counter
counter = 1

#functions
def window2():
    global counter

    #counter logic
    if counter < 2:
        window2 = tk2.Tk()
        window2.geometry("350x350")
        window2.config(bg="#F7DC6F")
        window2.resizable(width=False, height=False)
        window2.title('Already Read Books')

        # Labels for window 2
        # label for displaying the already read books
        lb_yourbooks = tk2.Label(window2, text="Your already books are: ", font=("Arial", 12, "bold"), fg="darkgreen", bg="#F7DC6F")

        def exit():
            window2.destroy()

        btn_exit2 = tk2.Button(window2, text="Exit", font=("Arial", 13), command=exit)

        # window 2
        btn_exit2.place(x=100, y=310)
        lb_yourbooks.place(x=70, y=5)

        counter +=1

    tk2.mainloop()

def rec_book():
    global current_book_key
    global current_genre
    # get the genre input
    genre = combo.get().lower()

    current_book = None

    # choose random book in genres
    if genre == "romance":
        if book_data.romance:  # Check if there are books left
            # Get a random book key
            book_key = random.choice(list(book_data.romance.keys()))
            # Get the book data
            current_book = book_data.romance[book_key]
            # Display the book
            display_rbook(f"Title: {current_book['name']}\nAuthor: {current_book['author']}\nISBN: {current_book['ISBN']}\nKeywords: {current_book['keywords']}")
            # Store the current book key as a global variable for the "Read Already" button

            current_book_key = book_key
            current_genre = "romance"
            print(f"Selected: {book_key} - {current_book['name']}")
        else:
            messagebox.showinfo("No Books Left", "You've read all the romance books!")
            print(already_read)

    elif genre == "dystopian":
        if book_data.dystopian:  # Check if there are books left
            # Get a random book key
            book_key = random.choice(list(book_data.dystopian.keys()))
            # Get the book data
            current_book = book_data.dystopian[book_key]
            # Display the book
            display_rbook(
                f"Title: {current_book['name']}\nAuthor: {current_book['author']}\nISBN: {current_book['ISBN']}\nKeywords: {current_book['keywords']}")
            # Store the current book key as a global variable for the "Read Already" button
            current_book_key = book_key
            current_genre = "dystopian"
            print(f"Selected: {book_key} - {current_book['name']}")
        else:
            messagebox.showinfo("No Books Left", "You've read all the dystopian books!")
            print(already_read)

    elif genre == "fantasy":
        if book_data.fantasy:  # Check if there are books left
            # Get a random book key
            book_key = random.choice(list(book_data.fantasy.keys()))
            # Get the book data
            current_book = book_data.fantasy[book_key]
            # Display the book
            display_rbook(
                f"Title: {current_book['name']}\nAuthor: {current_book['author']}\nISBN: {current_book['ISBN']}\nKeywords: {current_book['keywords']}")
            # Store the current book key as a global variable for the "Read Already" button
            current_book_key = book_key
            current_genre = "fantasy"
            print(f"Selected: {book_key} - {current_book['name']}")
        else:
            messagebox.showinfo("No Books Left", "You've read all the fantasy books!")
            print(already_read)

    elif genre == "suspense":
        if book_data.suspense:  # Check if there are books left
            # Get a random book key
            book_key = random.choice(list(book_data.suspense.keys()))
            # Get the book data
            current_book = book_data.suspense[book_key]
            # Display the book
            display_rbook(
                f"Title: {current_book['name']}\nAuthor: {current_book['author']}\nISBN: {current_book['ISBN']}\nKeywords: {current_book['keywords']}")
            # Store the current book key as a global variable for the "Read Already" button
            current_book_key = book_key
            current_genre = "suspense"
            print(f"Selected: {book_key} - {current_book['name']}")
        else:
            messagebox.showinfo("No Books Left", "You've read all the suspense books!")
            print(already_read)

    else:
        messagebox.showinfo("Genre Not Found", f"Sorry, we don't have books in the '{genre}' genre.")

#empty list for already read books to be added:
already_read = []

# Create a new function for the "Read Already" button
def mark_as_read():
    global current_book_key
    print("Mark as read: ", current_book_key)
    global current_genre
    # Check if a book is currently selected
    if current_book_key is None or current_genre is None:
        messagebox.showinfo("No Book Selected", "Please recommend a book first!")
        return

    # Remove the book from the appropriate dictionary
    if current_genre == "romance":
        if current_book_key in book_data.romance:
            read_already = (list(current_book_key))
            read_already.append(current_book_key)
            print("read list", read_already)
            removed_book = book_data.romance.pop(current_book_key)
            messagebox.showinfo("Book Removed",
                                f"'{removed_book['name']}' has been removed from your recommendations.")
            # Clear the display
            tbox_genre.config(state='normal')
            tbox_genre.delete('1.0', tk.END)
            tbox_genre.config(state='disabled')

            #add to already read list
            already_read.insert(0, read_already)

            # Reset the current book
            current_book_key = None
            current_genre = None

    elif current_genre == "dystopian":
        if current_book_key in book_data.dystopian:
            read_already = (list(current_book_key))
            read_already.append(current_book_key)
            print("read list", read_already)
            removed_book = book_data.dystopian.pop(current_book_key)
            messagebox.showinfo("Book Removed",
                                f"'{removed_book['name']}' has been removed from your recommendations.")
            # Clear the display
            tbox_genre.config(state='normal')
            tbox_genre.delete('1.0', tk.END)
            tbox_genre.config(state='disabled')

            # add to already read list
            already_read.insert(0, read_already)

            # Reset the current book
            current_book_key = None
            current_genre = None

    elif current_genre == "fantasy":
        if current_book_key in book_data.fantasy:
            read_already = (list(current_book_key))
            read_already.append(current_book_key)
            print("read list", read_already)
            removed_book = book_data.fantasy.pop(current_book_key)
            messagebox.showinfo("Book Removed",
                                f"'{removed_book['name']}' has been removed from your recommendations.")
            # Clear the display
            tbox_genre.config(state='normal')
            tbox_genre.delete('1.0', tk.END)
            tbox_genre.config(state='disabled')

            # add to already read list
            already_read.insert(0, read_already)

            # Reset the current book
            current_book_key = None
            current_genre = None

    elif current_genre == "suspense":
        if current_book_key in book_data.suspense:
            read_already = (list(current_book_key))
            read_already.append(current_book_key)
            print("read list", read_already)
            removed_book = book_data.suspense.pop(current_book_key)
            messagebox.showinfo("Book Removed",
                                f"'{removed_book['name']}' has been removed from your recommendations.")
            # Clear the display
            tbox_genre.config(state='normal')
            tbox_genre.delete('1.0', tk.END)
            tbox_genre.config(state='disabled')

            # add to already read list
            already_read.insert(0, read_already)

            # Reset the current book
            current_book_key = None
            current_genre = None


def display_rbook(book):
    tbox_genre.config(state='normal')
    ##book info is dispayed in the text boz after clearning the previous info in the textbox
    tbox_genre.delete('1.0', tk.END)
    tbox_genre.insert(tk.END, book)
    tbox_genre.config(state='disabled')

def exit():
    window1.destroy()

#global variables
current_book_key = None
current_genre = None
global read_already_list

# MAIN

# creating custom window 1
window1 = tk.Tk()
window1.geometry("350x350")
window1.config(bg="#F7DC6F")
window1.resizable(width=False, height=False)
window1.title('Book Recommender!')




# Combobox for genres
combo = ttk.Combobox(
    state="radonly",
    values=["Romance", "Dystopian", "Fantasy", "Suspense"]
)

#Labels for window 1
# Labels for heading and subheading of GUI
lb_heading = tk.Label(text="Book Recommender!", font=("Arial", 20), fg="black", bg="#F7DC6F")
lb_subheading = tk.Label(font=("Arial", 12), text="Enter your favourite genre.",
                         fg="black", bg="#F7DC6F")

# Labels for date, month and year
lb_genre = tk.Label(text="Genre: ", font=('Arial', 12, "bold"), fg="darkgreen", bg="#F7DC6F")

# Label for text box that will display the book
lb_rbook = tk.Label(text="The recommended book for your is: ", font=('Arial', 12, "bold"), fg="darkgreen",
                             bg="#F7DC6F")
tbox_genre = tk.Text(width=30, height=6, state="disabled")


# Button to recomend book
btn_recomend_book = tk.Button(text="Recommend Book!", font=("Arial", 13), command=rec_book)

# Button to exit application for both windows
btn_exit = tk.Button(text="Exit", font=("Arial", 13), command=exit)


#button to re-recomend book
btn_read = tk.Button(text="Read Already", font=("Arial", 13), command=mark_as_read)
                     #if pressed, then take out current book from list to be chosen
#button to display all already read books
btn_showread = tk.Button(window1, text="Show read books", font=("Arial", 13), command=window2)



# Placing the elements on
# window1
lb_heading.place(x=70, y=5)
lb_subheading.place(x=50, y=40)
lb_genre.place(x=100, y=70)
combo.place(x=180, y=70)
btn_recomend_book.place(x=100, y=100)
btn_read.place(x=120, y=140)
lb_rbook.place(x=50, y=170)
tbox_genre.place(x=50, y=200)
btn_exit.place(x=100, y=310)
btn_showread.place(x=170, y=310)



tk.mainloop()