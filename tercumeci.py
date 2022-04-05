from tkinter import*
from tkinter import ttk,messagebox
import googletrans
import textblob


root=Tk()
root.title("Tərcüməçi")
root.geometry("900x350+300+100")
root.configure(bg="#7E7E7E")
title=Label(root,
    text="Tərcüməçi",
    bg='#074463',
    bd=12,
    fg="white",
    relief=GROOVE,
    font=("times new roman",30,"bold")
    ,pady=2).pack(fill=X)

def translate_it():
    translate_text.delete(1.0,END)
    try:
        for key, value in languages.items():
            if (value==orginal_combo.get()):
                from_language_key=key
       
        for key, value in languages.items():
            if (value==translated_combo.get()):
                to_language_key=key

        words=textblob.TextBlob(orginal_text.get(1.0,END)) 
        words=words.translate(from_lang=from_language_key,to=to_language_key) 
     
        translate_text.insert(1.0,words)
    except Exception as e:
        messagebox.showerror("Tranlator","Düzgün Daxil Edin")

def temizle():
    orginal_text.delete(1.0,END)
    translate_text.delete(1.0,END)
    orginal_combo.set("Dil seçin")
    translated_combo.set("Dil seçin")

def deyismek():
    o=orginal_combo.get()
    t=translated_combo.get()

    orginal_combo.set(t)
    translated_combo.set(o)
    

languages=googletrans.LANGUAGES
language_list=list(languages.values())

orginal_combo=ttk.Combobox(root,font=("Helvetica 17 bold"),value=language_list)
orginal_combo.current(21)
orginal_combo.set("azerbaijani")
orginal_combo.place(x=10,y=90,relheight=0.11,relwidth=0.35)

orginal_text=Text(root,font="Helvetica 12 bold",height=10,width=35,bg="#2E86C1")
orginal_text.place(x=10,y=140)

translated_combo=ttk.Combobox(root,font=("arial 17 bold"),value=language_list)
translated_combo.current(21)
translated_combo.set("english")
translated_combo.place(x=570,y=90,relheight=0.11,relwidth=0.35)

translate_text=Text(root,font="arial 12 bold",height=10,width=35,bg="#CD6155")
translate_text.place(x=570,y=140)

#-----------------------------------------BUtton---------------------------------------------------

deyis_b=Button(root,text="Dili dəyişdirin",font=("Helvetica",14),command=deyismek)
deyis_b.place(x=390,y=80)

translate_b=Button(root,text="Tərcümə et",font=("Helvetica",18),command=translate_it)
translate_b.place(x=380,y=140)

temizle_b=Button(root,text="   Təmizlə   ",font=("Helvetica",18),command=temizle)
temizle_b.place(x=380,y=200)

cix_b=Button(root,text="   Çıxmaq   ",font=("Helvetica",18),command=root.quit)
cix_b.place(x=380,y=260)

root.mainloop()