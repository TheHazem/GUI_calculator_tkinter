# gui calculator with tkinter
from tkinter import *
from tkinter import font
###################
# creating window
window = Tk()
# some used vars #
greyy = "#474747"
myfont = font.Font(weight = "bold", size = 20)

show = "" # 11+222
n1 = "" # 11
n2 = ""#22
sign = ""#+
ifsign = False# true
old1 = "" #  233
result = "" # 

def old():
    global show,n1,n2,sign,ifsign,old1,result
    if sign == "+":
        if "." in show:
            old1 = float(n1) + float(n2)
        elif "." not in show:
            old1 = int(n1) + int(n2)
    lbl= Label(window, text = show, fg='white',bg = "#3d3d3d" ,width =15, height = 3 )
    lbl.place (x=0, y=0)
    lbl["font"] = font.Font(weight ="bold", size = 27)

    if sign == "-":
        if "." in show:
            old1 = float(n1) - float(n2)
        elif "." not in show:
            old1 = int(n1) - int(n2)
    lbl= Label(window, text = show, fg='white',bg = "#3d3d3d" ,width =15, height = 3 )
    lbl.place (x=0, y=0)
    lbl["font"] = font.Font(weight ="bold", size = 27)
    
    if sign == "x":
        if "." in show:
            old1 = float(n1) * float(n2)
        elif "." not in show:
            old1 = int(n1) * int(n2)
    lbl= Label(window, text = show, fg='white',bg = "#3d3d3d" ,width =15, height = 3 )
    lbl.place (x=0, y=0)
    lbl["font"] = font.Font(weight ="bold", size = 27)
    
    if sign == "÷":
        if "." in show:
            old1 = float(n1) / float(n2)
        elif "." not in show:
            old1 = int(n1) / int(n2)
    lbl= Label(window, text = show, fg='white',bg = "#3d3d3d" ,width =15, height = 3 )
    lbl.place (x=0, y=0)
    lbl["font"] = font.Font(weight ="bold", size = 27)
    
    if sign == "%":
        if "." in show:
            old1 = float(n1) / 100
        elif "." not in show:
            old1 = int(n1) / 100
    lbl= Label(window, text = show, fg='white',bg = "#3d3d3d" ,width =15, height = 3 )
    lbl.place (x=0, y=0)
    lbl["font"] = font.Font(weight ="bold", size = 27)
    
    if sign == "-/+":
                if "." not in show:
                    if n2 == "":
                        old1 = int(n1) * (-1)
                    else :
                        old1 = (int(n1) + int(n2)) * (-1)
    lbl= Label(window, text = show, fg='white',bg = "#3d3d3d" ,width =15, height = 3 )
    lbl.place (x=0, y=0)
    lbl["font"] = font.Font(weight ="bold", size = 27)
    

def clearr():
    global show,n1,n2,sign,ifsign,old1,result
    show = ""
    n1 = ""
    n2 = ""
    sign = ""
    ifsign = False
    old1 = ""
    result = ""
    lbl= Label(window, text = show, fg='white',bg = "#3d3d3d" ,width =15, height = 3 )
    lbl.place (x=0, y=0)
    lbl["font"] = font.Font(weight ="bold", size = 27)


def equal():
    global show,n1,n2,sign,ifsign,old1,result
    old()
    n1 = str(old1)
    n2 = ""
    result = old1
    show = str(old1)
    sign = ""
    ifsign = False
    lbl= Label(window, text = show, fg='white',bg = "#3d3d3d" ,width =15, height = 3 )
    lbl.place (x=0, y=0)
    lbl["font"] = font.Font(weight ="bold", size = 27)


def plus():
    global show,n1,n2,sign,ifsign,old1,result
    if "+" in show:
        old()
        n1 = str(old1)
        n2 = ""
        show = show + "+"
        sign = "+"
        ifsign = True
    else:
        show = show + "+"
        sign = "+"
        ifsign = True
    lbl= Label(window, text = show, fg='white',bg = "#3d3d3d" ,width =15, height = 3 )
    lbl.place (x=0, y=0)
    lbl["font"] = font.Font(weight ="bold", size = 27)

