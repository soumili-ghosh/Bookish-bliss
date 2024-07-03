import tkinter as tk
from tkinter import PhotoImage
import os
def main():
    root = tk.Tk()
    root.title("Bookish bliss")
    root.geometry("1000x600")
    root.resizable(False,False)
    root.configure(bg="white")
    def com():
        root.destroy()
        os.system("python -u login.py") 

    def com1():
        root.destroy()
        os.system("python -u admin.py") 
    
    # Background setup
    background_image = PhotoImage(file="bg.png")
    background_label = tk.Label(root, image=background_image)
    background_label.place(relwidth=1, relheight=1)

    # User Login Button
    user_login_button = tk.Button(root, text="User Login", font=("Helvetica", 16), bg="light blue", fg="black",command=com)
    user_login_button.place(relx=0.3, rely=0.5, anchor='center')

    # Admin Login Button
    admin_login_button = tk.Button(root, text="Admin Login", font=("Helvetica", 16), bg="light pink", fg="black",command=com1)
    admin_login_button.place(relx=0.75, rely=0.5, anchor='center')

    # Mainloop
    root.mainloop()

if __name__ == "__main__":
    main()
