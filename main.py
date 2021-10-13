from tkinter import *
from tkinter import Checkbutton,Pack,Tk
from tkinter.font import BOLD
from PIL import Image, ImageTk
from data import ip,youtube,specs
from os import getcwd

color = "#E0E0E0"
version = "Tools v1.0"

root = Tk()
root.title(version)
root.resizable(False, False)

root.geometry("300x200")
root.config(bg=color)

def op_ip():
    root.withdraw()
    ip.wid()
    root.deiconify()


def op_yt():
    root.withdraw()
    youtube.wid()
    root.deiconify()


def op_ph():
    root.withdraw()
    specs.wid()
    root.deiconify()


img_tools = ImageTk.PhotoImage(Image.open(getcwd()+"/data/icons/tools.png").resize((200,200),Image.ANTIALIAS))
label_tools= Label(root,image=img_tools,bg=color)
label_tools.place(x=50,y=-60)

img_yt_btn = ImageTk.PhotoImage(Image.open(getcwd()+"/data/icons/yt_btn.png").resize((int(6.95*30),30),Image.ANTIALIAS))
button_yt = Button(root, command=op_yt,image=img_yt_btn,border=0,bg=color,activebackground=color,highlightthickness=0)
button_yt.place(x=5,y=70)

img_ip_btn = ImageTk.PhotoImage(Image.open(getcwd()+"/data/icons/ip_btn.png").resize((int(3.75*30),30),Image.ANTIALIAS))
button_ip = Button(root, command=op_ip,image=img_ip_btn,border=0,bg=color,activebackground=color,highlightthickness=0)
button_ip.place(x=5,y=105)

img_ph_btn = ImageTk.PhotoImage(Image.open(getcwd()+"/data/icons/ph_btn.png").resize((int(5*30),30),Image.ANTIALIAS))
button_ph = Button(root, command=op_ph,image=img_ph_btn,border=0,bg=color,activebackground=color,highlightthickness=0)
button_ph.place(x=5,y=140)

root.mainloop()