from tkinter import*
from tkinter import ttk
import tkinter
import tkinter.messagebox
from PIL import Image,ImageTk
from attendance import Attendance
from developer import Developer
from help_desk import Help_Desk
from time import strftime
from datetime import datetime



class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

       
        #image1------------------------------------------------------------------------------------
        img_1 = Image.open(r"C:\Users\shiva\Desktop\advanced attendence system\images\image1.jpeg")
        img_1 = img_1.resize((510,150),Image.ADAPTIVE)
        self.photoimg_1 = ImageTk.PhotoImage(img_1)

        flb_1 = Label(self.root,image=self.photoimg_1)
        flb_1.place(x=0,y=0,width=510,height=150)


        #image2------------------------------------------------------------------------------------
        img_2 = Image.open(r"C:\Users\shiva\Desktop\advanced attendence system\images\image30.webp")
        img_2 = img_2.resize((510,150),Image.ADAPTIVE)
        self.photoimg_2 = ImageTk.PhotoImage(img_2)

        flb_1 = Label(self.root,image=self.photoimg_2)
        flb_1.place(x=510,y=0,width=510,height=150)
                                                         

        #image3------------------------------------------------------------------------------------
        img_3 = Image.open(r"C:\Users\shiva\Desktop\advanced attendence system\images\image1.jpeg")
        img_3 = img_1.resize((510,150),Image.ADAPTIVE)
        self.photoimg_3 = ImageTk.PhotoImage(img_3)

        flb_1 = Label(self.root,image=self.photoimg_3)
        flb_1.place(x=1020,y=0,width=510,height=150)


        #title-------------------------------------------------------------------------------------
        title_lb1 = Label(self.root,text="!!! WELCOME !!!",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lb1.place(x=0,y=150,width=1530,height=60)

        #time-------------------------------------------------
        def time():
            string = strftime('%H:%M:%S %p')  
            tlb1.config(text=string)
            #time function calling
            tlb1.after(1000,time)

        tlb1=Label(title_lb1,font=("times new roman",20,"bold"),bg="white",fg="red")
        tlb1.place(x=100,y=0,width=150,height=50)   
        time()



        #background image--------------------------------------------------------------------------
        bg_img = Image.open(r"C:\Users\shiva\Desktop\advanced attendence system\images\image46.jpg")
        bg_img = bg_img.resize((1530,570),Image.ADAPTIVE)
        self.photobg_img = ImageTk.PhotoImage(bg_img)

        flb_1 = Label(self.root,image=self.photobg_img)
        flb_1.place(x=0,y=210,width=1530,height=570)


        #attendance button----------------------------------------
        img_9 = Image.open(r"C:\Users\shiva\Desktop\advanced attendence system\images\image6.jpeg")
        img_9 = img_9.resize((180,180),Image.ADAPTIVE)
        self.photoimg_9 = ImageTk.PhotoImage(img_9)

        b6 = Button(self.root,image=self.photoimg_9,command=self.attendance,cursor="hand2")
        b6.place(x=800,y=280,width=180,height=180)

        b6_6 = Button(self.root,text="Attendance",cursor="hand2",command=self.attendance,font=("times new roman",18,"bold"),bg="white",fg="red")
        b6_6.place(x=800,y=460,width=180,height=30)


        #help desk button----------------------------------------
        img_10 = Image.open(r"C:\Users\shiva\Desktop\advanced attendence system\images\image7.png")
        img_10 = img_10.resize((180,180),Image.ADAPTIVE)
        self.photoimg_10 = ImageTk.PhotoImage(img_10)

        b7 = Button(self.root,image=self.photoimg_10,command=self.help_desk,cursor="hand2")
        b7.place(x=1080,y=280,width=180,height=180)

        b7_7 = Button(self.root,text="Help Desk",command=self.help_desk,cursor="hand2",font=("times new roman",18,"bold"),bg="white",fg="red")
        b7_7.place(x=1080,y=460,width=180,height=30)


        #developer button----------------------------------------
        img_11 = Image.open(r"C:\Users\shiva\Desktop\advanced attendence system\images\image10.jpeg")
        img_11 = img_11.resize((180,180),Image.ADAPTIVE)
        self.photoimg_11 = ImageTk.PhotoImage(img_11)

        b8 = Button(self.root,image=self.photoimg_11,command=self.developer,cursor="hand2")
        b8.place(x=800,y=560,width=180,height=180)

        b3_3 = Button(self.root,text="Developer",cursor="hand2",command=self.developer,font=("times new roman",18,"bold"),bg="white",fg="red")
        b3_3.place(x=800,y=740,width=180,height=30)


        #exit button----------------------------------------
        img_12 = Image.open(r"C:\Users\shiva\Desktop\advanced attendence system\images\image11.jpeg")
        img_12 = img_12.resize((180,180),Image.ADAPTIVE)
        self.photoimg_12 = ImageTk.PhotoImage(img_12)

        b9 = Button(self.root,image=self.photoimg_12,command=self.iExit,cursor="hand2")
        b9.place(x=1080,y=560,width=180,height=180)

        b4_4 = Button(self.root,text="Exit",command=self.iExit,cursor="hand2",font=("times new roman",18,"bold"),bg="white",fg="red")
        b4_4.place(x=1080,y=740,width=180,height=30)



    #BUTTON FUNCTION--------------------------------------
    def attendance(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def developer(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)

    def help_desk(self):
        self.new_window=Toplevel(self.root)
        self.app=Help_Desk(self.new_window)  

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure exit this project",parent=self.root)
        if self.iExit>0:
            self.root.destroy()
        else:
            return
              




        




                                                








if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()        