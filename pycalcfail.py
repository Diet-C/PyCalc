import tkinter as tk

global storednum
storednum = 0
clearNextButton = False
add = False

def InsertNumber(number):
    global clearNextButton
    if clearNextButton:
        e.delete(0,'end')
    e.insert('end', number)
    clearNextButton = False
    
def Clear():
    e.delete(0,'end')
    global storednum
    storednum = 0

def Add():
    temp = e.get()
    global storednum
    storednum += int(temp)
    global clearNextButton
    clearNextButton = True
    global add
    add = True

def Subtract():
    temp = e.get()
    global storednum
    storednum -= int(temp)
    global clearNextButton
    clearNextButton = True
    global add
    add = False
    
def Enter():
    if add:
        temp = e.get()
        global storednum
        storednum += int(temp)
    else:
        temp = e.get()
        storednum -= int(temp)
    e.delete(0,'end')
    e.insert(0, storednum)
    global clearNextButton
    clearNextButton = True


root = tk.Tk()
root.title("PyCalc")
root.configure(background='gray')


e = tk.Entry(root, width=50, borderwidth=5)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

#make buttons

button1 = tk.Button(root, text='1', padx=40, pady=20, command=lambda:InsertNumber(1))
button2 = tk.Button(root, text='2', padx=40, pady=20, command=lambda:InsertNumber(2))
button3 = tk.Button(root, text='3', padx=40, pady=20, command=lambda:InsertNumber(3))
button4 = tk.Button(root, text='4', padx=40, pady=20, command=lambda:InsertNumber(4))
button5 = tk.Button(root, text='5', padx=40, pady=20, command=lambda:InsertNumber(5))
button6 = tk.Button(root, text='6', padx=40, pady=20, command=lambda:InsertNumber(6))
button7 = tk.Button(root, text='7', padx=40, pady=20, command=lambda:InsertNumber(7))
button8 = tk.Button(root, text='8', padx=40, pady=20, command=lambda:InsertNumber(8))
button9 = tk.Button(root, text='9', padx=40, pady=20, command=lambda:InsertNumber(9))
button0 = tk.Button(root, text='0', padx=87, pady=20, command=lambda:InsertNumber(0))

buttonAdd = tk.Button(root, text='+', padx=39, pady=20, command=Add)
buttonSubtract = tk.Button(root, text='-', padx=40, pady=20, command=Subtract)
buttonEnter = tk.Button(root, text='=', padx=39, pady=20, command=Enter)
buttonClear = tk.Button(root, text='Clear', padx=29, pady=20, command=Clear)

#place buttons

button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)

button0.grid(row=4, column=0, columnspan=2)

buttonAdd.grid(row=3, column=3)
buttonSubtract.grid(row=2, column=3)
buttonEnter.grid(row=4, column=3)
buttonClear.grid(row=1, column=3)



root.mainloop()

