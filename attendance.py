from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog


mydata=[]
class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #variables-------------------------------------
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()
        
      





        #first image-------------------------------------------
        img1 = Image.open(r"C:\Users\shiva\Desktop\advanced attendence system\images\image12.jpg")
        img1 = img1.resize((765,180),Image.ADAPTIVE)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        flb_1 = Label(self.root,image=self.photoimg1)
        flb_1.place(x=0,y=0,width=765,height=180)
#second image-------------------------------------------
        img2 = Image.open(r"C:\Users\shiva\Desktop\advanced attendence system\images\image13.jpg")
        img2 = img2.resize((765,180),Image.ADAPTIVE)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        flb_1 = Label(self.root,image=self.photoimg2)
        flb_1.place(x=765,y=0,width=765,height=180)
#background image--------------------------------------
        img4 = Image.open(r"C:\Users\shiva\Desktop\advanced attendence system\images\image3.jpg")
        img4 = img4.resize((1530,610),Image.ADAPTIVE)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        bg_img = Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=180,width=1530,height=610)  

        title_lb1 = Label(bg_img,text="STUDENT ATTENDANCE SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="darkgreen")
        title_lb1.place(x=0,y=0,width=1530,height=45)

#creating frame----------------------------------------
        main_frame = Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=15,y=60,width=1500,height=555) 

