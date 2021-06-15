import sys
import tkinter as tk
from tkinter.constants import END
from matplotlib import image
import matplotlib.pyplot as plt
import numpy as np
from io import *
from tkinter.messagebox import * 


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
        self.new_button = tk.Button(self)
        self.new_button["text"] = "Enter the function"
        self.new_button["command"] = self.take_entry
        self.new_button.pack()
        self.entry_field = tk.Entry(self,width = 50,borderwidth=5, bg="GREEN")
        self.entry_field.pack()
        self.range_label = tk.Label(self, text = "Enter the end Value")
        self.range_label.pack()
        self.entry_field_end_value = tk.Entry(self,width = 50,borderwidth=5, bg="GREEN")
        self.entry_field_end_value.pack()
        self.quit_button = tk.Button(self)
        self.quit_button["text"] = "Quit"
        self.quit_button["command"] = self.quit_function
        self.quit_button.pack(side="bottom")

    def quit_function(self):
        self.LABEL_1 = tk.Label(text="Quitting the program")
        self.LABEL_1.pack()
        sys.exit()

    def say_hi(self):
        self.myLabel = tk.Label(self)
        self.myLabel["text"] = "Enter the Function and the end value\nfor example, end value = 4 means\n range is 0 to 4pi\nThen Click on the enter Function button\n after u r click\n quit"
        self.myLabel.pack()
        self.myLabel.pack(side = "top")
    
    def take_entry(self):

        self.entered_text = self.entry_field.get()
        self.range_value = int(self.entry_field_end_value.get())
        if self.entered_text=="sinx":
            x = np.arange(0,self.range_value*np.pi,0.1)
            y = np.sin(x)
            plt.plot(x,y)
            plt.show()
            self.entry_field.delete(0,END)
            self.entry_field_end_value.delete(0,END)

        elif self.entered_text == "cosx":
            x = np.arange(0,self.range_value*np.pi,0.1)
            y = np.cos(x)
            plt.plot(x,y)
            plt.show()
            self.entry_field.delete(0,END)
            self.entry_field_end_value.delete(0,END)
        
        else:
            showerror("Error","Function under development")


root = tk.Tk()
app = Application(master = root)
app.mainloop()
