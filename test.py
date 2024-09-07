# from tkinter import *
# from tkinter import ttk, messagebox
# from PIL import Image, ImageTk
#
#
# def ReSizeIcon(img, width, height):
# 	resizedIcon = img.resize((width, height), Image.Resampling.LANCZOS)
# 	return ImageTk.PhotoImage(resizedIcon)
#
# class Main(object):
# 	def __init__(self, master):
# 		self.master = master
#
# 		pass
#
#
#
# def main():
# 	root = Tk()
# 	app = Main(root)
# 	root.title('Gorth Library Maganement Application')
# 	root.geometry('1600x1000')
# 	root.iconbitmap('./icons/app.png')
# 	root.iconphoto(True, PhotoImage(file='./icons/app.png'))
# 	root.configure(background="#FF00AA")
#
# 	test = Image.open('./lib.png')
# 	[imageSizeWidth, imageSizeHeight] = test.size
# 	# img = (ReSizeIcon(test, (imageSizeWidth // 2), (imageSizeHeight // 2)))
# 	img = ReSizeIcon(test, 1600, 1000)
# 	label = Label(image=img)
# 	label.pack()
#
# 	root.mainloop()
#
# if __name__ == '__main__':
# 	main()
#
#
from tkinter import *
import tkinter as tk

# root = Tk()
#
# class RoundedButton(tk.Canvas):
#     def __init__(self, parent, width, height, cornerradius, padding, color, bg, command=None):
#         tk.Canvas.__init__(self, parent, borderwidth=0,
#             relief="flat", highlightthickness=0, bg=bg)
#         self.command = command
#
#         if cornerradius > 0.5*width:
#             print("Error: cornerradius is greater than width.")
#             return None
#
#         if cornerradius > 0.5*height:
#             print("Error: cornerradius is greater than height.")
#             return None
#
#         rad = 2*cornerradius
#         def shape():
#             self.create_polygon((padding,height-cornerradius-padding,padding,cornerradius+padding,padding+cornerradius,padding,width-padding-cornerradius,padding,width-padding,cornerradius+padding,width-padding,height-cornerradius-padding,width-padding-cornerradius,height-padding,padding+cornerradius,height-padding), fill=color, outline=color)
#             self.create_arc((padding,padding+rad,padding+rad,padding), start=90, extent=90, fill=color, outline=color)
#             self.create_arc((width-padding-rad,padding,width-padding,padding+rad), start=0, extent=90, fill=color, outline=color)
#             self.create_arc((width-padding,height-rad-padding,width-padding-rad,height-padding), start=270, extent=90, fill=color, outline=color)
#             self.create_arc((padding,height-padding-rad,padding+rad,height-padding), start=180, extent=90, fill=color, outline=color)
#
#
#         id = shape()
#         (x0,y0,x1,y1)  = self.bbox("all")
#         width = (x1-x0)
#         height = (y1-y0)
#         self.configure(width=width, height=height)
#         self.bind("<ButtonPress-1>", self._on_press)
#         self.bind("<ButtonRelease-1>", self._on_release)
#
#     def _on_press(self, event):
#         self.configure(relief="sunken")
#
#     def _on_release(self, event):
#         self.configure(relief="raised")
#         if self.command is not None:
#             self.command()
#
# def test():
#     print("Hello")
#
# canvas = Canvas(root, height=300, width=500)
# canvas.pack()
#
# button = RoundedButton(root, 200, 100, 50, 2, 'red', 'white', command=test)
# button.place(relx=.1, rely=.1)
#
# root.mainloop()

# import customtkinter
# from CTkListbox import *


# def show_value(selected_option):
#     # detailsbox.delete()
#     detailsbox.insert(0, selected_option)
#
#
# root = customtkinter.CTk()
#
# listbox = CTkListbox(root, command=show_value)
# listbox.pack(side='left', expand=True, padx=10, pady=10)
#
# detailsbox = CTkListbox(root)
# detailsbox.pack(side='right', expand=True, padx=10, pady=10)
#
# listbox.insert(0, "Japtor")
# listbox.insert(1, "Option 1")
# listbox.insert(2, "Option 2")
# listbox.insert(3, "Option 3")
# listbox.insert(4, "Option 4")
# listbox.insert(5, "Option 5")
# listbox.insert(6, "Option 6")
# listbox.insert(7, "Option 7")
# listbox.insert("END", "Option 8")
#
# root.mainloop()

# from CTkMessagebox import CTkMessagebox
# import customtkinter


# def show_info():
#     # Default messagebox for showing some information
#     CTkMessagebox(title="Info", message="This is a CTkMessagebox!")


# def show_checkmark():
#     # Show some positive message with the checkmark icon
#     CTkMessagebox(message="CTkMessagebox is successfully installed.",
#                   icon="check", option_1="Thanks")


# def show_error():
#     # Show some error message
#     CTkMessagebox(title="Error", message="Something went wrong!!!", icon="cancel")


