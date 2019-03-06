from tkinter import *

p = []
n = 0
opr = 0
num1 = 0
num2 = 0
x = 0
p2 =0
result = 0
clk = 0
clicked = 0


root = Tk()

root.title("Calculator")


def clear(n):
    expression_field.delete(n, END)

    return


def display(value):
    expression_field.insert(END,value)


expression_field = Entry(root, border="10", bg="#F7F4D5", font=("Courier New", 22, "bold"), justify="right")
expression_field.grid(rowspan=2, columnspan=5, ipadx=120, ipady=20)

bu1 = Button(root,text='9',border = "10", font=("Courier New",16,'bold'), bg = "#FFF2F2")
bu1.grid(row=2, column=0,sticky= 'snew',ipadx=10,ipady=20)
bu1.config(command=lambda : ButtonClick(9))

bu2 = Button(root,text='8',border = "10",font=("Courier New",16,'bold'), bg = "#FFF2F2")
bu2.grid(row=2, column=1,sticky= 'snew',ipadx=10,ipady=20 )
bu2.config(command=lambda : ButtonClick(8))

bu3 = Button(root,text='7',border = "10",font=("Courier New",16,'bold'), bg = "#FFF2F2")
bu3.grid(row=2, column=2,sticky= 'snew',ipadx=10,ipady=20 )
bu3.config(command=lambda : ButtonClick(7))

bu_add = Button(root,text='+',border = "10", font=("Courier New",16,'bold'), bg = "#FFF2F2")
bu_add.grid(row = 2,rowspan = 2, column=4,sticky= 'snew',ipadx=10,ipady=20)
bu_add.config(command=lambda : ButtonClick("10"))

bu_minius = Button(root,text='-',border = "10", font=("Courier New",16,'bold'), bg = "#FFF2F2")
bu_minius.grid(row = 4,rowspan = 2, column=4,sticky= 'snew',ipadx=10,ipady=20)
bu_minius.config(command=lambda : ButtonClick("11"))


bu4 = Button(root,text='6',border = "10",font=("Courier New",16,'bold'), bg = "#FFF2F2")
bu4.grid(row=3, column=0,sticky= 'snew',ipadx=10,ipady=20 )
bu4.config(command=lambda : ButtonClick(6))


bu5 = Button(root,text='5',border = "10",font=("Courier New",16,'bold'), bg = "#FFF2F2")
bu5.grid(row=3, column=1,sticky= 'snew',ipadx=10,ipady=20 )
bu5.config(command=lambda : ButtonClick(5))


bu6 = Button(root,text='4',border = "10",font=("Courier New",16,'bold'), bg = "#FFF2F2")
bu6.grid(row=3, column=2,sticky= 'snew',ipadx=10,ipady=20 )
bu6.config(command=lambda : ButtonClick(4))


bu7 = Button(root,text='3',border = "10",font=("Courier New",16,'bold'), bg = "#FFF2F2")
bu7.grid(row=4, column=0,sticky= 'snew',ipadx=10,ipady=20 )
bu7.config(command=lambda : ButtonClick(3))


bu8 = Button(root,text='2',border = "10",font=("Courier New",16,'bold'), bg = "#FFF2F2")
bu8.grid(row=4, column=1,sticky= 'snew',ipadx=10,ipady=20 )
bu8.config(command=lambda : ButtonClick(2))


bu9 = Button(root,text='1',border = "10",font=("Courier New",16,'bold'), bg = "#FFF2F2")
bu9.grid(row=4, column=2,sticky= 'snew',ipadx=10,ipady=20 )
bu9.config(command=lambda : ButtonClick(1))

allclear= Button(root,text='AC',border = "10",font=("Courier New",16,'bold'), bg = "#FFF2F2")
allclear.grid(row=5, column=0,sticky= 'snew',ipadx=10,ipady=20 )
allclear.config(command=lambda : ButtonClick('AC'))

bu0= Button(root,text='0',border = "10",font=("Courier New",16,'bold'), bg = "#FFF2F2")
bu0.grid(row=5, column=1,sticky= 'snew',ipadx=10,ipady=20 )
bu0.config(command=lambda : ButtonClick('0'))

equal= Button(root,text='=',border = "10",font=("Courier New",16,'bold'), bg = "#FFF2F2")
equal.grid(row=5, column=2,sticky= 'snew',ipadx=10,ipady=20 )
equal.config(command=lambda : ButtonClick('='))

bu_percent = Button(root,text='ANS',border = "10",font=("Courier New",16,'bold'), bg = "#FFF2F2")
bu_percent.grid(row=2, column=3,sticky= 'snew',ipadx=10,ipady=20 )
bu_percent.config(command=lambda : ButtonClick('ANS'))

C = Button(root,text='C',border = "10",font=("Courier New",16,'bold'), bg = "#FFF2F2")
C.grid(row=3, column=3,sticky= 'snew',ipadx=10,ipady=20 )
C.config(command=lambda : ButtonClick('C'))

bu_multiply = Button(root,text='x',border = "10",font=("Courier New",16,'bold'), bg = "#FFF2F2")
bu_multiply.grid(row=4, column=3,sticky= 'snew',ipadx=10,ipady=20 )
bu_multiply.config(command=lambda : ButtonClick('12'))

bu_divide = Button(root,text='/',border = "10",font=("Courier New",16,'bold'), bg = "#FFF2F2")
bu_divide.grid(row=5, column=3,sticky= 'snew',ipadx=10,ipady=20 )
bu_divide.config(command=lambda : ButtonClick('13'))


def ButtonClick(id):
    global p
    global n
    global opr
    global num1
    global num2
    global result
    global clk
    global clicked

    if id == "=":
        try:
            num2 = convert(p, n)
            if opr == 10:
                result = num1+num2
            if opr == 11:
                result = num1-num2
            if opr == 12:
                result = num1*num2
            if opr == 13:
                result = num1/num2
            display(" = ")
            display(result)
            print(num1, num2, result)
        except:
            clear(0)
            display("Maths error")

    elif id == "AC":
        p.clear()
        result = 0
        n = 0
        num1 = 0
        num2 = 0
        clear(0)
        clk = 0

    elif id == "ANS":
        clear(0)
        display(" ANS ")
        num1 = result
        clk = 1
    elif int(id) in range(0,10):
        display(id)
        p.append(id)
        n = n + 1
        clicked = clicked + 1

    elif int(id) in range(10, 14):
        if clk == 1:
            num1 = result
        else:
            num1 = convert(p, n)
        if int(id) == 10:
            display(" + ")
            opr = 10
        if int(id) == 11:
            display(" - ")
            opr =11
        if int(id) == 12:
            display(" X ")
            opr = 12
        if int(id) == 13:
            display(" / ")
            opr = 13
        p.clear()
        n = 0


def convert(p, n):
    x = 0
    for i in p:
        x = x + i * pow(10, n - 1)
        n = n - 1
    return x

root.mainloop()

