import re
from sys import path
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import os
import mysql.connector
import cv2
import numpy as np
from tkinter import messagebox
from time import strftime
from datetime import datetime
import csv
from tkinter import filedialog

mydata=[]
class Attendance:
    
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Attendance Pannel")

        #-----------Variables-------------------
        self.var_id=StringVar()
        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_dep=StringVar()
        self.var_time=StringVar()
        self.var_date=StringVar()
        self.var_attend=StringVar()


        # backgorund image 
        bg1=Image.open(r"Images_GUI\bg0.jpg")
        bg1=bg1.resize((1366,768),Image.LANCZOS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=0,width=1366,height=768)


        #title section
        title_lb1 = Label(bg_img,bg='#FCFCFC')
        title_lb1.place(x=0,y=0,width=1366,height=45)

        #  logo  
        logo=Image.open(r"C:\Users\NIDHI\OneDrive\Desktop\Face_Recognition_System\Images_GUI\logo-color.png")
        logo=logo.resize((145,43),Image.LANCZOS)
        self.logo=ImageTk.PhotoImage(logo)

        std_b1 = Button(title_lb1,image=self.logo,cursor="hand2",bd=0)
        std_b1.place(x=6,y=2,width=145,height=43)


            # ============================Time================
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000, time)

        lbl = Label(title_lb1, font = ('times new roman',11),foreground='#104e8b',background='#FCFCFC')
        lbl.place(x=1260,y=4,width=80,height=30)
        time()           

        #========================Section Creating==================================

        # Creating Frame 
        main_frame = Frame(bg_img,bd=1 ,bg="#FCFCFC") #bd mean border 
        main_frame.place(x=250,y=60,width=700,height=650)

        # Left Label Frame 
        left_frame = LabelFrame(main_frame,bd=1 ,relief=RIDGE,font=("Microsof YaHei UI Light",12) ,fg="#104e8b",bg="#FCFCFC")
        left_frame.place(x=20,y=30,width=660,height=600)

        

        # ==================================Text boxes and Combo Boxes====================

        #Student id
        studentId_label = Label(left_frame,text="Std-ID:",font=("Microsof YaHei UI Light",12) ,fg="#104e8b",bg="#FCFCFC")
        studentId_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)

        studentId_entry = ttk.Entry(left_frame,textvariable=self.var_id,foreground="#104e8b",width=15,font=("Microsof YaHei UI Light",12))
        studentId_entry.grid(row=0,column=1,padx=5,pady=5,sticky=W)

        #Student Roll
        student_roll_label = Label(left_frame,text="Roll.No:",font=("Microsof YaHei UI Light",12) ,fg="#104e8b",bg="#FCFCFC")
        student_roll_label.grid(row=0,column=2,padx=5,pady=5,sticky=W)

        student_roll_entry = ttk.Entry(left_frame,textvariable=self.var_roll,foreground="#104e8b",width=15,font=("Microsof YaHei UI Light",12))
        student_roll_entry.grid(row=0,column=3,padx=5,pady=5,sticky=W)

        #Studnet Name
        student_name_label = Label(left_frame,text="Std-Name:",font=("Microsof YaHei UI Light",12) ,fg="#104e8b",bg="#FCFCFC")
        student_name_label.grid(row=1,column=0,padx=5,pady=5,sticky=W)

        student_name_entry = ttk.Entry(left_frame,textvariable=self.var_name,foreground="#104e8b",width=15,font=("Microsof YaHei UI Light",12))
        student_name_entry.grid(row=1,column=1,padx=5,pady=5,sticky=W)

        #time
        time_label = Label(left_frame,text="Time:",font=("Microsof YaHei UI Light",12) ,fg="#104e8b",bg="#FCFCFC" )
        time_label.grid(row=1,column=2,padx=5,pady=5,sticky=W)

        time_entry = ttk.Entry(left_frame,textvariable=self.var_time,width=15,foreground="#104e8b",font=("Microsof YaHei UI Light",12))
        time_entry.grid(row=1,column=3,padx=5,pady=5,sticky=W)

        #Date 
        date_label = Label(left_frame,text="Date:",font=("Microsof YaHei UI Light",12) ,fg="#104e8b",bg="#FCFCFC" )
        date_label.grid(row=2,column=0,padx=5,pady=5,sticky=W)

        date_entry = ttk.Entry(left_frame,textvariable=self.var_date,width=15,foreground="#104e8b",font=("Microsof YaHei UI Light",12))
        date_entry.grid(row=2,column=1,padx=5,pady=5,sticky=W)

        #Attendance
        student_attend_label = Label(left_frame,text="Attend-status:",font=("Microsof YaHei UI Light",12) ,fg="#104e8b",bg="#FCFCFC" )
        student_attend_label.grid(row=2,column=2,padx=5,pady=5,sticky=W)

        attend_combo=ttk.Combobox(left_frame,textvariable=self.var_attend,width=13,foreground="#104e8b",font=("Microsof YaHei UI Light",12),state="readonly")
        attend_combo["values"]=("Status","Present","Absent")
        attend_combo.current(0)
        attend_combo.grid(row=2,column=3,padx=5,pady=5,sticky=W)

        # ===============================Table Sql Data View==========================
        table_frame = Frame(left_frame,bd=1 ,relief=RIDGE)
        table_frame.place(x=10,y=120,width=635,height=399)

        #scroll bar 
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        #create table 
        self.attendanceReport_left = ttk.Treeview(table_frame,column=("ID","Roll_No","Name","Time","Date","Attend"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.attendanceReport_left.xview)
        scroll_y.config(command=self.attendanceReport_left.yview)

        self.attendanceReport_left.heading("ID",text="Std-ID")
        self.attendanceReport_left.heading("Roll_No",text="Roll.No")
        self.attendanceReport_left.heading("Name",text="Std-Name")
        self.attendanceReport_left.heading("Time",text="Time")
        self.attendanceReport_left.heading("Date",text="Date")
        self.attendanceReport_left.heading("Attend",text="Attend-status")
        self.attendanceReport_left["show"]="headings"


        # Set Width of Colums 
        self.attendanceReport_left.column("ID",width=100)
        self.attendanceReport_left.column("Roll_No",width=100)
        self.attendanceReport_left.column("Name",width=100)
        self.attendanceReport_left.column("Time",width=100)
        self.attendanceReport_left.column("Date",width=100)
        self.attendanceReport_left.column("Attend",width=100)
        
        self.attendanceReport_left.pack(fill=BOTH,expand=1)
        self.attendanceReport_left.bind("<ButtonRelease>",self.get_cursor_left)
    

        # =========================buttons sections start here========================

        #Button Frame
        btn_frame = Frame(left_frame,bd=2 ,relief=RIDGE)
        btn_frame.place(x=10,y=525,width=635,height=60)

        #Import button
        save_btn=Button(btn_frame,command=self.importCsv,text="Import CSV",width=12,font=("Microsof YaHei UI Light",12),fg="white",bg="#104e8b" )
        save_btn.grid(row=0,column=0,padx=6,pady=10,sticky=W)

        #Export button
        update_btn=Button(btn_frame,command=self.exportCsv,text="Export CSV",width=12,font=("Microsof YaHei UI Light",12),fg="white",bg="#104e8b")
        update_btn.grid(row=0,column=1,padx=6,pady=8,sticky=W)

        #Update button
        del_btn=Button(btn_frame,command=self.action,text="Update",width=12,font=("Microsof YaHei UI Light",12),fg="white",bg="#104e8b")
        del_btn.grid(row=0,column=2,padx=6,pady=10,sticky=W)

        #reset button
        reset_btn=Button(btn_frame,command=self.reset_data,text="Reset",width=12,font=("Microsof YaHei UI Light",12),fg="white",bg="#104e8b" )
        reset_btn.grid(row=0,column=3,padx=6,pady=10,sticky=W)



       
    # # ===============================update function for data=================
    def update_data(self):
        if self.var_id.get()=="" or self.var_roll.get=="" or self.var_name.get()=="" or self.var_time.get()=="" or self.var_date.get()=="" or self.var_attend.get()=="Status":
            messagebox.showerror("Error","Please Fill All Fields are Required!",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to Update this Student Attendance!",parent=self.root)
                if Update > 0:
                    conn = mysql.connector.connect(username='root', password='',host='localhost',database='face_recognition',port=3306)
                    mycursor = conn.cursor()
                    mycursor.execute("update stdattendance set std_id=%s,std_roll_no=%s,std_name=%s,std_time=%s,std_date=%s,std_attendance=%s where std_id=%s",( 
                    self.var_id.get(),
                    self.var_roll.get(),
                    self.var_name.get(),
                    self.var_time.get(),
                    self.var_date.get(),
                    self.var_attend.get(),
                    self.var_id.get()  
                    ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Successfully Updated!",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)
    # =============================Delete Attendance form my sqldb============================
    def delete_data(self):
        if self.var_id.get()=="":
            messagebox.showerror("Error","Student Id Must be Required!",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete","Do you want to Delete?",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(username='root', password='',host='localhost',database='face_recognition',port=3306)
                    mycursor = conn.cursor() 
                    sql="delete from stdattendance where std_id=%s"
                    val=(self.var_id.get(),)
                    mycursor.execute(sql,val)
                else:
                    if not delete:
                        return

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully Deleted!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)  
    # ===========================fetch data form mysql attendance===========

    def fetch_data(self):
        conn = mysql.connector.connect(username='root', password='',host='localhost',database='face_recognition',port=3306)
        mycursor = conn.cursor()

        mycursor.execute("select * from stdattendance")
        data=mycursor.fetchall()

        if len(data)!= 0:
            self.attendanceReport.delete(*self.attendanceReport.get_children())
            for i in data:
                self.attendanceReport.insert("",END,values=i)
            conn.commit()
        conn.close()

    #============================Reset Data======================
    def reset_data(self):
        self.var_id.set("")
        self.var_roll.set("")
        self.var_name.set("")
        self.var_time.set("")
        self.var_date.set("")
        self.var_attend.set("Status")

    # =========================Fetch Data Import data ===============

    def fetchData(self,rows):
        # global mydata
        # mydata = rows
        self.attendanceReport_left.delete(*self.attendanceReport_left.get_children())
        for i in rows:
            self.attendanceReport_left.insert("",END,values=i)
            print(i)
        
    #==================Import CSV=============
    def importCsv(self):
        global mydata
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
        self.fetchData(mydata)
            

    #==================Export CSV=============
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("Error","No Data Found!",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Successful","Exported Data to \""+os.path.basename(fln)+" \"Successfully!")
        except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)    

    #=============Cursur Function for CSV========================

    def get_cursor_left(self,event=""):
        cursor_focus = self.attendanceReport_left.focus()
        content = self.attendanceReport_left.item(cursor_focus)
        data = content["values"]

        self.var_id.set(data[0]),
        self.var_roll.set(data[1]),
        self.var_name.set(data[2]),
        self.var_time.set(data[3]),
        self.var_date.set(data[4]),
        self.var_attend.set(data[5])  

     #=============Cursur Function for mysql========================

    def get_cursor_right(self,event=""):
        cursor_focus = self.attendanceReport.focus()
        content = self.attendanceReport.item(cursor_focus)
        data = content["values"]

        self.var_id.set(data[0]),
        self.var_roll.set(data[1]),
        self.var_name.set(data[2]),
        self.var_time.set(data[3]),
        self.var_date.set(data[4]),
        self.var_attend.set(data[5])    
    #=========================================Update CSV============================

    # export upadte
    def action(self):
        if self.var_id.get()=="" or self.var_roll.get=="" or self.var_name.get()=="" or self.var_time.get()=="" or self.var_date.get()=="" or self.var_attend.get()=="Status":
            messagebox.showerror("Error","Please Fill All Fields are Required!",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(username='root', password='',host='localhost',database='face_recognition',port=3306)
                mycursor = conn.cursor()
                mycursor.execute("insert into stdattendance values(%s,%s,%s,%s,%s,%s)",(
                self.var_id.get(),
                self.var_roll.get(),
                self.var_name.get(),
                self.var_time.get(),
                self.var_date.get(),
                self.var_attend.get()
                ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","All Records are Saved in Database!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)



if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()