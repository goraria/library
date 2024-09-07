# import tkinter
import tkinter
from tkinter import *
from PIL import ImageTk, Image
# from PIL import Image, ImageTk
import pymysql
from tkinter import messagebox
from AddBook import *
from DeleteBook import *
from ReturnBook import returnBook
from ViewBooks import *
from IssueBook import *


class App(tkinter.Tk, Frame):
    def __init__(self, master, *pargs):
        Frame.__init__(self, master, *pargs)
        super().__init__()
        self.title("Library powered by Japtor")
        self.minsize(width=512, height=512)
        self.geometry("1024x768")
        self.configure(background="white")


        self.image = Image.open("./lib.jpg")
        self.img_copy= self.image.copy()
        self.background_image = ImageTk.PhotoImage(self.image)
        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

        mypass = "Jiang@99@03$0820"  # use your own password
        mydatabase = ""  # The database name

        con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)  # root is the username here
        cur = con.cursor()  # cur -> cursor

    def _resize_image(self, event):
        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))
        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)



app = App()
app.pack(fill=BOTH, expand=YES)

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

background_image = background_image.resize(
    (newImageSizeWidth, newImageSizeHeight))  # , resample=Image.ANTIALIAS()
img = ImageTk.PhotoImage(background_image)
Canvas1 = Canvas(app)
Canvas1.create_image(1024, 768, image=img)
Canvas1.config(bg="white", width=newImageSizeWidth, height=newImageSizeHeight)
Canvas1.pack(expand=True, fill=BOTH)


headingFrame1 = Frame(app ,bg="#FFBB00",bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)
headingLabel = Label(headingFrame1, text="Welcome to\nJaptor Library", bg='black', fg='white', font=('SF Pro Text',20))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

btn1 = Button(app, text="Add Book Details", bg='black', fg='black', command=addBook, font=('SF Pro Text', 20))
btn1.place(relx=0.28, rely=0.4, relwidth=0.45, relheight=0.1)

btn2 = Button(app, text="Delete Book", bg='black', fg='black', command=delete, font=('SF Pro Text', 20))
btn2.place(relx=0.28, rely=0.5, relwidth=0.45, relheight=0.1)

btn3 = Button(app, text="View Book List", bg='black', fg='black', command=View, font=('SF Pro Text', 20))
btn3.place(relx=0.28, rely=0.6, relwidth=0.45, relheight=0.1)

btn4 = Button(app, text="Issue Book to Student", bg='black', fg='black', command=issueBook, font=('SF Pro Text', 20))
btn4.place(relx=0.28, rely=0.7, relwidth=0.45, relheight=0.1)

btn5 = Button(app, text="Return Book", bg='black', fg='black', command=returnBook, font=('SF Pro Text', 20))
btn5.place(relx=0.28, rely=0.8, relwidth=0.45, relheight=0.1)

app.mainloop()