from pickle import FRAME
from tkinter import*
from tkinter import ttk

import cv2
from train import Train
from PIL import Image,ImageTk
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from time import strftime
from datetime import datetime
import os
from tkinterhtml import TkinterHtml
from chatbot import ChatBot  
from timetable_dash import TimeTable_Dashboard
from notice import Notice
import subprocess


class Face_Recognition_System:
    def __init__(self,root):
            self.root = root
            self.root.geometry("1366x768+0+0")
            self.root.title("Intelligent College Manager")
            self.root.configure(bg="#F0F8FF")
           



            
            # background image 
            bg1 = Image.open(r"C:\Users\NIDHI\OneDrive\Desktop\Face_Recognition_System\Images_GUI\bg0.jpg")
            bg1=bg1.resize((1360,768),Image.LANCZOS)
            self.photobg1 = ImageTk.PhotoImage(bg1)

            # set image is label
            bg_img = Label(self.root,image=self.photobg1)
            bg_img.place(x=0,y=0,width=1360,height=768)
            # title section
            title_lb1 = Label(bg_img,bg="#FCFCFC",fg="black")
            title_lb1.place(x=0,y=0,width=1366,height=44)


             # main page video
            video_source_college = r"Images_GUI\icmvideo.mp4"
            video_player_college = VideoPlayer(self.root, video_source_college, window_size=(1163, 350), position=(100, 53))
            # video_player_college.place(x=85,y=50,width=1220,height=350)
            
            
           #  logo  
            logo=Image.open(r"C:\Users\NIDHI\OneDrive\Desktop\Face_Recognition_System\Images_GUI\logo-color.png")
            logo=logo.resize((150,43),Image.LANCZOS)
            self.logo=ImageTk.PhotoImage(logo)

            std_b1 = Button(title_lb1,image=self.logo,cursor="hand2",bd=0)
            std_b1.place(x=6,y=1,width=150,height=43)

            # ===============Time===========
            def time():
                string = strftime('%H:%M:%S %p')
                lbl.config(text = string)
                lbl.after(1000, time)

            lbl = Label(title_lb1, font = ('times new roman',11),background='#FCFCFC',foreground='black')
            lbl.place(x=1260,y=4,width=80,height=30)
            time()    

           
           
            # sudent button 88888888888888888888888888888888888
            std_img_btn=Image.open(r"C:\Users\NIDHI\OneDrive\Desktop\Face_Recognition_System\Images_GUI\student_test.PNG")
            std_img_btn=std_img_btn.resize((265,125),Image.LANCZOS)
            self.std_img1=ImageTk.PhotoImage(std_img_btn)

            std_b1 = Button(bg_img,command=self.student_pannels,image=self.std_img1,cursor="hand2",bd=0)
            std_b1.place(x=100,y=410,width=265,height=125)

          

            # Detect Face  button 2
            det_img_btn=Image.open(r"C:\Users\NIDHI\OneDrive\Desktop\Face_Recognition_System\Images_GUI\face_test.png")
            det_img_btn=det_img_btn.resize((265,125),Image.LANCZOS)
            self.det_img1=ImageTk.PhotoImage(det_img_btn)

            det_b1 = Button(bg_img,command=self.face_rec,image=self.det_img1,cursor="hand2",bd=0)
            det_b1.place(x=400,y=410,width=265,height=125)

           

            # Attendance System  button 3
            att_img_btn=Image.open(r"C:\Users\NIDHI\OneDrive\Desktop\Face_Recognition_System\Images_GUI\attend_test.PNG")
            att_img_btn=att_img_btn.resize((265,125),Image.LANCZOS)
            self.att_img1=ImageTk.PhotoImage(att_img_btn)

            att_b1 = Button(bg_img,command=self.attendance_pannel,image=self.att_img1,cursor="hand2",bd=0)
            att_b1.place(x=700,y=410,width=265,height=125)

      
            #  Notice  button 4
            hlp_img_btn=Image.open(r"C:\Users\NIDHI\OneDrive\Desktop\Face_Recognition_System\Images_GUI\notice_test.png")
            hlp_img_btn=hlp_img_btn.resize((265,125),Image.LANCZOS)
            self.hlp_img1=ImageTk.PhotoImage(hlp_img_btn)

            hlp_b1 = Button(bg_img,image=self.hlp_img1,command=self.notice,cursor="hand2",bd=0)
            hlp_b1.place(x=1000,y=410,width=265,height=125)


            # Above 4 butons end
            # ---------------------------------------------------------------------------------------------------------------------------
            # Start below butons
            #  Train   button 5
            tra_img_btn=Image.open(r"C:\Users\NIDHI\OneDrive\Desktop\Face_Recognition_System\Images_GUI\train_test.png")
            tra_img_btn=tra_img_btn.resize((265,125),Image.LANCZOS)
            self.tra_img1=ImageTk.PhotoImage(tra_img_btn)

            tra_b1 = Button(bg_img,command=self.train_pannels,image=self.tra_img1,cursor="hand2",bd=0)
            tra_b1.place(x=100,y=548,width=265,height=125)


            # timetable   button 6
            pho_img_btn=Image.open(r"C:\Users\NIDHI\OneDrive\Desktop\Face_Recognition_System\Images_GUI\time_test.png")
            pho_img_btn=pho_img_btn.resize((265,125),Image.LANCZOS)
            self.pho_img1=ImageTk.PhotoImage(pho_img_btn)

            pho_b1 = Button(bg_img,command=self.timetable,image=self.pho_img1,cursor="hand2",bd=0)
            pho_b1.place(x=400,y=548,width=265,height=125)
            
            # chatbot button 7
            dev_img_btn = Image.open(r"C:\Users\NIDHI\OneDrive\Desktop\Face_Recognition_System\Images_GUI\chat_test.png")
            dev_img_btn = dev_img_btn.resize((265,125), Image.LANCZOS)
            self.dev_img1 = ImageTk.PhotoImage(dev_img_btn)

            dev_b1 = Button(bg_img, command=self.chatbot, image=self.dev_img1, cursor="hand2",bd=0)
            dev_b1.place(x=700, y=548, width=265, height=125)
        
            # teacher   button 8
            exi_img_btn=Image.open(r"C:\Users\NIDHI\OneDrive\Desktop\Face_Recognition_System\Images_GUI\teacher_test.png")
            exi_img_btn=exi_img_btn.resize((265,125),Image.LANCZOS)
            self.exi_img1=ImageTk.PhotoImage(exi_img_btn)

            exi_b1 = Button(bg_img, command=self.teacher,image=self.exi_img1,cursor="hand2",bd=0)
            exi_b1.place(x=1000,y=548,width=265,height=125)


