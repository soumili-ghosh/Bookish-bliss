import tkinter as tk
from itertools import cycle
import os
class AnimatedButton(tk.Button):
    def __init__(self, master=None, **kwargs):
        tk.Button.__init__(self, master, **kwargs)
        self.color_cycle = cycle(['#ffaaaa', '#aaffaa', '#aaaaff', '#ffffaa', '#ffaaff', '#aaffff'])
        self.animate()

    def animate(self):
        self.config(bg=next(self.color_cycle))
        self.after(500, self.animate)

def create_buttons():
    root = tk.Tk()
    root.title("Bookish bliss")
    def add_book():
        root.destroy()
        os.system("python -u addbook.py")
    def show_book():
        root.destroy()
        os.system("python -u show.py")

    def sell_book():
        root.destroy()
        os.system("python -u buy.py")

    canvas = tk.Canvas(root, width=956, height=501)
    canvas.pack()

    # Load the background image
    bg_image = tk.PhotoImage(file="another.png")
    canvas.create_image(0, 0, anchor=tk.NW, image=bg_image)

    # Keep a reference to the image object to prevent it from being garbage collected
    canvas.image = bg_image
    add_button = AnimatedButton(root, text="Add Book", font=("Helvetica", 18), command=add_book)
    add_button.place(x=150,y=380) # Add some padding for spacing

    show_button = AnimatedButton(root, text="Show Book", font=("Helvetica", 18), command=show_book)
    show_button.place(x=420,y=380)

    sell_button = AnimatedButton(root, text="Sell Book", font=("Helvetica", 18), command=sell_book)
    sell_button.place(x=760,y=380)


    root.resizable(False, False)
    root.mainloop()

if __name__ == "__main__":
    create_buttons()
