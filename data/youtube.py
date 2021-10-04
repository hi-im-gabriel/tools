from tkinter import *
from tkinter import filedialog,messagebox,Checkbutton,Pack,Tk,ttk
from PIL import Image, ImageTk
from pytube import YouTube
from os import getcwd

def wid():
    color = "#404040"
    version = "YouTube Downloader"

    root_yt = Toplevel()
    root_yt.title(version)
    root_yt.resizable(False,False)

    root_yt.geometry("600x150")
    root_yt.config(bg=color)

    stringURL = StringVar()
    stringDirectory = StringVar()
    stringCheckmp4 = StringVar()
    stringCheckmp4.set('0')
    stringCheckmp3 = StringVar()
    stringCheckmp3.set('0')
    url = str()
    
    def save_file():
        global path
        path = filedialog.askdirectory()
        stringDirectory.set(path)
    def down():
        if stringCheckmp4.get()=='1':down_mp4()
        elif stringCheckmp3.get()=='1':down_mp3()
        else:messagebox.showinfo(version,"Choose an option first, mp3 or mp4.")
        progressbar.place_forget()
        progressbar.update()
    def show_progress(stream=None, chunk=None, bytes_remaining=None):
        progressbar.place(x=149,y=118)
        total_size = stream.filesize
        percent_count = float("%.2f" % (100 - ( 100 * (bytes_remaining/total_size))))
        progressbar.config(value=percent_count)
        progressbar.update()
    def down_mp4():
        global url
        try:
            url = stringURL.get()   
            youtube = YouTube(url,on_progress_callback=show_progress)
            video = youtube.streams.filter(progressive=True,file_extension="mp4").get_highest_resolution()
            try:
                video.download(path, youtube.title)
                try:
                    msg =f"Title: {youtube.title}\n\nChannel: {youtube.author}\n\nSucess\n{path}"
                except:
                    msg="Unknown error"
            except:
                msg="Invalid directory!"
        except:
            msg="Invalid URL!"
        messagebox.showinfo(version,msg)
        progressbar.config(value=0.0)
        progressbar.update()   
    def down_mp3():
        global url
        try:
            url = stringURL.get()   
            youtube = YouTube(url,on_progress_callback=show_progress)   
            audio = youtube.streams.get_audio_only()
            try:
                audio.download(path, youtube.title+".mp3")
                try:
                    msg =f"Title: {youtube.title}\n\nChannel: {youtube.author}\n\nSucess\n{path}"
                except:
                    msg="Unknown error"
            except:
                msg="Invalid directory!"
        except:
            msg="Invalid URL!"
        messagebox.showinfo(version,msg)
        progressbar.config(value=0.0)
        progressbar.update()

    def close_yt():
        root_yt.quit()
        root_yt.destroy()

    class EntryWithPlaceholder(Entry):
        def __init__(self, *args, **kwargs):
            self.placeholder = kwargs.pop("placeholder", "")
            super().__init__(*args, **kwargs)

            self.insert("end", self.placeholder)
            self.bind("<FocusIn>", self.remove_placeholder)
            self.bind("<FocusOut>", self.add_placeholder)

        def remove_placeholder(self, event):
            if self.get() == self.placeholder:
                self.delete(0, "end")
                self.config(fg='black')
        def add_placeholder(self,event):
            if self.placeholder and self.get() == "":
                self.insert(0, self.placeholder)
                self.config(fg='grey')
 
    img_yt = ImageTk.PhotoImage(Image.open(getcwd()+"/data/icons/YouTube.ico"))
    img_folder = ImageTk.PhotoImage(Image.open(getcwd()+"/data/icons/folder.png").resize((30,30),Image.ANTIALIAS))
    img_down = ImageTk.PhotoImage(Image.open(getcwd()+"/data/icons/down.png").resize((int(40*3.39),45),Image.ANTIALIAS))

    label_img_yt = Label(root_yt, image=img_yt, bg=color).pack(anchor=NW)

    entry_url = EntryWithPlaceholder(root_yt, textvariable=stringURL, width=53,fg='grey',placeholder="Enter url, ex: https://www.youtube.com/watch?v=PVjiKRfKpPI")
    entry_url.place(x=150, y=10)

    entry_direct = Entry(root_yt, textvariable=stringDirectory, width=49,state=DISABLED)
    entry_direct.place(x=150, y=40)

    button_save = Button(root_yt, command=save_file,border=0,image=img_folder,bg=color,borderwidth=0,highlightthickness=0,activebackground=color)
    button_save.place(x=550, y=36)
    button_down = Button(root_yt, command=down,border=0,image=img_down,bg=color,borderwidth=0,highlightthickness=0,activebackground=color)
    button_down.place(x=390, y=64)

    check_mp4 = Checkbutton(root_yt, text="Video (.mp4)",fg='white',selectcolor='black',command=lambda: check_mp3.deselect(),bg=color,highlightthickness=0,activebackground=color,activeforeground='white',variable=stringCheckmp4)
    check_mp4.place(x=142,y=68)

    check_mp3 = Checkbutton(root_yt, text="Music (.mp3)",fg='white',selectcolor='black',command=lambda: check_mp4.deselect(),bg=color,highlightthickness=0,activebackground=color,activeforeground='white',variable=stringCheckmp3)
    check_mp3.place(x=261,y=68)

    progressbar = ttk.Progressbar(root_yt,orient="horizontal",length=430, mode='determinate',maximum=100.0)

    root_yt.protocol("WM_DELETE_WINDOW",lambda: close_yt())
    root_yt.mainloop()