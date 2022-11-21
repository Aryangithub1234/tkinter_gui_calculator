from tkinter import *
import math
root = Tk()
def click(event):
    global screenvalue
    text = event.widget.cget("text")  #button se text leta h
    # print(text)
    if text == "=":
        if screenvalue.get().isdigit():
            value = int(screenvalue.get())
        else:
            value = eval(e.get())
        screenvalue.set(value)
        e.update()

    elif text == "c":
        screenvalue.set("")
        e.update()
    elif text == "sin":
       s = math.sin(screenvalue.get().isnumeric())
       screenvalue.set(s)
       e.update()
    elif text == "cos":
        c = math.cos(screenvalue.get().isnumeric())
        screenvalue.set(c)
        e.update()
    elif text == "tan":
        t = math.tan(screenvalue.get().isnumeric())
        screenvalue.set(t)
        e.update()
    elif text == "sinh":
        si = math.sinh(screenvalue.get().isnumeric())
        screenvalue.set(si)
        e.update()
    elif text == "cosh":
        co = math.cosh(screenvalue.get().isnumeric())
        screenvalue.set(co)
        e.update()
    elif text == "tanh":
        th = math.tanh(screenvalue.get().isnumeric())
        screenvalue.set(th)
        e.update()
    elif text == "^":
        squareroot = math.sqrt(screenvalue.get().isnumeric())
        screenvalue.set(math.sqrt(squareroot))
        e.update()
    else:
        screenvalue.set(screenvalue.get()+text)
        e.update()

root.geometry("450x700")
root.title("Aryan GUI Calculator")
root.configure(bg="black")
screenvalue = StringVar()
screenvalue.set("")
Label(root,font="copperplate 25",bg="black",fg="cadetblue4",text="Calculator").pack()

e = Entry(root,textvariable=screenvalue,font="lucida 40 italic",bg="#32CD32",fg="black",relief=GROOVE)
e.pack(fill=X,padx=20,pady=20)

f1 = Frame(root,padx=10,pady=10,bg="black",relief=RAISED)
b1 = Button(f1,text="7",font="lucida 20 italic",bg="orange",padx=35,relief=SUNKEN)
b1.pack(side=LEFT,padx=5,pady=5)
b1.bind("<Button-1>",click)
b2 = Button(f1,text="8",font="lucida 20 italic",bg="orange",padx=35,relief=SUNKEN)
b2.pack(side=LEFT,padx=5,pady=5)
b2.bind("<Button-1>",click)
b3 = Button(f1,text="9",font="lucida 20 italic",bg="orange",padx=35,relief=SUNKEN)
b3.pack(side=LEFT,padx=5,pady=5)
b3.bind("<Button-1>",click)
b4 = Button(f1,text="*",font="lucida 20 italic",bg="black",padx=15,fg="blue",relief=SUNKEN)
b4.pack(side=LEFT,padx=5,pady=5)
b4.bind("<Button-1>",click)
f1.pack()

f2 = Frame(root,padx=15,pady=15,bg="black",relief=RAISED)
b5 = Button(f2,text="4",font="lucida 20 italic",bg="orange",padx=35,relief=SUNKEN)
b5.pack(side=LEFT,padx=5,pady=5)
b5.bind("<Button-1>",click)
b6 = Button(f2,text="5",font="lucida 20 italic",bg="orange",padx=35,relief=SUNKEN)
b6.pack(side=LEFT,padx=5,pady=5)
b6.bind("<Button-1>",click)
b7 = Button(f2,text="6",font="lucida 20 italic",bg="orange",padx=35,relief=SUNKEN)
b7.pack(side=LEFT,padx=5,pady=5)
b7.bind("<Button-1>",click)
b8 = Button(f2,text="-",font="lucida 20 italic",bg="black",padx=15,fg="blue",relief=SUNKEN)
b8.pack(side=LEFT,padx=5,pady=5)
b8.bind("<Button-1>",click)
f2.pack()

