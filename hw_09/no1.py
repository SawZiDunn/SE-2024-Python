from tkinter import *
from tkinter import messagebox

class PhoneInterface:
    def __init__(self) -> None:
        master = Tk()
        master.title = "KMITL Phone"
        self.nums = ""

        frame = Frame(master)
        frame.pack()

        self.textBox = Entry(frame, font=("Arial", 16))

        button1 = Button(frame, text="1", width=7, height=1, command=lambda: self.append("1"))
        button2 = Button(frame, text="2", width=7, height=1, command=lambda: self.append("2"))
        button3 = Button(frame, text="3", width=7, height=1, command=lambda t="3": self.append(t))
        button4 = Button(frame, text="4", width=7, height=1, command=lambda t="4": self.append(t))
        button5 = Button(frame, text="5", width=7, height=1, command=lambda t="5": self.append(t))
        button6 = Button(frame, text="6", width=7, height=1, command=lambda t="6": self.append(t))
        button7 = Button(frame, text="7", width=7, height=1, command=lambda t="7": self.append(t))
        button8 = Button(frame, text="8", width=7, height=1, command=lambda t="8": self.append(t))
        button9 = Button(frame, text="9", width=7, height=1, command=lambda t="9": self.append(t))

        button10 = Button(frame, text="*", width=7, height=1, command=lambda t="*": self.append(t))
        button11 = Button(frame, text="0", width=7, height=1, command=lambda t="0": self.append(t))
        button12 = Button(frame, text="#", width=7, height=1, command=lambda t="#": self.append(t))
        
        button13 = Button(frame, text="Talk", width=10, height=1, command=self.dial)
        button14 = Button(frame, text="<", width=10, height=1, command=self.delete)

        self.textBox.grid(row=1, column=1, columnspan=3)
        button1.grid(row=2, column=1)
        button2.grid(row=2, column=2)
        button3.grid(row=2, column=3)
        button4.grid(row=3, column=1)
        button5.grid(row=3, column=2)
        button6.grid(row=3, column=3)
        button7.grid(row=4, column=1)
        button8.grid(row=4, column=2)
        button9.grid(row=4, column=3)

        button10.grid(row=5, column=1)
        button11.grid(row=5, column=2)
        button12.grid(row=5, column=3)

        button13.grid(row=6, column=1, columnspan=2)
        button14.grid(row=6, column=2, columnspan=2)
        
        master.mainloop()

    def append(self, text):
        self.nums += text
        self.textBox.delete(0, END)
        self.textBox.insert(0, self.nums)

    def delete(self):
        self.nums = self.nums[0:-1]
        self.textBox.delete(0, END)
        self.textBox.insert(0, self.nums)

    def dial(self):
        if self.nums:
            messagebox.showinfo(message=f"Dialling {self.nums}")
        else:
            messagebox.showinfo(message="There's no number!")


PhoneInterface()

        



