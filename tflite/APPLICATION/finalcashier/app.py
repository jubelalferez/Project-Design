from tkinter import *
import tkinter.messagebox
from tkinter import Tk
from db import Database
import os
from db import *
import functools

#db.reset_all()


# **** Functions ****

def custorder():
    populate_list()
    populate_totalp()
    populate_totalw()

def purorder():
    db.reset_all()
    populate_list()
    populate_totalp()
    populate_totalw()

def populate_list():
    parts_list.delete(0, END)
    for row in db.fetch():
            parts_list.insert(END, row)

def populate_totalp():
    displaytotalp.delete(0, END)
    for roww in db.display_price():
            displaytotalp.insert(END, roww)

def populate_totalw():
    displaytotalw.delete(0, END)
    for rowww in db.display_weight():
            displaytotalw.insert(END, rowww)

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
root.title('JSJ Marketing by Group 10 - CASHIER')

# **** Calling an image from the project file ****
# **** The simplest form, using PhotoImage() class ****
# **** You can only do this if you copy a file then paste it inside the project ****
logoPhoto = PhotoImage(file="ui/logoz.png")
logophotolabel = Label(root, image=logoPhoto)
logophotolabel.place(x=15, y=15, anchor=NW)

# **** Picture button. ADD TO CART. DELETE ITEM. PRINT ALL ITEM ****
photoadd = PhotoImage(file="ui/addsz.png")
button_1 = Button(root, image=photoadd, relief="raised", bd="3", command=custorder)
button_1.bind("<Button-1>", custorder)
button_1.place(x=50, y=550)

newcust_text = StringVar()
newcustlabel = Label(root, text='NEW CUSTOMER', font = ('Roboto',13))
newcustlabel.place(x=50, y=525)

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

# Parts List (Listbox)
parts_list = Listbox(root, relief="raised", height=5, width=20, border=0, font = ('Roboto',30))
parts_list.grid(padx=40, pady=138, columnspan=3, rowspan=6)  #columnspan=3, rowspan=6, pady=10, padx=20)
parts_list.bind('<<ListboxSelect>>', select_item)

# Parts List (Listbox)
displaytotalp = Listbox(root, relief="raised", height=1, width=10, border=0, font = ('Roboto',14))
displaytotalp.place(x=280, y=420)
displaytotalp.bind('<<ListboxSelect>>', select_item)

totalprice = StringVar()
totalpricelabel = Label(root, text='Total Price(₱)', font = ('Roboto',13))
totalpricelabel.place(x=135, y=420)
totalprice_entry = Entry(root, textvariable=totalprice)

# Parts List (Listbox)
displaytotalw = Listbox(root, relief="raised", height=1, width=10, border=0, font = ('Roboto',14))
displaytotalw.place(x=280, y=440)
displaytotalw.bind('<<ListboxSelect>>', select_item)

totalweight = StringVar()
totalweightlabel = Label(root, text='Total Weight(g)', font = ('Roboto',13))
totalweightlabel.place(x=135, y=440)
totalweight_entry = Entry(root, textvariable=totalweight)

# Create scrollbar
scrollbar = Scrollbar(root, width=20, border=0)
scrollbar.place(x=509, y=280, anchor=W)

# Set scroll to listbox
parts_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=parts_list.yview)
# Bind select
parts_list.bind('<<ListboxSelect>>', select_item)

# Instanciate database object
db = Database(r'\\raspberrypi\share\jsj.db') 

root.geometry('560x680+600+3')
root.mainloop()