import tkinter as tk
from matplotlib import image
import matplotlib.pyplot as plt
import numpy as np
from io import *
from PIL import * 


class Application(tk.Frame):

    def __init__(self, master = None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.entry_field = tk.Entry(self,width = 50,borderwidth=5,bg="RED")
        self.entry_field.pack()

    def create_widgets(self):
        self.Button_1 = tk.Button(self)
        self.Button_1["text"] = "Hello There\nClick"
        self.Button_1["fg"] = "RED"
        self.Button_1["command"] = self.say_hi
        self.Button_1.pack(side="top")
        self.new_button = tk.Button(self)
        self.new_button["text"] = "Enter the function"
        self.new_button["command"] = self.take_entry
        self.new_button.pack()

    def say_hi(self):
        self.myLabel = tk.Label(self,text = "Hello World")
        self.myLabel.pack(side = "top")
    
    def take_entry(self):
        self.entered_text = self.entry_field.get()
        ImageObject = StringIO()
        if self.entered_text=="sinx":
            self.canvas = tk.Canvas(self,width = 300,height = 300)
            self.canvas.pack()
            x = np.arange(0,2*np.pi,0.1)
            y = np.sin(x)
            fig_1 = plt.figure()
            plt.plot(x,y)
            ImageObject.seek(0)
            self.canvas.create_image(0,0,image = plt.show())

root = tk.Tk()
app = Application(master = root)
app.mainloop()