def minus():
    global show,n1,n2,sign,ifsign,old1,result
    if "-" in show:
        old()
        n1 = str(old1)
        n2 = ""
        show = show + "-"
        sign = "-"
        ifsign = True
    else:
        show = show + "-"
        sign = "-"
        ifsign = True
    lbl= Label(window, text = show, fg='white',bg = "#3d3d3d" ,width =15, height = 3 )
    lbl.place (x=0, y=0)
    lbl["font"] = font.Font(weight ="bold", size = 27)

def multt():
    global show,n1,n2,sign,ifsign,old1,result
    if "x" in show:
        old()
        n1 = str(old1)
        n2 = ""
        show = show + "x"
        sign = "x"
        ifsign = True
    else:
        show = show + "x"
        sign = "x"
        ifsign = True
    lbl= Label(window, text = show, fg='white',bg = "#3d3d3d" ,width =15, height = 3 )
    lbl.place (x=0, y=0)
    lbl["font"] = font.Font(weight ="bold", size = 27)

def divid():
    global show,n1,n2,sign,ifsign,old1,result
    if "÷" in show:
        old()
        n1 = str(old1)
        n2 = ""
        show = show + "÷"
        sign = "÷"
        ifsign = True
    else:
        show = show + "÷"
        sign = "÷"
        ifsign = True
    lbl= Label(window, text = show, fg='white',bg = "#3d3d3d" ,width =15, height = 3 )
    lbl.place (x=0, y=0)
    lbl["font"] = font.Font(weight ="bold", size = 27)

def percent():
    global show,n1,n2,sign,ifsign,old1,result
    if "%" in show:
        old()
        n1 = str(old1)
        n2 = ""
        show = show + "%"
        sign = "%"
        ifsign = True
    else:
        show = show + "%"
        sign = "%"
        ifsign = True
    lbl= Label(window, text = show, fg='white',bg = "#3d3d3d" ,width =15, height = 3 )
    lbl.place (x=0, y=0)
    lbl["font"] = font.Font(weight ="bold", size = 27)

#####################################################
def posneg():
    global show,n1,n2,sign,ifsign,old1,result
    if "-/+" in show:
        old()
        n1 = str(old1)
        n2 = ""
        show = show + "-/+"
        sign = "-/+"
        ifsign = True
    else:
        show = show + "-/+"
        sign = "-/+"
        ifsign = True
    lbl= Label(window, text = show, fg='white',bg = "#3d3d3d" ,width =15, height = 3 )
    lbl.place (x=0, y=0)
    lbl["font"] = font.Font(weight ="bold", size = 27)




def zero():
    global show,n1,n2,sign,ifsign,old1,result
    show = show + "0"
    if ifsign == False:
        n1 = n1 + "0"
    elif ifsign == True:
        n2 = n2 + "0"
    lbl= Label(window, text = show, fg='white',bg = "#3d3d3d" ,width =15, height = 3 )
    lbl.place (x=0, y=0)
    lbl["font"] = font.Font(weight ="bold", size = 27)


def one():
    global show,n1,n2,sign,ifsign,old1,result
    show = show + "1"
    if ifsign == False:
        n1 = n1 + "1"
    elif ifsign == True:
        n2 = n2 + "1"
    lbl= Label(window, text = show, fg='white',bg = "#3d3d3d" ,width =15, height = 3 )
    lbl.place (x=0, y=0)
    lbl["font"] = font.Font(weight ="bold", size = 27)



def two():
    global show,n1,n2,sign,ifsign,old1,result
    show = show + "2"
    if ifsign == False:
        n1 = n1 + "2"
    elif ifsign == True:
        n2 = n2 + "2"
    lbl= Label(window, text = show, fg='white',bg = "#3d3d3d" ,width =15, height = 3 )
    lbl.place (x=0, y=0)
    lbl["font"] = font.Font(weight ="bold", size = 27)



