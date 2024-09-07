from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import pymysql

import main

myPassword = 'Jiang@99@03$0820' #use your own password
myDatabase = 'se_proj' #The database name

myConnect = pymysql.connect(
    host='localhost',
    user='root',
    password=myPassword,
    database=myDatabase
) #root is the username here
myCursor = myConnect.cursor()

class GiveBook(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry('1280x720')
        self.title('Give Book')
        self.resizable(False, False)

        ####

        self.topFrame = Frame(self, height=50)
        self.topFrame.pack(fill=X)
        self.bottomFrame = Frame(self, height=490)
        self.bottomFrame.pack(fill=X)

        self.topImage = main.ReSizeIcon(Image.open('./icons/member.png'), 50, 50)
        topImageLabel = Label(self.topFrame, image=self.topImage)
        topImageLabel.place(x=0, y=0)
        heading = Label(self.topFrame, text='Add Memeber to Library', font=('Arial Bold', 24))
        heading.place(x=60, y=10)

        ####

        self.bookName = StringVar()
        self.labelName = Label(self.bottomFrame, text='Name: ', font=('Arial Bold', 16))
        self.labelName.place(x=50, y=50)
        self.comboName = ttk.Combobox(self.bottomFrame, textvariable=self.bookName)
        self.comboName['value'] = bookList
        self.comboName.current(self.id_book - 1)
        self.comboName.place(x=150, y=50)

        self.memName = StringVar()
        self.labelMember = Label(self.bottomFrame, text='Member: ', font=('Arial Bold', 16))
        self.labelMember.place(x=50, y=100)
        self.comboMemeber = ttk.Combobox(self.bottomFrame, textvariable=self.memName)
        self.comboMemeber['value'] = memberList
        self.comboMemeber.place(x=150, y=50)

        # self.labelBirthday = Label(self.bottomFrame, text='Birthday: ', font=('Arial Bold', 16))
        # self.labelBirthday.place(x=50, y=150)
        # self.entryBirthday = Entry(self.bottomFrame, width=32, bd=4)
        # self.entryBirthday.insert(0, 'Birthday of Reader')
        # self.entryBirthday.place(x=150, y=150)

        # self.labelAddress = Label(self.bottomFrame, text='Address: ', font=('Arial Bold', 16))
        # self.labelAddress.place(x=50, y=200)
        # self.entryAddress = Entry(self.bottomFrame, width=32, bd=4)
        # self.entryAddress.insert(0, 'Address of Reader')
        # self.entryAddress.place(x=150, y=200)

        ####

        button = Button(self.bottomFrame, text='Add Member', command=self.LendBook)
        button.place(x=350, y=400)

    def LendBook(self):
        nameBook = self.bookName.get()
        nameMem = self.memName.get()
        self.id_book = nameBook.split('-')[0]

        if (nameBook and nameMem) != '':
            try:
                query = 'INSERT INTO `BorrowBook` (`name_book`, `name`) VALUES (%s, %s)'
                myCursor.execute(query, (nameBook, nameMem))
                myConnect.commit()
                messagebox.showinfo('Success', 'Successfully', icon='info')
                myCursor.execute('UPDATE `Book` SET `borrowed` = %s WHERE `name_book` = %s', (bool(1), self.id_book))
                myConnect.commit()
            except:
                messagebox.showerror('Error', 'Can\'t connect to Database', icon='error')
        else:
            messagebox.showwarning('Warning', 'Book was in Database', icon='warning')

