import tkinter as tk
from tkinter import *
from tkinter import ttk
import random
#import time
import tkinter
from tkinter import messagebox
import mysql.connector



class hostel:
    def __init__(self,root):
        self.root=root
        self.root.title("Hostel management system")
        self.root.geometry("1540x800+0+0")


        #================variable=========================

        self.student_var=StringVar()
        self.name_var=StringVar()
        self.address_var=StringVar()
        self.mobile_var=StringVar()
        self.email_var=StringVar()
        self.course_var=StringVar()
        self.sem_var=StringVar()
        self.cate_var=StringVar()
        self.mfee_var=StringVar()
        self.room_var=StringVar()
       

        lbltitle=Label(self.root,bd=20,relief=RIDGE,text="Hostel Management System",fg="red",bg="blue",font=("times new random",50,"bold"))
        lbltitle.pack(side=TOP,fill=X)



        #====================data frame=========================



        Dataframe=Frame(self.root,bd=20,relief=RIDGE)
        Dataframe.place(x=0,y=130,width=1530,height=330)


        #=======================data frameleft================

        DataframeLeft=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,bg="powder blue",fg="green",text="Students information",
                                                        font=("times new roman",12,"bold"))
        DataframeLeft.place(x=0,y=5,width=750,height=300) 

        lblStudentid=Label(DataframeLeft,bg="powder blue",text="Student_id",font=("times new roman",12,"bold"),padx=2,pady=6)  
        lblStudentid.grid(row=0,column=0,sticky=W)

        comMember=ttk.Combobox(DataframeLeft,textvariable=self.student_var,font=("times new roman",12,"bold"),width=27,state="readonly")
        comMember["value"]=("admin Staf","student")
        comMember.grid(row=0,column=1)

        lblname=Label(DataframeLeft,bg="powder blue",text="Name",font=("times new roman",12,"bold"),padx=2,pady=6)  
        lblname.grid(row=2,column=0,sticky=W)
        txtname=Entry(DataframeLeft,font=("times new roman",12,"bold"),textvariable=self.name_var,width=29) 
        txtname.grid(row=2,column=1)


        lbladd=Label(DataframeLeft,bg="powder blue",text="Address",font=("times new roman",12,"bold"),padx=2,pady=6)  
        lbladd.grid(row=1,column=0,sticky=W)
        txtadd=Entry(DataframeLeft,font=("times new roman",12,"bold"),textvariable=self.address_var,width=29) 
        txtadd.grid(row=1,column=1)


        lblmob=Label(DataframeLeft,bg="powder blue",text="Mobile number",font=("times new roman",12,"bold"),padx=2,pady=6)  
        lblmob.grid(row=3,column=0,sticky=W)
        txtmob=Entry(DataframeLeft,font=("times new roman",12,"bold"),textvariable=self.mobile_var,width=29) 
        txtmob.grid(row=3,column=1)

        lblemail=Label(DataframeLeft,bg="powder blue",text="Email address",font=("times new roman",12,"bold"),padx=2,pady=6)  
        lblemail.grid(row=4,column=0,sticky=W)
        txtemail=Entry(DataframeLeft,font=("times new roman",12,"bold"),textvariable=self.email_var,width=29) 
        txtemail.grid(row=4,column=1)


        lblcourse=Label(DataframeLeft,bg="powder blue",text="Course",font=("times new roman",12,"bold"),padx=2,pady=6)  
        lblcourse.grid(row=5,column=0,sticky=W)
        txtcourse=Entry(DataframeLeft,font=("times new roman",12,"bold"),textvariable=self.course_var,width=29) 
        txtcourse.grid(row=5,column=1)

        lblsem=Label(DataframeLeft,bg="powder blue",text="Semister",font=("times new roman",12,"bold"),padx=2,pady=6)  
        lblsem.grid(row=6,column=0,sticky=W)
        txtsem=Entry(DataframeLeft,font=("times new roman",12,"bold"),textvariable=self.sem_var,width=29) 
        txtsem.grid(row=6,column=1)


        lblroom=Label(DataframeLeft,bg="powder blue",text="Room number",font=("times new roman",12,"bold"),padx=2,pady=6)  
        lblroom.grid(row=3,column=5,sticky=W)
        txtroom=Entry(DataframeLeft,font=("times new roman",12,"bold"),textvariable=self.room_var,width=29) 
        txtroom.grid(row=3,column=6)

        lblcate=Label(DataframeLeft,bg="powder blue",text="Category",font=("times new roman",12,"bold"),padx=2,pady=6)  
        lblcate.grid(row=1,column=5,sticky=W)
        txtcate=Entry(DataframeLeft,font=("times new roman",12,"bold"),textvariable=self.cate_var,width=29) 
        txtcate.grid(row=1,column=6)



        lblmfee=Label(DataframeLeft,bg="powder blue",text="Monthly fee",font=("times new roman",12,"bold"),padx=2,pady=6)  
        lblmfee.grid(row=2,column=5,sticky=W)
        txtmfee=Entry(DataframeLeft,font=("times new roman",12,"bold"),textvariable=self.mfee_var,width=29) 
        txtmfee.grid(row=2,column=6)


        #==================data frame right=========================



        DataframeRight=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,bg="powder blue",fg="green",
                                                        font=("times new roman",12,"bold"),text="Room Details")
        DataframeRight.place(x=770,y=5,width=480,height=300)   


        self.txtBox=Text(DataframeRight,font=("arial",12,"bold"),width=26,height=13,padx=2,pady=6)
        self.txtBox.grid(row=0,column=2)

        listScrollbar=Scrollbar(DataframeRight)
        listScrollbar.grid(row=0,column=1,sticky="ns")

        listRooms=["room-1","room-2","room-3","room-4","room-5","room-6","room-7","room-8","room-9","room-10","room-11","room-12","room-13","room-14","room-15","room-16"]

        def SelectRoom(event=""):
            value=str(listBox.get(listBox.curselection()))
            x=value
            if (x=="room-1"):
                self.room_var.set("room-1:bed-1")
                self.mfee_var.set("rs 500")
            elif (x=="room-2"):
                self.room_var.set("room-2:bed-1")
                self.mfee_var.set("rs 500")
            elif (x=="room-3"):
                self.room_var.set("room-3:bed-1")
                self.mfee_var.set("rs 500")
            elif (x=="room-4"):
                self.room_var.set("room-4:bed-1")
                self.mfee_var.set("rs 500") 
            elif (x=="room-5"):
                self.room_var.set("room-5:bed-1")
                self.mfee_var.set("rs 500") 
            elif (x=="room-6"):
                self.room_var.set("room-6:bed-1")
                self.mfee_var.set("rs 500") 
            elif (x=="room-7"):
                self.room_var.set("room-7:bed-1")
                self.mfee_var.set("rs 500") 
            elif (x=="room-8"):
                self.room_var.set("room-8:bed-1")
                self.mfee_var.set("rs 500") 
            elif (x=="room-9"):
                self.room_var.set("room-9:bed-1")
                self.mfee_var.set("rs 500") 
            elif (x=="room-10"):
                self.room_var.set("room-10:bed-1")
                self.mfee_var.set("rs 500") 
            elif (x=="room-11"):
                self.room_var.set("room-11:bed-1")
                self.mfee_var.set("rs 500") 
            elif (x=="room-12"):
                self.room_var.set("room-12:bed-1")
                self.mfee_var.set("rs 500") 
            elif (x=="room-13"):
                self.room_var.set("room-13:bed-1")
                self.mfee_var.set("rs 500")
            elif (x=="room-14"):
                self.room_var.set("room-14:bed-1")
                self.mfee_var.set("rs 500") 
            elif (x=="room-15"):
                self.room_var.set("room-15:bed-1")
                self.mfee_var.set("rs 500") 
            elif (x=="room-16"):
                self.room_var.set("room-16:bed-1")
                self.mfee_var.set("rs 500") 
             
            

        listBox=Listbox(DataframeRight,font=("arial",12,"bold"),width=20,height=14)

        listBox.bind("<<ListboxSelect>>",SelectRoom)

        listBox.grid(row=0,column=0,padx=4)
        listScrollbar.config(command=listBox.yview)

        for item in listRooms:
            listBox.insert(END,item)




        #======================button frame=================


        Framebutton=Frame(self.root,bd=10,relief=RIDGE,bg="powder blue")
        Framebutton.place(x=0,y=460,width=1270,height=55) 

        btnAddData=Button(Framebutton,command=self.add_data,text="Add Data",font=("arial",12,"bold"),width=20,bg="blue",fg="white")
        btnAddData.grid(row=0,column=0)      

        btnAddData=Button(Framebutton,command=self.showData,text="Show Data",font=("arial",12,"bold"),width=20,bg="blue",fg="white")
        btnAddData.grid(row=0,column=1)      

        btnAddData=Button(Framebutton,command=self.update,text="Update",font=("arial",12,"bold"),width=20,bg="blue",fg="white")
        btnAddData.grid(row=0,column=2)      

        btnAddData=Button(Framebutton,command=self.delete,text="delete",font=("arial",12,"bold"),width=20,bg="blue",fg="white")
        btnAddData.grid(row=0,column=3)      

        btnAddData=Button(Framebutton,command=self.reset,text="Reset",font=("arial",12,"bold"),width=15,bg="blue",fg="white")
        btnAddData.grid(row=0,column=4)      

        btnAddData=Button(Framebutton,command=self.iExit,text="Exit",font=("arial",12,"bold"),width=23,bg="blue",fg="white")
        btnAddData.grid(row=0,column=5)      





         
         
        #======================info frame=================

        FrameDetails=Frame(self.root,bd=10,relief=RIDGE,padx=20,bg="powder blue")
        FrameDetails.place(x=0,y=510,width=1270,height=130)

        Table_frame=Frame(FrameDetails,bd=5,relief=RIDGE,bg="powder blue")
        Table_frame.place(x=0,y=2,width=1200,height=100)


        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)





        self.hostel_table=ttk.Treeview(Table_frame,column=("student_id","name","address","mobile number","email","course","sem","cate","mfee","room number"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)

        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)

        xscroll.config(command=self.hostel_table.xview)
        yscroll.config(command=self.hostel_table.yview)

        self.hostel_table.heading("student_id",text="Student_id")
        self.hostel_table.heading("name",text="Name")
        self.hostel_table.heading("address",text="Address")
        self.hostel_table.heading("mobile number",text="Mobile Number")
        self.hostel_table.heading("email",text="Email ")
        self.hostel_table.heading("course",text="Course")
        self.hostel_table.heading("sem",text="Semister")
        self.hostel_table.heading("cate",text="Category")
        self.hostel_table.heading("mfee",text="Monthly Fee")
        self.hostel_table.heading("room number",text="Room Number")


        self.hostel_table["show"]="headings"
        self.hostel_table.pack(fill=BOTH,expand=1)


        self.fatch_data()
        self.hostel_table.bind("<ButtonRelease-1>",self.get_cursor)


    def add_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Yuvaraj@123",database="hostel_management_system")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(     
                                                                                        self.student_var.get(),
                                                                                        self.name_var.get(),
                                                                                        self.address_var.get(),
                                                                                        self.mobile_var.get(),
                                                                                        self.email_var.get(),
                                                                                        self.course_var.get(),
                                                                                        self.sem_var.get(),
                                                                                        self.cate_var.get(),
                                                                                        self.mfee_var.get(),
                                                                                        self.room_var.get()
                                                                                     ))
        conn.commit()
        self.fatch_data()
        conn.close()

        messagebox.showinfo("success","student Id has been inserted successfully")                                                                                

    

    def update(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Yuvaraj@123",database="hostel_management_system")
        my_cursor=conn.cursor()
        my_cursor.execute("update student set name=%s,address=%s,mobile_no=%s,email=%s,course=%s,sem=%s,cate=%s,mfee=%s,room_no=%s where student_id=%s",(                                                                                                                                                                                                                                                              self.name_var.get(),
                                                                                                                                                                        self.address_var.get(),
                                                                                                                                                                        self.mobile_var.get(),
                                                                                                                                                                        self.email_var.get(),
                                                                                                                                                                        self.course_var.get(),
                                                                                                                                                                        self.sem_var.get(),
                                                                                                                                                                        self.cate_var.get(),
                                                                                                                                                                        self.mfee_var.get(),
                                                                                                                                                                        self.room_var.get(),  
                                                                                                                                                                        self.student_var.get(),
                                                                                       

                                                                                                                                                                       ))

        conn.commit()
        self.fatch_data()
        self.reset()
        conn.close()

        messagebox.showinfo("success","Student has been Updated")
    
    
    def fatch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Yuvaraj@123",database="hostel_management_system")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        rows=my_cursor.fetchall()


        if len(rows)!=0:
            self.hostel_table.delete(*self.hostel_table.get_children())
            for i in rows:
                self.hostel_table.insert("",END,values=i)
            conn.commit()
        conn.close()        



    def get_cursor(self,event=""):
        cursor_row=self.hostel_table.focus()
        content=self.hostel_table.item(cursor_row)
        row=content['values']


        self.student_var.set(row[0]),
        self.name_var.set(row[1]),
        self.address_var.set(row[2]),
        self.mobile_var.set(row[3]),
        self.email_var.set(row[4]),
        self.course_var.set(row[5]),
        self.sem_var.set(row[6]),
        self.cate_var.set(row[7]),
        self.mfee_var.set(row[8]),
        self.room_var.set(row[9])



    def showData(self):
        self.txtBox.insert(END,"Student id\t:"+ self.student_var.get() + "\n")
        self.txtBox.insert(END,"Name\t:"+ self.name_var.get() + "\n")
        self.txtBox.insert(END,"Address\t:"+ self.address_var.get() + "\n")
        self.txtBox.insert(END,"Mobile Number\t:"+ self.mobile_var.get() + "\n")
        self.txtBox.insert(END,"Email\t:"+ self.email_var.get() + "\n")
        self.txtBox.insert(END,"Course\t:"+ self.course_var.get() + "\n")
        self.txtBox.insert(END,"Semister\t:"+ self.sem_var.get() + "\n")
        self.txtBox.insert(END,"Category\t:"+ self.cate_var.get() + "\n")
        self.txtBox.insert(END,"Monthly Fee\t:"+ self.mfee_var.get() + "\n")
        self.txtBox.insert(END,"Room\t:"+ self.room_var.get() + "\n")
        

    def reset(self):
        self.student_var.set(""),
        self.name_var.set(""),
        self.address_var.set(""),
        self.mobile_var.set(""),
        self.email_var.set(""),
        self.course_var.set(""),
        self.sem_var.set(""),
        self.cate_var.set(""),
        self.mfee_var.set(""),
        self.room_var.set("")
        self.txtBox.delete("1.0",END)


    def iExit(self):
        iExit=tkinter.messagebox.askyesno("hostel management system","Do You Want To Exit")
        if iExit>0:
            self.root.destroy()
            return


                 
    def delete(self):
        if self.student_var.get()=="" or self.name_var.get()=="":
            messagebox.showerror("Error","First select the student id")
        
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Yuvaraj@123",database="hostel_management_system")
            my_cursor=conn.cursor()
            query="delete from student where student_id=%s"
            value=(self.student_var.get(),)
            my_cursor.execute(query,value)

            conn.commit()
            self.fatch_data()
            self.reset()
            conn.close()
            

            messagebox.showinfo("success","student id has been  deleted")





if __name__ == "__main__":
    root=Tk()   
    obj=hostel(root)
    root.mainloop()   