
from tkcalendar import *
from tkinter import *
from tkinter import Toplevel
from tkinter import messagebox
from tkinter.ttk import Treeview
from tkinter import ttk
from os import system
import smtplib


root = Tk()
root.iconbitmap('LibraryIcon.ico')

root.geometry("1000x562+200+80")
root.resizable(False, False)
root.title("LOGIN SYSTEM")

bg = PhotoImage(file = "loginBg1.png")
bg = bg.subsample(1,1)

can = Canvas(root)
can.place(x=0,y=0,relwidth = 1 ,relheight = 1)
can.create_image(0,0,image = bg ,anchor = 'nw')

#Images Used inside Login Page
ForpassImg = PhotoImage(file = "loginBg1.png")
ForpassImg = ForpassImg.subsample(2,2)

logoimg = PhotoImage(file='LoginIcon.png')
logoimg = logoimg.subsample(3, 3)

usernameimg = PhotoImage(file='User.png')
usernameimg = usernameimg.subsample(1, 1)

passwordimg = PhotoImage(file='pass.png')
passwordimg = passwordimg.subsample(1, 1)

def send(reciver,message):
    sender="ghoshsoumili58@gmail.com"
    password="hfbn dbxx vogz hcqo"
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(sender,password)
    print("Login successfully")
    server.sendmail(sender,reciver,message)
    print("Email sent succesfully!!")
def loginbtnfunc():                                     #Login Button Function
    
    username = "Book"
    password = "root"

    if usernameEntry.get()==username and passwordEntry.get()==password:
        messagebox.showinfo(title="Login Successful!", message="You successfully logged in.")
        root.destroy()
        system('python -u book.py')
        
    else:
        messagebox.showerror(title="Error", message="Invalid login.")
        
# Login Frame Labels

titleLabel = Label(can ,text='LOGIN SYSTEM', font=('Georgia', 20, 'italic bold'), bg='#6D93B1', fg='White' ,height = 2,
                   relief='groove' ,bd=2 )
titleLabel.place(x=1,y=1,relwidth = 1)

can.create_image((430,80),image = logoimg ,anchor = 'nw')

can.create_image((297,275),image = usernameimg ,anchor = 'nw')

can.create_text((370,289),text = "Username :",font=('times', 15, 'italic bold'))

can.create_image((297,358),image = passwordimg ,anchor = 'nw')

can.create_text((370,368),text = "Password :",font=('times', 15, 'italic bold'))

#Login Entry Boxes
username = StringVar()
password = StringVar()

usernameEntry = Entry(root, textvariable=username, width=25, font=('times', 15, 'italic'), bd=5, bg='lightblue')
usernameEntry.place(x=420, y=270)
usernameEntry.focus()

passwordEntry = Entry(root, width=25, show='*', textvariable=password, font=('times', 15, 'italic'), bd=5, bg='lightblue')
passwordEntry.place(x=420, y=350)

#Login Submit Button
loginbtn = Button(root, text='Login', font=('times', 13, 'italic bold'), bg='lightgreen', bd=5, activebackground='green',
                  activeforeground='white', command=loginbtnfunc ,width = 8)
loginbtn.place(x=580, y=410)

def ForGetPass(event):
    root.withdraw()
    Forget = Toplevel()
    Forget.geometry('500x290')
    Forget.resizable(False,False)
    Forget.title('Forget PassWord')

    for_frame =  Frame(Forget,bd= 4,relief ='groove',bg= 'red')
    for_frame.place(x=0,y=0,relwidth=1 ,relheight=1)

    forcan = Canvas(for_frame )
    forcan.place(x=0, y=0, relwidth=1, relheight=1)
    forcan.create_image(0, 0, image=ForpassImg, anchor='nw')

    ForTitle = Label(forcan,text= 'Enter Verified Email ID' ,font= ('serif',15,'italic'), bg='#6D93B1', fg='White' ,bd=3,
                     relief = 'groove')
    ForTitle.place(x= 10 ,y= 5 ,width = 468)

    forcan.create_text((115,125),text = 'Email : ', font= ('Time',12,'bold'))

    Emailval = StringVar()
    ForEmailVal = Entry(for_frame,textvariable = Emailval, font= ('Time',12,'italic') ,bd = 3 ,width = 28)
    ForEmailVal.place(x=145, y=110)
def open_email_window():
    email_window = Toplevel()
    email_window.title("Enter Email")
    email_window.geometry("300x150")
    email_window.resizable(False, False)
    
    # Label and Entry for email address
    email_label = Label(email_window, text="Enter Your Email:", font=('Arial', 12))
    email_label.pack(pady=5)
    
    email_entry = Entry(email_window, font=('Arial', 12), width=30)
    email_entry.pack(pady=5)
    
    # Function to send the email
    def send_email():
        recipient_email = email_entry.get()
        message = "Userid= Book and password = root."
        send(recipient_email, message)
        messagebox.showinfo("Email Sent", "Email has been sent successfully!")
        email_window.destroy()
    
    # OK Button to trigger sending email
    ok_button = Button(email_window, text="OK", font=('Arial', 12), command=send_email)
    ok_button.pack(pady=10)
    
# Button to open the email input window
forget_password_button = Button(root, text="Get Credentials", font=('Arial', 12), command=open_email_window)
forget_password_button.place(x=420, y=410)

root.mainloop()
