import mysql.connector
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import Label, Entry, Button, StringVar
import webbrowser
import os
def fetch_data():
    # Establish the database connection
    conn = mysql.connector.connect(
        host='localhost',      # e.g., 'localhost'
        user='root',  # e.g., 'root'
        password='',
        database='bookshop'
    )
    
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM add_book")
    
    # Fetch the data
    rows = cursor.fetchall()
    
    # Fetch column names
    cursor.execute("SHOW COLUMNS FROM add_book")
    columns = [column[0] for column in cursor.fetchall()]
    
    conn.close()
    
    return columns, rows

def populate_treeview(tree, columns, rows):
    # Clear any existing data in the treeview
    for row in tree.get_children():
        tree.delete(row)
    
    # Insert new data
    for row in rows:
        tree.insert("", "end", values=row)

def open_website():
    webbrowser.open("https://paytm.com/")



def create_window(columns, rows, image_path):
    root = tk.Tk()
    root.title("SELL BOOK")

    def com():
        root.destroy()
        os.system("python -u front.py") 

    # Load the background image
    bg_image = Image.open("SELL.png")
    bg_photo = ImageTk.PhotoImage(bg_image)

    canvas = tk.Canvas(root, width=bg_photo.width(), height=bg_photo.height())
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=bg_photo, anchor="nw")

    # Create the Treeview widget in the specified area
    tree_frame = tk.Frame(root, bg="white")
    tree_frame.place(x=148, y=220, width=600, height=205)

    tree = ttk.Treeview(tree_frame, columns=columns, show='headings')

    # Define headings
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=100)
    
    tree.pack(fill=tk.BOTH, expand=True)

    # Populate the treeview with data
    populate_treeview(tree, columns, rows)
    root.resizable(False, False)
    back_button = Button(root, text="BACK TO MAIN", font=("Helvetica", 12), bg="red", fg="white",command=com)
    back_button.place(x=180, y=150)
    back_button = Button(root, text="PURCHASE BOOK", font=("Helvetica", 12), bg="yellow", fg="black",command=open_website)
    back_button.place(x=580, y=150)
    root.mainloop()

if __name__ == "__main__":
    columns, rows = fetch_data()
    image_path = "/mnt/data/SELL.png"
    create_window(columns, rows, image_path)
