from tkinter import *
from tkinter import ttk, messagebox
from customtkinter import *
from PIL import Image, ImageTk
from CTkListbox import *
from CTkMessagebox import *
import datetime
import pymysql
import os

set_appearance_mode("System")
set_default_color_theme("blue")

main_color = '#62e2ff'
hover_color = '#74f0ff'

myPassword = 'Jiang@99@03$0820'
myDatabase = 'se_proj'

myConnect = pymysql.connect(
    host='localhost',
    user='root',
    password=myPassword,
    database=myDatabase
)
myCursor = myConnect.cursor()

currentTime = datetime.datetime.now()
currentDate = str(currentTime.year) + '-' + str(currentTime.month) + '-' + str(currentTime.day)
currentClock = str(currentTime.hour) + ':' + str(currentTime.minute) + ':' + str(currentTime.second)


class BackgroundImageAutoFitContent(CTkFrame):
    path = './icons/theme.png'

    def ChangeImage(self, path):
        img = Image.open(path)
        return img

    def __init__(self, master, *pargs):
        CTkFrame.__init__(self, master, *pargs)
        self.image = self.ChangeImage(self.path)
        self.imageCopy = self.image.copy()
        self.backgroundImage = ImageTk.PhotoImage(self.image)
        self.background = Label(self, image=self.backgroundImage)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self.ResizeImage)

    def ResizeImage(self, event):
        newWidth = event.width
        newHeight = event.height
        self.image = self.imageCopy.resize((newWidth, newHeight))
        self.backgroundImage = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.backgroundImage)


