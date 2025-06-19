from tkinter import*

def bclick(number):
    global val
    val=val+str(number)
    data.set(val)

def bclear():
    global val
    val=""
    data.set("")

def bEquals():
    global val
    result=str(eval(val))
    data.set(result)
    
root=Tk() 
root.title("my cal")
root.geometry("361x381")
val=""
data=StringVar()
display=Entry(root,textvariable=data,bd=29,justify="right",bg="powder blue",font=("ariel",20))
display.grid(row=0,columnspan=4)
b7=Button(root,text="7",font=("arial",12,"bold"),bd=12,height=2,width=6,command=lambda:bclick(7))
b7.grid(row=1,column=0)
b8=Button(root,text="8",font=("arial",12,"bold"),bd=12,height=2,width=6,command=lambda:bclick(8))
b8.grid(row=1,column=1)
b9=Button(root,text="9",font=("arial",12,"bold"),bd=12,height=2,width=6,command=lambda:bclick(9))
b9.grid(row=1,column=2)
b_add=Button(root,text="+",font=("arial",12,"bold"),bd=12,height=2,width=6,command=lambda:bclick('+'))
b_add.grid(row=1,column=3)

b4=Button(root,text="4",font=("arial",12,"bold"),bd=12,height=2,width=6,command=lambda:bclick(4))
b4.grid(row=2,column=0)
b5=Button(root,text="5",font=("arial",12,"bold"),bd=12,height=2,width=6,command=lambda:bclick(5))
b5.grid(row=2,column=1)
b6=Button(root,text="6",font=("arial",12,"bold"),bd=12,height=2,width=6,command=lambda:bclick(6))
b6.grid(row=2,column=2)
b_sub=Button(root,text="-",font=("arial",12,"bold"),bd=12,height=2,width=6,command=lambda:bclick('-'))
b_sub.grid(row=2,column=3)

b1=Button(root,text="1",font=("arial",12,"bold"),bd=12,height=2,width=6,command=lambda:bclick(1))
b1.grid(row=3,column=0)
b2=Button(root,text="2",font=("arial",12,"bold"),bd=12,height=2,width=6,command=lambda:bclick(2))
b2.grid(row=3,column=1)
b3=Button(root,text="3",font=("arial",12,"bold"),bd=12,height=2,width=6,command=lambda:bclick(3))
b3.grid(row=3,column=2)
b_mul=Button(root,text="*",font=("arial",12,"bold"),bd=12,height=2,width=6,command=lambda:bclick('*'))
b_mul.grid(row=3,column=3)

bc=Button(root,text="c",font=("arial",12,"bold"),bd=12,height=2,width=6,command=bclear)
bc.grid(row=4,column=0)
b0=Button(root,text="0",font=("arial",12,"bold"),bd=12,height=2,width=6,command=lambda:bclick(0))
b0.grid(row=4,column=1)
b_div=Button(root,text="/",font=("arial",12,"bold"),bd=12,height=2,width=6,command=lambda:bclick('/'))
b_div.grid(row=4,column=2)
b_equal=Button(root,text="=",font=("arial",12,"bold"),bd=12,height=2,width=6,command=bEquals)
b_equal.grid(row=4,column=3)
 
root.mainloop()

