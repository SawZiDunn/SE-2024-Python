from tkinter import *
from tkinter import messagebox

class Spinner:
    def __init__(self) -> None:
        window = Tk()
        window.title = "Currency Converter"

        frame = Frame(window)
        frame.pack()
        self.input = DoubleVar()

        entry = Entry(frame, textvariable=self.input)
        button1 = Button(frame, text="USD -> THB", command=self.usd_to_thb)
        button2 = Button(frame, text="THB -> USD", command=self.thb_to_usd)

        entry.grid(row=1, column=1)
        button1.grid(row=2, column=1)
        button2.grid(row=3, column=1)

        window.mainloop()

    def usd_to_thb(self):
        result = self.input.get() * 30
        messagebox.showinfo("Currency Converter", f"{self.input.get()} USD = {result} THB")
        

    def thb_to_usd(self):
        result = self.input.get() / 30
        messagebox.showinfo("Currency Converter", f"{self.input.get()} THB = {result:.2f} USD")
        

Spinner()