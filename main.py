from tkinter import *
from tkinter import messagebox,Checkbutton,Pack,Tk
from tkinter.font import BOLD
from PIL import Image, ImageTk
from data import ip,youtube
from os import getcwd

color = "#E0E0E0"#"#404040"
version = "Tools v0.3"

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

img_tools = ImageTk.PhotoImage(Image.open(getcwd()+"/data/icons/tools.png").resize((200,200),Image.ANTIALIAS))
label_tools= Label(root,image=img_tools,bg=color)
label_tools.place(x=50,y=-60)

img_yt_btn = ImageTk.PhotoImage(Image.open(getcwd()+"/data/icons/yt_btn.png").resize((int(6.95*30),30),Image.ANTIALIAS))
botao_yt = Button(root, command=op_yt,image=img_yt_btn,border=0,bg=color,activebackground=color,highlightthickness=0)
botao_yt.place(x=5,y=70)

img_ip_btn = ImageTk.PhotoImage(Image.open(getcwd()+"/data/icons/ip_btn.png").resize((int(3.75*30),30),Image.ANTIALIAS))
botao_ip = Button(root, command=op_ip,image=img_ip_btn,border=0,bg=color,activebackground=color,highlightthickness=0)
botao_ip.place(x=5,y=105)

root.mainloop()