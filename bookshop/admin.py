import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
def loginbtnfunc():                                     #Login Button Function
    password = "BBIT"

    if  password_entry.get()==password:
        messagebox.showinfo(title="Login Successful!", message="You successfully logged in.")
        root.destroy()
        os.system('python -u front.py')
        
    else:
        messagebox.showerror(title="Error", message="Invalid login.")

# Create the main window
root = tk.Tk()
root.title("Admin Login")
root.geometry("800x530")
root.resizable(False,False)
# Load the background image
bg_image = Image.open("ADMIN.png")
bg_image = bg_image.resize((800, 600), Image.BICUBIC)
bg_photo = ImageTk.PhotoImage(bg_image)

# Create a canvas and set the background image
canvas = tk.Canvas(root, width=800, height=600)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg_photo, anchor="nw")

# Create the password label and entry
password_label = tk.Label(root, text="PASSWORD:", font=("Arial", 14), bg="#5a67d8", fg="white")
password_label_window = canvas.create_window(200, 380, anchor="nw", window=password_label)

password_entry = tk.Entry(root, show="*", font=("Arial", 14))
password_entry_window = canvas.create_window(350, 380, anchor="nw", window=password_entry)

# Create the login button
login_button = tk.Button(root, text="LOGIN", font=("Arial", 14), bg='#d4af37', command=loginbtnfunc)
login_button_window = canvas.create_window(380, 440, anchor="nw", window=login_button)

# Create the back button
back_button = tk.Button(root, text="BACK", font=("Arial", 14), bg='#ff3b3b', fg='white', command=root.quit)
back_button_window = canvas.create_window(20, 550, anchor="nw", window=back_button)

root.mainloop()
