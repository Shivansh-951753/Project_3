from tkinter import*
import tkinter.messagebox as tkmb
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
import mysql.connector
import os
import numpy as np
import cv2

class Help_Desk:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #title----------------------------------------------------
        title_lb1 = Label(self.root,text="!!!Help Desk!!!",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lb1.place(x=0,y=0,width=1530,height=60)

        #top image------------------------------------------------------
        img_top = Image.open(r"C:\Users\shiva\Desktop\advanced attendence system\images\image48.webp")
        img_top = img_top.resize((1530,730),Image.ADAPTIVE)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        flb_1 = Label(self.root,image=self.photoimg_top)
        flb_1.place(x=0,y=60,width=1530,height=730)

        #email----------------------------------------------
        dev_label=Label(self.root,text="Email: Shivansh1072001@gmail.com ",font=("times new roman",25,"bold"),bg="white",fg="blue")
        dev_label.place(x=747,y=430)

        







if __name__ == "__main__":
    root = Tk()
    obj = Help_Desk(root)
    root.mainloop()         