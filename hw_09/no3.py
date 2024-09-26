from tkinter import *

class DrawCircle:
    def __init__(self) -> None:
        master = Tk()
        self.canvas = Canvas(master, width=700, height=400, bg="white")
        self.canvas.pack()

        self.canvas.bind("<Button-1>", self.draw_circle)
        self.canvas.bind("<Button-3>", self.remove_circle)
        master.mainloop()

    def draw_circle(self, event):
        self.canvas.create_oval(event.x - 15, event.y + 15, event.x + 15, event.y - 15, tags="circle")


    def remove_circle(self, event):
        item_to_delete = self.canvas.find_closest(event.x, event.y)
        if "circle" in self.canvas.gettags(item_to_delete):
            self.canvas.delete(item_to_delete) 
        

DrawCircle()