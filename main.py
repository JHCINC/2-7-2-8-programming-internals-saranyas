'''Book Recommender'''
# Date: 24/3/2025
#                  Imports
# used to create a custom window
import tkinter as tk
import tkinter as tk2
from tkinter import messagebox
from tkinter import ttk

#import book_data
import book_data

#import random for random selection of books
import random

#functions

def display_already_read():
    # Get reference to the text box in window2
    global tbox_read_already


    # Enable the textbox for editing
    tbox_read_already.config(state='normal')
    tbox_read_already.delete('1.0', tk2.END)

    # Add each book from the already read list to the textbox
    if already_read_list:
        for item in already_read_list:
            if isinstance(item, list):
                book_key = ''.join(item[:-1])  # Convert list of characters back to string
                tbox_read_already.insert(tk2.END, str(book_key) + "\n")
            else:
                tbox_read_already.insert(tk2.END, str(item) + "\n")
    else:
        tbox_read_already.insert(tk2.END, "No books in your read list yet.")

    # Disable the textbox again
    tbox_read_already.config(state='disabled')

#rec book for recomend a book
def rec_book():
    global current_book_key
    global current_genre
    # get the genre input
    genre = combo.get().lower()

    current_book = None

    # choose random book in genres
    #in romance
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
            print(already_read_list)

    #in dystopian
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
            print(already_read_list)

    #in fantasy
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
            print(already_read_list)

    #in suspence
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
            print(already_read_list)

    else:
        messagebox.showinfo("Genre Not Found", f"Sorry, we don't have books in the '{genre}' genre. Please choose a genre from the dropdown menu.")



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
    #from romance
    if current_genre == "romance":
        if current_book_key in book_data.romance:
            read_already = (list(current_book_key))
            read_already.append(current_book_key)
            print("read list", read_already)
            removed_book = book_data.romance.pop(current_book_key)
            messagebox.showinfo("Book Removed",
                                f"'{removed_book['name']}' has been removed from your recommendations.")
            # Clear the display
            tbox_book.config(state='normal')
            tbox_book.delete('1.0', tk.END)
            tbox_book.config(state='disabled')

            #add to already read list
            already_read_list.insert(0, read_already)

            # Reset the current book
            current_book_key = None
            current_genre = None

    #from dystopian
    elif current_genre == "dystopian":
        if current_book_key in book_data.dystopian:
            read_already = (list(current_book_key))
            read_already.append(current_book_key)
            print("read list", read_already)
            removed_book = book_data.dystopian.pop(current_book_key)
            messagebox.showinfo("Book Removed",
                                f"'{removed_book['name']}' has been removed from your recommendations.")
            # Clear the display
            tbox_book.config(state='normal')
            tbox_book.delete('1.0', tk.END)
            tbox_book.config(state='disabled')

            # add to already read list
            already_read_list.insert(0, read_already)

            # Reset the current book
            current_book_key = None
            current_genre = None

    #from fantasy
    elif current_genre == "fantasy":
        if current_book_key in book_data.fantasy:
            read_already = (list(current_book_key))
            read_already.append(current_book_key)
            print("read list", read_already)
            removed_book = book_data.fantasy.pop(current_book_key)
            messagebox.showinfo("Book Removed",
                                f"'{removed_book['name']}' has been removed from your recommendations.")
            # Clear the display
            tbox_book.config(state='normal')
            tbox_book.delete('1.0', tk.END)
            tbox_book.config(state='disabled')

            # add to already read list
            already_read_list.insert(0, read_already)

            # Reset the current book
            current_book_key = None
            current_genre = None

    #from suspence
    elif current_genre == "suspense":
        if current_book_key in book_data.suspense:
            read_already = (list(current_book_key))
            read_already.append(current_book_key)
            print("read list", read_already)
            removed_book = book_data.suspense.pop(current_book_key)
            messagebox.showinfo("Book Removed",
                                f"'{removed_book['name']}' has been removed from your recommendations.")
            # Clear the display
            tbox_book.config(state='normal')
            tbox_book.delete('1.0', tk.END)
            tbox_book.config(state='disabled')

            # add to already read list
            already_read_list.insert(0, read_already)

            # Reset the current book
            current_book_key = None
            current_genre = None