# def show_warning():
#     # Show some retry/cancel warnings
#     msg = CTkMessagebox(title="Warning Message!", message="Unable to connect!",
#                         icon="warning", option_1="Cancel", option_2="Retry")

#     if msg.get() == "Retry":
#         show_warning()


# def ask_question():
#     # get yes/no answers
#     msg = CTkMessagebox(title="Exit?", message="Do you want to close the program?",
#                         icon="question", option_1="Cancel", option_2="No", option_3="Yes")
#     response = msg.get()

#     if response == "Yes":
#         app.destroy()
#     else:
#         print("Click 'Yes' to exit!")


# app = customtkinter.CTk()
# app.rowconfigure((0, 1, 2, 3, 4, 5), weight=1)
# app.columnconfigure(0, weight=1)
# app.minsize(200, 250)

# customtkinter.CTkLabel(app, text="CTk Messagebox Examples").grid(padx=20)
# customtkinter.CTkButton(app, text="Check CTkMessagebox", command=show_checkmark).grid(padx=20, pady=10, sticky="news")
# customtkinter.CTkButton(app, text="Show Info", command=show_info).grid(padx=20, pady=10, sticky="news")
# customtkinter.CTkButton(app, text="Show Error", command=show_error).grid(padx=20, pady=10, sticky="news")
# customtkinter.CTkButton(app, text="Show Warning", command=show_warning).grid(padx=20, pady=10, sticky="news")
# customtkinter.CTkButton(app, text="Ask Question", command=ask_question).grid(padx=20, pady=(10, 20), sticky="news")

# app.mainloop()

# from PIL import Image
# import customtkinter
# import os

# IMAGE_WIDTH = desired_width
# IMAGE_HEIGHT = desired_height
# IMAGE_PATH = 'image/image.png'

# your_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(IMAGE_PATH)), size=(IMAGE_WIDTH , IMAGE_HEIGHT))
# label = customtkinter.CTkLabel(master=your_master, image=your_image, text='')
# label.grid(column=0, row=0)

# Import all files from
# tkinter and overwrite
# all the tkinter files
# by tkinter.ttk
# from tkinter import *
# from tkinter.ttk import *

# # creates tkinter window or root window
# root = Tk()
# root.geometry('200x100')

# # function to be called when mouse enters in a frame
# def enter(event):
# 	print('Button-2 pressed at x = % d, y = % d'%(event.x, event.y))

# # function to be called when mouse exits the frame
# def exit_(event):
# 	print('Button-3 pressed at x = % d, y = % d'%(event.x, event.y))

# # frame with fixed geometry
# frame1 = Frame(root, height = 100, width = 200)

# # these lines are showing the
# # working of bind function
# # it is universal widget method
# frame1.bind('<Enter>', enter)
# frame1.bind('<Leave>', exit_)

# frame1.pack()

# mainloop()


# # Import all files from
# # tkinter and overwrite
# # all the tkinter files
# # by tkinter.ttk
# from tkinter import *
# from tkinter.ttk import *

# # creates tkinter window or root window
# root = Tk()
# root.geometry('200x100')

# # function to be called when button-2 of mouse is pressed
# def pressed2(event):
# 	print('Button-2 pressed at x = % d, y = % d'%(event.x, event.y))

# # function to be called when button-3 of mouse is pressed
# def pressed3(event):
# 	print('Button-3 pressed at x = % d, y = % d'%(event.x, event.y))

# ## function to be called when button-1 is double clocked
# def double_click(event):
# 	print('Double clicked at x = % d, y = % d'%(event.x, event.y))

# frame1 = Frame(root, height = 100, width = 200)

# # these lines are binding mouse
# # buttons with the Frame widget
# frame1.bind('<Button-2>', pressed2)
# frame1.bind('<Button-3>', pressed3)
# frame1.bind('<Double 1>', double_click)

# frame1.pack()

# mainloop()

# import customtkinter


# class MyTabView(customtkinter.CTkTabview):
#     def __init__(self, master, **kwargs):
#         super().__init__(master, **kwargs)

#         # create tabs
#         self.add("tab 1")
#         self.add("tab 2")

#         # add widgets on tabs
#         self.label = customtkinter.CTkLabel(master=self.tab("tab 1"))
#         self.label.grid(row=0, column=0, padx=20, pady=10)
        
# 		self.delete('tab 2')


# class App(customtkinter.CTk):
#     def __init__(self):
#         super().__init__()

#         self.tab_view = MyTabView(master=self)
#         self.tab_view.grid(row=0, column=0, padx=20, pady=20)


# app = App()
# app.mainloop()



# range = ((0, 1, 2, 3, 4), (0, 1, 2, 3, 4), (0, 1, 2, 3, 4))
# for index in range:
#     pass index[3]
#     pass
#     pass




str = '1. Borrow\nBookID: Milano\nPersonID: Japtor'

j = str.split('\n')

print(str.split('\n')[1][8:]) # 3 8 10