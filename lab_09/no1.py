from tkinter import *

class Spinner:
    def __init__(self) -> None:
        window = Tk()
        window.title = "Spinner"
        self.count = 0

        frame = Frame(window)
        frame.pack()

        self.label = Label(frame, text=self.count, borderwidth=1, bg="white")
        self.label.pack()

        up_button = Button(frame, text="+", command=self.count_up, width=7, height=1)
       
        down_button = Button(frame, text="-", command=self.count_down, width=7, height=1)
      
        reset_button = Button(frame, text="Reset", command=self.reset, width=7, height=1)

        self.label.grid(row=2, column=1)
        up_button.grid(row=1, column=2)
        down_button.grid(row=2, column=2)
        reset_button.grid(row=3, column=2)

        window.mainloop()

    def count_up(self):
        self.count += 1

        self.label["text"] = self.count

    def count_down(self):
        self.count -= 1
        self.label["text"] = self.count

    def reset(self):
        self.count = 0
 
        self.label["text"] = self.count

Spinner()