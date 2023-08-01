from tkinter import *
root=Tk()
root.title("CALCULATOR /Task 3")
root.geometry("1300x600")

calculation=""
def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0,"end")
    text_result.insert(1.0,calculation)

def evaluate_claculation():
    global calculation
    try:
        calculation=str(eval(calculation))
        text_result.delete(1.0,"end")
        text_result.insert(1.0,calculation)
    except:
        clear_field()
        text_result.insert(1.0,"Error")
def clear_field():
    global calculation
    calculation=""
    text_result.delete(1.0,"end")

text_result=Text(root,height=2,width=50,font=("Arial",34))
text_result.grid(pady=20,columnspan=5)

btn_1=Button(root,text="1",command=lambda: add_to_calculation(1),width=15,font=("Arial",24))
btn_1.grid(row=2,column=1)
btn_2=Button(root,text="2",command=lambda: add_to_calculation(2),width=15,font=("Arial",24))
btn_2.grid(row=2,column=2)
btn_3=Button(root,text="3",command=lambda: add_to_calculation(3),width=15,font=("Arial",24))
btn_3.grid(row=2,column=3)
btn_4=Button(root,text="4",command=lambda: add_to_calculation(4),width=15,font=("Arial",24))
btn_4.grid(row=3,column=1)
btn_5=Button(root,text="5",command=lambda: add_to_calculation(5),width=15,font=("Arial",24))
btn_5.grid(row=3,column=2)
btn_6=Button(root,text="6",command=lambda: add_to_calculation(6),width=15,font=("Arial",24))
btn_6.grid(row=3,column=3)
btn_7=Button(root,text="7",command=lambda: add_to_calculation(7),width=15,font=("Arial",24))
btn_7.grid(row=4,column=1)
btn_8=Button(root,text="8",command=lambda: add_to_calculation(8),width=15,font=("Arial",24))
btn_8.grid(row=4,column=2)
btn_9=Button(root,text="9",command=lambda: add_to_calculation(9),width=15,font=("Arial",24))
btn_9.grid(row=4,column=3)
btn_0=Button(root,text="0",command=lambda: add_to_calculation(0),width=15,font=("Arial",24))
btn_0.grid(row=5,column=2)

add_btn=Button(root,text="+",command=lambda: add_to_calculation("+"),width=15,font=("Arial",24))
add_btn.grid(row=2,column=4)
btn_sub=Button(root,text="-",command=lambda: add_to_calculation("-"),width=15,font=("Arial",24))
btn_sub.grid(row=3,column=4)
btn_mul=Button(root,text="*",command=lambda: add_to_calculation("*"),width=15,font=("Arial",24))
btn_mul.grid(row=4,column=4)
btn_div=Button(root,text="/",command=lambda: add_to_calculation("/"),width=15,font=("Arial",24))
btn_div.grid(row=5,column=4)
btn_open=Button(root,text="(",command=lambda: add_to_calculation("("),width=15,font=("Arial",24))
btn_open.grid(row=5,column=1)
btn_close=Button(root,text=")",command=lambda: add_to_calculation(")"),width=15,font=("Arial",24))
btn_close.grid(row=5,column=3)
btn_equal=Button(root,text="=",command=evaluate_claculation,width=31,font=("Arial",24))
btn_equal.grid(row=6,column=1,columnspan=2)
btn_clear=Button(root,text="AC",command=clear_field,width=31,font=("Arial",24))
btn_clear.grid(row=6,column=3,columnspan=2)

label=Label(root,text="#TASK3 CALCULATOR",font=("Arial",24))
label.grid(pady=50,row=8,column=3)



root.mainloop()