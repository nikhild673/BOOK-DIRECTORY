import sqlite3

conn=sqlite3.connect("directory.db")
c=conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS book(Title char,Author int,Year int,ISBN int)")

def exit():
    result=messagebox.askyesno("Alert","do you want to exit")
    if result==True:
        sys.exit()
    else:
        pass

def add_entry():
    # a=entry1.get()
    # b=entry2.get()
    # c=entry3.get()
    # d=entry4.get()
    conn = sqlite3.connect("directory.db")
    c = conn.cursor()
    c.execute("insert into book(Title,Author,Year,ISBN) VALUES (?,?,?,?)",( "a" ,"b", 5, 8 ))
    conn.commit()


def view_all():
    cursor = sqlite3.connect('test.db')
    cursor.execute("select * from book");
    # l.insert(END,entry1.get())
    cursor.commit()
    cursor.close()