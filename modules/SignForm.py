from tkinter import *
from customtkinter import *
from PIL import Image, ImageTk
from CTkListbox import *
import pymysql
import os

import AddBook
import AddMember

set_appearance_mode("System")
set_default_color_theme("blue")

main_color = '#62e2ff'
hover_color = '#74f0ff'

myPassword = 'Jiang@99@03$0820'
myDatabase = 'se_proj'

myConnect = pymysql.connect(host='localhost', user='root', password=myPassword, database=myDatabase)
myCursor = myConnect.cursor()


def CheckButton(button):
    if True:
        button.config(state='enabled')
    else:
        button.config(state='disabled')

class App(CTk):
    def __init__(self):
        super().__init__()
        appIconConst = PhotoImage(file='./icons/app.png')
        self.title('Gorth Library Maganement Application')
        self.minsize(width=1280, height=720)
        self.geometry('1280x720')
        self.iconbitmap('./icons/bitmap.ico')
        self.resizable(False, False)
        self.iconphoto(True, appIconConst, appIconConst)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        ####

        # imagePath = os.path.join(os.path.dirname(os.path.realpath(__file__)), "icons")
        self.logoImage = CTkImage(Image.open('./icons/logo_modified.png'), size=(50, 50))
        self.largeTestImage = CTkImage(Image.open('./icons/cmd.png'), size=(200, 200))
        self.iconImage = CTkImage(Image.open('./icons/cmd.png'), size=(20, 20))
        self.addUserImage = CTkImage(Image.open('./icons/member.png'), size=(40, 40))

        ####

        self.navigationFrame = CTkFrame(self)
        self.navigationFrame.grid(row=0, column=0, sticky="nsew")
        self.navigationFrame.grid_rowconfigure(4, weight=1)

        self.navigationFrameLabel = CTkLabel(self.navigationFrame, text='  Gorth Inc.', image=self.logoImage, compound='left', font=CTkFont('Arial', size=20, weight='bold'))
        self.navigationFrameLabel.grid(row=0, column=0, padx=20, pady=20)

        self.userButton = CTkButton(self.navigationFrame, height=50, text="Users", image=self.addUserImage,
                                     fg_color='transparent', text_color=('black', 'white'), hover_color=('gray75', 'gray25'), anchor='w',
                                     font=CTkFont('Arial', size=14, weight='normal'))
        self.userButton.grid(row=3, column=0, padx=5, pady=(5, 0), sticky="ew")

        self.appearanceModeMenu = CTkOptionMenu(self.navigationFrame, values=['System', 'Light', 'Dark'], command=self.change_appearance_mode_event)
        self.appearanceModeMenu.grid(row=6, column=0, padx=20, pady=20, sticky="s")

        ####

        self.contentFrame = CTkFrame(self, fg_color=('#AAAAAA', '#555555'))
        self.contentFrame.grid(row=0, column=1, sticky="nsew")
        self.contentFrame.grid_rowconfigure(0, weight=1)
        self.contentFrame.grid_columnconfigure(0, weight=1)

        ####

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

        self.signMainCenterFrame = CTkFrame(self.signCenterFrame, fg_color=('#555555', '#AAAAAA'))
        self.signMainCenterFrame.grid(row=0, column=0, padx=5, sticky='nsew')
        self.signMainCenterFrame.grid_columnconfigure(0, weight=1)
        self.signMainCenterFrame.grid_rowconfigure(0, weight=1)

        self.signBottomFrame = CTkFrame(self.signFrame, fg_color='transparent')
        self.signBottomFrame.grid(row=2, column=0, sticky='nsew')
        self.signBottomFrame.columnconfigure(0, weight=1)

        ##

        self.signinImg = CTkImage(Image.open('./icons/book.png'), size=(50, 50))
        self.signinButton = CTkButton(self.signTopFrame, text='Sign In', image=self.signinImg, anchor="w", width=150,
                                       height=50, border_width=0, compound='left', font=('Arial Bold', 16),
                                       command=self.SigninEvent)
        self.signinButton.pack(side='left', padx=(5, 0), pady=5)

        self.signupImg = CTkImage(Image.open('./icons/book.png'), size=(50, 50))
        self.signupButton = CTkButton(self.signTopFrame, text='Sign Up', image=self.signupImg, anchor="w", width=150,
                                       height=50, border_width=0, compound='left', font=('Arial Bold', 16),
                                       command=self.SignupEvent)
        self.signupButton.pack(side='left', padx=(5, 0), pady=5)

        ##

        self.signoutImg = CTkImage(Image.open('./icons/launch.png'), size=(50, 50))
        self.singoutButton = CTkButton(self.signBottomFrame, text='Sign Out', image=self.signoutImg, anchor="w", width=150, height=50,
                                    border_width=0, compound='left', font=('Arial Bold', 16), state='disabled',
                                       command=self.SignoutEvent)
        self.singoutButton.pack(side='left', padx=(5, 0), pady=5)

        ####

        self.bgImage = CTkImage(Image.open('./icons/theme.png'), size=(1200, 600))
        self.bgImageLabel = CTkLabel(self.signMainCenterFrame, image=self.bgImage, text=None)
        self.bgImageLabel.grid(row=0, column=0)

        #### # Sign in
        
        self.signinFrame = CTkFrame(self.signMainCenterFrame)
        self.signinFrame.grid(row=0, column=0, sticky='ns')
        self.signinLogo = CTkLabel(self.signinFrame, text=None, image=self.logoImage, compound='center')
        self.signinLogo.grid(row=1, column=0, pady=10)
        self.signinLabel = CTkLabel(self.signinFrame, text="Sign in", font=CTkFont(family='Arial', size=20, weight="bold"))
        self.signinLabel.grid(row=0, column=0, padx=30, pady=30)
        self.usernameEntry = CTkEntry(self.signinFrame, width=200, placeholder_text="username")
        self.usernameEntry.grid(row=2, column=0, padx=30, pady=(15, 15))
        self.passwordEntry = CTkEntry(self.signinFrame, width=200, show="*", placeholder_text="password")
        self.passwordEntry.grid(row=3, column=0, padx=30, pady=(0, 15))
        self.signinFormButton = CTkButton(self.signinFrame, text="Sign in", command=self.MainEvent, width=200)
        self.signinFormButton.grid(row=4, column=0, padx=30, pady=(15, 15))

        #### # Sign up

        self.signupFrame = CTkFrame(self.signMainCenterFrame)
        self.signupFrame.grid(row=0, column=0, sticky='ns')
        self.signupLogo = CTkLabel(self.signupFrame, text=None, image=self.logoImage, compound='center')
        self.signupLogo.grid(row=1, column=0, pady=10)
        self.signupLabel = CTkLabel(self.signupFrame, text="Sign up", font=CTkFont(family='Arial', size=20, weight="bold"))
        self.signupLabel.grid(row=0, column=0, padx=30, pady=30)
        self.usernameEntry = CTkEntry(self.signupFrame, width=200, placeholder_text="id person") # CCCD
        self.usernameEntry.grid(row=2, column=0, padx=30, pady=(15, 15))
        self.signupFormButton = CTkButton(self.signupFrame, text="Sign up", command=self.SignupEvent, width=200)
        self.signupFormButton.grid(row=4, column=0, padx=30, pady=(15, 15))
        self.signupFrame.grid_forget()

        ####

        self.mainFrame = CTkFrame(self.signMainCenterFrame)
        self.mainFrame.grid_columnconfigure(0, weight=1)
        self.mainLabel = CTkLabel(self.mainFrame, text="Home", font=CTkFont(size=20, weight="bold"))
        self.mainLabel.grid(row=0, column=0, padx=30, pady=(30, 15))
        self.backButton = CTkButton(self.mainFrame, text="Back", command=self.SigninEvent, width=200)
        self.backButton.grid(row=1, column=0, padx=30, pady=(15, 15))
        self.mainFrame.grid_forget()

        ####

        self.SelectFrameByName('user')

        ####

    def SelectFrameByName(self, name):
        self.userButton.configure(fg_color=('gray75', 'gray25') if name == "user" else 'transparent')

    def change_appearance_mode_event(self, new_appearance_mode):
        set_appearance_mode(new_appearance_mode)

    ####
    
    def SigninEvent(self):
        # print("Login pressed - username:", self.usernameEntry.get(), "password:", self.passwordEntry.get())
        self.singoutButton.configure(state='disabled')
        self.mainFrame.grid_forget()
        self.signupFrame.grid_forget()
        self.signinFrame.grid(row=0, column=0, sticky='ns')

    def SignupEvent(self):
        self.singoutButton.configure(state='disabled')
        self.mainFrame.grid_forget()
        self.signinFrame.grid_forget()
        self.signupFrame.grid(row=0, column=0, sticky='ns')

    def SignoutEvent(self):
        self.signinButton.configure(state='enabled')
        self.signupButton.configure(state='enabled')
        self.singoutButton.configure(state='disabled')
        self.mainFrame.grid_forget()
        self.signinFrame.grid(row=0, column=0, sticky='ns')

    def MainEvent(self):
        self.signinButton.configure(state='disabled')
        self.signupButton.configure(state='disabled')
        self.singoutButton.configure(state='enabled')
        self.signinFrame.grid_forget()
        self.signupFrame.grid_forget()
        self.mainFrame.grid(row=0, column=0, sticky='nsew')

    # def BackEvent(self):
    #     self.mainFrame.grid_forget()
    #     self.signinFrame.grid(row=0, column=0, sticky='ns')




if __name__ == '__main__':
    app = App()
    app.mainloop()


