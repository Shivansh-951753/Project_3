from tkinter import*
import tkinter.messagebox as tkmb
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
import mysql.connector
import os
import numpy as np
import cv2

class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #title----------------------------------------------------
        title_lb1 = Label(self.root,text="!!!Developer!!!",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lb1.place(x=0,y=0,width=1530,height=60)

        #top image------------------------------------------------------
        img_top = Image.open(r"C:\Users\shiva\Desktop\advanced attendence system\images\image49.webp")
        img_top = img_top.resize((1530,730),Image.ADAPTIVE)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        flb_1 = Label(self.root,image=self.photoimg_top)
        flb_1.place(x=0,y=60,width=1530,height=730)

        #frame-------------------------------------------------
        main_frame = Frame(flb_1,bd=2,bg="white")
        main_frame.place(x=1030,y=0,width=500,height=600)

        img_2 = Image.open(r"C:\Users\shiva\Desktop\advanced attendence system\images\bholu.jpg")
        img_2 = img_2.resize((150,150),Image.ADAPTIVE)
        self.photoimg_2 = ImageTk.PhotoImage(img_2)

        flb_1 = Label(main_frame,image=self.photoimg_2)
        flb_1.place(x=300,y=0,width=150,height=150)

        #developer info--------------------------------------------
        dev_label=Label(main_frame,text="Hello my name is Shivansh Singh.",font=("times new roman",15,"bold"),bg="white",fg="blue")
        dev_label.place(x=0,y=5)

        dev_label=Label(main_frame,text="I am java developer.",font=("times new roman",15,"bold"),bg="white",fg="blue")
        dev_label.place(x=0,y=40)
        #------------------------------------------------------------------

        #img_2 = Image.open(r"C:\Users\shiva\Desktop\advanced attendence system\images\pandey.jpeg")
        #img_2 = img_2.resize((200,200),Image.ADAPTIVE)
        #self.photoimg_2 = ImageTk.PhotoImage(img_2)

        #flb_1 = Label(main_frame,image=self.photoimg_2)
        #flb_1.place(x=300,y=0,width=200,height=200)








if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()         