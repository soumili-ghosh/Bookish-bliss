import tkinter as tk
from tkinter import PhotoImage
import os
# Function to animate the button by blinking
def animate_button():
    current_color = button.cget("bg")
    new_color = "yellow" if current_color == "green" else "green"
    button.config(bg=new_color)
    root.after(500, animate_button)  # Change color every 500 milliseconds (0.5 seconds)

root = tk.Tk()
root.title("Bookish Bliss")
root.geometry("908x516")  # Ensure correct case for 'x'

def sell_book():
        root.destroy()
        os.system("python -u buy1.py")

# Set the background image
bg_image = PhotoImage(file="book1.png")
bg_label = tk.Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create the button
button = tk.Button(root, text="PURCHASE BOOK", bg="green", font=("Arial", 12, "bold"),command=sell_book)
button.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

# Start the animation
animate_button()

root.mainloop()
