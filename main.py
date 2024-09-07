from tkinter import *
from tkinter import ttk, messagebox
from customtkinter import *
from PIL import Image, ImageTk
from CTkListbox import *
from CTkMessagebox import *
import datetime
import pymysql
import os
import sys
# from app import *
# from beta import *

from publicbeta import *
from publicvie import *

set_appearance_mode("System")
set_default_color_theme("dark-blue")

main_color = '#62e2ff'
hover_color = '#74f0ff'

myPassword = ''
myDatabase = 'se_proj'

myConnect = pymysql.connect(
    host='localhost',
    user='root',
    password=myPassword,
    database=myDatabase
)
myCursor = myConnect.cursor()

if __name__ == '__main__':
    app = App()
    # app = Ware()
    app.mainloop()
