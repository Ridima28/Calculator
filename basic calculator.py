from tkinter import *
window = Tk()
window.title("Calculator")
window.geometry("500x900")
icon = PhotoImage(file = "logo.png")
window.config(background = "black")
window.iconphoto(True, icon) 

def button_press(num):
    
    global equation
    equation += str(num)
    text_label.set(equation)

def equals():
    try:
        global equation
        total = str(eval(equation))
        text_label.set(total)
    except SyntaxError:
        text_label.set("Syntax Error")
        equation = ""
    except ZeroDivisionError:
        text_label.set("Arithematic Error")
        equation = ""
 
def clear():
    global equation 
    equation = ""
    text_label.set("") 

def backspace():
    global equation
    equation = equation[:-1]
    text_label.set(equation)


equation = "" 
text_label = StringVar()
label = Label(window, textvariable = text_label,
              bg = "black",
              fg= "white",
              height = 6, 
              width = 650,
              font = ("Arial", 40, "bold"),
              anchor = "e",
              justify = "right",
              
              )
label.pack(padx = 10)

frame = Frame(window)
frame.pack()

clear_button = Button(frame, text = "AC", bd= 0, font = 35, bg= "grey", fg = "white", height=4, width = 9,
                 command = clear)
clear_button.grid(row = 0, column= 0)
buttonbp = Button(frame, text = "BP", bd= 0, font = 35, bg= "grey", fg = "white", height=4, width = 9,
                 command = backspace)
buttonbp.grid(row = 0, column= 1)

division_button = Button(frame, text = "/", bd= 0, font = 35, bg= "grey", fg = "white", height=4, width = 9,
                 command = lambda: button_press("/"))
division_button.grid(row = 0, column= 2)

multiply_button = Button(frame, text = "x", bd= 0, font = 35, bg= "grey", fg = "white", height=4, width = 9,
                 command = lambda: button_press("x"))
multiply_button.grid(row = 0, column= 3)
add_button = Button(frame, text = "+", bd= 0, font = 35, bg= "grey", fg = "white", height=4, width = 9,
                 command = lambda: button_press("+"))
add_button.grid(row = 1, column= 3)
minus_button = Button(frame, text = "-", bd= 0, font = 35, bg= "grey", fg = "white", height=4, width = 9,
                 command = lambda: button_press("-"))
minus_button.grid(row = 2, column= 3)
button1 = Button(frame, text = "1", bd= 0, font = 35, bg= "grey", fg = "white", height=4, width = 9,
                 command = lambda: button_press("1"))
button1.grid(row = 1, column= 0)
button2 = Button(frame, text = "2", bd= 0, font = 35, bg= "grey", fg = "white", height=4, width = 9,
                 command = lambda: button_press("2"))
button2.grid(row = 1, column= 1)
button3 = Button(frame, text = "3", bd= 0, font = 35, bg= "grey", fg = "white", height=4, width = 9,
                 command = lambda: button_press("3"))
button3.grid(row = 1, column= 2)

button4 = Button(frame, text = "4", bd= 0, font = 35, bg= "grey", fg = "white", height=4, width = 9,
                 command = lambda: button_press("4"))
button4.grid(row = 2, column= 0)
button5 = Button(frame, text = "5", bd= 0, font = 35, bg= "grey", fg = "white", height=4, width = 9,
                 command = lambda: button_press("5"))
button5.grid(row = 2, column= 1)
button6 = Button(frame, text = "6", bd= 0, font = 35, bg= "grey", fg = "white", height=4, width = 9,
                 command = lambda: button_press("6"))
button6.grid(row = 2, column= 2)

button7 = Button(frame, text = "7", bd= 0, font = 35, bg= "grey", fg = "white", height=4, width = 9,
                 command = lambda: button_press("7"))
button7.grid(row = 3, column= 0)
button8 = Button(frame, text = "8", bd= 0, font = 35, bg= "grey", fg = "white", height=4, width = 9,
                 command = lambda: button_press("8"))
button8.grid(row = 3, column= 1)
button9 = Button(frame, text = "9", bd= 0, font = 35, bg= "grey", fg = "white", height=4, width = 9,
                 command = lambda: button_press("9"))
button9.grid(row = 3, column= 2)


button0 = Button(frame, text = "0", bd= 0, font = 35, bg= "grey", fg = "white", height=4, width = 9,
                 command = lambda: button_press("0"))
button0.grid(row = 4, column= 0)
button00 = Button(frame, text = "00", bd= 0, font = 35, bg= "grey", fg = "white", height=4, width = 9,
                 command = lambda: button_press("00"))
button00.grid(row = 4, column= 1)
buttondot =  Button(frame, text = ".", bd= 0, font = 35, bg= "grey", fg = "white", height=4, width = 9,
                 command = lambda: button_press("."))
buttondot.grid(row = 4, column= 2)



equal_button = Button(frame, text = "=", bd= 0, font = 35, bg= "orange", fg = "white", height=4, width = 9, border = 0,
                 command = equals)

equal_button.grid(row = 3, column= 3, rowspan= 4, sticky= N+S+E+W)



























window.mainloop()