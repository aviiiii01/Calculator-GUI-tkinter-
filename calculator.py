from tkinter import *
import re
root=Tk()

e=Entry(root,fg='white',bg='skyblue',width=60,borderwidth=5)
e.grid(row=0,column=0,columnspan=4,padx=10,pady=10)

#operation shi kr na bhaiii!!!! kl last din h bsss!!
def button_click(number):
    e.insert(END,number)

def clear():
    e.delete(0,END)

def back():
    x=e.get()
    e.delete(len(x)-1,END)

 

def add():  
    global math
    global x    
    math='add'
    x=int(e.get())
    e.delete(0,END)

def sub():  
    global math
    global x
    math='sub'
    x=int(e.get())
    e.delete(0,END)

def mul():  
    global math
    global x
    math='mul'
    x=int(e.get())
    e.delete(0,END)

def div(): 
    global math
    global x 
    math='div'
    x=int(e.get())
    e.delete(0,END)

def percent():
    global math
    global x 
    math='percent'
    x=int(e.get())
    e.delete(0,END)


def equal():
    result= 0
    if math=='add':
        y=e.get()
        result=int(y)+x
    if math=='sub':
        y=e.get()
        result=x-int(y)
    if math=='mul':
        y=e.get()
        result=int(y)*x
    if math=='div':
        y=e.get()
        result=x/int(y)
    if math=='percent':
        y=e.get()
        result=(x/100)*int(y)
    e.delete(0,END)
    e.insert(END,result)


    


button7=Button(root,text='7',pady=30,padx=45,bg='black',fg='skyblue',command=lambda:button_click(7))
button8=Button(root,text='8',pady=30,padx=45,bg='black',fg='skyblue',command=lambda:button_click(8))
button9=Button(root,text='9',pady=30,padx=45,bg='black',fg='skyblue',command=lambda:button_click(9))
button4=Button(root,text='4',pady=30,padx=45,bg='black',fg='skyblue',command=lambda:button_click(4))
button5=Button(root,text='5',pady=30,padx=45,bg='black',fg='skyblue',command=lambda:button_click(5))
button6=Button(root,text='6',pady=30,padx=45,bg='black',fg='skyblue',command=lambda:button_click(6))
button1=Button(root,text='1',pady=30,padx=45,bg='black',fg='skyblue',command=lambda:button_click(1))
button2=Button(root,text='2',pady=30,padx=45,bg='black',fg='skyblue',command=lambda:button_click(2))
button3=Button(root,text='3',pady=30,padx=45,bg='black',fg='skyblue',command=lambda:button_click(3))
button0=Button(root,text='0',pady=30,padx=45,bg='black',fg='skyblue',command=lambda:button_click(0))

plus=Button(root,text='+',pady=30,padx=45,fg='yellow',bg='black',command=add)
subs=Button(root,text='-',pady=30,padx=45,fg='yellow',bg='black',command=sub)
muls=Button(root,text='*',pady=30,padx=45,fg='yellow',bg='black',command=mul)
divs=Button(root,text='/',pady=30,padx=45,fg='yellow',bg='black',command=div)
equals=Button(root,text='=',pady=30,padx=45,fg='yellow',bg='black',command=equal)
dot=Button(root,text='...',pady=30,padx=45,fg='yellow',bg='black',command=lambda:button_click('.'))
backs=Button(root,text='[x]',pady=28,padx=43,fg='yellow',bg='black',command=back)
ce=Button(root,text='CE',pady=28,padx=43,fg='yellow',bg='black',command=clear)
percents=Button(root,text='%',pady=28,padx=43,fg='yellow',bg='black',command=percent)
c=Button(root,text='C',pady=28,padx=43,fg='yellow',bg='black',command=clear)

percents.grid(row=1,column=0)
ce.grid(row=1,column=1)
plus.grid(row=2,column=3)
subs.grid(row=3,column=3)
muls.grid(row=4,column=3)
equals.grid(row=5,column=2)
dot.grid(row=5,column=0)
backs.grid(row=1,column=3)
c.grid(row=1,column=2)
divs.grid(row=5,column=3)



button7.grid(row=2,column=0)
button8.grid(row=2,column=1)
button9.grid(row=2,column=2)
button4.grid(row=3,column=0)
button5.grid(row=3,column=1)
button6.grid(row=3,column=2)
button1.grid(row=4,column=0)
button2.grid(row=4,column=1)
button3.grid(row=4,column=2)
button0.grid(row=5,column=1)

root.mainloop()