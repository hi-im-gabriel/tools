#x=list(map(int,input().split()))
#s=sorted(s,key=len,reverse=True)
#f=list(dict.fromkeys(f)) remover repetidos
#s=re.sub(r"[^0-9 ]"," ",s) dxar apenas numeros
#a=set(d).intersection(e)
#import string
#alfa=list(string.ascii_lowercase) lsit do alfa
#d=dict()
#d[key]=s[value]
#d=dict(sorted(d.items(), key=lambda item: item[1]))
from tkinter import *
import tkinter
import requests
root = Tk()
root.title("Consultar IP")
root.geometry("410x440")

frame = Frame(root)
input = Entry(frame, width = 50)
input.pack()
result = ''
text = Text(root, font = ('ariel',20))

def buscaip():
    try:
        text.configure(font=("Times New Roman", 12, "bold"),state='normal')
        text.delete('1.0',tkinter.END)
    except:
        pass
    global result
    result = input.get()
    try:
        api=requests.get('http://ipwhois.app/json/'+result).json()
    except:
        msg="IP Inválido"
    try:
        msg=f'''
IP: {api['ip']}
TIPO: {api['type']}
CONTINENTE: {api['continent']}
CÓDIGO DO CONTINENTE: {api['continent_code']}
PAÍS: {api['country']}
CAPITAL DO PAIS: {api['country_capital']}
CÓDIGO TELEFÕNICO DO PAÍS: {api['country_phone']}
REGIÃO: {api['region']}
CIDADE: {api['city']}
LATITUDE: {api['latitude']}
LONGITUDE: {api['longitude']}
ORG: {api['org']}
ISP: {api['isp']}
HORÁRIO PADRÃO: {api['timezone']}
NOME DO HORÁRIO PADRÃO: {api['timezone_name']}
GMT: {api['timezone_gmt']}
MOEDA: {api['currency']}
CODIGO DA MOEDA: {api['currency_code']}
            '''
    except:
        msg="IP Inválido"
    text.insert('1.0',msg)
    text.configure(font=("Times New Roman", 12, "bold"),state=DISABLED)


button = Button(frame, text = 'CONSULTAR', command = buscaip)                                                 
button.pack(side = RIGHT)
frame.pack(side = TOP)
text.pack()
root.mainloop()