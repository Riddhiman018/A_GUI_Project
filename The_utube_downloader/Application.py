import smtplib
import tkinter as tk
from tkinter.messagebox import *
from tkinter.constants import LEFT, RIGHT
from matplotlib.pyplot import connect, grid
from pytube import YouTube
import random
import math
from smtplib import SMTP_SSL
import ssl
import email.utils
import email
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

class Second_App(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.master = master
        self.pack(side = "bottom")
        self.OTP_Verify()
    
    def OTP_Verify(self):
        self.New_Label = tk.Label(self,text = "Click on button to generate OTP")
        self.New_Label.pack()
        self.Gen_OTP = tk.Button(self)
        self.Gen_OTP["text"] = "Generate"
        self.Gen_OTP["command"] = self.send_mail        
        self.Gen_OTP.pack(side = "bottom",anchor="s")

    def send_mail(self):
        port = 465  #secure ssl port
        create_server_link = ssl.create_default_context()
        message = "Hello"

        with SMTP_SSL('smtp.gmail.com',port,context=create_server_link) as server: #started an smtp server
            server.login("yorb99test@gmail.com","Hello123!@#")
            server.sendmail("yorb99test@gmail.com","shubro18@gmail.com",message)
            self.MyLabel = tk.Label(self, text="Sent Check Mail")
            self.MyLabel.pack(side="bottom")
            server.quit()


root = tk.Tk()
app = My_Application(master=root)
app2 = Second_App(master=root)
root.mainloop()