#to display recomended book
def display_rbook(book):
    tbox_book.config(state='normal')
    ##book info is dispayed in the text boz after clearning the previous info in the textbox
    tbox_book.delete('1.0', tk.END)
    tbox_book.insert(tk.END, book)
    tbox_book.config(state='disabled')

#exit
def exit():
    window1.destroy()



#global variables
current_book_key = None
current_genre = None
global already_read_list
window_2 = None
tboz_read_already = None
#empty list for already read books to be added:
already_read_list = []


ontop = False

def setflag(event):
    global ontop
    ontop = False


#top = window 2
def top():
    global ontop, window_2, tbox_read_already
    if not ontop:
        window_2 = tk.Toplevel()
        window_2.geometry("350x350")
        window_2.config(bg="#4ecdc4")
        window_2.resizable(width=False, height=False)
        window_2.title('Already Read Books')

        def exit_2():
            window_2.destroy()

        # Labels for window 2
        # Label for displaying the already read books
        lb_yourbooks = tk.Label(window_2, text="Your already read books are: ",
                                 font=("Arial", 12, "bold"), fg="#1a535c", bg="#4ecdc4")

        # Exit button
        btn_exit2 = tk.Button(window_2, text="Back Home", font=("Arial", 13), command=exit_2)

        # Box to display the books names:
        tbox_read_already = tk.Text(window_2, width=30, height=15)


        # Call the function to display already read books
        display_already_read()

        # top things place
        btn_exit2.place(x=100, y=310)
        lb_yourbooks.place(x=70, y=5)
        tbox_read_already.place(x=50, y=50)

        # Set the ontop flag to True and bind the destroy event to reset the flag
        window_2.bind('<Destroy>', setflag)
    ontop = True

#MAIN

# creating custom window 1
window1 = tk.Tk()
window1.geometry("350x350")
window1.config(bg="#4ecdc4")
window1.title('Book Recommender!')

#button to display all already read books
root = window1
btn_showread = tk.Button(window1, text="Show read books", font=("Arial", 13), command=top)
btn_showread.pack()



# Combobox for genres
combo = ttk.Combobox(
    state="radonly",
    values=["Romance", "Dystopian", "Fantasy", "Suspense"]
)

#Labels for window 1
# Labels for heading and subheading of GUI
lb_heading = tk.Label(window1,text="Book Recommender!", font=("Arial", 20), fg="black", bg="#4ecdc4")
lb_subheading = tk.Label(window1,font=("Arial", 12), text="Enter your favourite genre.",
                         fg="black", bg="#4ecdc4")

# Labels for date, month and year
lb_genre = tk.Label(window1,text="Genre: ", font=('Arial', 12, "bold"), fg="#1a535c", bg="#4ecdc4")

# Label for text box that will display the book
lb_rbook = tk.Label(window1,text="The recommended book for your is: ", font=('Arial', 12, "bold"), fg="#1a535c",
                             bg="#4ecdc4")
tbox_book = tk.Text(window1,width=30, height=6, state="disabled")


# Button to recomend book
btn_recomend_book = tk.Button(window1,text="Recommend Book!", font=("Arial", 13), command=rec_book)

# Button to exit application for both windows
btn_exit = tk.Button(window1,text="Exit", font=("Arial", 13), command=exit)


#button to re-recomend book
btn_read = tk.Button(window1, text="Read Already", font=("Arial", 13), command=mark_as_read)
                     #if pressed, then take out current book from list to be chosen




# Placing the elements on
# window1
lb_heading.place(x=70, y=5)
lb_subheading.place(x=50, y=40)
lb_genre.place(x=100, y=70)
combo.place(x=180, y=70)
btn_recomend_book.place(x=100, y=100)
btn_read.place(x=120, y=140)
lb_rbook.place(x=50, y=170)
tbox_book.place(x=50, y=200)
btn_exit.place(x=100, y=310)
btn_showread.place(x=170, y=310)




tk.mainloop()