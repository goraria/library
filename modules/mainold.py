from tkinter import *
from tkinter import ttk, messagebox
# import customtkinter
from customtkinter import *
from PIL import Image, ImageTk
import pymysql

import AddBook
import AddMember
import GiveBook

myPassword = 'Jiang@99@03$0820'
myDatabase = 'se_proj'

myConnect = pymysql.connect(host='localhost', user='root', password=myPassword, database=myDatabase)
myCursor = myConnect.cursor()

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
            members = myCursor.execute('SELECT * FROM `Borrower`')
            result = myCursor.fetchall()
            count = 0

            self.listBooks.delete(0, 'end')
            for book in result:
                # print(book)
                self.listBooks.insert(count, str(book[0]) + '. ' + book[1])
                count += 1

            def BookInfo(evt):
                value = str(self.listBooks.get(self.listBooks.curselection()))
                id = value.split('-')[0]
                book = myCursor.execute('SELECT * FROM `Book` WHERE id_book=%s', (id, ))
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

            def DoubleClick(evt):
                value = str(self.listBooks.get(self.listBooks.curselection()))
                id_given = value.split('-')[0]
                give_book = self.GiveBook()

                myCursor.execute('SELECT * FROM `Book`')
                bookInfo = myCursor.fetchall()
                bookList = []
                for book in books:
                    bookList.append(str(book[0]) + '. ' + book[1])
                
                myCursor.execute('SELECT * FROM `Borrower`')
                memberInfo = myCursor.fetchall()
                memberList = []
                for member in members:
                    memberList.append(str(member[0]) + '. ' + member[1])

            self.listBooks.bind('<<ListboxSelect>>', BookInfo)
            self.tabs.bind('<<NotebookTabChanged>>', DisplayStatistics)
            # self.tabs.bind('<<ButtonRelease-1>>', DisplayBooks)
            self.listBooks.bind('<Double-Button-1>', DoubleClick)

        def DisplayStatistics(evt):
            myCursor.execute('SELECT COUNT(id_book) FROM `Book`')
            countBook = myCursor.fetchall()
            myCursor.execute('SELECT COUNT(id_person) FROM `Borrower`')
            countBorrower = myCursor.fetchall()
            myCursor.execute('SELECT COUNT(id_book) FROM `Book` WHERE `borrowed` = True')
            borrowedBook = myCursor.fetchall()

            self.labelBookCount.configure(text='All Books: ' + str(countBook[0][0]) + ' in library')
            self.labelMemberCount.configure(text='Member: ' + str(countBorrower[0][0]) + ' in library')
            self.labelTakenCount.configure(text='Borrowed Books: ' + str(borrowedBook[0][0]) + ' out library')

            DisplayBooks(self)

        mainFrame = Frame(self.master)
        mainFrame.pack()
        topFrame = Frame(mainFrame, width=1280, height=80, relief=SUNKEN) # , padx=20 , bg='#FF00AA'
        topFrame.pack(side=TOP, fill=X)
        centerFrame = Frame(mainFrame, width=1280, height=640, relief=RIDGE)
        centerFrame.pack(side=TOP)
        centerLeftFrame = Frame(centerFrame, width=720, height=640, relief=SUNKEN)
        centerLeftFrame.pack(side=LEFT)
        centerRightFrame = Frame(centerFrame, width=560, height=640, relief=SUNKEN)
        centerRightFrame.pack(side=RIGHT)

        ####

        searchBar = LabelFrame(centerRightFrame, text='Search Box', width=560, font=('Arial Bold', 24))
        searchBar.pack(fill=BOTH, side=TOP, padx=20, pady=20)
        self.labelSearch = Label(searchBar, text='Search: ', font=('Arial Bold', 18))
        self.labelSearch.grid(row=0, column=0, padx=10, pady=10)
        self.entrySearch = Entry(searchBar, font=('Arial Bold', 16), width=24, bg='white', fg='black') # , bd=10
        self.entrySearch.grid(row=0, column=1, columnspan=3) #
        self.buttonSearch = Button(searchBar, text='Search', bg='white', font=('Arial Bold', 16), borderwidth=0, command=self.SearchBook)
        self.buttonSearch.grid(row=0, column=4, padx=10, pady=10)

        listBar = LabelFrame(centerRightFrame, text='List Box', width=560, height=160, font=('Arial Bold', 24))
        listBar.pack(fill=BOTH, side=TOP, padx=20, pady=20)
        self.labelList = Label(listBar, text='Sort by:', font=('Arial Bold', 18))
        self.labelList.grid(row=0, column=0, padx=10, pady=10)
        self.listChoice = IntVar()
        radioButton1 = Radiobutton(listBar, text='All Books', var=self.listChoice, value=1, font=('Arial Bold', 12))
        radioButton2 = Radiobutton(listBar, text='In Library', var=self.listChoice, value=2, font=('Arial Bold', 12))
        radioButton3 = Radiobutton(listBar, text='Borrowed Books', var=self.listChoice, value=3, font=('Arial Bold', 12))
        radioButton1.grid(row=0, column=1)
        radioButton2.grid(row=0, column=2)
        radioButton3.grid(row=0, column=3)
        buttonList = Button(listBar, text='List Books', bg='white', borderwidth=0, font=('Arial Bold', 16), command=self.ListBook)
        buttonList.grid(row=1, column=3, padx=10, pady=10)

        imageBar = Frame(centerRightFrame)
        imageBar.pack(fill=BOTH)
        self.titleRight = Label(imageBar, text='Welcome to Gorth Library', font=('Arial Bold', 30))
        self.titleRight.pack(fill=BOTH)
        self.imageLibrary = ReSizeIcon(Image.open('./icons/library.png'), 440, 275)
        self.labelImage = Label(imageBar, image=self.imageLibrary)
        # self.labelImage = Label(imageBar, image='')
        self.labelImage.pack(fill=BOTH)

        ####

        self.iconCorp = ReSizeIcon(Image.open('./icons/logo_modified.png'), 50, 50)
        self.buttonCorp = Button(topFrame, text='Gorth Inc.', image=self.iconCorp, anchor="w", width=150, height=50, border=0, borderwidth=0, compound=LEFT, font=('Arial Bold', 16))
        self.buttonCorp.pack(side=LEFT)

        self.iconAddBook = ReSizeIcon(Image.open('./icons/book.png'), 50, 50)
        self.buttonAddBook = Button(topFrame, text='Add Book', image=self.iconAddBook, anchor="w", width=150, height=50, border=0, borderwidth=0, compound=LEFT, font=('Arial Bold', 16), command=self.AddBook)
        self.buttonAddBook.pack(side=LEFT) # , padx=10

        self.iconDelBook = ReSizeIcon(Image.open('./icons/book.png'), 50, 50)
        self.buttonDelBook = Button(topFrame, text='Del Book', image=self.iconDelBook, anchor="w", width=150, height=50, border=0, borderwidth=0, compound=LEFT, font=('Arial Bold', 16), command=self.DelBook)
        self.buttonDelBook.pack(side=LEFT) # , padx=10

        self.iconAddMember = ReSizeIcon(Image.open('./icons/member.png'), 50, 50)
        self.buttonAddMember = Button(topFrame, text='Add Member', image=self.iconAddMember, anchor="w", width=150, height=50, border=0, borderwidth=0, compound=LEFT, font=('Arial Bold', 16), command=self.AddMember)
        self.buttonAddMember.pack(side=LEFT) # , padx=10

        self.iconDelMember = ReSizeIcon(Image.open('./icons/member.png'), 50, 50)
        self.buttonDelMember = Button(topFrame, text='Del Member', image=self.iconDelMember, anchor="w", width=150, height=50, border=0, borderwidth=0, compound=LEFT, font=('Arial Bold', 16), command=self.DelMember)
        self.buttonDelMember.pack(side=LEFT) # , padx=10

        self.iconGive = ReSizeIcon(Image.open('./icons/lib.png'), 50, 50)
        self.buttonGive = Button(topFrame, text='Give Book', image=self.iconGive, anchor="w", width=150, height=50, border=0, borderwidth=0, compound=LEFT, font=('Arial Bold', 16), command=GiveBook)
        self.buttonGive.pack(side=LEFT) # , padx=10

        # self.iconSignup = ReSizeIcon(Image.open('./icons/lib.png'), 50, 50)
        # self.buttonSignup = Button(topFrame, text='Signup', image=self.iconSignup, anchor="e", width=150, height=50, border=0, borderwidth=0, compound=RIGHT, font=('Arial Bold', 16))
        # self.buttonSignup.pack(side=RIGHT) # , padx=10
        #
        # self.iconLogout = ReSizeIcon(Image.open('./icons/lib.png'), 50, 50)
        # self.buttonLogout = Button(topFrame, text='Logout', image=self.iconLogout, anchor="e", width=150, height=50, border=0, borderwidth=0, compound=RIGHT, font=('Arial Bold', 16))
        # self.buttonLogout.pack(side=RIGHT) # , padx=10
        #
        # self.iconLogin = ReSizeIcon(Image.open('./icons/lib.png'), 50, 50)
        # self.buttonLogin = Button(topFrame, text='Login', image=self.iconLogin, anchor="e", width=150, height=50, border=0, borderwidth=0, compound=RIGHT, font=('Arial Bold', 16))
        # self.buttonLogin.pack(side=RIGHT) # , padx=10

        ####

        self.tabs = ttk.Notebook(centerLeftFrame, width=720, height=640) #
        self.tabs.pack()
        self.tabIcon1 = ReSizeIcon(Image.open('./icons/lib.png'), 50, 50)
        self.tabIcon2 = ReSizeIcon(Image.open('./icons/lib.png'), 50, 50)
        self.tab1 = Frame(self.tabs)
        self.tab2 = Frame(self.tabs)
        self.tabs.add(self.tab1, text='Library Management', image=self.tabIcon1, compound=LEFT)
        self.tabs.add(self.tab2, text='Statistics', image=self.tabIcon2, compound=LEFT)

        self.listBooks = Listbox(self.tab1, width=32, height=32, font=('Arial Bold', 14)) # , bd=5
        self.scrollBar = Scrollbar(self.tab1, orient=VERTICAL)
        self.listBooks.grid(row=0, column=0, padx=(10, 0), pady=10, sticky=N) #
        # self.scrollBar.config(yscrollcommand=self.scrollBar.set)
        self.scrollBar.grid(row=0, column=0, sticky=N + S + E)
        ##
        self.listDetails = Listbox(self.tab1, width=58, height=32, font=('Arial Bold', 14)) # , bd=5
        self.listDetails.grid(row=0, column=1, padx=(10, 0), pady=10, sticky=N) #
        ####
        self.labelBookCount = Label(self.tab2, text='', pady=20, font=('Arial Bold', 14))
        self.labelBookCount.grid(row=0,)
        self.labelMemberCount = Label(self.tab2, text='', pady=20, font=('Arial Bold', 14))
        self.labelMemberCount.grid(row=1, sticky=W)
        self.labelTakenCount = Label(self.tab2, text='', pady=20, font=('Arial Bold', 14))
        self.labelTakenCount.grid(row=2, sticky=W)

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

    def GiveBook(self):
        give = GiveBook.GiveBook()

    def SearchBook(self):
        value = self.entrySearch.get()
        # check = 'SELECT * FROM `Book` WHERE `name_book` = %s OR `author` = %s OR `publisher` = %s OR `types` = %s OR `content` = %s'
        # search = myCursor.execute(check, (name_book, author, publisher, types, content))
        check = 'SELECT * FROM `Book` WHERE `name_book` = %s'
        myCursor.execute(check, ('%' + value + '%',))
        search = myCursor.fetchall()
        # print(search)
        self.listBooks.delete(0, 'end')
        count = 0
        for book in search:
            self.listBooks.insert(count, str(book[0]) + '. ' + book[1])
            count += 1

    def ListBook(self):
        value = self.listChoice.get()
        if value == 1:
            check = 'SELECT * FROM `Book`'
            myCursor.execute(check)
            allBook = myCursor.fetchall()
            self.listBooks.delete(0, 'end')

            count = 0
            for book in allBook:
                self.listBooks.insert(count, str(book[0]) + '. ' + book[1])
                count += 1
        elif value == 2:
            check = 'SELECT * FROM `Book` WHERE `borrowed` = %s'
            myCursor.execute(check, bool('0'))
            bookInLibrary = myCursor.fetchall()
            self.listBooks.delete(0, 'end')

            count = 0
            for book in bookInLibrary:
                self.listBooks.insert(count, str(book[0]) + '. ' + book[1])
                count +=1

        elif value == 3:
            check = 'SELECT * FROM `Book` WHERE `borrowed` = %s'
            myCursor.execute(check, bool('1'))
            takenBook = myCursor.fetchall()
            self.listBooks.delete(0, 'end')

            count = 0
            for book in takenBook:
                self.listBooks.insert(count, str(book[0]) + '. ' + book[1])
                count +=1



def main():
    root = Tk()
    app = Main(root)
    root.title('Gorth Library Maganement Application')
    root.minsize(width=1280, height=720)
    root.geometry('1280x720')
    root.iconbitmap('./icons/bitmap.ico')
    root.iconphoto(True, PhotoImage(file='./icons/app.png'), PhotoImage(file='./icons/app.png'))
    root.configure(background="#FF00AA")
    root.mainloop() # command=self.quit

if __name__ == '__main__':
    main()
