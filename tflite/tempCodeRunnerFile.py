def populate_list():
    parts_list.delete(0, END)
    for row in db.fetch():
            parts_list.insert(END, row)