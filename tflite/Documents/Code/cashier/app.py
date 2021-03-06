from tkinter import *
import tkinter.messagebox
from tkinter import Tk
from db import Database
import os
from db import *
import functools


# Instanciate database object
db = Database(r'\\raspberrypi\share\jsj.db') 

# **** Functions ****
def populate_list():
    order_list.delete(0, END)
    for row in db.fetch():
            order_list.insert(END, row)

def populate_order():
    order_list.delete(0, END)
    for row_o in db.getordero(orderid_entry.get(),orderid_entry.get(),orderid_entry.get(),orderid_entry.get()):
            order_list.insert(END, row_o)
    for row_a in db.getordera(orderid_entry.get(),orderid_entry.get(),orderid_entry.get(),orderid_entry.get()):
            order_list.insert(END, row_a)
    for row_b in db.getorderb(orderid_entry.get(),orderid_entry.get(),orderid_entry.get(),orderid_entry.get()):
            order_list.insert(END, row_b)

def populate_ordertp():
    displaytotalp.delete(0, END)
    for row in db.getordertp(orderid_entry.get(),orderid_entry.get(),orderid_entry.get()):
            displaytotalp.insert(END, row)

def populate_ordertw():
    displaytotalw.delete(0, END)
    for row in db.getordertw(orderid_entry.get(),orderid_entry.get(),orderid_entry.get()):
            displaytotalw.insert(END, row)
     
def select_item(event):
    try:
        global selected_item
        index = order_list.curselection()[0]
        selected_item = order_list.get(index)
        print(selected_item)

    except IndexError:
        pass
    
def cashchange():
    cashchange_list.delete(0, END)
    for row in db.getchange(cashtender_entry.get(),orderid_entry.get(),orderid_entry.get(),orderid_entry.get()):
            cashchange_list.insert(END, row)

def searchorder():
    populate_order()
    populate_ordertp()
    populate_ordertw()

def custorder():
    tkinter.messagebox.showinfo('Order', 'Order Purchased')
  

#Main Window
root = Tk()
root.title('JSJ Marketing by Group 10 - CASHIER')

#Logo
logoPhoto = PhotoImage(file="ui/logoz.png")
logophotolabel = Label(root, image=logoPhoto)
logophotolabel.place(x=15, y=15, anchor=NW)

# **** Picture button. ADD TO CART. DELETE ITEM. PRINT ALL ITEM ****
button_1_label = Label(root, text='Purchase', font=('Roboto', 14))
button_1_label.place(x=20, y=510)
photoadd = PhotoImage(file="ui/addsz.png")
button_1 = Button(root, image=photoadd, relief="raised", bd="3", command=custorder)
button_1.bind("<Button-1>")
button_1.place(x=20, y=540)

#newcust_text = StringVar()
#newcustlabel = Label(root, text='NEW CUSTOMER', font = ('Roboto',13))
#newcustlabel.place(x=50, y=525)

"""TEXTS"""

orderid_label = Label(root, text='Order ID: ', font=('Roboto', 14))
orderid_label.grid(row=0, column=0, sticky=W)
orderid_label.place(x=210, y=60)
orderid_entry = Entry(root)
orderid_entry.grid(row=1, column=2)
orderid_entry.place(x=290, y=66)

searchorder_btn = Button(root, text='Search', width=12, command=searchorder)
searchorder_btn.grid(row=2, column=2)
searchorder_btn.place(x=430, y=63)

item_text = StringVar()
itemlabel = Label(root, text='ITEM')
itemlabel.place(x=120, y=120)

quantity_text = StringVar()
quantitylabel = Label(root, text='QTY')
quantitylabel.place(x=200, y=120)

price_text = StringVar()
pricelabel = Label(root, text='PRICE(₱)')
pricelabel.place(x=230, y=120)

weight_text = StringVar()
weightlabel = Label(root, text='WEIGHT(g)')
weightlabel.place(x=310, y=120)

#Item List (Listbox)
order_list = Listbox(root, relief="raised", height=5, width=20, border=0, font = ('Roboto',30))
order_list.grid(padx=40, pady=138, columnspan=3, rowspan=6)  #columnspan=3, rowspan=6, pady=10, padx=20)
order_list.bind('<<ListboxSelect>>', select_item)

#Total Price (Listbox)
displaytotalp = Listbox(root, relief="raised", height=1, width=10, border=0, font = ('Roboto',14))
displaytotalp.place(x=280, y=420)
displaytotalp.bind('<<ListboxSelect>>', select_item)

totalpricelabel = Label(root, text='Total Price(₱)', font = ('Roboto',13))
totalpricelabel.place(x=145, y=420)

#Total Weight (Listbox)
displaytotalw = Listbox(root, relief="raised", height=1, width=10, border=0, font = ('Roboto',14))
displaytotalw.place(x=280, y=445)
displaytotalw.bind('<<ListboxSelect>>', select_item)

totalweightlabel = Label(root, text='Total Weight(g)', font = ('Roboto',13))
totalweightlabel.place(x=145, y=445)

cashtender_label = Label(root, text='Cash Tendered(₱)', font = ('Roboto',13))
cashtender_label.place(x=150, y=523)
cashtender_entry = Entry(root)
cashtender_entry.grid(row=1, column=2)
cashtender_entry.place(x=300, y=525)

cashenter_btn = Button(root, text='Enter', width=12, command=cashchange)
cashenter_btn.grid(row=2, column=2)
cashenter_btn.place(x=440, y=522)

cashchange_label = Label(root, text='Change(₱)', font = ('Roboto',13))
cashchange_label.place(x=208, y=552)
cashchange_list = Listbox(root, relief="raised", height=1, width=10, border=0, font = ('Roboto',14))
cashchange_list.place(x=300, y=552)
cashchange_list.bind('<<ListboxSelect>>')


# Create scrollbar
scrollbar = Scrollbar(root, width=20, border=0)
scrollbar.place(x=509, y=280, anchor=W)

# Set scroll to listbox
order_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=order_list.yview)
# Bind select
order_list.bind('<<ListboxSelect>>', select_item)


root.geometry('560x680+600+3') #Window size
root.mainloop()