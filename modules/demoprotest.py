from tkinter import *
from customtkinter import *
from PIL import Image, ImageTk

root = CTk()
root.title("Title")
root.geometry("800x500")
root.configure(background='transparent')


class BackgroundImageAutoFitContent(CTkFrame):
    def __init__(self, master, *pargs):
        CTkFrame.__init__(self, master, *pargs)
        self.image = Image.open('./library.jpg')
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


evt = BackgroundImageAutoFitContent(root)
evt.pack(fill=BOTH, expand=YES)

root.mainloop()

# Import the required libraries
# from tkinter import *
# from PIL import ImageTk, Image
#
# # Create an instance of Tkinter Frame
# win = Tk()
#
# # Set the geometry of Tkinter Frame
# win.geometry("700x450")
#
# # Open the Image File
# bg = ImageTk.PhotoImage(file="./library.jpg")
#
# # Create a Canvas
# canvas = Canvas(win, width=700, height=3500)
# canvas.pack(fill=BOTH, expand=True)
#
# # Add Image inside the Canvas
# canvas.create_image(0, 0, image=bg, anchor='nw')
#
# # Function to resize the window
# def resize_image(e):
#    global image, resized, image2
#    # open image to resize it
#    image = Image.open("tutorialspoint.png")
#    # resize the image with width and height of root
#    resized = image.resize((e.width, e.height), Image.ANTIALIAS)
#
#    image2 = ImageTk.PhotoImage(resized)
#    canvas.create_image(0, 0, image=image2, anchor='nw')
#
# # Bind the function to configure the parent window
# win.bind("<Configure>", resize_image)
# win.mainloop()
