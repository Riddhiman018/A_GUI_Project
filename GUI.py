import tkinter as tk

class Application(tk.Frame):

    def __init__(self, master = None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.Button_1 = tk.Button(self)
        self.Button_1["text"] = "Hello There\nClick"
        self.Button_1["fg"] = "RED"
        self.Button_1["command"] = self.say_hi
        self.Button_1.pack(side="top")
        self.Button_1.pack(side="bottom")

    def say_hi(self):
        myLabel = tk.Label(self,text = "Hello World")
        myLabel.pack(side = "top")

root = tk.Tk()
app = Application(master = root)
app.mainloop()
