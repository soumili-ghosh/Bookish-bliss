import mysql.connector
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import Button
import os

def fetch_data():
        # Establish the database connection
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
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

def create_window(columns, rows, image_path):
        root = tk.Tk()
        root.title("Bookish bliss")
        def com():
            root.destroy()
            os.system("python -u front.py") 
        # Load the background image
        bg_image = Image.open(image_path)
        bg_photo = ImageTk.PhotoImage(bg_image)

        canvas = tk.Canvas(root, width=bg_photo.width(), height=bg_photo.height())
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=bg_photo, anchor="nw")

        # Keep a reference to the image object to prevent it from being garbage collected
        canvas.image = bg_photo

        # Create the Treeview widget in the specified area
        tree_frame = tk.Frame(root, bg="white")
        tree_frame.place(x=148, y=230, width=664, height=235)

        tree = ttk.Treeview(tree_frame, columns=columns, show='headings')

        # Define headings
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=100)

        tree.pack(fill=tk.BOTH, expand=True)

        # Populate the treeview with data
        populate_treeview(tree, columns, rows)

        # Add the BACK TO MAIN button
        back_button = Button(root, text="BACK TO MAIN", font=("Helvetica", 12), bg="red", fg="white", command=com)
        back_button.place(x=120, y=500)

        root.resizable(False, False)
        root.mainloop()

columns, rows = fetch_data()
image_path = "BOOK.png"  # Adjust the path as necessary
create_window(columns, rows, image_path)