class App(CTk):
    def __init__(self):
        super().__init__()
        appIconConst = PhotoImage(file='./icons/app.png')
        self.title('Gobrary Library Management Application')
        self.minsize(width=1280, height=720)
        self.geometry('1280x720')
        self.iconbitmap('./icons/bitmap.ico')
        self.iconphoto(True, appIconConst, appIconConst)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        ############ # App #############

        self.logoImage = CTkImage(Image.open('./icons/logo_modified.png'), size=(50, 50))
        self.appImage = CTkImage(Image.open('./icons/app.png'), size=(60, 60))
        self.largeTestImage = CTkImage(Image.open('./icons/cmd.png'), size=(200, 200))
        self.iconImage = CTkImage(Image.open('./icons/cmd.png'), size=(20, 20))
        self.homeImage = CTkImage(Image.open('./icons/homes.png'), size=(40, 40))
        self.bookImage = CTkImage(Image.open('./icons/dup.png'), size=(40, 40))
        self.addUserImage = CTkImage(Image.open('./icons/user.png'), size=(40, 40))

        ####

        self.navigationFrame = CTkFrame(self)
        self.navigationFrame.grid(row=0, column=0, sticky="nsew")
        self.navigationFrame.grid_rowconfigure(4, weight=1)

        self.navigationFrameLabel = CTkLabel(
            self.navigationFrame, text='  Gobrary', image=self.appImage,
            compound='left', font=CTkFont('Arial', size=20, weight='bold')
        )
        self.navigationFrameLabel.grid(row=0, column=0, padx=20, pady=20)

        self.homeButton = CTkButton(
            self.navigationFrame, height=50, text="Home",
            image=self.homeImage, fg_color='transparent',
            text_color=('black', 'white'), hover_color=('gray75', 'gray25'),
            font=CTkFont('Arial', size=14, weight='normal'), anchor='w',
            command=self.HomeButtonEvent
        )
        self.homeButton.grid(row=1, column=0, padx=5, pady=(5, 0), sticky="ew")

        self.bookButton = CTkButton(
            self.navigationFrame, height=50, text="Book",
            image=self.bookImage, fg_color='transparent',
            text_color=('black', 'white'), hover_color=('gray75', 'gray25'),
            anchor='w', font=CTkFont('Arial', size=14, weight='normal'),
            command=self.BookButtonEvent
        )
        self.bookButton.grid(row=2, column=0, padx=5, pady=(5, 0), sticky="ew")

        self.userButton = CTkButton(
            self.navigationFrame, height=50, text="Account",
            image=self.addUserImage, fg_color='transparent',
            text_color=('black', 'white'), hover_color=('gray75', 'gray25'),
            anchor='w', font=CTkFont('Arial', size=14, weight='normal'),
            command=self.UserButtonEvent
        )
        self.userButton.grid(row=3, column=0, padx=5, pady=(5, 0), sticky="ew")

        self.appearanceModeMenu = CTkOptionMenu(
            self.navigationFrame, values=['System', 'Light', 'Dark'],
            command=self.ChangeAppearanceModeEvent
        )
        self.appearanceModeMenu.grid(row=6, column=0, padx=20, pady=20, sticky="s")

        ####

        self.contentFrame = CTkFrame(self, fg_color=('#AAAAAA', '#555555'))
        self.contentFrame.grid(row=0, column=1, sticky="nsew")
        self.contentFrame.grid_rowconfigure(0, weight=1)
        self.contentFrame.grid_columnconfigure(1, weight=1)

        ####

        self.homeFrame = CTkFrame(self.contentFrame, fg_color='transparent')
        self.homeFrame.grid_columnconfigure(0, weight=1)
        self.homeFrame.grid_rowconfigure(0, weight=0)
        self.homeFrame.grid_rowconfigure(1, weight=1)
        self.homeFrame.grid_rowconfigure(2, weight=0)
        self.bookFrame = CTkFrame(self.contentFrame, fg_color='transparent')
        self.bookFrame.grid_columnconfigure(0, weight=1)
        self.bookFrame.grid_columnconfigure(1, weight=0)
        self.bookFrame.grid_rowconfigure(0, weight=0)
        self.bookFrame.grid_rowconfigure(1, weight=1)
        self.bookFrame.grid_rowconfigure(2, weight=0)
        self.userFrame = CTkFrame(self.contentFrame, fg_color='transparent')
        self.userFrame.grid_columnconfigure(0, weight=1)

        #### # Home

        self.homeTopFrame = CTkFrame(self.homeFrame, fg_color='transparent')
        self.homeTopFrame.grid(row=0, column=0, sticky='nsew')
        self.homeTopFrame.grid_columnconfigure(0, weight=1)
        self.homeTopFrame.grid_rowconfigure(0, weight=1)

        self.homeCenterFrame = CTkFrame(self.homeFrame, fg_color='transparent')
        self.homeCenterFrame.grid(row=1, column=0, padx=5, sticky='nsew')
        self.homeCenterFrame.grid_columnconfigure(0, weight=1)
        self.homeCenterFrame.grid_rowconfigure(0, weight=1)

        self.homeBottomFrame = CTkFrame(self.homeFrame, fg_color='transparent')
        self.homeBottomFrame.grid(row=2, column=0, sticky='nsew')
        self.homeBottomFrame.columnconfigure(0, weight=1)

        ##

        self.homeBackgroundImageFrame = CTkFrame(self.homeCenterFrame)
        self.homeBackgroundImageFrame.grid(row=0, column=0, sticky='nsew')
        # BackgroundImageAutoFitContent.path = './icons/candy.png'
        self.homeBackgroundImageLabel = BackgroundImageAutoFitContent(self.homeBackgroundImageFrame)
        self.homeBackgroundImageLabel.pack(fill=BOTH, expand=YES)

        ##

        self.homeWelcomeFrame = CTkFrame(self.homeCenterFrame, bg_color='transparent')
        self.homeWelcomeFrame.grid(row=0, column=0, sticky='new')
        self.homeWelcomeFrame.grid_columnconfigure(0, weight=1)
        self.homeWelcomeLabel = CTkLabel(
            self.homeWelcomeFrame, text='Welcome to Gobrary',
            bg_color='transparent', text_color=('black', 'white'),
            font=CTkFont('Arial', size=32, weight='bold')
        )
        self.homeWelcomeLabel.grid(row=0, column=0, pady=20, sticky='nsew')

        self.homeCopyrightFrame = CTkFrame(self.homeCenterFrame, bg_color='transparent')
        self.homeCopyrightFrame.grid(row=0, column=0, sticky='sew')
        self.homeCopyrightFrame.grid_columnconfigure(0, weight=1)
        self.homeCopyrightLabel = CTkLabel(
            self.homeCopyrightFrame,
            text='Powered by Gorth Inc. Copyright © 2020 - 2023 Gorth Inc. All rights reserved.',
            bg_color='transparent', text_color=('black', 'white'),
            font=CTkFont('Arial', size=20, weight='normal')
        )
        self.homeCopyrightLabel.grid(row=0, column=0, pady=20, sticky='nsew')
        
        ##

        self.iconLibrary = CTkImage(Image.open('./icons/logo_modified.png'), size=(50, 50))
        self.buttonLibrary = CTkButton(
            self.homeTopFrame, text='Gorth Inc.',
            image=self.iconLibrary, width=150, height=50, fg_color='black', hover_color='white',
            compound='left', anchor="w", font=CTkFont('Arial', size=16, weight='bold')
        )
        self.buttonLibrary.pack(side='left', padx=(5, 0), pady=5)

        self.iconHomeAccount = CTkImage(Image.open('./icons/user.png'), size=(50, 50))
        self.buttonHomeAccount = CTkButton(
            self.homeTopFrame, text='Account',
            image=self.iconHomeAccount, width=150, height=50,
            compound='left', anchor="w", font=CTkFont('Arial', size=16, weight='bold'),
            command=self.UserButtonEvent
        )
        self.buttonHomeAccount.pack(side='right', padx=(0, 5), pady=5)

        self.iconNothing = CTkImage(Image.open('./icons/launch.png'), size=(50, 50))
        self.buttonNothing = CTkButton(
            self.homeBottomFrame, text='Nothing :)',
            image=self.iconNothing, width=150, height=50,
            compound='left', anchor="w", font=CTkFont('Arial', size=16, weight='bold'), state='disabled'
        )
        self.buttonNothing.pack(side='right', padx=(0, 5), pady=5)

        #### # Book

        self.bookTopFrame = CTkFrame(self.bookFrame, fg_color='transparent')
        self.bookTopFrame.grid(row=0, column=0, sticky='nsew')
        self.bookTopFrame.grid_columnconfigure(0, weight=1)
        self.bookTopFrame.grid_rowconfigure(0, weight=1)

        self.bookMainFrame = CTkFrame(self.bookFrame, fg_color=('#555555', '#AAAAAA'))
        self.bookMainFrame.grid(row=1, column=0, padx=5, sticky='nsew')
        self.bookMainFrame.grid_rowconfigure(0, weight=1)
        self.bookMainFrame.grid_columnconfigure(0, weight=1)

        self.bookCenterFrame = CTkFrame(self.bookMainFrame, fg_color='transparent')
        self.bookCenterFrame.grid(row=0, column=0)
        self.bookCenterFrame.grid_columnconfigure(0, weight=6)
        self.bookCenterFrame.grid_columnconfigure(1, weight=4)
        self.bookCenterFrame.grid_rowconfigure(0, weight=1)

        self.bookCenterLeftFrame = CTkFrame(self.bookCenterFrame, fg_color=('#555555', '#AAAAAA'))
        self.bookCenterLeftFrame.grid(row=0, column=0, sticky='nsew')
        self.bookCenterLeftFrame.grid_columnconfigure(0, weight=1)
        self.bookCenterLeftFrame.grid_rowconfigure(0, weight=1)

        self.bookCenterRightFrame = CTkFrame(self.bookCenterFrame, fg_color=('#555555', '#AAAAAA'))
        self.bookCenterRightFrame.grid(row=0, column=1, sticky='nsew')
        self.bookCenterRightFrame.grid_columnconfigure(0, weight=1)
        self.bookCenterRightFrame.grid_rowconfigure((0, 1), weight=1)
        self.bookCenterRightTopFrame = CTkFrame(self.bookCenterRightFrame, fg_color=('#DBDBDB', '#2B2B2B'))
        self.bookCenterRightTopFrame.grid(row=0, column=0, padx=(0, 5), pady=5, sticky='nsew')
        self.bookCenterRightTopFrame.grid_columnconfigure(0, weight=1)
        self.bookCenterRightTopFrame.grid_rowconfigure(0, weight=1)
        self.bookCenterRightBottomFrame = CTkFrame(self.bookCenterRightFrame, fg_color=('#DBDBDB', '#2B2B2B'))
        self.bookCenterRightBottomFrame.grid(row=1, column=0, padx=(0, 5), pady=(0, 5), sticky='nsew')
        self.bookCenterRightBottomFrame.grid_columnconfigure(0, weight=1)
        self.bookCenterRightBottomFrame.grid_rowconfigure(0, weight=1)

        self.bookBottomFrame = CTkFrame(self.bookFrame, fg_color='transparent')
        self.bookBottomFrame.grid(row=2, column=0, sticky='nsew')
        self.bookBottomFrame.grid_columnconfigure(0, weight=1)

        ##

        self.iconHomeBook = CTkImage(Image.open('./icons/list.png'), size=(50, 50))
        self.buttonHomeBook = CTkButton(
            self.bookTopFrame, text='Home List',
            image=self.iconHomeBook, width=150, height=50,
            compound='left', anchor="w", font=CTkFont('Arial', size=16, weight='bold'),
            state='disabled', command=self.HomeListEvent
        )
        self.buttonHomeBook.pack(side='left', padx=(5, 0), pady=5)
        self.buttonHomeBook.pack_forget()

        self.iconAddBook = CTkImage(Image.open('./icons/book.png'), size=(50, 50))
        self.buttonAddBook = CTkButton(
            self.bookTopFrame, text='Add Book',
            image=self.iconAddBook, width=150, height=50,
            compound='left', anchor="w", font=CTkFont('Arial', size=16, weight='bold'),
            command=self.AddBookEvent
        )
        self.buttonAddBook.pack(side='left', padx=(5, 0), pady=5)
        self.buttonAddBook.pack_forget()

        self.iconDelBook = CTkImage(Image.open('./icons/recbin.png'), size=(50, 50))
        self.buttonDelBook = CTkButton(
            self.bookTopFrame, text='Del Book',
            image=self.iconDelBook, width=150, height=50,
            compound='left', anchor="w", font=CTkFont('Arial', size=16, weight='bold'),
            command=self.DelBookEvent
        )
        self.buttonDelBook.pack(side='left', padx=(5, 0), pady=5)
        self.buttonDelBook.pack_forget()

        self.iconBorBook = CTkImage(Image.open('./icons/bor.png'), size=(50, 50))
        self.buttonBorBook = CTkButton(
            self.bookTopFrame, text='Borrow',
            image=self.iconBorBook, width=150, height=50,
            compound='left', anchor="w", font=CTkFont('Arial', size=16, weight='bold'),
            command=self.BorBookEvent
        )
        self.buttonBorBook.pack(side='left', padx=(5, 0), pady=5)
        self.buttonBorBook.pack_forget()

        self.iconRtnBook = CTkImage(Image.open('./icons/rtn.png'), size=(50, 50))
        self.buttonRtnBook = CTkButton(
            self.bookTopFrame, text='Return',
            image=self.iconRtnBook, width=150, height=50,
            compound='left', anchor="w", font=CTkFont('Arial', size=16, weight='bold'),
            command=self.RtnBookEvent
        )
        self.buttonRtnBook.pack(side='left', padx=(5, 0), pady=5)
        self.buttonRtnBook.pack_forget()

        ##

        self.iconBookAccount = CTkImage(Image.open('./icons/user.png'), size=(50, 50))
        self.buttonBookAccount = CTkButton(
            self.bookTopFrame, text='Account',
            image=self.iconBookAccount, width=150, height=50,
            compound='left', anchor="w", font=CTkFont('Arial', size=16, weight='bold'),
            command=self.UserButtonEvent
        )
        self.buttonBookAccount.pack(side='right', padx=(0, 5), pady=5)

        self.iconGiveBook = CTkImage(Image.open('./icons/launch.png'), size=(50, 50))
        self.buttonGiveBook = CTkButton(
            self.bookBottomFrame, text='Nothing :)',
            image=self.iconGiveBook, width=150, height=50,
            compound='left', anchor="w", font=CTkFont('Arial', size=16, weight='bold'),
            state='disabled'
        )
        self.buttonGiveBook.pack(side='right', padx=(0, 5), pady=5)

        ##

        self.tabs = CTkTabview(self.bookCenterLeftFrame)
        self.tabs.grid(padx=5, pady=(0, 5), sticky='nsew')
        self.tab1 = self.tabs.add('Library Management')
        self.tab1.columnconfigure(0, weight=6)
        self.tab1.columnconfigure(1, weight=4)
        self.tab1.rowconfigure(0, weight=1)
        self.tab2 = self.tabs.add('Statistics')

        ##

        self.listBooks = CTkListbox(
            self.tab1, text_color=('black', 'white'),
            font=CTkFont(family='Arial', size=14, weight='bold'),
            command=self.BookInfo
        )
        self.listBooks.grid(row=0, column=0, padx=(10, 0), pady=(0, 10), sticky='nsew')
        self.listDetails = CTkListbox(
            self.tab1, text_color=('black', 'white'),
            font=CTkFont('Arial', size=14, weight='bold')
        )
        self.listDetails.grid(row=0, column=1, padx=(10, 10), pady=(0, 10), sticky='nsew')
        ##
        self.labelBookCount = CTkLabel(self.tab2, text='', font=CTkFont('Arial', size=20, weight='bold'))
        self.labelBookCount.grid(row=0, padx=50, pady=(50, 20), sticky='w')
        self.labelMemberCount = CTkLabel(self.tab2, text='a', font=CTkFont('Arial', size=20, weight='bold'))
        self.labelMemberCount.grid(row=1, padx=50, pady=20, sticky='w')
        self.labelTakenCount = CTkLabel(self.tab2, text='a', font=CTkFont('Arial', size=20, weight='bold'))
        self.labelTakenCount.grid(row=2, padx=50, pady=20, sticky='w')

        ##

        self.searchBar = CTkFrame(self.bookCenterRightTopFrame)
        self.searchBar.grid(row=0, column=0, sticky='ns')
        self.searchBar.grid_columnconfigure(0, weight=1)
        self.searchBar.grid_rowconfigure((0, 3), weight=1)
        self.searchBar0 = CTkLabel(
            self.searchBar, text='Search Box',
            fg_color='transparent', text_color=('black', 'white'),
            font=CTkFont('Arial', size=24, weight='bold')
        )
        self.searchBar0.grid(row=0, column=0, pady=30, sticky='n')
        self.searchBar1 = CTkFrame(self.searchBar, fg_color='transparent')
        self.searchBar1.grid(row=1, column=0, pady=15, sticky='s')
        self.searchBar2 = CTkFrame(self.searchBar, fg_color='transparent')
        self.searchBar2.grid(row=2, column=0, pady=15, sticky='n')
        self.searchBar3 = CTkFrame(self.searchBar, fg_color='transparent')
        self.searchBar3.grid(row=3, column=0, pady=15, sticky='s')
        self.labelSearch = CTkLabel(
            self.searchBar1, text='Search: ', text_color=('black', 'white'),
            font=CTkFont('Arial', size=18, weight='bold')
        )
        self.labelSearch.grid(row=1)
        self.entrySearch = CTkEntry(self.searchBar2, font=CTkFont('Arial', size=16, weight='bold'), width=320)
        self.entrySearch.grid(row=2)
        self.buttonSearch = CTkButton(
            self.searchBar3, text='Search', width=160,
            font=CTkFont('Arial', size=16, weight='bold'),
            command=self.SearchBook
        )
        self.buttonSearch.grid(row=3)

        self.listBar = CTkFrame(self.bookCenterRightBottomFrame)
        self.listBar.grid(row=0, column=0, sticky='ns')
        self.listBar.grid_columnconfigure(0, weight=1)
        self.listBar.grid_rowconfigure((0, 2), weight=1)
        self.listBar0 = CTkLabel(
            self.listBar, text='List Box',
            fg_color='transparent', text_color=('black', 'white'),
            font=CTkFont('Arial', size=24, weight='bold')
        )
        self.listBar0.grid(row=0, column=0, pady=30, sticky='n')
        self.listBar1 = CTkFrame(self.listBar, fg_color='transparent')
        self.listBar1.grid(row=1, column=0, pady=15, sticky='s')
        self.listBar2 = CTkFrame(self.listBar, fg_color='transparent')
        self.listBar2.grid(row=2, column=0, pady=15, sticky='n')
        self.listBar3 = CTkFrame(self.listBar, fg_color='transparent')
        self.listBar3.grid(row=3, column=0, pady=15, sticky='s')
        self.labelList = CTkLabel(
            self.listBar1, text='Sort by:', text_color=('black', 'white'),
            font=CTkFont('Arial', size=18, weight='bold')
        )
        self.labelList.grid(row=1)
        self.listChoice = IntVar()
        ##
        self.radioButton1 = CTkRadioButton(
            self.listBar2, text='All Books',
            variable=self.listChoice, value=1,
            font=CTkFont('Arial', size=12, weight='bold')
        )
        self.radioButton2 = CTkRadioButton(
            self.listBar2, text='In Library',
            variable=self.listChoice, value=2,
            font=CTkFont('Arial', size=12, weight='bold')
        )
        self.radioButton3 = CTkRadioButton(
            self.listBar2, text='Borrowed Books',
            variable=self.listChoice, value=3,
            font=CTkFont('Arial', size=12, weight='bold')
        )
        self.radioButton1.grid(row=0, column=0)
        self.radioButton2.grid(row=0, column=1)
        self.radioButton3.grid(row=0, column=2)
        self.buttonList = CTkButton(
            self.listBar3, text='List Books', width=160,
            font=CTkFont('Arial', size=16, weight='bold'),
            command=self.ListBook
        )
        self.buttonList.grid(row=3, column=0)

        self.bookCenterFrame.grid_forget()

        ############ # Form ############

        #### # BorBook Form

        self.borFrame = CTkFrame(self.bookMainFrame, fg_color=('#DBDBDB', '#2B2B2B'))
        self.borFrame.grid(row=0, column=0, sticky='nsew')
        self.borFrame.grid_columnconfigure(0, weight=1)
        self.borFrame.grid_rowconfigure(8, weight=1)
        self.borLabel = CTkLabel(
            self.borFrame, text="Borrow Book",
            font=CTkFont(family='Arial', size=20, weight="bold")
        )
        self.borLabel.grid(row=0, column=0, padx=30, pady=30)
        self.borNameEntry = CTkEntry(
            self.borFrame, width=320, placeholder_text="name book",
            font=CTkFont(family='Arial', size=14)
        )
        self.borNameEntry.grid(row=1, column=0, padx=30, pady=(15, 15))
        self.borFormButton = CTkButton(self.borFrame, text="Borrow", width=160, command=self.BorBook)
        self.borFormButton.grid(row=9, column=0, padx=30, pady=(15, 15))
        self.borFrame.grid_forget()

        #### # RtnBook Form

        self.rtnFrame = CTkFrame(self.bookMainFrame, fg_color=('#DBDBDB', '#2B2B2B'))
        self.rtnFrame.grid(row=0, column=0, sticky='nsew')
        self.rtnFrame.grid_columnconfigure(0, weight=1)
        self.rtnFrame.grid_rowconfigure(8, weight=1)
        self.rtnLabel = CTkLabel(
            self.rtnFrame, text="Return Book",
            font=CTkFont(family='Arial', size=20, weight="bold")
        )
        self.rtnLabel.grid(row=0, column=0, padx=30, pady=30)
        self.rtnNameEntry = CTkEntry(
            self.rtnFrame, width=320, placeholder_text="name book",
            font=CTkFont(family='Arial', size=14)
        )
        self.rtnNameEntry.grid(row=1, column=0, padx=30, pady=(15, 15))
        self.rtnFormButton = CTkButton(self.rtnFrame, text="Return", width=160, command=self.RtnBook)
        self.rtnFormButton.grid(row=9, column=0, padx=30, pady=(15, 15))
        self.rtnFrame.grid_forget()

        #### # AddBook Form

        self.addFrame = CTkFrame(self.bookMainFrame, fg_color=('#DBDBDB', '#2B2B2B'))
        self.addFrame.grid(row=0, column=0, sticky='nsew')
        self.addFrame.grid_columnconfigure(0, weight=1)
        self.addFrame.grid_rowconfigure(8, weight=1)
        self.addLabel = CTkLabel(
            self.addFrame, text="Add Book",
            font=CTkFont(family='Arial', size=20, weight="bold")
        )
        self.addLabel.grid(row=0, column=0, padx=30, pady=30)
        self.addNameEntry = CTkEntry(
            self.addFrame, width=320, placeholder_text="name book",
            font=CTkFont(family='Arial', size=14)
        )
        self.addNameEntry.grid(row=1, column=0, padx=30, pady=(15, 15))
        self.addAuthorEntry = CTkEntry(
            self.addFrame, width=320, placeholder_text="author",
            font=CTkFont(family='Arial', size=14)
        )
        self.addAuthorEntry.grid(row=2, column=0, padx=30, pady=(0, 15))
        self.addPublisherEntry = CTkEntry(
            self.addFrame, width=320, placeholder_text="publisher",
            font=CTkFont(family='Arial', size=14)
        )
        self.addPublisherEntry.grid(row=3, column=0, padx=30, pady=(0, 15))
        self.addTypesEntry = CTkEntry(
            self.addFrame, width=320, placeholder_text="types",
            font=CTkFont(family='Arial', size=14)
        )
        self.addTypesEntry.grid(row=4, column=0, padx=30, pady=(0, 15))
        self.addQuantityEntry = CTkEntry(
            self.addFrame, width=320, placeholder_text="quantity",
            font=CTkFont(family='Arial', size=14)
        )
        self.addQuantityEntry.grid(row=5, column=0, padx=30, pady=(0, 15))
        self.addContentEntry = CTkEntry(
            self.addFrame, width=320, placeholder_text="content",
            font=CTkFont(family='Arial', size=14)
        )
        self.addContentEntry.grid(row=6, column=0, padx=30, pady=(0, 15))
        self.addStoragedEntry = CTkEntry(
            self.addFrame, width=320, placeholder_text="storaged",
            font=CTkFont(family='Arial', size=14)
        )
        self.addStoragedEntry.grid(row=7, column=0, padx=30, pady=(0, 15))
        self.addFormButton = CTkButton(self.addFrame, text="Add", width=160, command=self.AddBook)
        self.addFormButton.grid(row=9, column=0, padx=30, pady=(15, 15))
        self.addFrame.grid_forget()

        #### # DelBook Form

        self.delFrame = CTkFrame(self.bookMainFrame, fg_color=('#DBDBDB', '#2B2B2B'))
        self.delFrame.grid(row=0, column=0, sticky='nsew')
        self.delFrame.grid_columnconfigure(0, weight=1)
        self.delFrame.grid_rowconfigure(8, weight=1)
        self.delLabel = CTkLabel(
            self.delFrame, text="Delete Book",
            font=CTkFont(family='Arial', size=20, weight="bold")
        )
        self.delLabel.grid(row=0, column=0, padx=30, pady=30)
        self.delNameEntry = CTkEntry(
            self.delFrame, width=320, placeholder_text="name book",
            font=CTkFont(family='Arial', size=14)
        )
        self.delNameEntry.grid(row=1, column=0, padx=30, pady=(15, 15))
        self.delAuthorEntry = CTkEntry(
            self.delFrame, width=320, placeholder_text="author",
            font=CTkFont(family='Arial', size=14)
        )
        self.delAuthorEntry.grid(row=2, column=0, padx=30, pady=(0, 15))
        self.delPublisherEntry = CTkEntry(
            self.delFrame, width=320, placeholder_text="publisher",
            font=CTkFont(family='Arial', size=14)
        )
        self.delPublisherEntry.grid(row=3, column=0, padx=30, pady=(0, 15))
        self.delQuantityEntry = CTkEntry(
            self.delFrame, width=320, placeholder_text="quantity",
            font=CTkFont(family='Arial', size=14)
        )
        self.delQuantityEntry.grid(row=4, column=0, padx=30, pady=(0, 15))
        self.delStoragedEntry = CTkEntry(
            self.delFrame, width=320, placeholder_text="storaged",
            font=CTkFont(family='Arial', size=14)
        )
        self.delStoragedEntry.grid(row=5, column=0, padx=30, pady=(0, 15))
        self.delFormButton = CTkButton(self.delFrame, text="Delete", width=160, command=self.DelBook)
        self.delFormButton.grid(row=9, column=0, padx=30, pady=(15, 15))
        self.delFrame.grid_forget()

        #### # User

        self.signFrame = CTkFrame(self.contentFrame, fg_color='transparent')
        self.signFrame.grid(row=0, column=0, sticky="nsew")
        self.signFrame.grid_columnconfigure(0, weight=1)
        self.signFrame.grid_rowconfigure(0, weight=0)
        self.signFrame.grid_rowconfigure(1, weight=1)
        self.signFrame.grid_rowconfigure(2, weight=0)

        ####

        self.signTopFrame = CTkFrame(self.signFrame, fg_color='transparent')
        self.signTopFrame.grid(row=0, column=0, sticky='nsew')
        self.signTopFrame.grid_columnconfigure(0, weight=1)
        self.signTopFrame.grid_rowconfigure(0, weight=1)

        self.signCenterFrame = CTkFrame(self.signFrame, fg_color='transparent')
        self.signCenterFrame.grid(row=1, column=0, sticky='nsew')
        self.signCenterFrame.grid_columnconfigure(0, weight=1)
        self.signCenterFrame.grid_rowconfigure(0, weight=1)

        self.signMainCenterFrame = CTkFrame(self.signCenterFrame, fg_color='transparent')
        self.signMainCenterFrame.grid(row=0, column=0, padx=5, sticky='nsew')
        self.signMainCenterFrame.grid_columnconfigure(0, weight=1)
        self.signMainCenterFrame.grid_rowconfigure(0, weight=1)

        self.signBottomFrame = CTkFrame(self.signFrame, fg_color='transparent')
        self.signBottomFrame.grid(row=2, column=0, sticky='nsew')
        self.signBottomFrame.columnconfigure(0, weight=1)

        ##

        self.signinImg = CTkImage(Image.open('./icons/signin.png'), size=(50, 50))
        self.signinButton = CTkButton(
            self.signTopFrame, text='Sign In',
            image=self.signinImg, width=150, height=50,
            compound='left', anchor="w", font=CTkFont('Arial', size=16, weight='bold'),
            command=self.SigninEvent, state='disabled'
        )
        self.signinButton.pack(side='left', padx=(5, 0), pady=5)

        self.signupImg = CTkImage(Image.open('./icons/signup.png'), size=(50, 50))
        self.signupButton = CTkButton(
            self.signTopFrame, text='Sign Up',
            image=self.signupImg, width=150, height=50,
            compound='left', anchor="w", font=CTkFont('Arial', size=16, weight='bold'),
            command=self.SignupEvent
        )
        self.signupButton.pack(side='left', padx=(5, 0), pady=5)

        self.signAccountImg = CTkImage(Image.open('./icons/user.png'), size=(50, 50))
        self.signAccountButton = CTkButton(
            self.signTopFrame, text='',
            image=self.signAccountImg, width=150, height=50,
            compound='left', anchor="w", font=CTkFont('Arial', size=16, weight='bold'),
            state='disabled'
        )
        self.signAccountButton.pack(side='right', padx=(0, 5), pady=5)
        self.signAccountButton.pack_forget()

        self.signoutImg = CTkImage(Image.open('./icons/launch.png'), size=(50, 50))
        self.signoutButton = CTkButton(
            self.signBottomFrame, text='Sign Out',
            image=self.signoutImg, width=150, height=50,
            compound='left', anchor="w", font=CTkFont('Arial', size=16, weight='bold'),
            state='disabled', command=self.LogedOut
        )
        self.signoutButton.pack(side='right', padx=(0, 5), pady=5)

        ####

        self.signBackgroundImageFrame = CTkFrame(self.signMainCenterFrame)
        self.signBackgroundImageFrame.grid(row=0, column=0, sticky='nsew')
        # BackgroundImageAutoFitContent.path = './icons/theme.png'
        self.signBackgroundImageLabel = BackgroundImageAutoFitContent(self.signBackgroundImageFrame)
        self.signBackgroundImageLabel.pack(fill=BOTH, expand=YES)

        #### # Sign in

        self.signinFrame = CTkFrame(self.signMainCenterFrame)
        self.signinFrame.grid(row=0, column=0, sticky='ns')
        self.signinFrame.grid_rowconfigure(8, weight=1)
        self.signinLogo = CTkLabel(self.signinFrame, text=None, image=self.logoImage, compound='center')
        self.signinLogo.grid(row=1, column=0, pady=10)
        self.signinLabel = CTkLabel(
            self.signinFrame, text="Sign in",
            font=CTkFont(family='Arial', size=20, weight="bold")
        )
        self.signinLabel.grid(row=0, column=0, padx=30, pady=30)
        self.usernameSigninEntry = CTkEntry(self.signinFrame, width=240, placeholder_text="username")
        self.usernameSigninEntry.grid(row=2, column=0, padx=30, pady=(15, 15))
        self.passwordSigninEntry = CTkEntry(self.signinFrame, width=240, show="*", placeholder_text="password")
        self.passwordSigninEntry.grid(row=3, column=0, padx=30, pady=(0, 15))
        self.signinFormButton = CTkButton(self.signinFrame, text="Sign in", command=self.SignIn, width=240)
        self.signinFormButton.grid(row=9, column=0, padx=30, pady=(15, 15))

        #### # Sign up

        self.signupFrame = CTkFrame(self.signMainCenterFrame)
        self.signupFrame.grid(row=0, column=0, sticky='ns')
        self.signupFrame.grid_rowconfigure(8, weight=1)
        self.signupLogo = CTkLabel(self.signupFrame, text=None, image=self.logoImage, compound='center')
        self.signupLogo.grid(row=1, column=0, pady=10)
        self.signupLabel = CTkLabel(
            self.signupFrame, text="Sign up",
            font=CTkFont(family='Arial', size=20, weight="bold")
        )
        self.signupLabel.grid(row=0, column=0, padx=30, pady=30)
        self.idSignupEntry = CTkEntry(self.signupFrame, width=240, placeholder_text="id person")  # CCCD
        self.idSignupEntry.grid(row=2, column=0, padx=30, pady=(15, 15))
        self.signupFormButton = CTkButton(self.signupFrame, text="Sign up", command=self.CheckID, width=240)  # CheckID
        self.signupFormButton.grid(row=9, column=0, padx=30, pady=(15, 15))
        self.signupFrame.grid_forget()

        #### # Register

        self.registerFrame = CTkFrame(self.signMainCenterFrame)
        self.registerFrame.grid(row=0, column=0, sticky='ns')
        self.registerFrame.grid_rowconfigure(8, weight=1)
        self.registerLogo = CTkLabel(self.registerFrame, text=None, image=self.logoImage, compound='center')
        self.registerLogo.grid(row=1, column=0, pady=10)
        self.registerLabel = CTkLabel(
            self.registerFrame, text="Register",
            font=CTkFont(family='Arial', size=20, weight="bold")
        )
        self.registerLabel.grid(row=0, column=0, padx=30, pady=30)
        self.usernameSignupEntry = CTkEntry(self.registerFrame, width=240, placeholder_text="username")
        self.usernameSignupEntry.grid(row=2, column=0, padx=30, pady=(15, 15))
        self.passwordSignupEntry = CTkEntry(self.registerFrame, width=240, placeholder_text="password")
        self.passwordSignupEntry.grid(row=3, column=0, padx=30, pady=(15, 15))
        self.fullnameSignupEntry = CTkEntry(self.registerFrame, width=240, placeholder_text="fullname")
        self.fullnameSignupEntry.grid(row=4, column=0, padx=30, pady=(15, 15))
        self.genderSignupFrame = CTkFrame(self.registerFrame, width=240, fg_color='transparent')
        self.genderSignupFrame.grid(row=5, column=0, padx=30, pady=(15, 15))
        self.genderChoice = StringVar()
        self.radioMaleButton = CTkRadioButton(
            self.genderSignupFrame, text='Male',
            variable=self.genderChoice, value='male',
            font=CTkFont('Arial', size=12, weight='bold')
        )
        self.radioFemaleButton = CTkRadioButton(
            self.genderSignupFrame, text='Female',
            variable=self.genderChoice, value='female',
            font=CTkFont('Arial', size=12, weight='bold')
        )
        self.radioMaleButton.grid(row=0, column=0, sticky='e')
        self.radioFemaleButton.grid(row=0, column=1, sticky='w')
        self.birthdaySignupFrame = CTkFrame(self.registerFrame, width=240, fg_color='transparent')
        self.birthdaySignupFrame.grid(row=6, column=0, padx=30, pady=(15, 15))
        self.birthdateSignupEntry = CTkEntry(self.birthdaySignupFrame, width=50, placeholder_text="day")
        self.birthdateSignupEntry.grid(row=0, column=0, padx=(0, 30), sticky='e')
        self.birthmonthSignupEntry = CTkEntry(self.birthdaySignupFrame, width=50, placeholder_text="month")
        self.birthmonthSignupEntry.grid(row=0, column=1, padx=(0, 30), sticky='e')
        self.birthyearSignupEntry = CTkEntry(self.birthdaySignupFrame, width=80, placeholder_text="year")
        self.birthyearSignupEntry.grid(row=0, column=2, sticky='w')
        self.addressSignupEntry = CTkEntry(self.registerFrame, width=240, placeholder_text="address")
        self.addressSignupEntry.grid(row=7, column=0, padx=30, pady=(15, 15))
        self.registerFormButton = CTkButton(self.registerFrame, text="Register", command=self.Register, width=240)
        self.registerFormButton.grid(row=9, column=0, padx=30, pady=(15, 15))
        self.registerFrame.grid_forget()

        ####

        self.SelectFrameByName('home')

        ####

        self.DisplayBooks()
        self.DisplayStatistics()

    ############ # Method ##########    ############################

    ############ # Frame ###########

    def SelectFrameByName(self, name):
        self.homeButton.configure(fg_color=('gray75', 'gray25') if name == "home" else 'transparent')
        self.bookButton.configure(fg_color=('gray75', 'gray25') if name == "book" else 'transparent')
        self.userButton.configure(fg_color=('gray75', 'gray25') if name == "user" else 'transparent')

        ####

        if name == 'home':
            self.homeFrame.grid(row=0, column=1, sticky='nsew')
        else:
            self.homeFrame.grid_forget()
        if name == 'book':
            self.bookFrame.grid(row=0, column=1, sticky='nsew')
        else:
            self.bookFrame.grid_forget()
        if name == 'user':
            self.signFrame.grid(row=0, column=1, sticky='nsew')
        else:
            self.signFrame.grid_forget()

    def HomeButtonEvent(self):
        self.SelectFrameByName('home')

    def BookButtonEvent(self):
        self.SelectFrameByName('book')

    def UserButtonEvent(self):
        self.SelectFrameByName('user')

    def ChangeAppearanceModeEvent(self, new_appearance_mode):
        set_appearance_mode(new_appearance_mode)

    ############ # Sign ############

    def SignIn(self):
        username = self.usernameSigninEntry.get().strip()
        password = self.passwordSigninEntry.get().strip()
        query = 'SELECT `id_person`, `password` FROM `account` WHERE `id_person` = %s AND `password` = %s'
        myCursor.execute(query, (username, password))
        user = myCursor.fetchone()
        checkAdmin = 'SELECT `id_librarian` FROM `librarian` WHERE `id_librarian` = %s'
        checkUser = 'SELECT `id_person` FROM `borrower` WHERE `id_person` = %s'
        if myCursor.execute(query, (username, password)) != 0 and len(username) == 12:
            if myCursor.execute(checkUser, username) != 0:
                self.UserUI()
            elif myCursor.execute(checkAdmin, username) != 0:
                self.AdminUI()
            else:
                messagebox.showerror('Error', 'Error username or password', icon='warning')
        else:
            messagebox.showerror('Error', 'Wrong username or password', icon='error')

    def Register(self):
        id_person = self.idSignupEntry.get().strip()
        username = self.usernameSignupEntry.get().strip()
        fullname = self.fullnameSignupEntry.get()
        password = self.passwordSignupEntry.get().strip()
        gender = self.genderChoice.get().strip()
        birthday = self.birthyearSignupEntry.get().strip() + '-' + self.birthmonthSignupEntry.get().strip() + '-' + self.birthdateSignupEntry.get().strip()
        address = self.addressSignupEntry.get()
        if (id_person and fullname and password and gender and birthday and address) != '':
            query1 = 'INSERT INTO `borrower` (`id_person`, `full_name`, `gender`, `birth_day`, `address`) VALUES (%s, %s, %s, %s, %s)'
            myCursor.execute(query1, (id_person, fullname, gender, birthday, address))
            query2 = 'INSERT INTO `account` (`id_person`, `username`, `password`) VALUES (%s, %s, %s)'
            myCursor.execute(query2, (id_person, username, password))
            myConnect.commit()
            messagebox.showinfo('Register', 'Your Account has been created Successfully', icon='info')
        else:
            messagebox.showwarning('Empty Fields', 'Make sure to enter all the information', icon='warning')

    def CheckID(self):
        id_person = self.idSignupEntry.get().strip()
        check = 'SELECT * FROM `account` WHERE `id_person` = %s'
        string1 = ' '
        string2 = string1.join(id_person)
        checknum = string2.split()
        count = 0
        for num in checknum:
            count += num.isnumeric()
        if id_person != '':
            if len(id_person) == 12:
                if count == 12:
                    if myCursor.execute(check, id_person) == 0:
                        self.RegisterEvent()
                    else:
                        messagebox.showerror('Error', 'You have an account with this ID', icon='error')
                else:
                    messagebox.showerror('Warning', 'ID must be number', icon='warning')
            else:
                messagebox.showerror('Warning', 'ID must be 12 character', icon='warning')
        else:
            messagebox.showerror('Warning', "Form can't be Empty", icon='warning')

    ############ # Module ##########

    def AddBook(self):
        name_book = self.addNameEntry.get().strip()
        author = self.addAuthorEntry.get().strip()
        publisher = self.addPublisherEntry.get().strip()
        types = self.addTypesEntry.get().strip()
        quantity = self.addQuantityEntry.get().strip()
        content = self.addContentEntry.get().strip()
        storage = self.addStoragedEntry.get().strip()

        if (name_book and author and publisher and types and quantity and storage) != '':
            check = 'SELECT `name_book`, `author`, `publisher`, `types`, `storage`, `content` FROM `Book` WHERE `name_book` = %s AND `author` = %s AND `publisher` = %s AND `types` = %s AND `storage` = %s AND `content` = %s'
            if myCursor.execute(check, (name_book, author, publisher, types, storage, content)) == 0:
                try:
                    query = 'INSERT INTO `Book` (`name_book`, `author`, `publisher`, `types`, `quantity`, `storage`, `content`, `borrowed`) VALUES (%s, %s, %s, %s, %s, %s, %s, False)'
                    myCursor.execute(query, (
                        name_book, author, publisher, types, int(quantity), storage, content))
                    myConnect.commit()
                    messagebox.showinfo('Success', 'Successfully', icon='info')
                except:
                    messagebox.showerror('Error', "Can't connect to Database", icon='error')
            else:
                update = 'UPDATE `Book` SET `quantity` = `quantity` + %s WHERE `name_book` = %s AND `author` = %s AND `publisher` = %s AND `types` = %s AND `content` = %s'
                myCursor.execute(update, (quantity, name_book, author, publisher, types, content))
                myConnect.commit()
                messagebox.showwarning('Warning', 'Book was in Database', icon='warning')
        else:
            messagebox.showwarning('Warning', "Form can't be Empty", icon='warning')

        self.DisplayStatistics()
        self.DisplayBooks()

    def DelBook(self):
        name_book = self.delNameEntry.get().strip()
        author = self.delAuthorEntry.get().strip()
        publisher = self.delPublisherEntry.get().strip()
        quantity = self.delQuantityEntry.get().strip()
        storage = self.delStoragedEntry.get().strip()

        # try:
        if (name_book and author and publisher and quantity and storage) != '':
            checkmore = 'SELECT `name_book`, `author`, `publisher`, `quantity`, `storage` FROM `Book` WHERE `name_book` = %s AND `author` = %s AND `publisher` = %s AND `quantity` <= %s AND `storage` = %s'
            checkless = 'SELECT `name_book`, `author`, `publisher`, `quantity`, `storage` FROM `Book` WHERE `name_book` = %s AND `author` = %s AND `publisher` = %s AND `quantity` > %s AND `storage` = %s'
            if myCursor.execute(checkmore, (name_book, author, publisher, int(quantity), storage)) != 0:
                try:
                    query = 'DELETE FROM `Book` WHERE `name_book` = %s AND `author` = %s AND `publisher` = %s AND `storage` = %s'
                    myCursor.execute(query, (name_book, author, publisher, storage))
                    myConnect.commit()
                    messagebox.showinfo('Success', 'Successfully', icon='info')
                except:
                    messagebox.showerror('Error', "Can't connect to Database", icon='error')
            elif myCursor.execute(checkless, (name_book, author, publisher, int(quantity), storage)) != 0:
                try:
                    update = 'UPDATE `Book` SET `quantity` = `quantity` - %s WHERE `name_book` = %s AND `author` = %s AND `publisher` = %s AND `storage` = %s'
                    myCursor.execute(update, (quantity, name_book, author, publisher, storage))
                    myConnect.commit()
                    messagebox.showinfo('Success', 'Deleted quantity of book', icon='info')
                except:
                    messagebox.showerror('Error', "Can't connect to Databases", icon='error')
            else:
                messagebox.showwarning('Warning', 'Not in Library', icon='warning')
        else:
            messagebox.showwarning('Warning', "Form can't be Empty", icon='warning')

        self.DisplayStatistics()
        self.DisplayBooks()

    def BorBook(self):
        name_book = self.borNameEntry.get().strip()
        id_person = self.usernameSigninEntry.get().strip()

        if (name_book and id_person) != '':
            check = 'SELECT `id_book`, `name_book` FROM `Book` WHERE `name_book` = %s'
            myCursor.execute(check, (name_book))
            checked = myCursor.fetchall()
            id_book = checked[0][0]
            if checked != 0:
                date = "SELECT `borrowed_date` FROM `ReturnedForm` WHERE `id_person` = %s AND `id_book` = %s AND `returned_date` = '1001-01-01'"
                if myCursor.execute(date, (id_person, id_book)) == 0 and self.BookInfo != 0:
                    try:
                        bor = 'INSERT INTO `BorrowedForm` (`id_person`, `id_book`, `borrowed_date`, `deadline`) VALUES (%s, %s, %s, DATE_ADD(%s, INTERVAL 7 DAY))'
                        myCursor.execute(bor, (id_person, id_book, currentDate, currentDate))
                        myConnect.commit()
                        rtn = 'INSERT INTO `ReturnedForm` (`id_person`, `id_book`, `borrowed_date`) VALUES (%s, %s, %s)'
                        myCursor.execute(rtn, (id_person, id_book, currentDate))
                        myConnect.commit()
                        update = 'UPDATE `Book` SET `borrowed` = True WHERE `name_book` = %s'
                        myCursor.execute(update, (name_book))
                        myConnect.commit()
                        messagebox.showinfo('Success', 'Successfully', icon='info')
                    except:
                        messagebox.showerror('Error', "Can't connect to Database", icon='error')
                else:
                    messagebox.showwarning('Warning', 'You was borrowed this book', icon='warning')
            else:
                messagebox.showwarning('Warning', "Book wasn't in Database", icon='warning')
        else:
            messagebox.showwarning('Warning', "Form can't be Empty", icon='warning')

        self.DisplayStatistics()
        self.DisplayBooks()

    def RtnBook(self):
        name_book = self.rtnNameEntry.get().strip()
        id_person = self.usernameSigninEntry.get().strip()

        if (name_book and id_person) != '':
            check = 'SELECT `id_book`, `name_book` FROM `Book` WHERE `name_book` = %s'
            myCursor.execute(check, (name_book))
            checked = myCursor.fetchall()
            id_book = checked[0][0]
            if checked != 0:
                date = "SELECT `borrowed_date` FROM `ReturnedForm` WHERE `id_person` = %s AND `id_book` = %s AND `returned_date` = '1001-01-01'"
                if myCursor.execute(date, (id_person, id_book)) != 0:
                    myCursor.execute(date, (id_person, id_book))
                    dated = myCursor.fetchall()
                    bordate = dated[0][0]
                    try:
                        update = 'UPDATE `ReturnedForm` SET `returned_date` = %s WHERE `id_person` = %s AND `id_book` = %s AND `borrowed_date` = %s'
                        myCursor.execute(update, (currentDate, id_person, id_book, bordate))
                        myConnect.commit()
                        messagebox.showinfo('Success', 'Successfully', icon='info')
                    except:
                        messagebox.showerror('Error', "Can't connect to Database", icon='error')
                else:
                    messagebox.showwarning('Warning', "You haven't borrowed this book", icon='warning')
            else:
                messagebox.showwarning('Warning', "Book wasn't in Database", icon='warning')
        else:
            messagebox.showwarning('Warning', "Form can't be Empty", icon='warning')

        self.DisplayStatistics()
        self.DisplayBooks()

    def SearchBook(self):
        value = self.entrySearch.get().strip()
        valued = '%' + value + '%'
        check = (
            'SELECT * FROM `Book` WHERE `name_book` LIKE %s OR `author` LIKE %s OR `publisher` LIKE %s OR `types` LIKE %s')
        myCursor.execute(check, (valued, valued, valued, valued))
        checkvalue = myCursor.fetchall()
        self.listBooks.delete('all', 'end')
        count = 0
        for name_book in checkvalue:
            self.listBooks.insert(count, str(name_book[0]) + '. ' + name_book[1])
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
            check = 'SELECT * FROM `Book` WHERE `borrowed` = False'
            myCursor.execute(check)
            bookInLibrary = myCursor.fetchall()
            self.listBooks.delete(0, 'end')

            count = 0
            for book in bookInLibrary:
                self.listBooks.insert(count, str(book[0]) + '. ' + book[1])
                count += 1

        elif value == 3:
            check = 'SELECT * FROM `Book` WHERE `borrowed` = True'
            myCursor.execute(check)
            takenBook = myCursor.fetchall()
            self.listBooks.delete(0, 'end')

            count = 0
            for book in takenBook:
                self.listBooks.insert(count, str(book[0]) + '. ' + book[1])
                count += 1

    def DisplayBooks(self):
        books = myCursor.execute('SELECT * FROM `Book`')
        members = myCursor.execute('SELECT * FROM `Borrower`')
        myCursor.execute('SELECT * FROM `Book`')
        result = myCursor.fetchall()
        count = 0
        for book in result:
            self.listBooks.insert(count, str(book[0]) + '. ' + book[1])
            count += 1

        def BookInfo(self, evt):
            value = str(self.listBooks.get(self.listBooks.curselection()))
            id = value.split('-')[0]
            myCursor.execute('SELECT * FROM `Book` WHERE id_book = %s', (id))
            bookInfo = myCursor.fetchall()

            self.listDetails.insert(0, 'Book Name: ' + bookInfo[0][1])
            self.listDetails.insert(1, 'Author Name: ' + bookInfo[0][2])
            self.listDetails.insert(2, 'Publisher Name: ' + bookInfo[0][3])
            self.listDetails.insert(3, 'Types: ' + bookInfo[0][4])
            self.listDetails.insert(4, 'Content: ' + bookInfo[0][7])

            if bookInfo[0][5] != 0:
                self.listDetails.insert(5, 'Quantity: Avaiable ' + str(bookInfo[0][5]))
            else:
                self.listDetails.insert(5, 'Quantity: Not Avaiable')

        def DoubleClick(self, evt):
            value = str(self.listBooks.get(self.listBooks.curselection()))
            id_given = value.split('-')[0]
            give_book = self.BorBook()

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
    
    def BookInfo(self, value):
        myCursor.execute('SELECT * FROM `Book` WHERE id_book = %s', (value.split('-')[0]))
        bookInfo = myCursor.fetchall()

        self.listDetails.insert(0, 'Book Name: ' + bookInfo[0][1])
        self.listDetails.insert(1, 'Author Name: ' + bookInfo[0][2])
        self.listDetails.insert(2, 'Publisher Name: ' + bookInfo[0][3])
        self.listDetails.insert(3, 'Types: ' + bookInfo[0][4])
        self.listDetails.insert(4, 'Content: ' + bookInfo[0][7])

        check = "SELECT COUNT(id_book) FROM `ReturnedForm` WHERE `id_book` = %s AND returned_date = '1001-01-01'"
        myCursor.execute(check, (bookInfo[0][0]))
        checked = myCursor.fetchall()

        quantity = int(bookInfo[0][5]) - int(checked[0][0])
        if (bookInfo[0][5] and (quantity)) != 0:
            self.listDetails.insert(5, 'Quantity: Avaiable ' + str(quantity))
        else:
            self.listDetails.insert(5, 'Quantity: Not Avaiable')

        return quantity

    def DisplayStatistics(self):
        myCursor.execute('SELECT COUNT(id_book) FROM `Book`')
        countBook = myCursor.fetchall()
        myCursor.execute('SELECT COUNT(id_person) FROM `Borrower`')
        countBorrower = myCursor.fetchall()
        myCursor.execute('SELECT COUNT(id_book) FROM `Book` WHERE `borrowed` = True')
        borrowedBook = myCursor.fetchall()

        self.labelBookCount.configure(text='All Books: ' + str(countBook[0][0]) + ' in library')
        self.labelMemberCount.configure(text='Member: ' + str(countBorrower[0][0]) + ' in library')
        self.labelTakenCount.configure(text='Borrowed Books: ' + str(borrowedBook[0][0]) + ' out library')

    def ReShowList(self):
        check = 'SELECT * FROM `Book`'
        myCursor.execute(check)
        allBook = myCursor.fetchall()
        self.listBooks.delete(0, 'end')

        count = 0
        for book in allBook:
            self.listBooks.insert(count, str(book[0]) + '. ' + book[1])
            count += 1

    ############ # UI ##############

    def AdminUI(self):
        self.buttonHomeBook.pack(side='left', padx=(5, 0), pady=5)
        self.buttonAddBook.pack(side='left', padx=(5, 0), pady=5)
        self.buttonDelBook.pack(side='left', padx=(5, 0), pady=5)
        self.buttonBookAccount.pack_forget()
        self.buttonGiveBook.pack(side='right', padx=(0, 5), pady=5)
        self.buttonHomeAccount.configure(text='Admin')

        self.signinButton.pack_forget()
        self.signupButton.pack_forget()
        self.signinFrame.grid_forget()
        self.signupFrame.grid_forget()
        self.signAccountButton.pack(side='right', padx=(0, 5), pady=5)
        self.signAccountButton.configure(text='Admin', state='enabled')
        self.signoutButton.configure(state='enabled')
        self.bookCenterFrame.grid_columnconfigure(0, weight=6)
        self.bookCenterFrame.grid_columnconfigure(1, weight=4)
        self.bookCenterFrame.grid_rowconfigure(0, weight=1)
        self.bookCenterFrame.grid(row=0, column=0, sticky='nsew')

    def UserUI(self):
        self.buttonHomeBook.pack(side='left', padx=(5, 0), pady=5)
        self.buttonBorBook.pack(side='left', padx=(5, 0), pady=5)
        self.buttonRtnBook.pack(side='left', padx=(5, 0), pady=5)
        self.buttonBookAccount.pack_forget()
        self.buttonGiveBook.pack(side='right', padx=(0, 5), pady=5)
        self.buttonHomeAccount.configure(text='User')

        self.signinButton.pack_forget()
        self.signupButton.pack_forget()
        self.signinFrame.grid_forget()
        self.signupFrame.grid_forget()
        self.signAccountButton.pack(side='right', padx=(0, 5), pady=5)
        self.signAccountButton.configure(text='User', state='enabled')
        self.signoutButton.configure(state='enabled')
        self.bookCenterFrame.grid_columnconfigure(0, weight=6)
        self.bookCenterFrame.grid_columnconfigure(1, weight=4)
        self.bookCenterFrame.grid_rowconfigure(0, weight=1)
        self.bookCenterFrame.grid(row=0, column=0, sticky='nsew')

    def LogedOut(self):
        self.buttonHomeBook.pack_forget()
        self.buttonAddBook.pack_forget()
        self.buttonDelBook.pack_forget()
        self.buttonBorBook.pack_forget()
        self.buttonRtnBook.pack_forget()
        self.signAccountButton.pack_forget()
        self.buttonHomeAccount.configure(text='Account')
        self.buttonBookAccount.pack(side='right', padx=(0, 5), pady=5)

        self.signinButton.pack(side='left', padx=(5, 0), pady=5)
        self.signupButton.pack(side='left', padx=(5, 0), pady=5)
        self.signinFrame.grid_forget()
        self.signupFrame.grid_forget()
        self.signAccountButton.pack_forget()
        self.signoutButton.configure(state='enabled')
        self.bookCenterFrame.grid_forget()

        self.SigninEvent()

    ############ # Event ###########

    def SigninEvent(self):
        self.signinButton.configure(state='disabled')
        self.signupButton.configure(state='enabled')
        self.signoutButton.configure(state='disabled')
        self.signupFrame.grid_forget()
        self.signinFrame.grid(row=0, column=0, sticky='ns')
        self.registerFrame.grid_forget()

    def SignupEvent(self):
        self.signinButton.configure(state='enabled')
        self.signupButton.configure(state='disabled')
        self.signoutButton.configure(state='disabled')
        self.signinFrame.grid_forget()
        self.signupFrame.grid(row=0, column=0, sticky='ns')

    def RegisterEvent(self):
        self.signinButton.configure(state='enabled')
        self.signupButton.configure(state='disabled')
        self.signoutButton.configure(state='disabled')
        self.signinFrame.grid_forget()
        self.signupFrame.grid_forget()
        self.registerFrame.grid(row=0, column=0, sticky='ns')

    def MainEvent(self):
        self.signinButton.configure(state='disabled')
        self.signupButton.configure(state='disabled')
        self.signoutButton.configure(state='enabled')
        self.signinFrame.grid_forget()
        self.signupFrame.grid_forget()

    ####

    def HomeListEvent(self):
        self.buttonHomeBook.configure(state='disabled')
        self.buttonAddBook.configure(state='enabled')
        self.buttonDelBook.configure(state='enabled')
        self.buttonBorBook.configure(state='enabled')
        self.buttonRtnBook.configure(state='enabled')
        self.bookCenterFrame.grid_columnconfigure(0, weight=6)
        self.bookCenterFrame.grid_columnconfigure(1, weight=4)
        self.bookCenterFrame.grid(row=0, column=0, sticky='nsew')
        self.addFrame.grid_forget()
        self.delFrame.grid_forget()
        self.borFrame.grid_forget()
        self.rtnFrame.grid_forget()
        self.ReShowList()

    def AddBookEvent(self):
        self.buttonHomeBook.configure(state='enabled')
        self.buttonAddBook.configure(state='disabled')
        self.buttonDelBook.configure(state='enabled')
        self.buttonBorBook.configure(state='enabled')
        self.buttonRtnBook.configure(state='enabled')
        self.bookMainFrame.grid_columnconfigure(0, weight=1)
        self.bookMainFrame.grid_columnconfigure(1, weight=0)
        self.bookCenterFrame.grid_forget()
        self.addFrame.grid(row=0, column=0, sticky='nsew')
        self.delFrame.grid_forget()
        self.borFrame.grid_forget()
        self.rtnFrame.grid_forget()

    def DelBookEvent(self):
        self.buttonHomeBook.configure(state='enabled')
        self.buttonAddBook.configure(state='enabled')
        self.buttonDelBook.configure(state='disabled')
        self.buttonBorBook.configure(state='enabled')
        self.buttonRtnBook.configure(state='enabled')
        self.bookMainFrame.grid_columnconfigure(0, weight=1)
        self.bookMainFrame.grid_columnconfigure(1, weight=0)
        self.bookCenterFrame.grid_forget()
        self.addFrame.grid_forget()
        self.delFrame.grid(row=0, column=0, sticky='nsew')
        self.borFrame.grid_forget()
        self.rtnFrame.grid_forget()

    def BorBookEvent(self):
        self.buttonHomeBook.configure(state='enabled')
        self.buttonAddBook.configure(state='enabled')
        self.buttonDelBook.configure(state='enabled')
        self.buttonBorBook.configure(state='disabled')
        self.buttonRtnBook.configure(state='enabled')
        self.bookMainFrame.grid_columnconfigure(0, weight=1)
        self.bookMainFrame.grid_columnconfigure(1, weight=0)
        self.bookCenterFrame.grid_forget()
        self.addFrame.grid_forget()
        self.delFrame.grid_forget()
        self.borFrame.grid(row=0, column=0, sticky='nsew')
        self.rtnFrame.grid_forget()

    def RtnBookEvent(self):
        self.buttonHomeBook.configure(state='enabled')
        self.buttonAddBook.configure(state='enabled')
        self.buttonDelBook.configure(state='enabled')
        self.buttonBorBook.configure(state='enabled')
        self.buttonRtnBook.configure(state='disabled')
        self.bookMainFrame.grid_columnconfigure(0, weight=1)
        self.bookMainFrame.grid_columnconfigure(1, weight=0)
        self.bookCenterFrame.grid_forget()
        self.addFrame.grid_forget()
        self.delFrame.grid_forget()
        self.borFrame.grid_forget()
        self.rtnFrame.grid(row=0, column=0, sticky='nsew')

