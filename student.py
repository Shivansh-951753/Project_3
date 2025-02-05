from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2





class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #variables-------------------------------------
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name= StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()
        self.var_radio1=StringVar()

#first image-------------------------------------------
        img1 = Image.open(r"C:\Users\shiva\Desktop\advanced attendence system\images\image12.jpg")
        img1 = img1.resize((510,130),Image.ADAPTIVE)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        flb_1 = Label(self.root,image=self.photoimg1)
        flb_1.place(x=0,y=0,width=510,height=130)
#second image-------------------------------------------
        img2 = Image.open(r"C:\Users\shiva\Desktop\advanced attendence system\images\image13.jpg")
        img2 = img2.resize((510,130),Image.ADAPTIVE)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        flb_1 = Label(self.root,image=self.photoimg2)
        flb_1.place(x=510,y=0,width=510,height=130)
#third image--------------------------------------------
        img3 = Image.open(r"C:\Users\shiva\Desktop\advanced attendence system\images\image14.jpg")
        img3 = img3.resize((510,130),Image.ADAPTIVE)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        flb_1 = Label(self.root,image=self.photoimg3)
        flb_1.place(x=1020,y=0,width=510,height=130)
#background image--------------------------------------
        img4 = Image.open(r"C:\Users\shiva\Desktop\advanced attendence system\images\image3.jpg")
        img4 = img4.resize((1530,660),Image.ADAPTIVE)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        bg_img = Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=130,width=1530,height=630)  

        title_lb1 = Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="darkgreen")
        title_lb1.place(x=0,y=0,width=1530,height=45)
#creating frame----------------------------------------
        main_frame = Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=15,y=60,width=1500,height=555) 
