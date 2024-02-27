import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from time import strftime
from datetime import datetime
import sys

# inputs in this window
subcode = subname = subtype = None

'''
    LIST OF FUNCTIONS USED FOR VARIOUS FUNCTIONS THROUGH TKinter INTERFACE
        * create_treeview()
        * update_treeview()
        * parse_data()
        * update_data()
        * remove_data()
'''

# create treeview (call this function once)
def create_treeview():
    tree['columns'] = ('one', 'two', 'three')
    tree.column("#0", width=0, stretch=tk.NO)
    tree.column("one", width=100, stretch=tk.NO)
    tree.column("two", width=400, stretch=tk.NO)
    tree.column("three", width=90, stretch=tk.NO)
    tree.heading('#0', text="")
    tree.heading('one', text="Code")
    tree.heading('two', text="Name")
    tree.heading('three', text="Type")


# update treeview (call this function after each update)
def update_treeview():
    for row in tree.get_children():
        tree.delete(row)
    cursor = conn.execute("SELECT * FROM SUBJECTS")
    for row in cursor:
        # print(row[0], row[1], row[2])
        if row[2] == 'T':
            t = 'Theory'
        elif row[2] == 'P':
            t = 'Practical'
        tree.insert(
            "",
            0,
            values=(row[0],row[1],t)
        )
    tree.place(x=630, y=150,width=595,height=465)


# Parse and store data into database and treeview upon clcicking of the add button
def parse_data():
    subcode = str(subcode_entry.get())
    subname = str(subname_entry.get("1.0", tk.END)).upper().rstrip()
    subtype = str(radio_var.get()).upper()

    if subcode=="":
        subcode = None
    if subname=="":
        subname = None

    if subcode is None or subname is None:
        messagebox.showerror("Bad Input", "Please fill up Subject Code and/or Subject Name!")
        subcode_entry.delete(0, tk.END)
        subname_entry.delete("1.0", tk.END)
        return

    conn.execute(f"REPLACE INTO SUBJECTS (SUBCODE, SUBNAME, SUBTYPE)\
        VALUES ('{subcode}','{subname}','{subtype}')")
    conn.commit()
    update_treeview()
    
    subcode_entry.delete(0, tk.END)
    subname_entry.delete("1.0", tk.END)


# update a row in the database
def update_data():
    subcode_entry.delete(0, tk.END)
    subname_entry.delete("1.0", tk.END)
    try:
        # print(tree.selection())
        if len(tree.selection()) > 1:
            messagebox.showerror("Bad Select", "Select one subject at a time to update!")
            return

        row = tree.item(tree.selection()[0])['values']
        subcode_entry.insert(0, row[0])
        subname_entry.insert("1.0", row[1])
        if row[2][0] == "T":
            R1.select()
        elif row[2][0] == "P":
            R2.select()

        conn.execute(f"DELETE FROM SUBJECTS WHERE SUBCODE = '{row[0]}'")
        conn.commit()
        update_treeview()

    except IndexError:
        messagebox.showerror("Bad Select", "Please select a subject from the list first!")
        return

# remove selected data from databse and treeview
def remove_data():
    if len(tree.selection()) < 1:
        messagebox.showerror("Bad Select", "Please select a subject from the list first!")
        return
    for i in tree.selection():
        # print(tree.item(i)['values'][0])
        conn.execute(f"DELETE FROM SUBJECTS WHERE SUBCODE = '{tree.item(i)['values'][0]}'")
        conn.commit()
        tree.delete(i)
        update_treeview()



