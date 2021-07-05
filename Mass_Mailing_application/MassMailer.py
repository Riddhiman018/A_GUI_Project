import tkinter as tk
from tkinter import filedialog
import sys
import smtplib
import ssl

recipient_list = []
#Just a comment

class First_Frame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack(side = "top",anchor = 'n')
        self.Entry_Plan = tk.Entry(self,width = 50,borderwidth=5)
        self.Entry_Plan.pack(side = "top")
        self.create_widgets()
    
    def create_widgets(self):
        self.First_Label = tk.Label(self,text = "Welcome To mass mailer\nHere u can send plain text mails in mass")
        self.First_Label.pack()
        self.Second_Label = tk.Label(self, text = "It is recommended that a seperate email ID is created for mass mailing.\nCurrently we support gmail accs. only")
        self.Second_Label.pack()
        self.ThirdLabel = tk.Label(self, text="Upload Recipient list in a text file\nEnsure app access is enabled in your email HOST(gmail)")
        self.ThirdLabel.pack()
        self.Upload_Recipient_list = tk.Button(self)
        self.Upload_Recipient_list['text'] = "Upload File"
        self.Upload_Recipient_list['command'] = self.File_Upload_and_mail
        self.Upload_Recipient_list.pack(side = "bottom")

    def File_Upload_and_mail(self):   
        f = filedialog.askopenfilename()
        with open(f,'r') as File:
            global recipient_list
            recipient_list = File.readlines()
        File.close()
        self.NewLabel = tk.Label(self)
        for i in recipient_list:
            self.NewLabel['text'] = i
            self.NewLabel.pack(side = "bottom",anchor = 'sw')
        self.ContinueLabel = tk.Label(self)
        self.ContinueLabel['text'] = "Send Mail?"
        self.Yes_Button = tk.Button(self)
        self.Yes_Button['text'] = "Yes"        
        self.Yes_Button['command'] = self.sendmail
        self.NoButton = tk.Button(self)
        self.NoButton['text'] = "Quit"
        self.NoButton['command'] = self.quit_c
        self.Yes_Button.pack()
        self.NoButton.pack()

    def quit_c(self):
        sys.exit()
    def sendmail(self):
        text = self.Entry_Plan.get()
        port = 465
        create_ssl = ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com',port,context=create_ssl) as server:
            server.login('yorb99test@gmail.com','Hello123!@#')
            server.sendmail('yorb99test@gmail.com',recipient_list,text)
            server.quit()

root = tk.Tk()
app = First_Frame(master=root)
app.mainloop()
