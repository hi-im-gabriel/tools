from tkinter import *
from tkinter import messagebox,Checkbutton,Pack,Tk,ttk
from tkinter.font import BOLD
from PIL import Image, ImageTk
from requests import get
from os import getcwd

def wid():
    color = "#404040"
    version = "Phone Specs"

    root_ph = Toplevel()
    root_ph.title(version)
    root_ph.resizable(False,False)

    root_ph.geometry("650x600")
    root_ph.config(bg=color)

    def search():
        global ph_links
        ph_models=[]
        ph_links=[]
        set_def_img()
        text_ph.config(state=NORMAL)
        text_ph.delete('1.0',END)
        text_ph.config(state=DISABLED)
        text_specs.config(state=NORMAL)
        text_specs.delete('1.0',END)
        text_specs.config(state=DISABLED)
        model=entry_ph.get()
        entry_ph.delete(0,END)
        entry_ph.config(state=DISABLED)
        entry_ph.update()
        combo_ph.set('')
        combo_ph.place_forget()
        combo_ph.update()
        button_specs.place_forget()
        button_specs.update()
        if model=="Enter a model, ex: iPhone 13" or len(model)<=5:entry_ph.config(state=NORMAL);entry_ph.update();entry_ph.focus();messagebox.showerror(version,"Enter at least 6 characters!");return
        try:s=get("https://phone-specs-api.azharimm.dev/search?query="+model).json()
        except:entry_ph.config(state=NORMAL);entry_ph.update();entry_ph.focus();messagebox.showerror(version,"API Error, try again later.");return
        s=s['data']['phones']
        if not bool(s):entry_ph.config(state=NORMAL);entry_ph.update();entry_ph.focus();messagebox.showerror(version,f"0 models found named\n'{model}'");return
        for i in s:ph_models.append(i.get('brand')+": "+i.get('phone_name'));ph_links.append(i.get('detail'))
        combo_ph.config(values=ph_models)
        entry_ph.config(state=NORMAL)
        entry_ph.update()
        combo_ph.place(x=165,y=50)
        combo_ph.update()
        button_specs.place(x=470,y=47)
        button_specs.update()
        entry_ph.focus()


    def specs():
        global ph_links
        index=combo_ph.current()
        if index==-1:messagebox.showerror(version,"Select a model!");return
        try:s=get(ph_links[index]).json()
        except:messagebox.showerror(version,"API Error, try again later.");return
        s=s['data']
        brand,phone_name,thumb,release,dimension,os,storage=s['brand'],s['phone_name'],s['thumbnail'],s['release_date'],s['dimension'],s['os'],s['storage']
        s=s['specifications']
        if len(s)==14:s.pop()

        network,launch,body,display,platform,memory,main_cam,selfie_cam,sound,comms,features,battery,misc=[dict() for _ in range(13)]

        temp=s[0]['specs'];s.pop(0)
        for p in temp:
            for i,j in p.items():
                if i=='val':network[p.get('key')]=j[0].replace('\n',' ,')

        temp=s[0]['specs'];s.pop(0)
        for p in temp:
            for i,j in p.items():
                if i=='val':launch[p.get('key')]=j[0].replace('\n',' ,')

        temp=s[0]['specs'];s.pop(0)
        for p in temp:
            for i,j in p.items():
                if i=='val':body[p.get('key')]=j[0].replace('\n',' ,')

        temp=s[0]['specs'];s.pop(0)
        for p in temp:
            for i,j in p.items():
                if i=='val':display[p.get('key')]=j[0].replace('\n',' ,')

        temp=s[0]['specs'];s.pop(0)
        for p in temp:
            for i,j in p.items():
                if i=='val':platform[p.get('key')]=j[0].replace('\n',' ,')

        temp=s[0]['specs'];s.pop(0)
        for p in temp:
            for i,j in p.items():
                if i=='val':memory[p.get('key')]=j[0].replace('\n',' ,')

        temp=s[0]['specs'];s.pop(0)
        for p in temp:
            for i,j in p.items():
                if i=='val':main_cam[p.get('key')]=j[0].replace('\n',' ,')
        if len(s)==6:
            temp=s[0]['specs'];s.pop(0)
            for p in temp:
                for i,j in p.items():
                    if i=='val':selfie_cam[p.get('key')]=j[0].replace('\n',' ,')
        else:selfie_cam=main_cam

        temp=s[0]['specs'];s.pop(0)
        for p in temp:
            for i,j in p.items():
                if i=='val':sound[p.get('key')]=j[0].replace('\n',' ,')

        temp=s[0]['specs'];s.pop(0)
        for p in temp:
            for i,j in p.items():
                if i=='val':comms[p.get('key')]=j[0].replace('\n',' ,')

        temp=s[0]['specs'];s.pop(0)
        for p in temp:
            for i,j in p.items():
                if i=='val':features[p.get('key')]=j[0].replace('\n',' ,')

        temp=s[0]['specs'];s.pop(0)
        for p in temp:
            for i,j in p.items():
                if i=='val':battery[p.get('key')]=j[0].replace('\n',' ,')

        temp=s[0]['specs'];s.pop(0)
        for p in temp:
            for i,j in p.items():
                if i=='val':misc[p.get('key')]=j[0].replace('\n',' ,')

        h = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.9" }
        try:
            r=get(thumb,headers=h).content
            with open(getcwd()+"/data/icons/img.png",'wb') as f:
                f.write(r)
        except:messagebox.showerror(version,"Failed to load phone thumbnail.")
        msg=f"{brand} {phone_name}\n\nRelease date: {release}\nDimensions: {dimension}\nSystem: {os}\nStorage: {storage}"
        text_ph.config(state=NORMAL)
        text_ph.delete('1.0',END)

        text_specs.config(state=NORMAL)
        text_specs.delete('1.0',END)

        text_ph.insert('1.0',msg)
        text_ph.tag_add('name','1.0','1.50')
        text_ph.tag_config('name',foreground='#66b2ff',font=BOLD)
        text_ph.tag_add('rele','3.0','3.13')
        text_ph.tag_config('rele',foreground='#66b2ff')
        text_ph.tag_add('dime','4.0','4.11')
        text_ph.tag_config('dime',foreground='#66b2ff')
        text_ph.tag_add('syst','5.0','5.7')
        text_ph.tag_config('syst',foreground='#66b2ff')
        text_ph.tag_add('stor','6.0','6.9')
        text_ph.tag_config('stor',foreground='#66b2ff')
        vect=[network,launch,body,display,platform,memory,main_cam,selfie_cam,sound,comms,features,battery,misc]
        titles=['NETWORK','LAUNCH','BODY','DISPLAY','PLATFORM','MEMORY','MAIN CAMERA','SELFIE CAMERA','SOUND','COMMS','FEATURES','BATTERY','MISC']
        msg=""
        temp1=0
        temp4=0
        dtags_specs=dict()
        for helloworld in vect:
            temp1+=1
            msg+=f"{titles[temp4]}\n"
            temp3=str(str(temp1)+'.'+str(0))
            temp2=str(str(temp1)+'.'+str(len(titles[temp4])))
            dtags_specs[temp3]=[temp2,'bugfix']
            temp4+=1
            temp1+=1
            for i,j in helloworld.items():
                msg+=f"{i}: {j}\n"
                temp3=str(str(temp1)+'.'+str(0))
                temp2=str(str(temp1)+'.'+str(len(i)+1))
                dtags_specs[temp3]=temp2
                temp1+=1
            msg+="\n"
        
        text_specs.insert('1.0',msg)
        try:
            for tag in text_specs.tag_names():text_specs.tag_delete(tag)
        except:pass
        for i,j in dtags_specs.items():
            try:
                text_specs.tag_add(i,i,j)
                text_specs.tag_config(i,foreground="#66b2ff",justify=LEFT)
            except:
                text_specs.tag_add(i,i,j[0])
                text_specs.tag_config(i,foreground="#66b2ff",justify=CENTER,font=BOLD)

        text_ph.config(state=DISABLED)
        text_specs.config(state=DISABLED)
        set_new_img()


    def set_new_img():
        try:
            temp_img=ImageTk.PhotoImage(Image.open(getcwd()+"/data/icons/img.png"))
            label_img_ph.image=temp_img
            label_img_ph.config(image=temp_img)
        except:messagebox.showerror(version,"Couldn't load model image.")
  
  
    def set_def_img():
        temp_img=ImageTk.PhotoImage(Image.open(getcwd()+"/data/icons/specs.png").resize((160,160),Image.ANTIALIAS))
        label_img_ph.image=temp_img
        label_img_ph.config(image=temp_img) 


    def close_ph():
        root_ph.quit()
        root_ph.destroy()


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


    img_ph = ImageTk.PhotoImage(Image.open(getcwd()+"/data/icons/specs.png").resize((160,160),Image.ANTIALIAS))
    label_img_ph = Label(root_ph, image=img_ph, bg=color)
    label_img_ph.pack(anchor=NW)

    entry_ph = EntryWithPlaceholder(root_ph, width=31,fg='grey',placeholder="Enter a model, ex: iPhone 13")
    entry_ph.place(x=165,y=20)
    entry_ph.focus()

    button_ph = Button(root_ph, command=search,text="Search",border=0,borderwidth=0,highlightthickness=0)
    button_ph.place(x=470,y=17)

    combo_ph = ttk.Combobox(root_ph,width=29,state='readonly')
    combo_ph.bind("<<ComboboxSelected>>",lambda e: combo_ph.selection_clear())

    button_specs = Button(root_ph,command=specs,text="Get info",border=0,borderwidth=0,highlightthickness=0)

    text_ph = Text(root_ph,width=58,height=8,state=DISABLED,background=color,fg='white')
    text_ph.place(x=165,y=80)

    text_specs = Text(root_ph,width=79,height=21,state=DISABLED,background=color,fg='white')
    text_specs.place(x=5,y=230)

    root_ph.protocol("WM_DELETE_WINDOW",lambda: close_ph())
    root_ph.mainloop()
