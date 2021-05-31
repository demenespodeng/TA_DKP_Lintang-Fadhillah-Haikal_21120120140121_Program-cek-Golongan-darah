from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from check import goldar
from tkinter.messagebox import showinfo
orang1 = goldar("","","","","","")

def submit():
    orang1.setantiA(stringSA.get())
    orang1.setantiB(stringSB.get())
    orang1.setantiAB(stringSAB.get())
    orang1.setantiD(stringSD.get())
    nama=stringnama.get()
    umur=stringumur.get()
    jk=stringjk.get()
    orang1.findgoldar()
    orang1.findrh()
    darah = orang1.getdarah()
    rhesus = orang1.getrhesus()
    print(nama)
    print(umur)
    print(jk)
    print(darah,rhesus)

    lbkartu = Label(window, text = "KARTU GOLONGAN DARAH", bg="#F08080").place(x=120,y=300)
    lbnama2 = Label(window, text = "Nama\t\t: " + nama,bg="#F08080").place(x = 30,y = 350) 
    lbumur2 = Label(window, text = "Umur\t\t: " + umur,bg="#F08080").place(x = 30,y = 380)   
    lbjk2 = Label(window, text = "Jenis Kelamin\t: " + jk,bg="#F08080").place(x = 30,y = 410)
    lbgoldar = Label(window, text = "Golongan Darah\t: " + darah,bg="#F08080").place(x = 30,y = 440)  
    lbrh = Label(window, text = "Rhesus\t\t: " + rhesus,bg="#F08080").place(x = 30,y = 470)        

window = Tk()  
window.geometry("400x600")
window.configure(bg="#FF69B4")
window.title("CEK GOLONGAN DARAH ANDA")

lbjudul = Label(window, text = "ISI IDENTITAS DAN HASIL KARTU CEK DARAH", bg="#F08080")

lbnama = Label(window, text = "Nama\t:",bg="#F08080").place(x = 30,y = 40)   
lbumur = Label(window, text = "Umur\t:",bg="#F08080").place(x = 30,y = 70)    
lbjk = Label(text = "Jenis Kelamin\t:",bg="#F08080").place(x = 30, y=100)
lbserumA = Label(text = "Serum Anti-A\t:",bg="#F08080").place(x=30, y=130)
lbserumB = Label(text = "Serum Anti-B\t:",bg="#F08080").place(x=30, y=160)
lbserumAB = Label(text = "Serum Anti-AB\t:",bg="#F08080").place(x=30, y=190)
lbserumD = Label(text = "Serum Anti-D\t:", bg="#F08080").place(x=30, y=220)

lbjudul.pack()

stringnama = StringVar()
stringumur = StringVar()
stringjk = StringVar()
stringSA = StringVar(value='Menggumpal')
stringSB = StringVar(value='Menggumpal')
stringSAB = StringVar(value='Menggumpal')
stringSD = StringVar(value='Menggumpal')

inama = Entry(window,width = 20, textvariable=stringnama, ).place(x = 150, y = 40)  
iumur = Entry(window, width= 20, textvariable=stringumur, ).place(x = 150, y = 70)
ijk = Entry(window, width = 20, textvariable=stringjk, ).place(x = 150, y = 100)

kondisi = ("Menggumpal", "Tidak Menggumpal")

CbA = ttk.Combobox(window,width=20, textvariable=stringSA,state="readonly")
CbA.place(x=150, y = 130)
CbA['values']=kondisi
CbB = ttk.Combobox(window,width=20, textvariable=stringSB,state="readonly")
CbB.place(x=150, y = 160)
CbB['values']=kondisi
CbAB = ttk.Combobox(window,width=20, textvariable=stringSAB,state="readonly")
CbAB.place(x=150, y = 190)
CbAB['values']=kondisi
CbD = ttk.Combobox(window,width=20, textvariable=stringSD,state="readonly")
CbD.place(x=150, y = 220)
CbD['values']=kondisi

btnsub = Button(window, text="SUBMIT", command = submit).place(x=170,y=270)

window.mainloop()
