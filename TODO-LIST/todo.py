from tkinter import *
from tkinter.font import Font
root=Tk()
root.title("TODO--LIST/Task 2")
root.geometry("800x600")
#defining font
my_font=Font(family="Brush Script MT",size=35,weight="bold")
my_frame=Frame(root)
my_frame.pack(pady=10)
label=Label(root,text="TODO LIST #TASK2",font=my_font)
label.pack(pady=20)
my_list=Listbox(my_frame,font=my_font,width=30,height=5,bg="SystemButtonFace",bd=0,
                fg="#464646",highlightthickness=0,)
my_list.pack(side=LEFT,fill=BOTH)
stuff=["Task1: password generator","Task2: TODO list","Task3: Weather App","Task4: Quiz game"]
for item in stuff:
    my_list.insert(END,item)

my_Scrollbar=Scrollbar(my_frame)
my_Scrollbar.pack(side=RIGHT,fill=BOTH)

my_list.config(yscrollcommand=my_Scrollbar.set)
my_Scrollbar.config(command=my_list.yview)

my_entry=Entry(root,font=("Times new roman",24))
my_entry.pack(pady=20)

button_frame=Frame(root)
button_frame.pack(pady=20)

def delete_item():
    my_list.delete(ANCHOR)
def add_item():
    my_list.insert(END,my_entry.get())
    my_entry.delete(0,END)

delete_button=Button(button_frame,text="Delete Item",command=delete_item)
add_button=Button(button_frame,text="Add Item",command=add_item)

delete_button.grid(row=0,column=0)
add_button.grid(row=0,column=1,padx=20)
root.mainloop()


















# def cross_off_item():
#     my_list.itemconfig(my_list.curselection(),)
# crossoff_button.grid(row=0,column=2)
# crossoff_button=Button(button_frame,text="cross off Item",command=cross_off_item)
