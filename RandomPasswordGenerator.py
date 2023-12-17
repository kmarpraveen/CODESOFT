from tkinter import *
import random
obj=Tk()
obj.config(bg='seashell3')
obj.geometry("342x275")
password_str=StringVar()
password_len=IntVar()
password_len.set(0)
def to_generate():
    characters=['a','b','c','d','e','f','g','h','i','j','k','l',
                'm','n','o','p','q','r','s','t','u','v','w','x',
                'y','z','A','B','C','D','E','F','G','H','I','J',
                'K','L','M','N','O','P','Q','R','S','T','U','V',
                'W','X','Y','Z','1','2','3','4','5','6','7','8',
                '9','0',' ','!','@','#','$','%','&','*','^','(',')']
    pword=""
    for i in range(password_len.get()):
        pword=pword+random.choice(characters)
    password_str.set(pword)
p_label=Label(obj, text="PASSWORD GENERATOR", font=('times new roman',20,'bold'),bg='PeachPuff4')
p_label.grid()
p_length=Label(obj, text='Enter Password Length', font=('calibri',18,'bold'),bg='ivory4')
p_length.grid(pady=4)
entry_length=Entry(obj, textvariable=password_len,width=5,font=('calibri',13,'bold'))
entry_length.grid(pady=4)
g_button=Button(obj, text='Generate password',command=to_generate, font=('calibri',18,'bold'), bg='ivory4')
g_button.grid(pady=6)
entry_output=Entry(obj, textvariable=password_str,font=('calibri',13,'bold'))
entry_output.grid(pady=4)
obj.mainloop()

