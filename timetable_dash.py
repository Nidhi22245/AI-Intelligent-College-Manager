from tkinter import* 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from register import Register
from time import strftime
from datetime import datetime
import mysql.connector
# --------------------------
from train import Train
from student import Student
from myattendance import MyAttendance
from face_recognition import Face_Recognition
from attendance import Attendance
import os
from tkinterhtml import TkinterHtml
from chatbot import ChatBot
import subprocess


class TimeTable_Dashboard:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("TimeTable Dashboard")

        # backgorund image 
        bg1=Image.open(r"C:\Users\NIDHI\OneDrive\Desktop\Face_Recognition_System\Images_GUI\bg0.jpg")
        bg1=bg1.resize((1366,768),Image.LANCZOS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=0,width=1366,height=768)


        #title section
        title_lb1 = Label(bg_img,bg='#FCFCFC')
        title_lb1.place(x=0,y=0,width=1366,height=45)

         # timetable image  
        img=Image.open(r"C:\Users\NIDHI\OneDrive\Desktop\Face_Recognition_System\Images_GUI\time_dashb.png")
        img=img.resize((700,410),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)
        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=25,y=150,width=700,height=410)
        
        #  logo  
        logo=Image.open(r"C:\Users\NIDHI\OneDrive\Desktop\Face_Recognition_System\Images_GUI\logo-color.png")
        logo=logo.resize((130,43),Image.LANCZOS)
        self.logo=ImageTk.PhotoImage(logo)

        std_b1 = Button(title_lb1,image=self.logo,cursor="hand2",bd=0)
        std_b1.place(x=6,y=3,width=130,height=43)

        # ============================Time================
        def time():
             string = strftime('%H:%M:%S %p')
             lbl.config(text = string) #fg="#104e8b",bg="#FCFCFC"
             lbl.after(1000, time)

        lbl = Label(title_lb1, font = ('Microsof YaHei UI Light',11),foreground='#104e8b',background="#FCFCFC")
        lbl.place(x=1260,y=4,width=80,height=30)
        time()        

        # student's timetable
        det_img_btn=Image.open(r"C:\Users\NIDHI\OneDrive\Desktop\Face_Recognition_System\Images_GUI\stud_time.PNG")
        det_img_btn=det_img_btn.resize((270,160),Image.LANCZOS)
        self.det_img1=ImageTk.PhotoImage(det_img_btn)

        det_b1 = Button(bg_img,command=self.time_stud,image=self.det_img1,cursor="hand2",)
        det_b1.place(x=760,y=180,width=270,height=160)


        # teacher's timetable
        att_img_btn=Image.open(r"C:\Users\NIDHI\OneDrive\Desktop\Face_Recognition_System\Images_GUI\teach_time.png")
        att_img_btn=att_img_btn.resize((270,160),Image.LANCZOS)
        self.att_img1=ImageTk.PhotoImage(att_img_btn)

        att_b1 = Button(bg_img,command=self.time_teach,image=self.att_img1,cursor="hand2",)
        att_b1.place(x=1050,y=180,width=270,height=160)


        #  Scheduling
        hlp_img_btn=Image.open(r"Images_GUI\scheduling_time.PNG")
        hlp_img_btn=hlp_img_btn.resize((270,160),Image.LANCZOS)
        self.hlp_img1=ImageTk.PhotoImage(hlp_img_btn)

        hlp_b1 = Button(bg_img,image=self.hlp_img1,cursor="hand2",command=self.time_schd)
        hlp_b1.place(x=760,y=380,width=270,height=160)



        # Subjects
        pho_img_btn=Image.open(r"Images_GUI\subjects_time.PNG")
        pho_img_btn=pho_img_btn.resize((270,160),Image.LANCZOS)
        self.pho_img1=ImageTk.PhotoImage(pho_img_btn)

        pho_b1 = Button(bg_img,command=self.time_subj,image=self.pho_img1,cursor="hand2")
        pho_b1.place(x=1050,y=380,width=270,height=160)




# ==================Funtion for Open Images Folder==================
    def open_img(self):
        os.startfile("data_img")
# ==================Functions Buttons=====================

    def time_stud(self):
         subprocess.call(["python", "timetable_stud.py"])   

    def time_teach(self):
         subprocess.call(["python", "timetable_fac.py"]) 

    def time_schd(self):
         subprocess.call(["python", "scheduler.py"]) 

    def time_subj(self):
         subprocess.call(["python", "subjects.py"])                    
    
    def open_img(self):
        os.startfile("dataset")

if __name__ == "__main__":
    root=Tk()
    obj=TimeTable_Dashboard(root)
    root.mainloop()       
