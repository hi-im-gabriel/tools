from tkinter import *
from tkinter import Checkbutton,Pack,Tk
import requests
from PIL import Image, ImageTk
from os import getcwd

def wid():
    color = "#404040"
    version = "IP Lookup"

    root_ip = Toplevel()
    root_ip.title(version)
    root_ip.resizable(False, False)

    root_ip.geometry("400x530")
    root_ip.config(bg=color)

    def search_ip():
        label_ip.config(state=DISABLED)
        final_ip.config(state=NORMAL)
        try:
            final_ip.delete('1.0',END)
        except:
            pass
        try:
            api=requests.get('http://ipwhois.app/json/'+label_ip.get()).json()
        except:
            msg="Invalid IP!"
        try:
            msg=f"IP: {api['ip']}\n\nTYPE: {api['type']}\nCONTINENT: {api['continent']}\nCODE: {api['continent_code']}\nCOUNTRY: {api['country']}\nCAPITAL: {api['country_capital']}\nCOUNTRY PHONE CODE: {api['country_phone']}\nREGION: {api['region']}\nCITY: {api['city']}\nLAT: {api['latitude']}\nLONG: {api['longitude']}\nORG: {api['org']}\nISP: {api['isp']}\nTIMEZONE: {api['timezone']}\nTIMEZONE NAME: {api['timezone_name']}\nGMT: {api['timezone_gmt']}\nCURR.: {api['currency']}\nCODE: {api['currency_code']}"
        except:
            msg="Invalid IP!"
        final_ip.insert('1.0',msg)
        
        label_ip.config(state=NORMAL)
        if len(msg)==11:final_ip.config(fg='red',state=DISABLED)
        else:
            final_ip.config(fg='black',state=DISABLED)
            final_ip.tag_add('ip','1.0','1.2')
            final_ip.tag_configure('ip',foreground='blue')
            final_ip.tag_add('type','3.0','3.4')
            final_ip.tag_configure('type',foreground='blue')
            final_ip.tag_add('continent','4.0','4.9')
            final_ip.tag_configure('continent',foreground='blue')
            final_ip.tag_add('continent_code','5.0','5.4')
            final_ip.tag_configure('continent_code',foreground='blue')
            final_ip.tag_add('country','6.0','6.7')
            final_ip.tag_configure('country',foreground='blue')
            final_ip.tag_add('capital','7.0','7.7')
            final_ip.tag_configure('capital',foreground='blue')
            final_ip.tag_add('pcode','8.0','8.18')
            final_ip.tag_configure('pcode',foreground='blue')
            final_ip.tag_add('region','9.0','9.6')
            final_ip.tag_configure('region',foreground='blue')
            final_ip.tag_add('city','10.0','10.4')
            final_ip.tag_configure('city',foreground='blue')
            final_ip.tag_add('lat','11.0','11.3')
            final_ip.tag_configure('lat',foreground='blue')
            final_ip.tag_add('long','12.0','12.4')
            final_ip.tag_configure('long',foreground='blue')
            final_ip.tag_add('org','13.0','13.3')
            final_ip.tag_configure('org',foreground='blue')
            final_ip.tag_add('isp','14.0','14.3')
            final_ip.tag_configure('isp',foreground='blue')
            final_ip.tag_add('tz','15.0','15.8')
            final_ip.tag_configure('tz',foreground='blue')
            final_ip.tag_add('tzn','16.0','16.13')
            final_ip.tag_configure('tzn',foreground='blue')
            final_ip.tag_add('gmt','17.0','17.3')
            final_ip.tag_configure('gmt',foreground='blue')
            final_ip.tag_add('curr','18.0','18.4')
            final_ip.tag_configure('curr',foreground='blue')
            final_ip.tag_add('currcode','19.0','19.4')
            final_ip.tag_configure('currcode',foreground='blue')
        label_ip.focus()

    def close_ip():
        root_ip.quit()
        root_ip.destroy()


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


    img_ip = ImageTk.PhotoImage(Image.open(getcwd()+"/data/icons/ip.ico"))
    label_img_ip = Label(root_ip, image=img_ip, bg=color)
    label_img_ip.place(x=0,y=0)

    label_ip = EntryWithPlaceholder(root_ip, width=15,fg='grey',placeholder="142.250.219.132")
    label_ip.place(x=145, y=100)
    label_ip.focus()

    button_ip = Button(root_ip, text="Search", width=5, command=search_ip,highlightthickness=0,border=0)
    button_ip.place(x=295, y=96)

    final_ip = Text(root_ip, width=43,height=20,state=DISABLED)
    final_ip.place(x=25,y=160)

    root_ip.protocol("WM_DELETE_WINDOW",lambda: close_ip())
    root_ip.mainloop()