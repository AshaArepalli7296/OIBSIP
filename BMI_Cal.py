def calculate():

    global meters

    result_entry=Entry(head,width=6,font=('Arial Bold',17),justify=CENTER)
    result_entry.grid(row=5,column=25)

    feet=c1.get()
    inches=c2.get()
    weight=weight_entry.get()
    
    try:
        try:
            if int(feet) in range(0,10) and int(inches) in range(0,12):
                Total_inches=(int(feet)*12)+int(inches)
                meters=(0.0254*Total_inches)

        except ValueError:
            messagebox.showerror('Error','Enter valid Height..!')

        bmi=float(weight)/(meters*meters)
        result_entry.insert(0,round(bmi,2))

        if bmi < 18.5:
            messagebox.showwarning('warning','OOPS!... YOU ARE UNDERWEIGHT')

        elif bmi > 18.5 and bmi < 25:
            messagebox.showinfo('result','GOOD!... YOU ARE IN CORRECT WEIGHT')

        elif bmi > 25:
            messagebox.showwarning('warning','OOPS!... YOU ARE OVERWEIGHT')

        else:
            pass

    except ValueError:
        messagebox.showerror('Error','Enter valid Weight..!')
    
    meters=0 

import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
import random
import string

head=tk.Tk()
head.title("BMI CALCULATER")
head.configure(bg='lightpink')
head.geometry('1000x800')

Label(head,text='BODY MASS INDEX CALCULATOR',font=("Arial bold",25)).grid(row=1,column=23,padx=5,pady=40)

Label(head,text=' Select Height   ',height=2,font=('Arial bold',20)).grid(row=4,column=17,padx=50,pady=35)

Label(head,text='    Feet    ',height=1,font=('Arial bold',17)).grid(row=5,column=17,padx=50,pady=35)

n=StringVar()
c1=ttk.Combobox(head,textvariable=n,font=('Arial bold',17),width=7)
c1['values']=(0,1,2,3,4,5,6,7,8,9)
c1.grid(row=5,column=20,columnspan=2)
c1.current()

Label(head,text='   Inches   ',height=1,font=('Arial bold',17)).grid(row=6,column=17,padx=50,pady=35)

n=StringVar()
c2=ttk.Combobox(head, textvariable=n,font=('Arial bold',17),width=7)
c2['values']=(0,1,2,3,4,5,6,7,8,9,10,11)
c2.grid(row=6,column=20,columnspan=2)
c2.current()

Label(head,text=' Enter your weight ',height=2,font=('Arial bold',20)).grid(row=4,column=23,padx=100,pady=35)
weight_entry=Entry(head,width=7,font=('Arial Bold',20),justify=CENTER)
weight_entry.grid(row=5,column=23)


Button(head,text=" Calculate BMI ",font=("Arial bold",20) ,bg='lightpink',bd='10',command=calculate).grid(row=4, column=25)




head.mainloop()