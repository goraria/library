# import tkinter
from tkinter import *
from PIL import ImageTk,Image #PIL -> Pillow
import pymysql
from tkinter import messagebox
from AddBook import *
from DeleteBook import *
from ReturnBook import returnBook
from ViewBooks import *
from IssueBook import *

mypass = "Jiang@99@03$0820" #use your own password
mydatabase = "se_proj" #The database name

con = pymysql.connect (host="localhost",user="root",password=mypass,database=mydatabase) #root is the username here
cur = con.cursor() #cur -> cursor

root = Tk()
root.title("Library powered by Japtor")
root.minsize(width=512,height=512)
root.geometry("1024x768")

same = True
n = .5

# Adding a background image
background_image = Image.open("lib.jpg")
[imageSizeWidth, imageSizeHeight] = background_image.size

newImageSizeWidth = int(imageSizeWidth * n)
if same:
    newImageSizeHeight = int(imageSizeHeight * n)
else:
    newImageSizeHeight = int(imageSizeHeight / n)

background_image = background_image.resize((newImageSizeWidth, newImageSizeHeight)) # , resample=Image.ANTIALIAS()
img = ImageTk.PhotoImage(background_image)
Canvas1 = Canvas(root)
Canvas1.create_image(1024, 768, image=img)
Canvas1.config(bg="white", width=newImageSizeWidth, height=newImageSizeHeight)
Canvas1.pack(expand=True, fill=BOTH)

headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
headingLabel = Label(headingFrame1, text="Welcome to\nJaptor Library", bg='black', fg='white', font=('SF Pro Text',20))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

btn1 = Button(root, text="Add Book Details", bg='black', fg='white', command=addBook, font=('SF Pro Text',20))
btn1.place(relx=0.28, rely=0.4, relwidth=0.45, relheight=0.1)

btn2 = Button(root, text="Delete Book", bg='black', fg='white', command=delete, font=('SF Pro Text',20))
btn2.place(relx=0.28, rely=0.5, relwidth=0.45, relheight=0.1)

btn3 = Button(root, text="View Book List", bg='black', fg='white', command=View, font=('SF Pro Text',20))
btn3.place(relx=0.28, rely=0.6, relwidth=0.45, relheight=0.1)

btn4 = Button(root, text="Issue Book to Student", bg='black', fg='white', command=issueBook, font=('SF Pro Text',20))
btn4.place(relx=0.28, rely=0.7, relwidth=0.45, relheight=0.1)

btn5 = Button(root, text="Return Book", bg='black', fg='white', command=returnBook, font=('SF Pro Text',20))
btn5.place(relx=0.28, rely=0.8, relwidth=0.45, relheight=0.1)
root.mainloop()