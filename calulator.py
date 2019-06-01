from tkinter import *


num1 = ""
num2 = ""
result = 0
click = 0
add,sub,mul,div = False,False,False,False


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

    global num1
    global num2
    global result
    global click
    global add
    global sub
    global mul
    global div

    if id == "=":
        try:

            if add == True:
                result = int(num1)+int(num2)
                add = False
            if sub == True:
                result = int(num1)-int(num2)
                sub = False
            if mul == True:
                result = int(num1)*int(num2)
                mul = False
            if div == 13:
                result = int(num1)/int(num2)
                div = False
            display(" = ")
            display(result)
            print(num1, num2, result)
        except:
            clear(0)
            display("Maths error")



    elif id == "AC":
        result = 0
        num1 = ""
        num2 = ""
        clear(0)


    elif id == "ANS":
        clear(0)
        display(" ANS ")
        num1 = result
        click = 1


    elif int(id) in range(0,9):
        display(id)
        if click == 0:
            num1 = num1+str(id)
        else:
            num2 = num2+str(id)


    elif int(id) == int(10):
        display("+")
        click = 1
        add = True


    elif int(id) == int(11):
        display("-")
        click = 1
        sub = True


    elif int(id) == int(12):
        display("X")
        click = 1
        mul = True


    elif int(id) == int(13):
        display("/")
        click = 1
        div = True



root.mainloop()

