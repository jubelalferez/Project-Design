from tkinter import *
import tkinter.messagebox
from tkinter import Tk
from db import Database
import os
from db import *
import functools

#db.reset_all()

# Instanciate database object
db = Database(r'\\raspberrypi\share\jsj.db')


# **** Functions ****

def populate_list():
    parts_list.delete(0, END)
    for row in db.fetch():
            parts_list.insert(END, row)

def select_item(event):
    try:
        global selected_item
        index = parts_list.curselection()[0]
        selected_item = parts_list.get(index)
        print(selected_item)

        item_entry.delete(0, END)
        quantity_entry.delete(0, END)
        price_entry.delete(0, END)
        weight_entry.delete(0, END)
    except IndexError:
        pass

#Main Window
root = Tk()
root.title('JSJ Marketing by Group 10 INVENTORY')

#Logo
logoPhoto = PhotoImage(file="ui/logoz.png")
logophotolabel = Label(root, image=logoPhoto)
logophotolabel.place(x=15, y=15, anchor=NW)

# **** Picture button. ADD TO CART. DELETE ITEM. PRINT ALL ITEM ****
photoref = PhotoImage(file="ui/refresh.png")
button_1 = Button(root, image=photoref, relief="raised", bd="3", command=populate_list)
button_1.bind("<Button-1>", populate_list)
button_1.place(x=240, y=550)

refreshlabel = Label(root, text='REFRESH INVENTORY', font = ('Roboto',14))
refreshlabel.place(x=200, y=515)

"""TEXTS"""
item_text = StringVar()
itemlabel = Label(root, text='ITEM')
itemlabel.place(x=120, y=120)
item_entry = Entry(root, textvariable=item_text)

quantity_text = StringVar()
quantitylabel = Label(root, text='QTY')
quantitylabel.place(x=200, y=120)
quantity_entry = Entry(root, textvariable=quantity_text)

price_text = StringVar()
pricelabel = Label(root, text='PRICE(₱)')
pricelabel.place(x=230, y=120)
price_entry = Entry(root, textvariable=price_text)

weight_text = StringVar()
weightlabel = Label(root, text='WEIGHT(g)')
weightlabel.place(x=310, y=120)
weight_entry = Entry(root, textvariable=weight_text)

#Parts List (Listbox)
parts_list = Listbox(root, relief="raised", height=5, width=20, border=0, font = ('Roboto',30))
parts_list.grid(padx=40, pady=138, columnspan=3, rowspan=6)  #columnspan=3, rowspan=6, pady=10, padx=20)
parts_list.bind('<<ListboxSelect>>', select_item)

# Create scrollbar
scrollbar = Scrollbar(root, width=20, border=0)
scrollbar.place(x=509, y=280, anchor=W)

# Set scroll to listbox
parts_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=parts_list.yview)
# Bind select
parts_list.bind('<<ListboxSelect>>', select_item)

populate_list()

root.geometry('560x680+600+3') #Window size
root.mainloop()