f3 = Frame(root,padx=10,pady=10,bg="black",relief=RAISED)
b9 = Button(f3,text="1",font="lucida 20 italic",bg="orange",padx=35,relief=SUNKEN)
b9.pack(side=LEFT,padx=5,pady=5)
b9.bind("<Button-1>",click)
b10 = Button(f3,text="2",font="lucida 20 italic",bg="orange",padx=35,relief=SUNKEN)
b10.pack(side=LEFT,padx=5,pady=5)
b10.bind("<Button-1>",click)
b11 = Button(f3,text="3",font="lucida 20 italic",bg="orange",padx=35,relief=SUNKEN)
b11.pack(side=LEFT,padx=5,pady=5)
b11.bind("<Button-1>",click)
b12 = Button(f3,text="//",font="lucida 20 italic",bg="black",padx=10,fg="blue",relief=SUNKEN)
b12.pack(side=LEFT,padx=5,pady=5)
b12.bind("<Button-1>",click)
f3.pack()


f4 = Frame(root,padx=10,pady=10,bg="black",relief=RAISED)
b13 = Button(f4,text="+",font="lucida 20 italic",bg="black",padx=35,fg="blue",relief=SUNKEN)
b13.pack(side=LEFT,padx=5,pady=5)
b13.bind("<Button-1>",click)
b14 = Button(f4,text="0",font="lucida 20 italic",bg="orange",padx=35,fg="black",relief=SUNKEN)
b14.pack(side=LEFT,padx=5,pady=5)
b14.bind("<Button-1>",click)
b15 = Button(f4,text="=",font="lucida 20 italic",bg="black",padx=35,fg="blue",relief=SUNKEN)
b15.pack(side=LEFT,padx=5,pady=5)
b15.bind("<Button-1>",click)
b16 = Button(f4,text=".",font="lucida 20 italic",bg="black",padx=15,fg="blue",relief=SUNKEN)
b16.pack(side=LEFT,padx=5,pady=5)
b16.bind("<Button-1>",click)
f4.pack()

f5 = Frame(root,padx=10,pady=10,bg="black",relief=RAISED)
b17 = Button(f5,text="sin",font="lucida 20 italic",bg="black",padx=25,fg="limegreen",relief=SUNKEN)
b17.pack(side=LEFT,padx=5,pady=5)
b17.bind("<Button-1>",click)
b18 = Button(f5,text="cos",font="lucida 20 italic",bg="black",padx=25,fg="limegreen",relief=SUNKEN)
b18.pack(side=LEFT,padx=5,pady=5)
b18.bind("<Button-1>",click)
b19 = Button(f5,text="tan",font="lucida 20 italic",bg="black",padx=25,fg="limegreen",relief=SUNKEN)
b19.pack(side=LEFT,padx=5,pady=5)
b19.bind("<Button-1>",click)
b20 = Button(f5,text="c",font="lucida 20 italic",bg="#DC143C",padx=9,fg="white",relief=SUNKEN)
b20.pack(side=LEFT,padx=5,pady=5)
b20.bind("<Button-1>",click)
f5.pack()

f6 = Frame(root,padx=10,pady=10,bg="black",relief=RAISED)
b21 = Button(f6,text="sinh",font="lucida 20 italic",bg="black",padx=20,fg="crimson",relief=SUNKEN)
b21.pack(side=LEFT,padx=5,pady=5)
b21.bind("<Button-1>",click)
b22 = Button(f6,text="cosh",font="lucida 20 italic",bg="black",padx=15,fg="crimson",relief=SUNKEN)
b22.pack(side=LEFT,padx=5,pady=5)
b22.bind("<Button-1>",click)
b23 = Button(f6,text="tanh",font="lucida 20 italic",bg="black",padx=15,fg="crimson",relief=SUNKEN)
b23.pack(side=LEFT,padx=5,pady=5)
b23.bind("<Button-1>",click)
b24 = Button(f6,text="^",font="lucida 20 italic",bg="deepskyblue3",padx=10,fg="white",relief=SUNKEN)
b24.pack(side=LEFT,padx=5,pady=5)
b24.bind("<Button-1>",click)

f6.pack()



root.mainloop()