from tkinter import Tk, Label, StringVar, Entry

# Make the tk window center to screen
def screen_center(root, width=0, height=0):
    screen_width = root.winfo_screenwidth()
    w = str(int(screen_width/2 - width/2))
    screen_height = root.winfo_screenheight()
    h = str(int(screen_height/2 - height/2))
    root.geometry(str(width) + "x"+ str(height) +"+"+ w +"+"+ h)

app = Tk()
app.title('Crud')
screen_center(app, 1080, 920)
# Define global variable
font = ("Times New Roman", 20)

# row 0
lbl_cusomter_id = Label(app, text="Customer ID: ", font=font, justify='left')
lbl_cusomter_id.grid(row=0, column=0, padx=20, pady=20, sticky="w")

customer_id_text = StringVar()
ent_customer_id = Entry(app, textvariable=customer_id_text, font=font)
ent_customer_id.grid(row=0, column=1)

# row 1
lbl_cusomter_name = Label(app, text="Customer Name: ", font=font, justify='left')
lbl_cusomter_name.grid(row=1, column=0, padx=20, pady=20, sticky='w')

customer_name_text = StringVar()
ent_customer_name = Entry(app, textvariable=customer_name_text, font=font)
ent_customer_name.grid(row=1, column=1)







app.mainloop()