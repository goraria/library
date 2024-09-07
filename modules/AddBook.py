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

class AddBook(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry('1280x720')
        self.title('Add Book')
        self.resizable(False, False)

        ####

        self.topFrame = Frame(self, height=50)
        self.topFrame.pack(fill=X)
        self.bottomFrame = Frame(self, height=490)
        self.bottomFrame.pack(fill=X)

        self.topImage = main.ReSizeIcon(Image.open('./icons/book.png'), 50, 50)
        topImageLabel = Label(self.topFrame, image=self.topImage)
        topImageLabel.place(x=0, y=0)
        heading = Label(self.topFrame, text='Add Book to Library', font=('Arial Bold', 24))
        heading.place(x=60, y=10)

        ####

        self.labelName = Label(self.bottomFrame, text='Name: ', font=('Arial Bold', 16))
        self.labelName.place(x=50, y=50)
        self.entryName = Entry(self.bottomFrame, width=32, bd=4)
        self.entryName.insert(0, 'Name of Book')
        self.entryName.place(x=150, y= 50)

        self.labelAuthor = Label(self.bottomFrame, text='Author: ', font=('Arial Bold', 16))
        self.labelAuthor.place(x=50, y=100)
        self.entryAuthor = Entry(self.bottomFrame, width=32, bd=4)
        self.entryAuthor.insert(0, 'Author of Book')
        self.entryAuthor.place(x=150, y=100)

        self.labelPublisher = Label(self.bottomFrame, text='Publisher: ', font=('Arial Bold', 16))
        self.labelPublisher.place(x=50, y=150)
        self.entryPublisher = Entry(self.bottomFrame, width=32, bd=4)
        self.entryPublisher.insert(0, 'Publisher of Book')
        self.entryPublisher.place(x=150, y=150)

        self.labelType = Label(self.bottomFrame, text='Type: ', font=('Arial Bold', 16))
        self.labelType.place(x=50, y=200)
        self.entryType = Entry(self.bottomFrame, width=32, bd=4)
        self.entryType.insert(0, 'Type of Book')
        self.entryType.place(x=150, y=200)

        self.labelQuantity = Label(self.bottomFrame, text='Quantity: ', font=('Arial Bold', 16))
        self.labelQuantity.place(x=50, y=250)
        self.entryQuantity = Entry(self.bottomFrame, width=32, bd=4)
        self.entryQuantity.insert(0, 'Quantity of Book')
        self.entryQuantity.place(x=150, y=250)

        self.labelContent = Label(self.bottomFrame, text='Content: ', font=('Arial Bold', 16))
        self.labelContent.place(x=50, y=300)
        self.entryContent = Entry(self.bottomFrame, width=32, bd=4)
        self.entryContent.insert(0, 'Content of Book')
        self.entryContent.place(x=150, y=300)
       
        self.labelStoraged = Label(self.bottomFrame, text='Storaged: ', font=('Arial Bold', 16))
        self.labelStoraged.place(x=50, y=350)
        self.entryStoraged = Entry(self.bottomFrame, width=32, bd=4)
        self.entryStoraged.insert(0, 'Storaged of Book')
        self.entryStoraged.place(x=150, y=350)
        
        ####

        button = Button(self.bottomFrame, text='Add Book', command=self.AddBook)
        button.place(x=350, y=400)

    def AddBook(self):
        id_book = 1
        name_book = self.entryName.get().strip().lower()
        author = self.entryAuthor.get().strip().lower()
        publisher = self.entryPublisher.get().strip().lower()
        types = self.entryType.get().strip().lower()
        quantity = self.entryQuantity.get().strip().lower()
        content = self.entryContent.get().strip().lower()
        storage = self.entryStoraged.get().strip().lower()
        borrowed = 0

        # try:
        if (name_book and author and publisher and types and quantity and storage) != '':
            check = 'SELECT `name_book`, `author`, `publisher`, `types`, `storage`, `content` FROM `Book` WHERE `name_book` = %s AND `author` = %s AND `publisher` = %s AND `types` = %s AND `storage` = %s AND `content` = %s'
            if myCursor.execute(check, (name_book, author, publisher, types, storage, content)) == 0:
                try:
                    query = 'INSERT INTO `Book` (`name_book`, `author`, `publisher`, `types`, `quantity`, `storage`, `content`, `borrowed`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'
                    myCursor.execute(query, (name_book, author, publisher, types, int(quantity), storage, content, bool(borrowed)))
                    myConnect.commit()
                    messagebox.showinfo('Success', 'Successfully', icon='info')
                except:
                    messagebox.showerror('Error', 'Can\'t connect to Database', icon='error')
            else:
                update = 'UPDATE `Book` SET `quantity` = quantity + %s WHERE `name_book` = %s AND `author` = %s AND `publisher` = %s AND `types` = %s AND `content` = %s'
                myCursor.execute(update, (quantity, name_book, author, publisher, types, content))
                myConnect.commit()
                messagebox.showwarning('Warning', 'Book was in Database', icon='warning')
        else:
            messagebox.showerror('Warning', 'Form can\'t be Empty', icon='warning')
        # except:
        #     messagebox.showerror('Error', 'Something Wrong!', icon='warning')

        # try:
        #     query = 'INSERT INTO `Test` (`name_book`, `author`, `publisher`, `types`, `quantity`, `storage`, `content`) VALUES(%s, %s, %s, %s, %s, %s, %s)'
        #     myCursor.execute(query, (name_book, author, publisher, types, quantity, storage, content))
        #     myConnect.commit()
        #     messagebox.showinfo('Success', 'Successfully', icon='info')
        # except:
        #     messagebox.showerror('Error', 'Something Wrong!', icon='warning')

        # try:
        #     with myConnect.cursor() as cursor:
        #         # check = 'SELECT * FROM `Test` WHERE (`name_book` = {name_book}, `author` = {author}, `publisher` = {publisher}, `types` = {types}, `quantity` = {quantity}, `storage` = {storage}, `content` = {content})'
        #         check = 'SELECT `name_book`, `author`, `publisher`, `types`, `quantity`, `storage`, `content` FROM `Test` WHERE `name_book` = %s AND `author` = %s AND `publisher` = %s AND `types` = %s AND `quantity` = %s AND `storage` = %s AND `content` = %s'

        #         try:
        #             if (cursor.execute(check, (name_book, author, publisher, types, quantity, storage, content))) == 0:
        #                 result = cursor.fetchall()
        #                 #
        #                 # Ans_input = input('Please enter Answer:-')
        #                 checked = 'INSERT INTO `Test` (`name_book`, `author`, `publisher`, `types`, `quantity`, `storage`, `content`) VALUES(%s, %s, %s, %s, %s, %s, %s)'

        #                 try:
        #                     cursor.execute(checked, (name_book, author, publisher, types, quantity, storage, content))
        #                     print("Task added successfully")
        #                 except:
        #                     print("Oops! Something wrong?")
        #             else:
        #                 cursor.execute(check)
        #                 result = cursor.fetchall()
        #                 print("Que\t\t Answer")
        #                 print("-------------------------")
        #                 for row in result:
        #                     print(str(row[0]) + "\t\t" + row[1])
        #         except:
        #             print("Oops! Something wrong!")

        #     myConnect.commit()

        # except:
        #     messagebox.showerror('Error', 'Something Wrong!', icon='warning')
        # finally:
        #     myConnect.close()































