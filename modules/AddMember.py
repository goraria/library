from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import pymysql

import main

myPassword = 'Jiang@99@03$0820'  # use your own password
myDatabase = 'se_proj'  # The database name

myConnect = pymysql.connect(
    host='localhost',
    user='root',
    password=myPassword,
    database=myDatabase
)  # root is the username here
myCursor = myConnect.cursor()


class AddMember(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry('960x540')
        self.title('Add Member')
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

        self.labelFullname = Label(self.bottomFrame, text='Fullname: ', font=('Arial Bold', 16))
        self.labelFullname.place(x=50, y=50)
        self.entryFullname = Entry(self.bottomFrame, width=32, bd=4)
        self.entryFullname.insert(0, 'Fullname of Reader')
        self.entryFullname.place(x=150, y=50)

        self.labelGender = Label(self.bottomFrame, text='Gender: ', font=('Arial Bold', 16))
        self.labelGender.place(x=50, y=100)
        self.entryGender = Entry(self.bottomFrame, width=32, bd=4)
        self.entryGender.insert(0, 'Gender of Reader')
        self.entryGender.place(x=150, y=100)

        self.labelBirthday = Label(self.bottomFrame, text='Birthday: ', font=('Arial Bold', 16))
        self.labelBirthday.place(x=50, y=150)
        self.entryBirthday = Entry(self.bottomFrame, width=32, bd=4)
        self.entryBirthday.insert(0, 'Birthday of Reader')
        self.entryBirthday.place(x=150, y=150)

        self.labelAddress = Label(self.bottomFrame, text='Address: ', font=('Arial Bold', 16))
        self.labelAddress.place(x=50, y=200)
        self.entryAddress = Entry(self.bottomFrame, width=32, bd=4)
        self.entryAddress.insert(0, 'Address of Reader')
        self.entryAddress.place(x=150, y=200)

        ####

        button = Button(self.bottomFrame, text='Add Member', command=self.AddMember)
        button.place(x=350, y=400)

    def AddMember(self):
        id_person = 1
        full_name = self.entryFullname.get()
        gender = self.entryGender.get()
        birth_day = self.entryBirthday.get()
        address = self.entryAddress.get()
        can_borrow = 0
        borrowed = 0

        # if (name_book and author and publisher and types and quantity and storage) != '':
        #     try:
        #         query = 'INSERT INTO `Book` (`name_book`, `author`, `publisher`, `types`, `quantity`, `storage`, `content`) VALUES(%s, %s, %s, %s, %s, %s, %s)'
        #         myCursor.execute(query, (name_book, author, publisher, types, quantity, storage, content))
        #         myConnect.commit()
        #         messagebox.showinfo('Success', 'Successfully', icon='info')
        #     except:
        #         messagebox.showerror('Error', 'Can\'t connect to Database', icon='warning')
        # else:
        #     messagebox.showerror('Error', 'Form can\'t be Empty', icon='warning')

        # try:
        #     with myConnect.cursor() as cursor:

        # try:
        #     query = 'INSERT INTO `Book` (`id_book`, `name_book`, `author`, `publisher`, `types`, `quantity`, `storage`, `content`, `borrowed`) VALUES(%d, %s, %s, %s, %s, %d, %s, %s, %d)'
        #     myCursor.execute(query, (id_book, name_book, author, publisher, types, quantity, storage, content, borrowed))
        #     myConnect.commit()
        #     messagebox.showinfo('Success', 'Successfully', icon='info')
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
        #         check = 'SELECT * FROM `Test` WHERE (`name_book` = %s AND `author` = %s AND `publisher` = %s AND `types` = %s AND `quantity` = %s AND `storage` = %s AND `content` = %s)' %(name_book, author, publisher, types, quantity, storage, content)
        #
        #         try:
        #             if (cursor.execute(check)) == 0:
        #                 # result = cursor.fetchall()
        #                 #
        #                 # Ans_input = input('Please enter Answer:-')
        #                 checked = 'INSERT INTO `Test` (`name_book`, `author`, `publisher`, `types`, `quantity`, `storage`, `content`) VALUES(%s, %s, %s, %s, %s, %s, %s)'
        #
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
        #
        #     myConnect.commit()
        #
        # except:
        #     messagebox.showerror('Error', 'Something Wrong!', icon='warning')
        # finally:
        #     myConnect.close()


