# ==================Funtion for Open Images Folder==================
    def open_img(self):
        os.startfile("dataset")

    def iExit(self):
        self.iExit=ttk.messagebox.askyesno("Face Recogition","Are you sure you  want to exit?",parent=self.root) 
        if self.iExit>0:
            exit.root.destroy()  
        else:
            return  

      

     


# ==================Functions Buttons=====================
    def student_pannels(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    
    # def run_program(self):
    #      subprocess.call(["python", "timetable_fac.py"])    

    def train_pannels(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def timetable(self):
        self.new_window=Toplevel(self.root)
        self.app=TimeTable_Dashboard(self.new_window)     
    
    def face_rec(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
    
    def attendance_pannel(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def teacher(self):
         subprocess.call(["python", "teacher.py"])  

    def chatbot(self):
        self.new_window = Toplevel(self.root) 
        self.app=ChatBot(self.new_window)  

    def notice(self):
        self.new_window = Toplevel(self.root) 
        self.app=Notice(self.new_window)      

    # def logout(n):
    #     f8=Frame(bg="pink")
    #     f8.pack()
    #     n.add(f8,text="Logout")    

    def Close(self):
        root.destroy()

class VideoPlayer:
    def __init__(self, parent_frame, video_source, window_size=(400, 300), position=(800, 50)):
        self.parent_frame = parent_frame
        self.video_source = video_source
        self.window_size = window_size
        self.position = position

        self.vid = cv2.VideoCapture(self.video_source)

        self.canvas = Canvas(self.parent_frame, width=window_size[0], height=window_size[1])
        self.canvas.place(x=position[0], y=position[1])

        self.update()

    def update(self):
        ret, frame = self.vid.read()

        if ret:
            self.photo = self.convert_to_photo(frame)
            self.canvas.create_image(0, 0, anchor=NW, image=self.photo)

        self.parent_frame.after(10, self.update)

    def convert_to_photo(self, frame):
        rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        pil_image = Image.fromarray(rgb_image)
        resized_image = pil_image.resize((self.canvas.winfo_width(), self.canvas.winfo_height()), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image=resized_image)
        return photo

    def release(self):
        self.vid.release()
        self.canvas.destroy()


if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()
