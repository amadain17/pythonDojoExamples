import tkinter as tk
from tkinter import ttk
from functools import partial
from collections import OrderedDict
import operator as op

funcs = OrderedDict([('Add', (op.add, '+')),
                     ('Subtract', (op.sub, '-')),
                     ('Multiply', (op.mul, '*')),
                     ('Divide', (op.truediv, '/')),
                     ('Power', (op.pow, '**'))])

def call_result(label_result, n1, n2, operation):
    num1 = (n1.get())
    num2 = (n2.get())
    op = (operation.get())
    result = funcs[op][0](float(num1), float(num2))
    output_opertaion = "%s %s %s" % (num1, funcs[op][1], num2)
    if int(result) == result and isinstance(result, float): result = int(result)
    label_result.config(text="\n\n%s = %s" % (output_opertaion, result), font=("Arial", 14, "italic"), anchor="center")
    return

root = tk.Tk()
root.geometry('500x200+100+200')
root.title('Rathdrum Dojo Calculator')
gui_style = ttk.Style()
gui_style.theme_use('clam')

frm = ttk.Frame(root, style='My.TFrame')
frm.pack(expand=True, fill='both')

number1 = tk.StringVar()
number2 = tk.StringVar()

labelTitle = ttk.Label(frm, text="Enter 2 numbers & select operation:").grid(row=0, column=2)
labelNum1 = ttk.Label(frm, text="1st number", width=15).grid(row=1, column=0, sticky='W')
entryNum1 = ttk.Entry(frm, textvariable=number1).grid(row=1, column=2)
labelNum2 = ttk.Label(frm, text="2nd number", width=15).grid(row=2, column=0, sticky='W')
entryNum2 = ttk.Entry(frm, textvariable=number2).grid(row=2, column=2)
labelNum3 = ttk.Label(frm, text="Operation", width=15).grid(row=3, column=0, sticky='W')
entryNum3 = ttk.Combobox(frm, values=list(funcs.keys()), width=18)
entryNum3.grid(row=3, column=2)
entryNum3.current(0)


labelResult = ttk.Label(frm)
labelResult.grid(row=5, columnspan=3)

call_result = partial(call_result, labelResult, number1, number2, entryNum3)
buttonCal = ttk.Button(frm, text="Calculate", command=call_result).grid(row=4, column=2)
root.mainloop()