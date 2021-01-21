from tkinter import Tk, Label, StringVar, Entry, ttk, Button, messagebox
# Make the tk window center to screen
def screen_center(root, width=0, height=0):
    screen_width = root.winfo_screenwidth()
    w = str(int(screen_width/2 - width/2))
    screen_height = root.winfo_screenheight()
    h = str(int(screen_height/2 - height/2))
    root.geometry(str(width) + "x"+ str(height) +"+"+ w +"+"+ h)


def add():
    if name_text.get() == '' or id_text.get() == '':
        messagebox.showwarning('Required field', 'Please enter all fields!')
        return
    tv.insert('', 'end', values=(id_text.get(), name_text.get(), gender_text.get()), tags=('font'))
    tv.tag_configure('font', font=font)
    clear()

def clear():
    name_text.set('')
    id_text.set('')
    ent_id.focus()

def update():
    if name_text.get() == '' or id_text.get() == '':
        messagebox.showwarning('Required field', 'Please enter all fields!')
        return
    tv.set(ITEMS, column=)
    clear()

def delete():
    selected_items = tv.selection()
    for selected_item in selected_items:
        tv.delete(selected_item)

def edit(event):
    clear()
    global ITEMS
    for selection in tv.selection():
        item = tv.item(selection)
        ITEMS = item
        ID, name, gender = item['values'][0:3]
    id_text.set(ID)
    name_text.set(name)
    gender_text.set(gender)

app = Tk()
app.title('Crud')
app.rowconfigure(3, weight=1)
app.columnconfigure(3, weight=1)
screen_center(app, 1080, 920)
# Define global variable
font = ("Times New Roman", 12)
btn_width = 15


# row 0
lbl_id = Label(app, text="Customer ID: ", font=font, justify='left')
lbl_id.grid(row=0, column=0, padx=20, pady=10, sticky="w")

id_text = StringVar()
ent_id = Entry(app, textvariable=id_text, font=font)
ent_id.grid(row=0, column=1, sticky='w')

# Button Add
btn_add = Button(app, justify='left', text='Add', width=btn_width, command = add, font=font)
btn_add.grid(row=0, column=2, padx=30)

# row 1
lbl_name = Label(app, text="Customer Name: ", font=font, justify='left')
lbl_name.grid(row=1, column=0, padx=20, pady=10, sticky='w')

name_text = StringVar()
ent_name = Entry(app, textvariable=name_text, font=font)
ent_name.grid(row=1, column=1, sticky='w')

# Button Update
btn_update = Button(app, justify='left', text='Update', width=btn_width, command = update, font=font)
btn_update.grid(row=1, column=2, padx=30)

# row 2
lbl_gender = Label(app, text="Customer Gender: ", font=font, justify='left')
lbl_gender.grid(row=2, column=0, padx=20, pady=10, sticky='w')

gender_text = StringVar()
cmb_gender = ttk.Combobox(app, state='readonly', values=('Male', 'Female'), textvariable=gender_text, font=font)
# Or can use like this: cmb_gender['values'] = ('Male', 'Female')
cmb_gender.grid(row=2, column=1, sticky='w')
cmb_gender.current(0)

# Button Update
btn_delete = Button(app, justify='left', text='Delete', width=btn_width, command = delete, font=font)
btn_delete.grid(row=2, column=2, padx=30)

# create Treeview as a Table
columns = ('Customer ID', 'Customer Name', 'Gender')
ac = ('one','two','three')

style = ttk.Style()
style.configure("Treeview.Heading", font=font)

tv = ttk.Treeview(app, show='headings', columns=ac, height=7)
tv.bind("<<TreeviewSelect>>", edit)
for i in range(len(columns)):
    tv.column(ac[i], width=100, anchor='w')
    tv.heading(ac[i], text=columns[i])
tv.grid(row=3, column=0,columnspan=4, sticky="NSEW")

app.mainloop()