from Tkinter import *
from logic import Calculator


class CalculatorButton:
    def __init__(self, parent, value):
        self.value = value
        button = Button(parent, text="%d" % value, command=self.add_digit)

    def add_digit(self):



class App:
    def __init__(self, parent):
        self.calculator = Calculator()
        window = PanedWindow(orient=VERTICAL)
        window.pack(fill=BOTH, expand=10)
        self.display = Label(window, text="0", justify=RIGHT)
        window.add(display)

        bottom = PanedWindow(orient=VERTICAL)
        zero = Button(bottom, text="0", command=add_digit(0))
        one = Button(bottom, text="1", command=add_digit(0))
        two = Button(bottom, text="2", command=add_digit(0))
        three = Button(bottom, text="3", command=add_digit(0))
        four = Button(bottom, text="4", command=add_digit(0))
        five = Button(bottom, text="5", command=add_digit(0))
        six = Button(bottom, text="6", command=add_digit(0))
        seven = Button(bottom, text="7", command=add_digit(0))
        eight = Button(bottom, text="8", command=add_digit(0))
        nine = Button(bottom, text="9", command=add_digit(0))

        bottom.pack(fill=BOTH, expand=1)
        bottom.add(zero)
        bottom.add(one)
        bottom.add(two)
        bottom.add(three)
        bottom.add(four)
        bottom.add(five)
        bottom.add(six)
        bottom.add(seven)
        bottom.add(eight)
        bottom.add(nine)

        window.add(bottom)

    def add_digit(self, digit):
        self.calculator


root = Tk()
app = App(root)
root.mainloop()
