import tkinter as tk
from tkinter.constants import LEFT, RIGHT
from matplotlib.pyplot import grid
from pytube import YouTube
import sys


class My_Application(tk.Frame):
    def __init__(self,master = None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.entry_field = tk.Entry(self, width=50,borderwidth=5)
        self.entry_field.pack(side = "top")
        self.Enter_widget()

    def Enter_widget(self):
        self.Enter_button = tk.Button(self)
        self.Enter_button["text"] = "Enter link and click"
        self.Enter_button["command"] = self.generate_title
        self.Enter_button.pack(side = "bottom")


    def generate_title(self):
        global text
        text = self.entry_field.get()
        yt = YouTube(text)
        self.new_Label = tk.Label(self, text = yt.title)
        self.new_Label.pack(side = "bottom")
        self.create_yes_no_button()

    def create_yes_no_button(self):
        self.yes_button = tk.Button(self)
        self.yes_button["text"] = "YES"
        self.yes_button["command"] = self.download_video
        self.yes_button.pack(side = LEFT)
        self.no_button = tk.Button(self, text = "NO")
        self.no_button["command"] = self.quit_func
        self.no_button.pack(side=RIGHT)

    def quit_func(self):
        sys.exit()
    
    def download_video(self):
        yt2 = YouTube(text)
        yt2.streams.filter(progressive=True)
        stream = yt2.streams.get_by_resolution("720p")
        stream.download(output_path=r"C:\Users\Riddhiman\Desktop")


root = tk.Tk()
app = My_Application(master=root)
app.mainloop()