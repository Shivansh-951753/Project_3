from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
from face_recognition import Face_Detection
from train import Train_Data
from main_1 import Face_Recognition_System
import os
from time import strftime
from datetime import datetime



class Face_Recognition:
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
        title_lb1 = Label(self.root,text=" !!!WELCOME!!! ",font=("times new roman",35,"bold"),bg="black",fg="white")
        title_lb1.place(x=0,y=150,width=1530,height=60)



        #background image--------------------------------------------------------------------------
        bg_img = Image.open(r"C:\Users\shiva\Desktop\advanced attendence system\images\image46.jpg")
        bg_img = bg_img.resize((1530,570),Image.ADAPTIVE)
        self.photobg_img = ImageTk.PhotoImage(bg_img)

        flb_1 = Label(self.root,image=self.photobg_img)
        flb_1.place(x=0,y=210,width=1530,height=570)

        #time-------------------------------------------------
        def time():
            string = strftime('%H:%M:%S %p')  
            tlb1.config(text=string)
            #time function calling
            tlb1.after(1000,time)

        tlb1=Label(title_lb1,font=("times new roman",20,"bold"),bg="black",fg="white")
        tlb1.place(x=100,y=0,width=150,height=50)   
        time()




        #student details button----------------------------------------
        img_4 = Image.open(r"C:\Users\shiva\Desktop\advanced attendence system\images\image4.jpg")
        img_4 = img_4.resize((180,180),Image.ADAPTIVE)
        self.photoimg_4 = ImageTk.PhotoImage(img_4)

        b1 = Button(self.root,image=self.photoimg_4,command=self.student_details,cursor="hand2")
        b1.place(x=800,y=280,width=180,height=180)

        b1_1 = Button(self.root,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",18,"bold"),bg="white",fg="red")
        b1_1.place(x=800,y=460,width=180,height=30)

        #face detect button----------------------------------------
        img_5 = Image.open(r"C:\Users\shiva\Desktop\advanced attendence system\images\image5.jpeg")
        img_5 = img_5.resize((180,180),Image.ADAPTIVE)
        self.photoimg_5 = ImageTk.PhotoImage(img_5)

        b2 = Button(self.root,image=self.photoimg_5,command=self.face_recognition,cursor="hand2")
        b2.place(x=1080,y=280,width=180,height=180)

        b2_2 = Button(self.root,text="Face Detector",command=self.face_recognition,cursor="hand2",font=("times new roman",18,"bold"),bg="white",fg="red")
        b2_2.place(x=1080,y=460,width=180,height=30)


        #train face  button----------------------------------------
        img_6 = Image.open(r"C:\Users\shiva\Desktop\advanced attendence system\images\image8.jpeg")
        img_6 = img_6.resize((180,180),Image.ADAPTIVE)
        self.photoimg_6 = ImageTk.PhotoImage(img_6)

        b3 = Button(self.root,image=self.photoimg_6,command=self.data_train,cursor="hand2")
        b3.place(x=800,y=560,width=180,height=180)

        b3_3 = Button(self.root,text="Train Data",command=self.data_train,cursor="hand2",font=("times new roman",18,"bold"),bg="white",fg="red")
        b3_3.place(x=800,y=740,width=180,height=30)


        #photos button----------------------------------------
        img_7 = Image.open(r"C:\Users\shiva\Desktop\advanced attendence system\images\image9.png")
        img_7 = img_7.resize((180,180),Image.ADAPTIVE)
        self.photoimg_7 = ImageTk.PhotoImage(img_7)

        b4 = Button(self.root,image=self.photoimg_7,command=self.open_img,cursor="hand2")
        b4.place(x=1080,y=560,width=180,height=180)

        b4_4 = Button(self.root,text="Photos",command=self.open_img,cursor="hand2",font=("times new roman",18,"bold"),bg="white",fg="red")
        b4_4.place(x=1080,y=740,width=180,height=30)


       #next page button--------------------------------------
        img_8 = Image.open(r"C:\Users\shiva\Desktop\advanced attendence system\images\image47.png")
        img_8 = img_8.resize((150,150),Image.ADAPTIVE)
        self.photoimg_8 = ImageTk.PhotoImage(img_8)

        b5_5 = Button(self.root,command=self.next_page,image=self.photoimg_8,cursor="hand2")
        b5_5.place(x=1340,y=420,width=150,height=150)

        b4_4 = Button(self.root,command=self.next_page,text="Next Page",cursor="hand2",font=("times new roman",18,"bold"),bg="white",fg="red")
        b4_4.place(x=1340,y=570,width=150,height=30)



    #-------------------modules button-----------------------
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def next_page(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition_System(self.new_window)

    def open_img(self):
        os.startfile("data")  

    def face_recognition(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Detection(self.new_window)   

    def data_train(self):
        self.new_window=Toplevel(self.root)
        self.app=Train_Data(self.new_window)    


                                                








if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()        