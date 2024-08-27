
# calculator made by gui


from tkinter import *
import math

cal = Tk()

data = ""

#===================================================fuction=============================================================================

def get_data(value):
    global data
    data = data +  str(value)
    var.set(data) 
    

def equal_data():
    global data
    try :                       # error is coimng so no stop a program and error show in display  
        total = str(eval(data))
        var.set(total)
        data = ""
    except :
         var.set("Error")    


def clear_data ():
    global data
    data = ""  
    var.set (" ") 



def click ( ) :
    print("entry :",entry.get())
    entry.delete(len(entry.get())-1)  



def square_root ():
    global data
    try :
         data = float(data)
         data = math.sqrt(data)
         var.set(float(data))
         data = str(data)
    except :
         var.set("Error")


def sine_value():
     global data
     try :
         data = float(data)
         data = math.sin(math.radians(data))
         var.set(float(data))
         data = str(data)
     except :
             var.set("Error")


def cos_value():
     global data
     try :
         data = float(data)
         data = math.cos(math.radians(data))
         var.set(float(data))
         data = str(data)
     except :
          var.set("Error")


def tan_value():
     global data
     try  :
          data = float(data)
          data = math.tan(math.radians(data))
          var.set(float(data))
          data = str(data)
     except :
          var.set("Error")


def square_count() :
     global data
     try :
         data = float(data)
         data = math.pow(data,2)
         var.set(float(data))
         data = str(data)
     except :
          var.set("Error")


def sinh_value():
     global data
     try :
         data = float(data)
         data = math.sinh(data)
         var.set(float(data))
         data = str(data)
     except :
          var.set("Error")
     
     
def cosh_value():
     global data
     try :
         data = float(data)
         data = math.cosh(data)
         var.set(float(data))
         data = str(data)
     except :
         var.set("Error")

def tanh_value():
     global data
     try :
         data = float(data)
         data = math.tanh(data)
         var.set(float(data))
         data = str(data)
     except :
         var.set("Error")


def expo_10 ():
     global data
     try :
         data = float(data)
         data = math.pow(10,data)
         var.set(float(data))
         data = str(data)
     except :
         var.set("Error")


def log ():
     global data
     try :
         data = float(data)
         data = math.log10(data)
         var.set(float(data))
         data = str(data)
     except :
         var.set("Error")


def third_root():
    global data
    try :
         data = float(data)
         data = math.cbrt(data)
         var.set(float(data))
         data = str(data)
    except :
         var.set("Error")


#=========================================create window==============================================================================


cal.title("calculator")      # create a windows with dimension
cal.config(bg = "gray")
cal.geometry("498x670+30+30")

lable = Label(cal,text = "Calculator",font=("times of roman",30,"bold"),bg = "gray")   # create label
lable.place( x= 110,y =20,width=280,height=50)

width = 498
height = 670

sy_width = cal.winfo_screenwidth()
sy_height = cal.winfo_screenheight()

c_y = int(sy_height / 2 - height / 2)
c_x = int(sy_width /2 - width /2 )

cal.geometry(f"{width}x{height}+{c_x}+{c_y}")         # centre position of window


#===========================================entry label=====================================================================================


var = StringVar()
entry = Entry(cal,relief = "sunken",font = ("times of roman",20,"bold"),bd = 10 , textvariable = var)  #entry label with dimension
entry.place(x = 37 , y = 85 , height= 60, width = 420 )           


#===========================================create buttons================================================================================


button_7 = Button(cal,text= "7",font=("arial", 15 ,"bold"),command=lambda: get_data(7))  #create button with dimension
button_7.place(x= 40 , y = 170 , width=97 , height= 50 )    

button_8 = Button(cal,text= "8",font=("arial",15 ,"bold"),command=lambda: get_data(8))
button_8.place(x= 147 , y = 170 , width=97 , height= 50 )

button_9 = Button(cal,text= "9",font=("arial",15 ,"bold"),command=lambda: get_data(9))
button_9.place(x= 254 , y = 170 , width=97, height= 50 )

button_mul = Button(cal,text= "*",font=("arial",15 ,"bold"),bg = "Lightgreen",command=lambda: get_data("*"))
button_mul.place(x= 361 , y = 170 , width=97 , height= 50 )



button_4 = Button(cal,text= "4",font=("arial",15 ,"bold"),command=lambda: get_data(4))   # create button with dimension
button_4.place(x= 40 , y = 230 , width=97 , height= 50 )    

button_5 = Button(cal,text= "5",font=("arial",15 ,"bold"),command=lambda: get_data(5))
button_5.place(x= 147 , y = 230 , width=97 , height= 50 )

button_6 = Button(cal,text= "6",font=("arial",15 ,"bold"),command=lambda: get_data(6))
button_6.place(x= 254 , y = 230 , width=97 , height= 50 )

button_min = Button(cal,text= "-",font=("arial",15 ,"bold"),bg ="Lightgreen" ,command=lambda: get_data("-"))
button_min.place(x= 361 , y = 230 , width=97 , height= 50 )



