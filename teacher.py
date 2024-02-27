import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import ttk
from tkinter import*
from PIL import Image,ImageTk
from time import strftime
from datetime import datetime
import sys

from login import resource_path

fid = passw = conf_passw = name = ini = email = subcode1 = subcode2 = None



# create treeview (call this function once)
def create_treeview():
    tree['columns'] = list(map(lambda x: '#' + str(x), range(1, 5)))
    tree.column("#0", width=0, stretch=tk.NO)
    tree.column("#1", width=100, stretch=tk.NO)
    tree.column("#2", width=300, stretch=tk.NO)
    tree.column("#3", width=100, stretch=tk.NO)
    tree.column("#4", width=100, stretch=tk.NO)
    tree.heading('#0', text="")
    tree.heading('#1', text="Fid")
    tree.heading('#2', text="Name")
    tree.heading('#3', text="Subject 1")
    tree.heading('#4', text="Subject 2")
    tree['height'] = 25



def update_treeview():
    for row in tree.get_children():
        tree.delete(row)
    cursor = conn.execute("SELECT FID, NAME, SUBCODE1, SUBCODE2 FROM FACULTY")
    for row in cursor:
        tree.insert(
            "",
            0,
            values=(row[0], row[1], row[2], row[3])
        )
    tree.place(x=620, y=95)



def parse_data():
    fid = str(fid_entry.get())
    passw = str(passw_entry.get())
    conf_passw = str(conf_passw_entry.get())
    name = str(name_entry.get()).upper()
    ini = str(ini_entry.get()).upper()
    email = str(email_entry.get())
    subcode1 = str(combo1.get())
    subcode2 = str(combo2.get())

    if fid == "" or passw == "" or \
        conf_passw == "" or name == "":
        messagebox.showwarning("Bad Input", "Some fields are empty! Please fill them out!")
        return

    if passw != conf_passw:
        messagebox.showerror("Passwords mismatch", "Password and confirm password didnt match. Try again!")
        passw_entry.delete(0, tk.END)
        conf_passw_entry.delete(0, tk.END)
        return

    if subcode1 == "NULL":
        messagebox.showwarning("Bad Input", "Subject 1 cant be NULL")
        return
    
    conn.execute(f"REPLACE INTO FACULTY (FID, PASSW, NAME, INI, EMAIL, SUBCODE1, SUBCODE2)\
        VALUES ('{fid}','{passw}','{name}', '{ini}', '{email}', '{subcode1}', '{subcode2}')")
    conn.commit()
    update_treeview()
    
    fid_entry.delete(0, tk.END)
    passw_entry.delete(0, tk.END)
    conf_passw_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    ini_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    combo1.current(0)
    combo2.current(0)
    


def update_data():
    fid_entry.delete(0, tk.END)
    passw_entry.delete(0, tk.END)
    conf_passw_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    ini_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    combo1.current(0)
    combo2.current(0)
    try:
      
        if len(tree.selection()) > 1:
            messagebox.showerror("Bad Select", "Select one faculty at a time to update!")
            return

        q_fid = tree.item(tree.selection()[0])['values'][0]
        cursor = conn.execute(f"SELECT * FROM FACULTY WHERE FID = '{q_fid}'")

        cursor = list(cursor)
        fid_entry.insert(0, cursor[0][0])
        passw_entry.insert(0, cursor[0][1])
        conf_passw_entry.insert(0, cursor[0][1])
        name_entry.insert(0, cursor[0][2])
        ini_entry.insert(0, cursor[0][3])
        email_entry.insert(0, cursor[0][4])
        combo1.current(subcode_li.index(cursor[0][5]))
        combo2.current(subcode_li.index(cursor[0][6]))

        conn.execute(f"DELETE FROM FACULTY WHERE FID = '{cursor[0][0]}'")
        conn.commit()
        update_treeview()

    except IndexError:
        messagebox.showerror("Bad Select", "Please select a faculty from the list first!")
        return


