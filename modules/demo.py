from tkinter import *
from tkinter import ttk, messagebox
# import customtkinter
from customtkinter import *
from CTkListbox import *
from PIL import Image, ImageTk
import pymysql

import AddBook
import AddMember

myPassword = 'Jiang@99@03$0820'
myDatabase = 'se_proj'

myConnect = pymysql.connect(host='localhost', user='root', password=myPassword, database=myDatabase)
myCursor = myConnect.cursor()

main_color = '#FFAACC'
hover_color = '#FFAAEE'

# myConnect = pymysql.connect('./demo.db')
# myCursor = myConnect.cursor()

def ReSizeIcon(img, width, height):
    resizedIcon = img.resize((width, height), Image.Resampling.LANCZOS)
    return ImageTk.PhotoImage(resizedIcon)


class Main(object):
    def __init__(self, master):
        self.master = master

        def DisplayBooks(self):
            books = myCursor.execute('SELECT * FROM `Book`')
            result = myCursor.fetchall()
            count = 0
            for book in result:
                # print(book)
                self.listBooks.insert(count, str(book[0]) + '. ' + book[1])
                count += 1

            def BookInfo(evt):
                value = str(self.listBooks.get(self.listBooks.curselection()))
                id = value.split('-')[0]
                book = myCursor.execute('SELECT * FROM `Book` WHERE id_book=%s', (id,))
                bookInfo = myCursor.fetchall()
                # print(bookInfo)

                self.listDetails.delete(0, 'end')
                self.listDetails.insert(0, 'Book Name: ' + bookInfo[0][1])
                self.listDetails.insert(1, 'Author Name: ' + bookInfo[0][2])
                self.listDetails.insert(2, 'Publisher Name: ' + bookInfo[0][3])
                self.listDetails.insert(3, 'Types: ' + bookInfo[0][4])
                self.listDetails.insert(4, 'Content: ' + bookInfo[0][6])

                if bookInfo[0][5] == 0:
                    self.listDetails.insert(5, 'Quantity: Avaiable' + bookInfo[0][5])
                else:
                    self.listDetails.insert(5, 'Quantity: Not Avaiable')
            self.listBooks.bind('<<ListboxSelect>>', BookInfo)

        def BookInfo(value):
            myCursor.execute('SELECT * FROM `Book` WHERE id_book = %s', (value.split('-')[0]))
            bookInfo = myCursor.fetchall()

            # self.listDetails.delete(0, 'end')
            self.listDetails.insert(0, 'Book Name: ' + bookInfo[0][1])
            self.listDetails.insert(1, 'Author Name: ' + bookInfo[0][2])
            self.listDetails.insert(2, 'Publisher Name: ' + bookInfo[0][3])
            self.listDetails.insert(3, 'Types: ' + bookInfo[0][4])
            self.listDetails.insert(4, 'Content: ' + bookInfo[0][6])

            if bookInfo[0][5] == 0:
                self.listDetails.insert(5, 'Quantity: Avaiable' + bookInfo[0][5])
            else:
                self.listDetails.insert(5, 'Quantity: Not Avaiable')

        mainFrame = CTkFrame(self.master)
        mainFrame.pack()
        topFrame = CTkFrame(mainFrame, width=1280, height=80)  # , padx=20 , bg='#FF00AA'
        topFrame.pack(side=TOP, fill=X)
        centerFrame = CTkFrame(mainFrame, width=1280, height=640)
        centerFrame.pack(side=TOP)
        centerLeftFrame = CTkFrame(centerFrame, width=720, height=640)
        centerLeftFrame.pack(side=LEFT)
        centerRightFrame = CTkFrame(centerFrame, width=560, height=640)
        centerRightFrame.pack(side=RIGHT)

        ####

        searchBar = CTkLabel(centerRightFrame, text='Search Box', width=560, font=('Arial Bold', 24))
        searchBar.pack(fill=BOTH, side=TOP, padx=20, pady=20)
        self.labelSearch = CTkLabel(searchBar, text='Search: ', text_color='black', font=('Arial Bold', 18))
        self.labelSearch.grid(row=0, column=0, padx=10, pady=10)
        self.entrySearch = Entry(searchBar, font=('Arial Bold', 16), width=24, bg='white', fg='black')  # , bd=10
        self.entrySearch.grid(row=0, column=1, columnspan=3)  #
        self.buttonSearch = CTkButton(searchBar, text='Search', bg_color='white', font=('Arial Bold', 16), command=self.SearchBook)
        self.buttonSearch.grid(row=0, column=4, padx=10, pady=10)

        listBar = CTkLabel(centerRightFrame, text='List Box', width=560, height=160, font=('Arial Bold', 24))
        listBar.pack(fill=BOTH, side=TOP, padx=20, pady=20)
        self.labelList = Label(listBar, text='Sort by:', font=('Arial Bold', 18))
        self.labelList.grid(row=0, column=0, padx=10, pady=10)
        self.listChoice = IntVar()

        radioButton1 = CTkRadioButton(listBar, text='All Books', variable=self.listChoice, value=1, font=('Arial Bold', 12))
        radioButton2 = CTkRadioButton(listBar, text='In Library', variable=self.listChoice, value=2, font=('Arial Bold', 12))
        radioButton3 = CTkRadioButton(listBar, text='Borrowed Books', variable=self.listChoice, value=3, font=('Arial Bold', 12))
        radioButton1.grid(row=0, column=1)
        radioButton2.grid(row=0, column=2)
        radioButton3.grid(row=0, column=3)
        buttonList = CTkButton(listBar, text='List Books', bg_color='white', border_width=0, font=('Arial Bold', 16))
        buttonList.grid(row=1, column=3, padx=10, pady=10)

        imageBar = CTkFrame(centerRightFrame)
        imageBar.pack(fill=BOTH)
        self.titleRight = Label(imageBar, text='Welcome to Gorth Library', font=('Arial Bold', 30))
        self.titleRight.pack(fill=BOTH)
        self.imageLibrary = ReSizeIcon(Image.open('./icons/library.png'), 440, 275)
        self.labelImage = Label(imageBar, image=self.imageLibrary)
        # self.labelImage = Label(imageBar, image='')
        self.labelImage.pack(fill=BOTH)

        ####

        self.iconCorp = ReSizeIcon(Image.open('./icons/logo_modified.png'), 50, 50)
        self.buttonCorp = CTkButton(topFrame, text='Gorth Inc.', image=self.iconCorp, anchor="w", width=150, height=50, border_width=0, compound='left', font=('Arial Bold', 16))
        self.buttonCorp.pack(side=LEFT)

        self.iconAddBook = ReSizeIcon(Image.open('./icons/book.png'), 50, 50)
        self.buttonAddBook = CTkButton(topFrame, text='Add Book', image=self.iconAddBook, anchor="w", width=150, height=50, border_width=0, compound='left', font=('Arial Bold', 16), command=self.AddBook)
        self.buttonAddBook.pack(side=LEFT)  # , padx=10

        self.iconDelBook = ReSizeIcon(Image.open('./icons/book.png'), 50, 50)
        self.buttonDelBook = CTkButton(topFrame, text='Del Book', image=self.iconDelBook, anchor="w", width=150, height=50, border_width=0, compound='left', font=('Arial Bold', 16), command=self.DelBook)
        self.buttonDelBook.pack(side=LEFT)  # , padx=10

        self.iconAddMember = ReSizeIcon(Image.open('./icons/member.png'), 50, 50)
        self.buttonAddMember = CTkButton(topFrame, text='Add Member', image=self.iconAddMember, anchor="w", width=150, height=50, border_width=0, compound='left', font=('Arial Bold', 16), command=self.AddMember)
        self.buttonAddMember.pack(side=LEFT)  # , padx=10

        self.iconDelMember = ReSizeIcon(Image.open('./icons/member.png'), 50, 50)
        self.buttonDelMember = CTkButton(topFrame, text='Del Member', image=self.iconDelMember, anchor="w", width=150, height=50, border_width=0, compound='left', font=('Arial Bold', 16), command=self.DelMember)
        self.buttonDelMember.pack(side=LEFT)  # , padx=10

        self.iconGive = ReSizeIcon(Image.open('./icons/lib.png'), 50, 50)
        self.buttonGive = CTkButton(topFrame, text='Give Book', image=self.iconGive, anchor="w", width=150, height=50, border_width=0, compound='left', font=('Arial Bold', 16))
        self.buttonGive.pack(side=LEFT)  # , padx=10

        self.iconAccount = ReSizeIcon(Image.open('./icons/lib.png'), 50, 50)
        self.buttonAccount = CTkButton(topFrame, text='Account', image=self.iconAccount, anchor="e", width=150, height=50, border_width=0, compound='right', font=('Arial Bold', 16))
        self.buttonAccount.pack(side=RIGHT) # , padx=10

        # self.iconSignup = ReSizeIcon(Image.open('./icons/lib.png'), 50, 50)
        # self.buttonSignup = CTkButton(topFrame, text='Signup', image=self.iconSignup, anchor="e", width=150, height=50, border_width=0, compound='right', font=('Arial Bold', 16))
        # self.buttonSignup.pack(side=RIGHT) # , padx=10
        #
        # self.iconLogout = ReSizeIcon(Image.open('./icons/lib.png'), 50, 50)
        # self.buttonLogout = CTkButton(topFrame, text='Logout', image=self.iconLogout, anchor="e", width=150, height=50, border_width=0, compound='right', font=('Arial Bold', 16))
        # self.buttonLogout.pack(side=RIGHT) # , padx=10
        #
        # self.iconLogin = ReSizeIcon(Image.open('./icons/lib.png'), 50, 50)
        # self.buttonLogin = CTkButton(topFrame, text='Login', image=self.iconLogin, anchor="e", width=150, height=50, border_width=0, compound='right', font=('Arial Bold', 16))
        # self.buttonLogin.pack(side=RIGHT) # , padx=10

        ####

        self.tabs = CTkTabview(centerLeftFrame, width=720, height=640)  #
        self.tabs.pack()
        # self.tabIcon1 = ReSizeIcon(Image.open('./icons/lib.png'), 50, 50)
        # self.tabIcon2 = ReSizeIcon(Image.open('./icons/lib.png'), 50, 50)
        self.tab1 = self.tabs.add('Library Management')
        self.tab2 = self.tabs.add('Statistics')

        self.listBooks = CTkListbox(self.tab1, width=320, height=580, text_color='black', select_color=main_color, hover_color=hover_color, font=('Arial Bold', 14), command=BookInfo)  # , bd=5
        # self.listBooks = Listbox(self.tab1, width=32, height=32, font=('Arial Bold', 14)) # , bd=5
        self.listBooks.grid(row=0, column=0, padx=(10, 0), pady=(0, 10), sticky=N)
        ##
        self.listDetails = CTkListbox(self.tab1, width=400, height=580, font=('Arial Bold', 14))  # , bd=5
        self.listDetails.grid(row=0, column=1, padx=(10, 10), pady=(0, 10), sticky=N)
        ####
        # self.labelBookCount = Label(self.tab2, text='', pady=20, font=('Arial Bold', 14))
        # self.labelBookCount.grid(row=0, )
        # self.labelMemberCount = Label(self.tab2, text='', pady=20, font=('Arial Bold', 14))
        # self.labelMemberCount.grid(row=1, sticky=W)
        # self.labelTakenCount = Label(self.tab2, text='', pady=20, font=('Arial Bold', 14))
        # self.labelTakenCount.grid(row=2, sticky=W)

        ####

        DisplayBooks(self)

    def AddBook(self):
        add = AddBook.AddBook()

    def DelBook(self):
        pass

    def AddMember(self):
        add = AddMember.AddMember()

    def DelMember(self):
        pass

    def SearchBook(self):
        value = self.entrySearch.get()
        check = 'SELECT * FROM `Book` WHERE `name_book` = %s OR `author` = %s OR `publisher` = %s OR `types` = %s OR `content` = %s'
        # search = myCursor.execute(check, (name_book, author, publisher, types, content))
        search = myCursor.execute(check, ('%' + value + '%'))
        myCursor.fetchall()
        print(search)


def main():
    set_appearance_mode("Light")  # Modes: "System" (standard), "Dark", "Light"
    set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

    root = CTk()
    app = Main(root)
    root.title('Gorth Library Maganement Application')
    root.minsize(width=1280, height=720)
    root.geometry('1280x720')
    root.iconbitmap('./icons/bitmap.ico')
    root.iconphoto(True, PhotoImage(file='./icons/app.png'))
    root.configure(background="#FF00AA")
    root.mainloop()


if __name__ == '__main__':
    main()