def three():
    global show,n1,n2,sign,ifsign,old1,result
    show = show + "3"
    if ifsign == False:
        n1 = n1 + "3"
    elif ifsign == True:
        n2 = n2 + "3"
    lbl= Label(window, text = show, fg='white',bg = "#3d3d3d" ,width =15, height = 3 )
    lbl.place (x=0, y=0)
    lbl["font"] = font.Font(weight ="bold", size = 27)

def four():
    global show,n1,n2,sign,ifsign,old1,result
    show = show + "4"
    if ifsign == False:
        n1 = n1 + "4"
    elif ifsign == True:
        n2 = n2 + "4"
    lbl= Label(window, text = show, fg='white',bg = "#3d3d3d" ,width =15, height = 3 )
    lbl.place (x=0, y=0)
    lbl["font"] = font.Font(weight ="bold", size = 27)
def five():
    global show,n1,n2,sign,ifsign,old1,result
    show = show + "5"
    if ifsign == False:
        n1 = n1 + "5"
    elif ifsign == True:
        n2 = n2 + "5"
    lbl= Label(window, text = show, fg='white',bg = "#3d3d3d" ,width =15, height = 3 )
    lbl.place (x=0, y=0)
    lbl["font"] = font.Font(weight ="bold", size = 27)

def six():
    global show,n1,n2,sign,ifsign,old1,result
    show = show + "6"
    if ifsign == False:
        n1 = n1 + "6"
    elif ifsign == True:
        n2 = n2 + "6"
    lbl= Label(window, text = show, fg='white',bg = "#3d3d3d" ,width =15, height = 3 )
    lbl.place (x=0, y=0)
    lbl["font"] = font.Font(weight ="bold", size = 27)

def seven():
    global show,n1,n2,sign,ifsign,old1,result
    show = show + "7"
    if ifsign == False:
        n1 = n1 + "7"
    elif ifsign == True:
        n2 = n2 + "7"
    lbl= Label(window, text = show, fg='white',bg = "#3d3d3d" ,width =15, height = 3 )
    lbl.place (x=0, y=0)
    lbl["font"] = font.Font(weight ="bold", size = 27)

def eight():
    global show,n1,n2,sign,ifsign,old1,result
    show = show + "8"
    if ifsign == False:
        n1 = n1 + "8"
    elif ifsign == True:
        n2 = n2 + "8"
    lbl= Label(window, text = show, fg='white',bg = "#3d3d3d" ,width =15, height = 3 )
    lbl.place (x=0, y=0)
    lbl["font"] = font.Font(weight ="bold", size = 27)

def nine():
    global show,n1,n2,sign,ifsign,old1,result
    show = show + "9"
    if ifsign == False:
        n1 = n1 + "9"
    elif ifsign == True:
        n2 = n2 + "9"
    lbl= Label(window, text = show, fg='white',bg = "#3d3d3d" ,width =15, height = 3 )
    lbl.place (x=0, y=0)
    lbl["font"] = font.Font(weight ="bold", size = 27)

def point():
    global show,n1,n2,sign,ifsign,old1,result
    show = show + "."
    if ifsign == False:
        n1 = n1 + "."
    elif ifsign == True:
        n2 = n2 + "."
    lbl= Label(window, text = show, fg='white',bg = "#3d3d3d" ,width =15, height = 3 )
    lbl.place (x=0, y=0)
    lbl["font"] = font.Font(weight ="bold", size = 27)






# making window dimentions
window.geometry("320x400")
# making window title
window.title("My Calculator")




