import pymysql
from tkinter import *
from PIL import *
from PIL import ImageTk,Image
from tkinter import messagebox
# from object import *

my_database = '' # The database name
my_password = 'Jiang@99@03$0820' # use your own password # Gorth$1999 # Jiang@99@03$0820

my_connection = pymysql.connect(host="localhost", user="root", password=my_password, database=my_database) # root is the username here
my_cursor = my_connection.cursor() # cursor -> cursor

def FindBook():
    print('Gorth Inc.')