#dividing frame and making labelframe--------------------
        #left label frame--------------------------------
        left_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details",font=("times new roman ",12,"bold"))
        left_frame.place(x=10,y=10,width=730,height=525)

        #------------------------------------------------
        img_left = Image.open(r"C:\Users\shiva\Desktop\advanced attendence system\images\image15.jpg")
        img_left = img_left.resize((730,160),Image.ADAPTIVE)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        flb_1 = Label(left_frame,image=self.photoimg_left)
        flb_1.place(x=10,y=5,width=710,height=180)

        #creating labelframe for current course information------------
        left_inside_frame = LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,font=("times new roman ",12,"bold"))
        left_inside_frame.place(x=10,y=200,width=710,height=290)

        #AttendanceId---------------------------------------------
        attendanceId_label=Label(left_inside_frame,text="AttendanceId:",font=("times new roman",13,"bold"),bg="white")
        attendanceId_label.grid(row=0,column=0,padx=10,pady=10,sticky=W)

        attendanceId_label_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_id,font=("times new roman",13,"bold"))
        attendanceId_label_entry.grid(row=0,column=1,padx=10,pady=10,sticky=W)

        #roll_no---------------------------------------------
        rollno_label=Label(left_inside_frame,text="Roll No:",font=("times new roman",13,"bold"),bg="white")
        rollno_label.grid(row=0,column=2,padx=10,pady=10,sticky=W)

        rollno_label_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_roll,font=("times new roman",13,"bold"))
        rollno_label_entry.grid(row=0,column=3,padx=10,pady=10,sticky=W)

        #name---------------------------------------------
        name_label=Label(left_inside_frame,text="Name:",font=("times new roman",13,"bold"),bg="white")
        name_label.grid(row=1,column=0,padx=10,pady=10,sticky=W)

        name_label_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_name,font=("times new roman",13,"bold"))
        name_label_entry.grid(row=1,column=1,padx=10,pady=10,sticky=W)

       #department---------------------------------------------
        department_label=Label(left_inside_frame,text="Department:",font=("times new roman",13,"bold"),bg="white")
        department_label.grid(row=1,column=2,padx=10,pady=10,sticky=W)

        department_label_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_dep,font=("times new roman",13,"bold"))
        department_label_entry.grid(row=1,column=3,padx=10,pady=10,sticky=W)

        #time---------------------------------------------
        time_label=Label(left_inside_frame,text="Time:",font=("times new roman",13,"bold"),bg="white")
        time_label.grid(row=2,column=0,padx=10,pady=10,sticky=W)

        time_label_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_time,font=("times new roman",13,"bold"))
        time_label_entry.grid(row=2,column=1,padx=10,pady=10,sticky=W)

        #date---------------------------------------------
        date_label=Label(left_inside_frame,text="Date:",font=("times new roman",13,"bold"),bg="white")
        date_label.grid(row=2,column=2,padx=10,pady=10,sticky=W)

        date_label_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_date,font=("times new roman",13,"bold"))
        date_label_entry.grid(row=2,column=3,padx=10,pady=10,sticky=W)

        #attendence status--------------------------------------------
        attendance_status_label=Label(left_inside_frame,text="Attendance status:",font=("times new roman",13,"bold"),bg="white")
        attendance_status_label.grid(row=3,column=0,padx=10,pady=10)

        attendance_status_label_combo=ttk.Combobox(left_inside_frame,font=("times new roman",13,"bold"),state="readonly",width=20,textvariable=self.var_atten_attendance)
        attendance_status_label_combo["values"]=("Status","Present","Absent")
        attendance_status_label_combo.current(0)
        attendance_status_label_combo.grid(row=3,column=1,padx=2,pady=5,sticky=W)

       #button creation-------------------------------------------------------------------
        btn_frame = Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=210,width=705,height=35)

        import_btn=Button(btn_frame,text="Import csv",command=self.importCsv,font=("times new roman",13,"bold"),bg="blue",fg="white",width=17)
        import_btn.grid(row=0,column=0)

        
        export_btn=Button(btn_frame,text="Export csv",command=self.exportCsv,font=("times new roman",13,"bold"),bg="blue",fg="white",width=17)
        export_btn.grid(row=0,column=1)

        
        delete_btn=Button(btn_frame,text="Update",font=("times new roman",13,"bold"),bg="blue",fg="white",width=17)
        delete_btn.grid(row=0,column=2)

        
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,font=("times new roman",13,"bold"),bg="blue",fg="white",width=17)
        reset_btn.grid(row=0,column=3)



        #right label frame-------------------------------
        right_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman ",12,"bold"))
        right_frame.place(x=760,y=10,width=730,height=525)

        right_inside_frame = LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,font=("times new roman ",12,"bold"))
        right_inside_frame.place(x=10,y=10,width=710,height=480)

        #scroll bar---------------------------------------------
        scroll_x=ttk.Scrollbar(right_inside_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(right_inside_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(right_inside_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll No")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")

        self.AttendanceReportTable["show"]="headings"

        self.AttendanceReportTable.column("id",width=150)
        self.AttendanceReportTable.column("roll",width=150)
        self.AttendanceReportTable.column("name",width=150)
        self.AttendanceReportTable.column("department",width=150)
        self.AttendanceReportTable.column("time",width=150)
        self.AttendanceReportTable.column("date",width=150)
        self.AttendanceReportTable.column("attendance",width=150)


        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        #binding---------------------------------------
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)


    #fetch data----------------------------------------

    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)
    #import csv---------------------------------------        
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
          csvread=csv.reader(myfile,delimiter=",")
          for i in csvread:
            mydata.append(i)
          self.fetchData(mydata)
    #export csv----------------------------------------
    def exportCsv(self):
       try:
          if len(mydata)<1:
             messagebox.showerror("No Data","No Data Found to Export",parent=self.root)
             return False
          fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
          with open(fln,mode="w",newline="") as myfile:
            exp_write=csv.writer(myfile,delimiter=",")
            for i in mydata:
              exp_write.writerow(i)
            messagebox.showinfo("Data Export","your data exported to "+os.path.basename(fln)+"successfully") 
       except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root) 

    #cursor--------------------------------------------------
    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        row=content["values"]
        self.var_atten_id.set(row[0])
        self.var_atten_roll.set(row[1])
        self.var_atten_name.set(row[2])
        self.var_atten_dep.set(row[3])
        self.var_atten_time.set(row[4])
        self.var_atten_date.set(row[5])
        self.var_atten_attendance.set(row[6])

    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")
        
        
        
            




          
            


            



       

        







if __name__ == "__main__":
   root = Tk()
   obj = Attendance(root)
   root.mainloop()        