# remove selected data 
def remove_data():
    if len(tree.selection()) < 1:
        messagebox.showerror("Bad Select", "Please select a faculty from the list first!")
        return
    for i in tree.selection():
        conn.execute(f"DELETE FROM FACULTY WHERE FID = '{tree.item(i)['values'][0]}'")
        conn.commit()
        tree.delete(i)
        update_treeview()


# toggles pwd
def show_passw():
    if passw_entry['show'] == "●":
        passw_entry['show'] = ""
        B1_show['text'] = '●'
        B1_show.update()
    elif passw_entry['show'] == "":
        passw_entry['show'] = "●"
        B1_show['text'] = '○'
        B1_show.update()
    passw_entry.update()




# main
if __name__ == "__main__":  

   

    # connecting database
    conn = sqlite3.connect(resource_path(r'C:\Users\NIDHI\OneDrive\Desktop\Face_Recognition_System\timetable.db'))

    # creating Tabe in the database
    conn.execute('CREATE TABLE IF NOT EXISTS FACULTY\
    (FID CHAR(10) NOT NULL PRIMARY KEY,\
    PASSW CHAR(50) NOT NULL,\
    NAME CHAR(50) NOT NULL,\
    INI CHAR(5) NOT NULL,\
    EMAIL CHAR(50) NOT NULL,\
    SUBCODE1 CHAR(10) NOT NULL,\
    SUBCODE2 CHAR(10)    )')



    # TKinter Window
    subtk = tk.Tk()
    subtk.geometry('1366x768')
    subtk.title('Teacher Pannel')

    
    # backgorund image 
    bg1=Image.open(resource_path(r"C:\Users\NIDHI\OneDrive\Desktop\Face_Recognition_System\Images_GUI\bg0.jpg"))
    bg1=bg1.resize((1366,768),Image.LANCZOS)
    photobg1=ImageTk.PhotoImage(bg1)

    # set image as lable
    bg_img = Label(subtk,image= photobg1)
    bg_img.place(x=0,y=0,width=1366,height=768)


    #title section
    title_lb1 = Label(bg_img,bg="#FCFCFC")
    title_lb1.place(x=0,y=0,width=1366,height=45)

     #  logo  
    logo=Image.open(resource_path(r"C:\Users\NIDHI\OneDrive\Desktop\Face_Recognition_System\Images_GUI\logo-color.png"))
    logo=logo.resize((130,43),Image.LANCZOS)
    logo=ImageTk.PhotoImage(logo)

    std_b1 = Button(title_lb1,image= logo,cursor="hand2",bd=0)
    std_b1.place(x=6,y=2,width=130,height=43)


    # ============================Time================
    def time():
        string = strftime('%H:%M:%S %p')
        lbl.config(text = string)
        lbl.after(1000, time)

    lbl = Label(title_lb1, font = ('times new roman',11),foreground='#104e8b',background='#FCFCFC')
    lbl.place(x=1260,y=4,width=80,height=30)
    time()  

    # Creating Frame 
    main_frame = Frame(bg_img,bd=1,bg="#FCFCFC" )  
    main_frame.place(x=80,y=80,width=1160,height=550)

    
    # Left Label Frame 
    left_frame = LabelFrame(main_frame,bd=1,relief=RIDGE,text="Teacher Details",font=("verdana",12),fg="#104e8b",bg="#FCFCFC")
    left_frame.place(x=15,y=10,width=500,height=520)


    # Teacher id
    tk.Label(subtk,text='Teacher id:',fg="#104e8b",bg="#FCFCFC",font=("Microsof YaHei UI Light",12)).place(x=160, y=130)

    # Entry1
    fid_entry = tk.Entry(subtk,font=("Microsof YaHei UI Light",12),fg="#104e8b",bg="#FCFCFC", width=25)
    fid_entry.place(x=290, y=130)

    # Password
    tk.Label(
        subtk,
        text='Password:',
        font=("Microsof YaHei UI Light",12),fg="#104e8b",bg="#FCFCFC"
    ).place(x=160, y=170)

    # Entry2
    passw_entry = tk.Entry(
        subtk,
        font=("Microsof YaHei UI Light",12),fg="#104e8b",bg="#FCFCFC",
        width=25,
        show="●"
    )
    passw_entry.place(x=290, y=170)

    # show button
    B1_show = tk.Button(
        subtk,
        text='○',
        font=('Consolas', 9, 'bold'),bd=0,bg="white",fg="#104e8b",
        command=show_passw
    )
    B1_show.place(x=502,y=170)

    tk.Label(
        subtk,
        text='Confirm Pwd:',fg="#104e8b",bg="#FCFCFC",
        font=("Microsof YaHei UI Light",12)
        ).place(x=160, y=210)

   
    conf_passw_entry = tk.Entry(
        subtk,
        font=("Microsof YaHei UI Light",12),fg="#104e8b",bg="#FCFCFC",
        width=25,
        show="●"
    )
    conf_passw_entry.place(x=290, y=210)

    # Teacher Name
    tk.Label(
        subtk,
        text='Teacher Name:',
        font=("Microsof YaHei UI Light",12),fg="#104e8b",bg="#FCFCFC"
    ).place(x=160, y=250)

    # Entry4
    name_entry = tk.Entry(
        subtk,
        font=("Microsof YaHei UI Light",12),fg="#104e8b",bg="#FCFCFC",
        width=25,
    )
    name_entry.place(x=290, y=250)

    # Initials
    tk.Label(
        subtk,
        text='Initials:',
        font=("Microsof YaHei UI Light",12),fg="#104e8b",bg="#FCFCFC"
    ).place(x=160, y=290)

    # Entry5
    ini_entry = tk.Entry(
        subtk,
        font=("Microsof YaHei UI Light",12),fg="#104e8b",bg="#FCFCFC",
        width=25,
    )
    ini_entry.place(x=290, y=290)

    # Email
    tk.Label(
        subtk,
        text='Email:',
        font=("Microsof YaHei UI Light",12),fg="#104e8b",bg="#FCFCFC" ).place(x=160, y=330)

    # Entry6
    email_entry = tk.Entry(
        subtk,
        font=("Microsof YaHei UI Light",12),fg="#104e8b",bg="#FCFCFC",
        width=25,
    )
    email_entry.place(x=290, y=330)

    # get subject code 
    cursor = conn.execute("SELECT SUBCODE FROM SUBJECTS")
    subcode_li = [row[0] for row in cursor]
    subcode_li.insert(0, 'NULL')

    # Subject 1
    tk.Label(
        subtk,
        text='Subject 1:',
        font=("Microsof YaHei UI Light",12),fg="#104e8b",bg="#FCFCFC"
    ).place(x=160, y=370)

    # ComboBox1
    combo1 = ttk.Combobox(
        subtk,
        values=subcode_li,foreground="#104e8b"
    )
    combo1.place(x=290, y=370)
    combo1.current(0)

    # Subject 2
    tk.Label(
        subtk,
        text='Subject 2:',
        font=("Microsof YaHei UI Light",12),fg="#104e8b",bg="#FCFCFC"
    ).place(x=160, y=410)

    # ComboBox2
    combo2 = ttk.Combobox(
        subtk,
        values=subcode_li,foreground="#104e8b"
    )
    combo2.place(x=290, y=410)
    combo2.current(0)

    # Add Teacher Button
    B1 = tk.Button(
        subtk,
        text='Add Teacher',
        font=("Microsof YaHei UI Light",12),fg="white",bg="#104e8b",
        command=parse_data
    )
    B1.place(x=110,y=500)

    # Update Teacher Button2
    B2 = tk.Button(
        subtk,
        text='Update Teacher',fg="white",bg="#104e8b",
        font=("Microsof YaHei UI Light",12),
        command=update_data
    )
    B2.place(x=270,y=500)

    # Treeview1
    tree = ttk.Treeview(subtk)
    create_treeview()
    update_treeview()

    # Delete Teacher(s) Button3
    B3 = tk.Button(
        subtk,
        text='Delete Teacher(s)',fg="white",bg="#104e8b",
        font=("Microsof YaHei UI Light",12),
        command=remove_data
    )
    B3.place(x=450,y=500)

    # looping Tkiniter window
    subtk.mainloop()
    conn.close() 