# creating box where result will be
lbl= Label(window, text = show, fg='white',bg = "#3d3d3d" ,width =15, height = 3 )
lbl.place (x=0, y=0)
lbl["font"] = font.Font(weight ="bold", size = 27)
# creating buttons 
##########################################################################
# addition
add = Button(window, text= " +  " , fg = "white", bg = "#DA9418", relief = "flat", command = plus)
add.pack()
add.place (x = 263, y =290)
add["font"] = myfont
# subtraction
sub = Button(window, text = "- ", fg = "white", bg = "#DA9418", width = 3, relief = "flat", command = minus)
sub.pack()
sub.place(x = 263, y = 235)
sub["font"] = myfont
# sub['font'] = font.Font(weight = "bold",size = 21)
# multiplication
mult = Button(window, text = " x  " ,fg = "white", bg = "#DA9418", relief = "flat", command = multt)
mult.pack()
mult.place(x= 263, y = 180)
mult["font"] = myfont
# divition 
divi = Button(window, text = " ÷  ", fg = "white", bg = "#DA9418", relief = "flat", command = divid)
divi.pack()
divi.place(x = 263, y = 125)
divi["font"] = myfont
# equal
equ = Button(window,text = " =  ", fg = 'white', bg = "#589F5E", relief = "flat", command = equal)
equ.pack()
equ.place(x = 263, y = 345 )
equ["font"] = myfont
# percente 
per = Button(window, text = ' % ', fg = 'black', bg = 'silver', width = 4, relief = "flat",command =  percent)
per.pack()
per.place(x = 185, y = 125)
per["font"] = myfont
# positive or negative
pos_or_neg = Button(window, text = " -/+ ", fg = "black", bg = "silver", width = 5, relief = "flat", command = posneg)
pos_or_neg.pack()
pos_or_neg.place(x = 91, y = 125)
pos_or_neg["font"] = myfont
# all to be cleared
clear = Button(window, text = " AC ", fg = "black", bg = "#C54848", width = 5, relief = "flat", command = clearr)
clear.pack()
clear.place(x = 0, y = 125)
clear["font"] = myfont
###########################################################################
# number Buttons
###########################################################################
# 0
zero = Button(window, text = " 0 ", fg = "white", bg = greyy , width = 11, relief = "flat", command = zero)
zero.pack()
zero.place(x = 0, y = 345) 
zero["font"] = myfont
# one
one = Button(window, text = " 1 ", fg = "white", bg = greyy, width = 5 , relief = "flat", command = one)
one.pack()
one.place(x = 0, y = 290)
one["font"] = myfont
# two
two = Button(window, text = " 2 ", fg = "white", bg = greyy, width = 5, relief = "flat", command = two)
two.pack()
two.place(x = 95, y = 290)
two["font"] = myfont
# three
three = Button(window, text = " 3 ", fg = "white", bg = greyy, width = 4, relief = "flat", command = three)
three.pack()
three.place(x = 185, y = 290)
three["font"] = myfont
# four
four = Button(window, text = " 4 ", fg = "white", bg = greyy, width = 5 , relief = "flat", command = four)
four.pack()
four.place(x = 0, y = 235)
four["font"] = myfont
# five 
five = Button(window, text = "5", fg = "white", bg = greyy, width = 5 , relief = "flat", command = five)
five.pack()
five.place(x = 95, y = 235)
five["font"] = myfont
# six
six = Button(window, text = " 6 ", fg = "white", bg = greyy, width = 4 , relief = "flat", command = six)
six.pack()
six.place(x = 185, y = 235)
six['font'] = myfont
# seven
seven = Button(window, text = ' 7 ', fg = "white", bg = greyy, width = 5 , relief = "flat", command = seven)
seven.pack()
seven.place(x = 0, y = 180)
seven["font"] = myfont
# eight
eight = Button(window, text = " 8 ", fg = "white", bg = greyy, width = 5 , relief = "flat", command = eight)
eight.pack()
eight.place(x = 95, y = 180)
eight["font"] = myfont

# nine
nine = Button(window, text = " 9 ", fg = "White", bg = greyy, width = 4, relief = "flat", command = nine)
nine.pack()
nine.place(x = 185, y = 180)
nine["font"] = myfont
# point
point = Button(window, text = " . ", fg = "white", bg = greyy , width = 4, relief = "flat", command = point)
point.pack()
point.place(x = 185, y = 345)
point["font"] = myfont
###########################################################################



# disable resizing in the app #################
window.resizable(False,False)######################
###############################################
window.mainloop()# making window don't close ##
###############################################