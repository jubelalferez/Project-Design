from tkinter import *
import tkinter.messagebox
from tkinter import Tk
from db import Database
import os
from db import *



# Instanciate database object
db = Database('jsj.db')


# **** Functions ****

def addorange():
    db.insert("ORANGE", "1", "10")
    populate_list()
    

def addapple():
    db.insert("APPLE", "1", "10")
    populate_list()

def addbanana():
    db.insert("BANANA", "1", "8")
    populate_list()

def addtocart():
    top = Toplevel()
    top.title("Products")
    top.geometry("300x300+710+180")

    #Orange
    #photo_orange = PhotoImage(file="ui/Orange.png")
    button_orange = Button(top, text="Orange", relief="raised", bd="3", command=addorange)
    button_orange.bind("<Button-1>")
    button_orange.place(x=15, y=15)

    #Apple
    button_apple = Button(top, text="Apple", relief="raised", bd="3", command=addapple)
    button_apple.bind("<Button-1>")
    button_apple.place(x=80, y=15)

    #Banana
    button_banana = Button(top, text="Banana", relief="raised", bd="3", command=addbanana)
    button_banana.bind("<Button-1>")
    button_banana.place(x=135, y=15)

    #tkinter.messagebox.showinfo('JSJ marketing by Group 10', 'An item is added to your Cart :)')

def checkout():
    tkinter.messagebox.showinfo('JSJ Marketing by Group 10',
                                'Make sure to double check your items and thank you for shopping :)')
    question = tkinter.messagebox.askquestion('Warning', 'Are sure to print the item?')
    if question == 'yes':
        os.system("sudo chmod a+w /dev/usb/lp0")
        os.system("sudo echo -e 'Thank you for shopping \n\n' > /dev/usb/lp0")
        print('Thank you for shopping')
    if question == 'no':
        print('Enjoy shopping')

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

        part_entry.delete(0, END)
        customer_entry.delete(0, END)
        total_entry.delete(0, END)
    except IndexError:
        pass

def remove_item():
    db.remove(selected_item[0])
    populate_list()

#Main Window
root = Tk()
root.title('JSJ Marketing by Group 10')

# **** Calling an image from the project file ****
# **** The simplest form, using PhotoImage() class ****
# **** You can only do this if you copy a file then paste it inside the project ****
logoPhoto = PhotoImage(file="ui/logoz.png")
logophotolabel = Label(root, image=logoPhoto)
logophotolabel.place(x=15, y=15, anchor=NW)

# **** Picture button. ADD TO CART. DELETE ITEM. PRINT ALL ITEM ****
photoadd = PhotoImage(file="ui/addsz.png")
button_1 = Button(root, image=photoadd, relief="raised", bd="3", command=addtocart)
button_1.bind("<Button-1>", addtocart)
button_1.place(x=40, y=550)

photodel = PhotoImage(file="ui/delete.png")
button_2 = Button(root, image=photodel, relief="raised", bd="3", command=remove_item)
button_2.bind("<Button-1>")
button_2.place(x=160, y=550)

photoprint = PhotoImage(file="ui/print.png")
button_3 = Button(root, image=photoprint, relief="raised", bd="3", command=checkout)
button_3.bind("<Button-1>", checkout)
button_3.place(x=420, y=550)

"""TEXTS"""
part_text = StringVar()
itemlabel = Label(root, text='ITEM DESCRIPTION')
itemlabel.place(x=40, y=120)
part_entry = Entry(root, textvariable=part_text)

customer_text = StringVar()
quantitylabel = Label(root, text='QUANTITY')
quantitylabel.place(x=230, y=120)
customer_entry = Entry(root, textvariable=customer_text)

total_text = StringVar()
pricelabel = Label(root, text='UNIT PRICE')
pricelabel.place(x=445, y=120)
total_entry = Entry(root, textvariable=total_text)

# Parts List (Listbox)
parts_list = Listbox(root, relief="raised", height=20, width=78, border=0)
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


root.geometry('560x680+600+3')
root.mainloop()