# main
if __name__ == "__main__":  

    '''
        DATABASE CONNECTIONS AND SETUP
    '''

    # connecting database
    conn = sqlite3.connect(r'C:\Users\NIDHI\OneDrive\Desktop\Face_Recognition_System\timetable.db')

    # creating Tabe in the database
    conn.execute('CREATE TABLE IF NOT EXISTS SUBJECTS\
    (SUBCODE CHAR(10) NOT NULL PRIMARY KEY,\
    SUBNAME CHAR(50) NOT NULL,\
    SUBTYPE CHAR(1) NOT NULL)')


    '''
        TKinter WINDOW SETUP WITH WIDGETS
            * Label(1-6)
            * Entry(1)
            * Text(1)
            * Radiobutton(1-2)
            * Treeview(1)
            * Button(1-2)
    '''

    # TKinter Window
    subtk = tk.Tk()
    subtk.geometry('1366x768')
    subtk.title('Subject Pannel')

    # backgorund image 
    bg1=Image.open(r"C:\Users\NIDHI\OneDrive\Desktop\Face_Recognition_System\Images_GUI\bg0.jpg")
    bg1=bg1.resize((1366,768),Image.LANCZOS)
    photobg1=ImageTk.PhotoImage(bg1)

    # set image as lable
    bg_img = Label(subtk,image= photobg1)
    bg_img.place(x=0,y=0,width=1366,height=768)


    #title section
    title_lb1 = Label(bg_img,bg='#FCFCFC')
    title_lb1.place(x=0,y=0,width=1366,height=45)

     #  logo  
    logo=Image.open(r"C:\Users\NIDHI\OneDrive\Desktop\Face_Recognition_System\Images_GUI\logo-color.png")
    logo=logo.resize((130,43),Image.LANCZOS)
    logo=ImageTk.PhotoImage(logo)

    std_b1 = Button(title_lb1,image= logo,cursor="hand2",bd=0)
    std_b1.place(x=6,y=2,width=130,height=43)


    # ============================Time================
    def time():
        string = strftime('%H:%M:%S %p')
        lbl.config(text = string)
        lbl.after(1000, time)

    lbl = Label(title_lb1, font = ('Microsof YaHei UI Light',11),foreground='#104e8b',background='#FCFCFC')
    lbl.place(x=1260,y=4,width=80,height=30)
    time()  

    # Creating Frame 
    main_frame = Frame(bg_img,bd=1 ,bg="#FCFCFC")  
    main_frame.place(x=80,y=80,width=1160,height=550)

    # Left Label Frame  text="Subjects",
    left_frame = LabelFrame(main_frame,bd=1,relief=RIDGE,font=('Microsof YaHei UI Light',11),fg="#104e8b",bg="#FCFCFC")
    left_frame.place(x=15,y=10,width=500,height=520)

    # Label1
    tk.Label(
        main_frame,
        text='List of Subjects',
        font=('Microsof YaHei UI Light', 20),fg="#104e8b",bg="#FCFCFC"
    ).place(x=559, y=25)

    # Label2
    tk.Label(
        main_frame,
        text='Subjects',
        font=('Microsof YaHei UI Light', 20),fg="#104e8b",bg="#FCFCFC"
    ).place(x=100, y=50)

    # # Label3
    # tk.Label(
    #     main_frame,
    #     text='Add information in the following prompt!',
    #     font=('Microsof YaHei UI Light', 10, 'italic')
    # ).place(x=100, y=85)

    # Label4
    tk.Label(
        main_frame,
        text='Subject Code:',
        font=('Microsof YaHei UI Light', 13),fg="#104e8b",bg="#FCFCFC"
    ).place(x=100, y=150)

    # Entry1
    subcode_entry = tk.Entry(
        main_frame,
        font=('Microsof YaHei UI Light', 13),
        fg="#104e8b",bg="#FCFCFC",width=20
    )
    subcode_entry.place(x=270, y=150)
    
    # Label5
    tk.Label(
        main_frame,
        text='Subject Name:',
        font=('Microsof YaHei UI Light', 13),fg="#104e8b",bg="#FCFCFC"
    ).place(x=100, y=200)

    # Text
    subname_entry = tk.Text(
        main_frame,
        font=('Microsof YaHei UI Light', 13),
        width=20,
        height=2,fg="#104e8b",bg="#FCFCFC",
        wrap=tk.WORD
    )
    subname_entry.place(x=270, y=200)

    # Label6
    tk.Label(
        main_frame,
        text='Subject Type:',
        font=('Microsof YaHei UI Light', 13),fg="#104e8b",bg="#FCFCFC"
    ).place(x=100, y=270)

    # RadioButton variable to store RadioButton Status
    radio_var = tk.StringVar()

    # RadioButton1
    R1 = tk.Radiobutton(
        main_frame,
        text='Theory',
        font=('Microsof YaHei UI Light', 12),
        variable=radio_var,
        value="T",fg="#104e8b",bg="#FCFCFC"
    )
    R1.place(x=270, y=270)
    R1.select()

    # RadioButton2
    R2 = tk.Radiobutton(
        main_frame,
        text='Practical',
        font=('Microsof YaHei UI Light', 12),
        variable=radio_var,fg="#104e8b",bg="#FCFCFC",
        value="P"
    )
    R2.place(x=270, y=300)
    R2.select()



    # Button1
    B1 = tk.Button(
        main_frame,
        text='   Save   ',
        font=('Microsof YaHei UI Light', 12,'bold'),bg="#104e8b",fg="#FCFCFC",
        command=parse_data
    )
    B1.place(x=80,y=400)

    # Button2
    B2 = tk.Button(
        main_frame,
        text='  Update  ',
        font=('Microsof YaHei UI Light', 12,'bold'),bg="#104e8b",fg="#FCFCFC",
        command=update_data
    )
    B2.place(x=210,y=400)

    # Treeview1
    tree = ttk.Treeview(subtk)
    create_treeview()
    update_treeview()

    # Button3
    B3 = tk.Button(
        main_frame,
        text='  Delete  ',
        font=('Microsof YaHei UI Light', 12,'bold'),bg="#104e8b",fg="#FCFCFC",
        command=remove_data
    )
    B3.place(x=350,y=400)

    # looping Tkiniter window
    subtk.mainloop()
    conn.close() # close database ad=fter all operations