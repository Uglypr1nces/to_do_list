from tkinter import *
from tkinter.font import Font

root = Tk()
root.geometry("500x500")
root.title("to do list")


my_font = Font(
    family="Terminal",
    size=20,
    weight="bold")

my_frame = Frame(root)
my_frame.pack(pady=10)

my_list = Listbox(my_frame,
    font=my_font,
    width=25,
    height=5,
    bg="systemButtonFace",
    bd=0,
    fg="#464646",
    highlightthickness=0,
    selectbackground = "#a6a6a6",
    activestyle = "none"
    )

my_list.pack(side=LEFT,fill=BOTH)

stuff = ["dont go outside", "dunno", "BEAT UP SOME OLD MAN"]
for item in stuff:
    my_list.insert(END, item)


myscrollbar = Scrollbar(my_frame)
myscrollbar.pack(side=RIGHT,fill=BOTH)


my_list.config(yscrollcommand=myscrollbar.set)
myscrollbar.config(command=my_list.yview)

my_entry = Entry(root, font=("Helvetica",24))
my_entry.pack(pady=20)

button_frame = Frame(root)
button_frame.pack(pady=20)

def delete_item():
    my_list.delete(ANCHOR)

def add_item():
    my_list.insert(END, my_entry.get())
    my_entry.delete(0,END)

def cross_item():
    my_list.itemconfig(
        my_list.curselection(),
        fg="#dedede")
    my_list.selection_clear(0,END)

def uncross_item():
    my_list.itemconfig(
        my_list.curselection(),
        fg="#464646")


delete_button = Button(button_frame,text="Delete smth",command=delete_item)
add_button = Button(button_frame,text="add smth",command=add_item)
cross_button = Button(button_frame,text="cross smth",command=cross_item)
uncross_button = Button(button_frame,text="uncross smth",command=uncross_item)

delete_button.grid(row=0, column=0)
add_button.grid(row=0, column=1,padx=20)
cross_button.grid(row=0, column=2)
uncross_button.grid(row=0, column=3,padx=20)


root.mainloop()