#dividing frame and making labelframe--------------------
        #left label frame--------------------------------
        left_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman ",12,"bold"))
        left_frame.place(x=10,y=10,width=730,height=525)
        #------------------------------------------------
        img_left = Image.open(r"C:\Users\shiva\Desktop\advanced attendence system\images\image15.jpg")
        img_left = img_left.resize((730,80),Image.ADAPTIVE)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        flb_1 = Label(left_frame,image=self.photoimg_left)
        flb_1.place(x=10,y=5,width=710,height=80)
        #creating labelframe for current course information------------
        current_course_frame = LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman ",12,"bold"))
        current_course_frame.place(x=10,y=90,width=710,height=100)
        #crearting department label -------------------------------------------
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",13,"bold"),state="readonly",width=20)
        dep_combo["values"]=("Select Department","Computer","IT","Civil","Mechnical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=5,sticky=W)

        #crearting course label -------------------------------------------
        course_label=Label(current_course_frame,text="Course",font=("times new roman",13,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",13,"bold"),state="readonly",width=20)
        course_combo["values"]=("Select Course","cs","ee","ce","me")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=5,sticky=W)

        #crearting year label -------------------------------------------
        year_label=Label(current_course_frame,text="Year",font=("times new roman",13,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",13,"bold"),state="readonly",width=20)
        year_combo["values"]=("Select Year","2020-21","2021-21","2022-23","2023-24")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=5,sticky=W)

        #crearting semester label -------------------------------------------
        semester_label=Label(current_course_frame,text="Semester",font=("times new roman",13,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10)

        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",13,"bold"),state="readonly",width=20)
        semester_combo["values"]=("Select Semester","sem-1","sem-2","sem-3","sem-4")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=5,sticky=W)

        #creating labelframe for class student information-------------------------------
        class_student_frame = LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman ",12,"bold"))
        class_student_frame.place(x=10,y=195,width=710,height=300)
        
        #StudentId---------------------------------------------
        studentId_label=Label(class_student_frame,text="StudentId:",font=("times new roman",13,"bold"),bg="white")
        studentId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        student_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=20,font=("times new roman",13,"bold"))
        student_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #Student Name------------------------------------------
        studentName_label=Label(class_student_frame,text="Student Name:",font=("times new roman",13,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentName_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=20,font=("times new roman",13,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #Class Division----------------------------------------
        classDivision_label=Label(class_student_frame,text="Class Division:",font=("times new roman",13,"bold"),bg="white")
        classDivision_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        #classDivision_entry=ttk.Entry(class_student_frame,textvariable=self.var_div,width=20,font=("times new roman",13,"bold"))
        #classDivision_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        div_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,font=("times new roman",12,"bold"),state="readonly",width=20)
        div_combo["values"]=("Select Division","A","B","C")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #Roll NO-----------------------------------------------
        rollNo_label=Label(class_student_frame,text="Roll No:",font=("times new roman",13,"bold"),bg="white")
        rollNo_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        rollNo_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20,font=("times new roman",13,"bold"))
        rollNo_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #Gender------------------------------------------------
        gender_label=Label(class_student_frame,text="Gender:",font=("times new roman",13,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        #gender_entry=ttk.Entry(class_student_frame,textvariable=self.var_gender,width=20,font=("times new roman",13,"bold"))
        #gender_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)
        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),state="readonly",width=20)
        gender_combo["values"]=("Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #DOB---------------------------------------------------
        Dob_label=Label(class_student_frame,text="DOB:",font=("times new roman",13,"bold"),bg="white")
        Dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        Dob_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=("times new roman",13,"bold"))
        Dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #Email-------------------------------------------------
        email_label=Label(class_student_frame,text="Email:",font=("times new roman",13,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("times new roman",13,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #Phone No----------------------------------------------
        phoneNo_label=Label(class_student_frame,text="Phone No:",font=("times new roman",13,"bold"),bg="white")
        phoneNo_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        phoneNo_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=("times new roman",13,"bold"))
        phoneNo_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        #Address-----------------------------------------------
        address_label=Label(class_student_frame,text="Address:",font=("times new roman",13,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        address_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=20,font=("times new roman",13,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        #Teacher Name------------------------------------------
        teacherName_label=Label(class_student_frame,text="Teacher Name:",font=("times new roman",13,"bold"),bg="white")
        teacherName_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        teacherName_entry=ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=20,font=("times new roman",13,"bold"))
        teacherName_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)
        
        #radia Buttons----------------------------------------------
        
        radionbtn1 = ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radionbtn1.grid(row=5,column=0)

        
        radionbtn2 = ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radionbtn2.grid(row=5,column=1)

        #buttion frame creation--------------------------------------
        btn_frame = Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=210,width=705,height=35)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,font=("times new roman",13,"bold"),bg="blue",fg="white",width=17)
        save_btn.grid(row=0,column=0)

        
        update_btn=Button(btn_frame,text="Update",command=self.update_data,font=("times new roman",13,"bold"),bg="blue",fg="white",width=17)
        update_btn.grid(row=0,column=1)

        
        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,font=("times new roman",13,"bold"),bg="blue",fg="white",width=17)
        delete_btn.grid(row=0,column=2)

        
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,font=("times new roman",13,"bold"),bg="blue",fg="white",width=17)
        reset_btn.grid(row=0,column=3)

        #----------------------------------------------------------------
        btn_frame1 = Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=240,width=705,height=30)

        take_photo_btn=Button(btn_frame1,text="Take Photo Sample",command=self.generate_dataset,font=("times new roman",13,"bold"),bg="blue",fg="white",width=34)
        take_photo_btn.grid(row=0,column=0)

        update_photo_btn=Button(btn_frame1,text="Update Photo Sample",font=("times new roman",13,"bold"),bg="blue",fg="white",width=34)
        update_photo_btn.grid(row=0,column=1)

        #right label frame-------------------------------
        right_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman ",12,"bold"))
        right_frame.place(x=760,y=10,width=730,height=525) 

        img_right = Image.open(r"C:\Users\shiva\Desktop\advanced attendence system\images\image16.jpg")
        img_right = img_right.resize((730,80),Image.ADAPTIVE)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        flb_1 = Label(right_frame,image=self.photoimg_right)
        flb_1.place(x=10,y=5,width=710,height=80)

        #search system---------------------------------------------------
        search_frame = LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman ",12,"bold"))
        search_frame.place(x=10,y=90,width=710,height=70)
        
        #-----------------------------------------------------------------
        search_label=Label(search_frame,text="Search By",font=("times new roman",12,"bold"),bg="red",fg="white")
        search_label.grid(row=0,column=0,padx=10,pady=10)

        #------------------------------------------------------------------
        search_combo=ttk.Combobox(search_frame,font=("times new roman",12,"bold"),state="readonly",width=15)
        search_combo["values"]=("Select","Roll No","Phone No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=5,sticky=W)

        #------------------------------------------------------------------
        search_entry=ttk.Entry(search_frame,width=20,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        search_btn=Button(search_frame,text="Search",font=("times new roman",12,"bold"),bg="blue",fg="white",width=12)
        search_btn.grid(row=0,column=3,padx=7)

        saveAll_btn=Button(search_frame,text="Save All",font=("times new roman",12,"bold"),bg="blue",fg="white",width=12)
        saveAll_btn.grid(row=0,column=4,padx=7)

        #table frame---------------------------------------------------------
        table_frame = Frame(right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=10,y=170,width=710,height=320)

        #creating scroll bar------------------------------------------------
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)


        #showing hidder----------------------------------------------------
        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentId")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="Roll No")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="Dob")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"] = "headings"

        #width set-----------------------------------------------------------
        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=150)
        

        self.student_table.pack(fill=BOTH,expand=1)
        #binding----------------------------------
        self.student_table.bind("<ButtonRelease>",self.get_cursor)

        self.fetch_data()

    #function for data entry-------------------------------
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Field are Required",parent=self.root)
        else:
            try:    
                conn = mysql.connector.connect(host="localhost",username="root",password="#shiva@#465#",database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                self.var_dep.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_semester.get(),
                                                                                                                self.var_std_id.get(),
                                                                                                                self.var_std_name.get(),
                                                                                                                self.var_div.get(),
                                                                                                                self.var_roll.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_dob.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_phone.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_teacher.get(),
                                                                                                                self.var_radio1.get()
                                                                                                            ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Sucess","Student details has been added Successfully",parent=self.root)

            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)        

    #fetching data from data base--------------------------------------------------------------
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="#shiva@#465#",database="face_recognizer")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close() 

    #for cursor-------------------------------------------------------------------------------           
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_semester.set(data[3])
        self.var_std_id.set(data[4])
        self.var_std_name.set(data[5])
        self.var_div.set(data[6])
        self.var_roll.set(data[7])
        self.var_gender.set(data[8])
        self.var_dob.set(data[9])
        self.var_email.set(data[10])
        self.var_phone.set(data[11])
        self.var_address.set(data[12])
        self.var_teacher.set(data[13])
        self.var_radio1.set(data[14])

    #update function------------------------------------------------
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Field are Required",parent=self.root)         
        else:
            try:
                update=messagebox.askyesno("update","Do you want to update this student datails",parent=self.root)
                if update>0:
                    conn = mysql.connector.connect(host="localhost",username="root",password="#shiva@#465#",database="face_recognizer")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(

                                                                                                                                                                                                                          self.var_dep.get(),
                                                                                                                                                                                                                          self.var_course.get(),
                                                                                                                                                                                                                          self.var_year.get(),
                                                                                                                                                                                                                          self.var_semester.get(),
                                                                                                                                                                                                                          self.var_std_name.get(),
                                                                                                                                                                                                                          self.var_div.get(),
                                                                                                                                                                                                                          self.var_roll.get(),
                                                                                                                                                                                                                          self.var_gender.get(),
                                                                                                                                                                                                                          self.var_dob.get(),
                                                                                                                                                                                                                          self.var_email.get(),
                                                                                                                                                                                                                          self.var_phone.get(),
                                                                                                                                                                                                                          self.var_address.get(),
                                                                                                                                                                                                                          self.var_teacher.get(),
                                                                                                                                                                                                                          self.var_radio1.get(),
                                                                                                                                                                                                                          self.var_std_id.get(),
                                                                                                                                                                                                                        
                                                                                                                                                                                                                        
                                                                                                                                                                                                                        
                                                                                                                                                                                                               
                                                                                                                                                                                                                        ))
                else:
                    if not update:
                        return
                messagebox.showinfo("Success""Student details successfully update!",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)           


    #----------------------------------------------------------------------------------------------------------------
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(host="localhost",username="root",password="#shiva@#465#",database="face_recognizer")
                    my_cursor = conn.cursor()
                    sql="delete from student where Student_id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student detials",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
    #reset function-----------------------------------------------------------------------------                           
    def reset_data(self):
        self.var_dep.set("Select Department"),
        self.var_course.set("Select Course"),
        self.var_year.set("Select Year"),
        self.var_semester.set("Select Semester"),
        self.var_std_id.set(""),
        self.var_std_name.set(""),
        self.var_div.set("Select Division"),
        self.var_roll.set(""),
        self.var_gender.set("Male"),
        self.var_dob.set(""),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_address.set(""),
        self.var_teacher.set(""), 
        self.var_radio1.set("")


    #generate data set and take a photo sample  ---------------------------------------------------------    
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Field are Required",parent=self.root)         
        else:
            try:
                conn = mysql.connector.connect(host="localhost",username="root",password="#shiva@#465#",database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(

                                                                                                                                                                                                                          self.var_dep.get(),
                                                                                                                                                                                                                          self.var_course.get(),
                                                                                                                                                                                                                          self.var_year.get(),
                                                                                                                                                                                                                          self.var_semester.get(),
                                                                                                                                                                                                                          self.var_std_name.get(),
                                                                                                                                                                                                                          self.var_div.get(),
                                                                                                                                                                                                                          self.var_roll.get(),
                                                                                                                                                                                                                          self.var_gender.get(),
                                                                                                                                                                                                                          self.var_dob.get(),
                                                                                                                                                                                                                          self.var_email.get(),
                                                                                                                                                                                                                          self.var_phone.get(),
                                                                                                                                                                                                                          self.var_address.get(),
                                                                                                                                                                                                                          self.var_teacher.get(),
                                                                                                                                                                                                                          self.var_radio1.get(),
                                                                                                                                                                                                                          self.var_std_id.get()==id+1
                                                                                                                                                                                                                    ))    
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close() 
                #--- load predefined data on face frontals from opencv-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #1.3--scaling factor
                    #5----minimum neighbor

                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return  face_cropped                                                                                                                                                                                                    
                                                                                                                                                                                                                        
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Croped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets completed!!!")
            
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
                        





                                                            




        

        


        

                            












if __name__ == "__main__":
   root = Tk()
   obj = Student(root)
   root.mainloop()
