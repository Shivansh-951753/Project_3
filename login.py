from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from main import Face_Recognition

def main():
    win = Tk()
    app = Login_Window(win)
    win.mainloop()


class Login_Window:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("login")



        title_lb1 = Label(self.root,text="!!! WELCOME !!!",font=("times new roman",35,"bold"),bg="RoyalBlue3",fg="white")
        title_lb1.place(x=0,y=0,width=1530,height=60)

        #background image---------------------------------
        img = Image.open(r"C:\Users\shiva\Desktop\advanced attendence system\images\image40.jpg")
        img = img.resize((1530,730),Image.ADAPTIVE)
        self.photoimg = ImageTk.PhotoImage(img)

        flb_1 = Label(self.root,image=self.photoimg)
        flb_1.place(x=0,y=60,width=1530,height=730)

        #frame-----------------------------------------------
        frame = Frame(flb_1,bg="black")
        frame.place(x=850,y=217,width=349,height=350)

        #----------------------------------------------------
        img_2 = Image.open(r"C:\Users\shiva\Desktop\advanced attendence system\images\image51.jpg")
        img_2 = img_2.resize((50,50),Image.ADAPTIVE)
        self.photoimg_2 = ImageTk.PhotoImage(img_2)

        flb_1 = Label(frame,image=self.photoimg_2)
        flb_1.place(x=150,y=10,width=50,height=50)

        flb_1_1 = Label(frame,text="Get Started",font=("times new roman",12,"bold"),bg="black",fg="white")
        flb_1_1.place(x=120,y=65,width=100,height=50)
         
        #-------------------------------------------------------
        user_name=Label(frame,text="Username:",font=("times new roman",15,"bold"),bg="black",fg="white")
        user_name.place(x=0,y=120,width=120,height=50)

        style = ttk.Style()
        style.configure("BW.TLabel", background="white")

        self.user_name_entry=ttk.Entry(frame,style="BW.TLabel",font=("times new roman",15,"bold"))
        self.user_name_entry.place(x=110,y=130,width=200,height=30)

        password=Label(frame,text="Password:",font=("times new roman",15,"bold"),bg="black",fg="white")
        password.place(x=0,y=180,width=120,height=50)

        self.password_entry=ttk.Entry(frame,style="BW.TLabel",font=("times new roman",15,"bold"))
        self.password_entry.place(x=110,y=190,width=200,height=30)

        #login button------------------------------------------------
        login_btn=Button(frame,text="Login",command=self.login,font=("times new roman",15,"bold"),bg="red",fg="white",bd=3,activeforeground="white",activebackground="red")
        login_btn.place(x=130,y=240,width=100,height=30)

        #register----------------------------------------
        register_btn=Button(frame,command=self.register_window,text="New User Register",font=("times new roman",12,"bold"),bg="black",fg="white",bd=0,activeforeground="white",activebackground="black")
        register_btn.place(x=80,y=280,width=200,height=30)

        #forget button---------------------------------------
        forget_btn=Button(frame,command=self.forget_password_window,text="Forget Password",font=("times new roman",12,"bold"),bg="black",fg="white",bd=0,activeforeground="white",activebackground="black")
        forget_btn.place(x=80,y=310,width=200,height=30)

    def new_method(self):
        style = ttk.Style()
        return style
    
    #-------------------------------------------------------
    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register_Window(self.new_window)


    #login function-----------------------------------------
    def login(self):
        if self.user_name_entry.get()=="" or self.password_entry.get()=="":
            messagebox.showerror("Error","All fields are required")
        elif self.user_name_entry.get()=="kapu" or self.password_entry.get()=="ashu":
            messagebox.showerror("Success","Welcome to codewithkiran channel please subscribe my channel")
        else:
            conn = mysql.connector.connect(host="localhost",username="root",password="#shiva@#465#",database="face_recognizer")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                                                                                       self.user_name_entry.get(),
                                                                                       self.password_entry.get()
                                                                                        
                                                                                        

                                                                                      ))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username and Password")
            else:
                open_main=messagebox.askyesno("YesNo","Access only admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recognition(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()


    #reset password-------------------------------------
    def reset_pass(self):
        if self.security_q.get()=="Select":
            messagebox.showerror("Error","Select the Security Question",parent=self.root2)
        elif self.security_a_entry.get()=="":
            messagebox.showerror("Error","Please Enter the Answer",parent=self.root2)
        elif self.reset_pass_word_entry.get()=="":
            messagebox.showerror("Error","Please Enter the New Password",parent=self.root2)
        else:
            conn = mysql.connector.connect(host="localhost",username="root",password="#shiva@#465#",database="face_recognizer")
            my_cursor = conn.cursor()
            query=("select * from register where email=%s and securityQ=%s and securityA=%s" )
            value=(self.user_name_entry.get(),self.security_q.get(),self.security_a_entry.get())
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row=="None":
                messagebox.showerror("Error","Please Enter the Correct Answer",parent=self.root2)
            else:
                query=("update register set password=%s where email=%s")
                value=(self.reset_pass_word_entry.get(),self.user_name_entry.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your password has been reset, Please login with new password",parent=self.root2)
                self.root2.destroy()


            

    #forget password----------------------------------------------
    def forget_password_window(self):
        if self.user_name_entry.get()=="":
            messagebox.showerror("Error","Please Enter the Email address to reset your password")
        else:
            conn = mysql.connector.connect(host="localhost",username="root",password="#shiva@#465#",database="face_recognizer")
            my_cursor = conn.cursor()
            query=("select * from register where email=%s")
            value=(self.user_name_entry.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("Error","Please Enter the Valid Email address to reset your password")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x450+610+170")
                #----------------------------------------------------------------------------------------------------
                l=Label(self.root2,text="Forget Password",font=("times new roman",20,"bold"),bg="white",fg="red")
                l.place(x=0,y=10,relwidth=1)
                #----------------------------------------------------------------------------------------------------
                security_q=Label(self.root2,text="Security Questions:",font=("times new roman",15,"bold"),bg="white")
                security_q.place(x=20,y=70)

                self.security_q=ttk.Combobox(self.root2,font=("times new roman",14,"bold"),state="readonly",width=20,background="white",foreground="black")
                self.security_q["values"]=("Select Questions ","Your birth place","Your friend name","your pet name")
                self.security_q.current(0)
                self.security_q.place(x=20,y=120,width=200)
                #---------------------------------------------------------------------------------------------------
                security_a=Label(self.root2,text="Security Answer:",font=("times new roman",15,"bold"),bg="white")
                security_a.place(x=20,y=170)

                self.security_a_entry=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.security_a_entry.place(x=20,y=220,width=200)
                #--------------------------------------------------------------------------------------------------------
                reset_pass_word=Label(self.root2,text="Reset Password:",font=("times new roman",15,"bold"),bg="white")
                reset_pass_word.place(x=20,y=270)

                self.reset_pass_word_entry=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.reset_pass_word_entry.place(x=20,y=320,width=200)

                #--------------------------------------------------------------------------------------------------------
                login_btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("times new roman",15,"bold"),bg="red",fg="white",bd=3,activeforeground="white",activebackground="red")
                login_btn.place(x=110,y=370,width=100,height=30)
                



                






    

            


        
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

        b1 = Button(frame,command=self.return_login,image=self.photolog_img,cursor="hand2")
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


    #next page login--------------------------------------------------------------
    def return_login(self):
        self.root.destroy()

                         

           
          














if __name__ == "__main__":
    main()
            