button_1 = Button(cal,text= "1",font=("arial",15 ,"bold"),command=lambda: get_data(1))   # create button with dimension
button_1.place(x= 40 , y = 290 , width=97 , height= 50 )    

button_2 = Button(cal,text= "2",font=("arial",15,"bold"),command=lambda: get_data(2))
button_2.place(x= 147 , y = 290 , width=97 , height= 50 )

button_3 = Button(cal,text= "3",font=("arial",15 ,"bold"),command=lambda: get_data(3))
button_3.place(x= 254 , y = 290 , width=97 , height= 50 )

button_plus = Button(cal,text= "+",font=("arial",15 ,"bold"),bg = "Lightgreen",command=lambda: get_data("+"))
button_plus.place(x= 361 , y = 290 , width=97 , height= 50 )



button_0 = Button(cal,text= "0",font=("arial",15 ,"bold"),command=lambda: get_data(0))   # create button with dimension
button_0.place(x= 40 , y = 350, width= 97 , height= 50 )    

button_dot = Button(cal,text= ".",font=("arial",15 ,"bold"),command=lambda: get_data("."))
button_dot.place(x= 147 , y = 350 , width=97 , height= 50 )

button_equal = Button(cal,text= "=",font=("arial",15,"bold"),command=equal_data)
button_equal.place(x= 254 , y = 350 , width=97 , height= 50 )

button_div = Button(cal,text= "/",font=("arial",15 ,"bold"),bg = "Lightgreen",command=lambda: get_data("/"))
button_div.place(x= 361 , y = 350 , width=97 , height= 50 )



button_allclear = Button(cal,text= "AC",font=("arial",15 ,"bold"),bg ="pink",command= clear_data) # create button with dimension
button_allclear.place(x= 40 , y = 410 , width= 97 , height= 50 )    

button_clear = Button(cal,text= "C ",font=("arial",15 ,"bold"),bg ="pink",command = click )
button_clear.place(x= 147 , y = 410, width= 97 , height= 50 )

button_sqareroot = Button(cal,text="\u221A",font=("arial", 20 ,"bold"),bg = "pink", command = square_root )
button_sqareroot.place(x= 254 , y = 410 , width= 97 , height= 50 )    

button_modulo = Button(cal,text= "% ",font=("arial",15 ,"bold"),bg ="Lightgreen",command=lambda: get_data("%"))
button_modulo.place(x= 361 , y = 410, width= 97 , height= 50 )



button_pi = Button(cal,text= "\u03c0",font=("arial",15 ,"bold"),bg="light blue", command = lambda : get_data(3.14)) #create button with dimension
button_pi.place(x= 40 , y = 470 , width= 97 , height= 50 )    

button_sin = Button(cal,text= "sin\u03B8",font=("arial",15 ,"bold"),bg = "light blue",command = sine_value)
button_sin.place(x= 147 , y = 470, width= 97 , height= 50 )

button_cos = Button(cal,text= "cos\u03B8",font=("arial",15,"bold"),bg ="light blue",command = cos_value)
button_cos.place(x= 254 , y = 470 , width= 97 , height= 50 )    

button_tan = Button(cal,text= "tan\u03b8",font=("arial",15 ,"bold"),bg = "light blue",command = tan_value)
button_tan.place(x= 361 , y = 470, width= 97 , height= 50 )



button_square = Button(cal,text= "x\u00b2" ,font=("arial",15 ,"bold"),bg ="light blue",command = square_count) #create button with dimension
button_square.place(x= 40 , y = 530 , width= 97 , height= 50 )    

button_sinh = Button(cal,text= "sinh ",font=("arial",15 ,"bold"),bg = "light blue",command = sinh_value)
button_sinh.place(x= 147 , y = 530, width= 97 , height= 50 )

button_cosh = Button(cal,text= "cosh",font=("arial",15,"bold"),bg ="light blue",command = cosh_value)
button_cosh.place(x= 254 , y = 530 , width= 97 , height= 50 )    

button_tanh = Button(cal,text= "tanh",font=("arial",15 ,"bold"),bg ="light blue",command = tanh_value)
button_tanh.place(x= 361 , y = 530, width= 97 , height= 50 )



button_exponentiation = Button(cal,text= "x\u02b8",font=("arial",15 ,"bold"),bg ="light blue",command=lambda: get_data('**'))  #create button with dimension
button_exponentiation.place(x= 40 , y = 590 , width= 97 , height= 50 )

button_10exop = Button(cal,text= "10\u02e3",font=("arial",15 ,"bold"),bg = "light blue",command = expo_10 )
button_10exop.place(x= 147 , y = 590, width= 97 , height= 50 )

button_log = Button(cal,text= "log",font=("arial",15,"bold"),bg ="light blue",command = log )
button_log.place(x= 254 , y = 590 , width= 97 , height= 50 )    

button_thirdroot= Button(cal,text= "\u00B3\u221A",font=("arial",15 ,"bold"),bg ="light blue",command = third_root) 
button_thirdroot.place(x= 361 , y = 590, width= 97 , height= 50 )


#================================================main loop==================================================================================================

cal.mainloop()  



