import sys
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from register import Register
import mysql.connector
from train import Train 
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
import os
from tkinterhtml import TkinterHtml
from main import Face_Recognition_System as fr
from teacher_dash import Teacher_dash as tr
from studentDashboard import Student_Dashboard as sd

# https://stackoverflow.com/questions/31836104/pyinstaller-and-onefile-how-to-include-an-image-in-the-exe-file
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1190x600+120+65")
        self.root.configure(bg="#F0F8FF")
        self.root.resizable(FALSE,FALSE)

        # # window transparency
        # self.root.attributes("-alpha", 0.9)
        
        self.var_ssq=StringVar()
        self.var_sa=StringVar()
        self.var_pwd=StringVar()

        Frame(width=900,height=475,bg='white',bd=5).place(x=150,y=70)

       
        bg=Image.open(resource_path(r"Images_GUI\login.jpg"))
        bg=bg.resize((550,450),Image.LANCZOS)
        self.photobg1=ImageTk.PhotoImage(bg)

        # side image 
        bg_imgg = Label(self.root,image=self.photobg1)
        bg_imgg.place(x=160,y=80,width=550,height=450)


        
        framee = Frame(self.root,bg="white",bd=5)
        framee.place(x=700,y=80,width=340,height=450)

        # logo
        img1 = Image.open(resource_path(r"Images_GUI\logo-color.png"))
        img1=img1.resize((200,100),Image.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        labelimg = Label(image=self.photoimage1 )
        labelimg.place(x=775,y=90, width=200,height=100)

        
        username =lb1= Label(framee,text="Username:",font=("Microsof YaHei UI Light",11),fg="#104e8b",bg="white")
        username.place(x=30,y=160)

        
        self.txtuser=ttk.Entry(framee,width=25,font=("Microsof YaHei UI Light",12),foreground="#104e8b")
        self.txtuser.place(x=33,y=190,width=270)


       
        pwd =lb1= Label(framee,text="Password:",font=("Microsof YaHei UI Light",11),fg="#104e8b",bg="white" )
        pwd.place(x=30,y=230)

        
        self.txtpwd=ttk.Entry(framee,width=25,font=("Microsof YaHei UI Light",12),show="*",foreground="#104e8b")
        self.txtpwd.place(x=33,y=260,width=270)


        
        loginbtn=Button(framee,command=self.login,text="Sign in",font=("Microsof YaHei UI Light",14),bg="#104e8b",bd=2,relief=RIDGE,fg="white" ,activeforeground="black",activebackground="white")
        loginbtn.place(x=33,y=320,width=270,height=35)
    
    def reg(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)


    def login(self):
        if (self.txtuser.get()=="" or self.txtpwd.get()==""):
            messagebox.showerror("Error","All Field Required!")
        elif(self.txtuser.get()=="admin" and self.txtpwd.get()=="123"):
                open_min=messagebox.askyesno("YesNo","Are you Accessing as Admin ?")
                if open_min>0:
                    self.new_window=Toplevel(self.root)
                    self.app=fr(self.new_window)
                else:
                    if not open_min:
                        # student portal here
                        return
        elif(self.txtuser.get()=="meghna bapat" and self.txtpwd.get()=="123"):
                open_min=messagebox.askyesno("YesNo","Are you Accessing as Teacher ?")
                if open_min>0:
                    self.new_window=Toplevel(self.root)
                    self.app=tr(self.new_window)
                else:
                    if not open_min:
                        # student portal here
                        return            
        
        else:
            # =======================================================
            conn = mysql.connector.connect(username='root', password='',host='localhost',database='face_recognition',port=3306)
            mycursor = conn.cursor()
            mycursor.execute("select * from student where email=%s and DOB=%s",(
                self.txtuser.get(),
                self.txtpwd.get()
            ))
            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username and Password!")
            else:
                    messagebox.showinfo("Sussessful","Welcome to Intelligent College Manager - Student")
                    self.new_window=Toplevel(self.root)
                    self.app=sd(self.new_window)
            
            conn.commit()
            conn.close()

# reset password
# forget_password
            

''' main function was here
   face recognition:
             studentDashboard:
                 some buttons functions'''

# main function was here


if __name__ == "__main__":
    root = Tk()
    app = Login(root)
    root.mainloop()