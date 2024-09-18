import tkinter
from tkinter import ttk


screen=tkinter.Tk()
screen.title("MyApp")
screen.config(bg="lightblue")
screen.geometry("500x400")

"""tkinter.Label(text="Firstname").pack()
tkinter.Label(text="Lastname").pack()"""


"""tkinter.Label(text="Firstname").place(x=0,y=0)
tkinter.Label(text="Lastname").place(x=0,y=30)"""

tkinter.Label(text="Firstname:",fg='red',bg='lightblue',font='Corbel 15 bold').grid(row=0,column=0,sticky='w')
tkinter.Label(text="Lastname:",fg='red',bg='lightblue',font='Corbel 15 bold').grid(row=1,column=0,sticky='w')

tkinter.Entry().grid(row=0,column=1,sticky='w')
tkinter.Entry().grid(row=1,column=1,sticky='w')

tkinter.Radiobutton(value=0,text="Male",fg='red',bg='lightblue',font='Corbel 15 bold').grid(row=2,column=0,sticky='w')
tkinter.Radiobutton(value=1,text="Female",fg='red',bg='lightblue',font='Corbel 15 bold').grid(row=2,column=1,sticky='w')

tkinter.Checkbutton(text="Python",fg='red',bg='lightblue',font='Corbel 15 bold').grid(row=3,column=0,sticky='w')
tkinter.Checkbutton(text="Java",fg='red',bg='lightblue',font='Corbel 15 bold').grid(row=4,column=0,sticky='w')
tkinter.Checkbutton(text="PHP",fg='red',bg='lightblue',font='Corbel 15 bold').grid(row=5,column=0,sticky='w')
tkinter.Checkbutton(text="Android/iOS",fg='red',bg='lightblue',font='Corbel 15 bold').grid(row=6,column=0,sticky='w')

city=['Rajkot','Baroda','Surat','Gandhinagar','Ahmedabad']

ttk.Combobox(values=city).grid(row=7,column=0,sticky='W')

def btnclick():
    print("Butom clicked!")

tkinter.Button(text="Submit",font='Corbel 15 bold',command=btnclick).place(x=220,y=300)

screen.mainloop()