import tkinter as tk
from tkinter import Label, Entry, Button, StringVar
import mysql.connector as mysql
import tkinter.messagebox as Messagebox
import os
def insert_book():
    def insert1():
        book = booken.get()
        author = authoren.get()
        selling = sellingen.get()
        cost = costen.get()
        if (book == "" or author == "" or selling == "" or cost == ""):
            Messagebox.showinfo("Insert status", "All Fields are required!!")
        else:
            con = mysql.connect(host="localhost", user="root", password="", database="bookshop")
            cursor = con.cursor()
            cursor.execute("Insert into add_book values(%s, %s, %s, %s)", (book, author, selling, cost))
            con.commit()
            Messagebox.showinfo("Insert status", "Inserted Successfully")
            con.close()

    root = tk.Tk()
    root.title("Bookish bliss")
    root.geometry("1040x610")
    def com():
        root.destroy()
        os.system("python -u front.py") 

    background_image = tk.PhotoImage(file="design1.png")
    background_label = tk.Label(root, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    book = Label(root, text="Book Name", font=('bold', 15), bg="White")
    book.place(x=100, y=360)
    author = Label(root, text="Author", font=('bold', 15), bg="White")
    author.place(x=100, y=400)
    cost = Label(root, text="Selling price", font=('bold', 15), bg="White")
    cost.place(x=100, y=440)
    selling = Label(root, text="Cost price", font=('bold', 15), bg="White")
    selling.place(x=100, y=480)

    global booken, authoren, sellingen, costen
    booken = Entry(root, font=("Helvetica", 12), bg="#e1edf2", fg="black", bd=2, relief=tk.GROOVE)
    booken.place(x=230, y=365)
    authoren = Entry(root, font=("Helvetica", 12), bg="#e1edf2", fg="black", bd=2, relief=tk.GROOVE)
    authoren.place(x=230, y=405)
    sellingen = Entry(root, font=("Helvetica", 12), bg="#e1edf2", fg="black", bd=2, relief=tk.GROOVE)
    sellingen.place(x=230, y=445)
    costen = Entry(root, font=("Helvetica", 12), bg="#e1edf2", fg="black", bd=2, relief=tk.GROOVE)
    costen.place(x=230, y=485)

    back_button = Button(root, text="BACK TO MAIN", font=("Helvetica", 12), bg="red", fg="white",command=com)
    back_button.place(x=120, y=550)

    add_button = Button(root, text="ADD BOOK", font=("Helvetica", 12), bg="green", fg="white", command=insert1)
    add_button.place(x=280, y=550)

    root.mainloop()

# if you want to be able to run this file directly as a script
if __name__ == "__main__":
    insert_book()
