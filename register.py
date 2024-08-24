from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector





class Register_Window:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("register")

        #text variable-----------------------------------------
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()
        self.var_check=IntVar()


        #bgimage----------------------------------------------------------
        bg_img = Image.open(r"C:\Users\shiva\Desktop\advanced attendence system\images\image43.jpg")
        bg_img = bg_img.resize((1530,790),Image.ADAPTIVE)
        self.photobg_img = ImageTk.PhotoImage(bg_img)

        flb_1 = Label(self.root,image=self.photobg_img)
        flb_1.place(x=0,y=0,width=1530,height=790)

        #frame--------------------------------------------------
        frame = Frame(self.root,bg="white")
        frame.place(x=200,y=150,width=1118,height=500)

        img_1 = Image.open(r"C:\Users\shiva\Desktop\advanced attendence system\images\image36.png")
        img_1 = img_1.resize((400,500),Image.ADAPTIVE)
        self.photoimg_1 = ImageTk.PhotoImage(img_1)

        flb_1 = Label(frame,image=self.photoimg_1)
        flb_1.place(x=0,y=0,width=400,height=500)

        #-------------------------------------------
        L_1=Label(frame,text="REGISTER HERE:",font=("times new roman",18,"bold"),bg="white",fg="green")
        L_1.place(x=420,y=20,width=200,height=50)
        
        #--------------------------------------------

        #label and entry------------------------------
        #row 1------------------------------------------
        first_name=Label(frame,text="First Name:",font=("times new roman",15,"bold"),bg="white")
        first_name.place(x=500,y=80)

        self.first_name_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        self.first_name_entry.place(x=500,y=110,width=200)


        last_name=Label(frame,text="Last Name:",font=("times new roman",15,"bold"),bg="white")
        last_name.place(x=800,y=80)

        self.last_name_entry=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15,"bold"))
        self.last_name_entry.place(x=800,y=110,width=200)

        #row 2----------------------------------------------
        contact_no=Label(frame,text="Contact No:",font=("times new roman",15,"bold"),bg="white")
        contact_no.place(x=500,y=150)

        self.contact_no_entry=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15,"bold"))
        self.contact_no_entry.place(x=500,y=180,width=200)


        email=Label(frame,text="Email:",font=("times new roman",15,"bold"),bg="white")
        email.place(x=800,y=150)

        self.email_entry=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15,"bold"))
        self.email_entry.place(x=800,y=180,width=200)

        #row 3--------------------------------------------------------
        security_q=Label(frame,text="Security Questions:",font=("times new roman",15,"bold"),bg="white")
        security_q.place(x=500,y=220)

        self.security_q=ttk.Combobox(frame,font=("times new roman",14,"bold"),textvariable=self.var_securityQ,state="readonly",width=20,background="white",foreground="black")
        self.security_q["values"]=("Select Questions ","Your birth place","Your friend name","your pet name")
        self.security_q.current(0)
        self.security_q.place(x=500,y=260,width=200)


        security_a=Label(frame,text="Security Answer:",font=("times new roman",15,"bold"),bg="white")
        security_a.place(x=800,y=220)

        self.security_a_entry=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15,"bold"))
        self.security_a_entry.place(x=800,y=260,width=200)

        #row 4--------------------------------------------------------
        password=Label(frame,text="Password:",font=("times new roman",15,"bold"),bg="white")
        password.place(x=500,y=300)

        self.password_entry=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15,"bold"))
        self.password_entry.place(x=500,y=340,width=200)


        conform_password=Label(frame,text="Conform Password:",font=("times new roman",15,"bold"),bg="white")
        conform_password.place(x=800,y=300)

        self.conform_password_entry=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15,"bold"))
        self.conform_password_entry.place(x=800,y=340,width=200)

        #checkbox------------------------------------------------------
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree The Terms & Condition",font=("times new roman",12,"bold"),onvalue=1,offvalue=0,background="white")
        checkbtn.place(x=500,y=380)

        #button--------------------------------------------------------
        reg_img = Image.open(r"C:\Users\shiva\Desktop\advanced attendence system\images\image53.png")
        reg_img = reg_img.resize((150,50),Image.ADAPTIVE)
        self.photoreg_img = ImageTk.PhotoImage(reg_img)

        b1 = Button(frame,command=self.register_data,image=self.photoreg_img,cursor="hand2")
        b1.place(x=500,y=425,width=150,height=50)


        log_img = Image.open(r"C:\Users\shiva\Desktop\advanced attendence system\images\image52.jpeg")
        log_img = log_img.resize((150,50),Image.ADAPTIVE)
        self.photolog_img = ImageTk.PhotoImage(log_img)

        b1 = Button(frame,image=self.photolog_img,cursor="hand2")
        b1.place(x=800,y=425,width=150,height=50)

    #function declaration----------------------------------
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","All fields are required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","Password and Confirm Password must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree our terms and condition")
        else:
             conn = mysql.connector.connect(host="localhost",username="root",password="#shiva@#465#",database="face_recognizer")
             my_cursor = conn.cursor()
             query=("select * from register where email=%s")
             value=(self.var_email.get(),)
             my_cursor.execute(query,value)
             row=my_cursor.fetchone()
             if row!=None:
                 messagebox.showerror("Error","User already exist,please try another email")
             else:
                 my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                          self.var_fname.get(),
                                          self.var_lname.get(),
                                          self.var_contact.get(),
                                          self.var_email.get(),
                                          self.var_securityQ.get(),
                                          self.var_securityA.get(),
                                          self.var_pass.get()
                                        ))
             conn.commit()
             conn.close()
             messagebox.showinfo("Success","Register Successfully")

             
                     
            
                
             








if __name__ == "__main__":
    root = Tk()
    obj = Register_Window(root)
    root.mainloop()          