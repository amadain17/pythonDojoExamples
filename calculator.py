import time, os
from collections import OrderedDict

funcs = OrderedDict([('Add', '+'), ('Subtract', '-'), ('Multiply', '*'), ('Divide', '/')])

def calc_func(func, number1, number2):
    if func == "Divide" and number2 == 0:
        return "You can't divide by zero"
    return "%s %s %s = %s" % (number1, funcs[func], number2, eval("%s %s %s" % (float(number1), funcs[func], number2)))

def choices():
    for i, key in enumerate(funcs.keys()):
        print("\t%s. %s" % (i+1, key))

while True:
    choices()
    choice = -1
    while int(choice) not in range(1, len(funcs.keys())+1):
        choice = int(input("Choose function to apply:\n"))

    choose = list(funcs.items())[choice-1][0]

    x = [int(i) for i in input("Enter the two numbers to %s:\n" % choose).split()]
    print(calc_func(choose, x[0], x[1])) if len(x)==2 else print("TWO numbers please")
    time.sleep(5)
    _=os.system('clear')
    again=input("again(y/n)?\n")
    if again=="n" : break
    _=os.system('clear')


