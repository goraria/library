import tkinter
import PIL
import pymysql
from tkinter import *
from PIL import *
from PIL import ImageTk,Image
from tkinter import messagebox
# from object import *
from FindBook import *

my_database = 'se_proj' # The database name
my_password = 'Jiang@99@03$0820' # use your own password # Gorth$1999 # Jiang@99@03$0820

my_connection = pymysql.connect(host="localhost", user="root", password=my_password, database=my_database) # root is the username here
my_cursor = my_connection.cursor() # cursor -> cursor

class Main(object):
    def __init__(self, master):
        self.master = master

class Example(Frame):
    def __init__(self, master, *pargs):
        Frame.__init__(self, master, *pargs)
        self.image = Image.open("./library.jpg")
        self.img_copy= self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

    def _resize_image(self,event):

        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))
        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image =  self.background_image)



# same = True
# zoom = 1
# # Adding a Background Image
# background_image = Image.open('library.jpg')
# [imageSizeWidth, imageSizeHeight] = background_image.size
#
# newImageSizeWidth = int(imageSizeWidth * zoom)
# if same:
#     newImageSizeHeight = int(imageSizeHeight * zoom)
# else:
#     newImageSizeHeight = int(imageSizeHeight / zoom)
#
# background_image = background_image.resize((newImageSizeWidth, newImageSizeHeight), resample=PIL.Image.Resampling.LANCZOS) # Image.ANTIALIAS
# image = ImageTk.PhotoImage(background_image)
#
# # def Canvases(self):
# canvas = Canvas(app)
# canvas.create_image(0, 0, image=image, anchor=NW)
# canvas.config(bg="white", width=newImageSizeWidth, height=newImageSizeHeight)
# canvas.pack(expand=True, fill=BOTH)
# canvas.grid(row=0, column=0)




def main():
    root = Tk()
    app = Main(root)
    root.title("Gorth Library Management")
    # root.geometry('1024x768')
    root.geometry("1200x750")  # 1600x1000
    root.iconbitmap('./library.jpg')
    # self.minsize(width=1024, height=768)
    # self.resizable(width=0, height=0)
    # root.configure(background="black")
    root.mainloop()

    exm = Example(root)
    exm.pack(fill=BOTH, expand=YES)

    heading_frame = Frame(app, bg="#FF00AA", bd=5)
    heading_frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.2)
    heading_label = Label(heading_frame, text="Welcome to Gorth Library Manager Application", bg='black', fg='white',
                          font=('Arial', 32))
    heading_label.place(relx=0, rely=0, relwidth=1, relheight=1)

    add_book_button = Button(app, text="Tìm sách", bg='black', fg='white', font=('Arial', 16))
    add_book_button.place(relx=0.1, rely=0.4, relwidth=0.15, relheight=0.1)
    find_book_button = Button(app, text="Mượn sách", bg='black', fg='white', font=('Arial', 16), command=FindBook)
    find_book_button.place(relx=0.1, rely=0.55, relwidth=0.15, relheight=0.1)
    view_book_button = Button(app, text="Xem Thư viện", bg='black', fg='white', font=('Arial', 16))
    view_book_button.place(relx=0.1, rely=0.7, relwidth=0.15, relheight=0.1)
    view_book_button = Button(app, text="Xem Thông tin", bg='black', fg='white', font=('Arial', 16))
    view_book_button.place(relx=0.75, rely=0.55, relwidth=0.15, relheight=0.1)
    delete_book_button = Button(app, text="Xóa sách", bg='black', fg='white', font=('Arial', 16))
    delete_book_button.place(relx=0.75, rely=0.7, relwidth=0.15, relheight=0.1)
    create_cart_button = Button(app, text="Tạo thẻ", bg='black', fg='white', font=('Arial', 16))
    create_cart_button.place(relx=0.75, rely=0.4, relwidth=0.15, relheight=0.1)

if __name__ == '__main__':
    main()
