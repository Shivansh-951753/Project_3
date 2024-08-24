from tkinter import*
import tkinter.messagebox as tkmb
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
import mysql.connector
import os
import numpy as np
import cv2



class Train_Data:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #title----------------------------------------------------
        title_lb1 = Label(self.root,text="TRAIN DATA SET",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lb1.place(x=0,y=0,width=1530,height=45)

        #top image------------------------------------------------------
        img_top = Image.open(r"C:\Users\shiva\Desktop\advanced attendence system\images\image22.webp")
        img_top = img_top.resize((1530,350),Image.ADAPTIVE)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        flb_1 = Label(self.root,image=self.photoimg_top)
        flb_1.place(x=0,y=45,width=1530,height=350)

        #-------------------------------------------------------------------------
        #img_lol1 = Image.open(r"C:\Users\shiva\Desktop\advanced attendence system\images\image1.jpeg")
        #img_lol1= img_lol1.resize((510,130),Image.ADAPTIVE)
        #self.photoimg_lol1 = ImageTk.PhotoImage(img_lol1)

        #flb_1 = Label(self.root,image=self.photoimg_lol1)
        #flb_1.place(x=0,y=365,width=510,height=105)

        #creating button---------------------------------------------------
        train_button=Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("times new roman",30,"bold"),bg="red",fg="white")
        train_button.place(x=0,y=395,width=1530,height=45)

        #-------------------------------------------------------------------------------------
        #img_lol2 = Image.open(r"C:\Users\shiva\Desktop\advanced attendence system\images\image1.jpeg")
        #img_lol2 = img_lol2.resize((510,130),Image.ADAPTIVE)
        #self.photoimg_lol2 = ImageTk.PhotoImage(img_lol2)

        #flb_1 = Label(self.root,image=self.photoimg_lol2)
        #flb_1.place(x=0,y=0,width=510,height=130)


        #bottom image-------------------------------------------------------------
        img_bottom = Image.open(r"C:\Users\shiva\Desktop\advanced attendence system\images\image23.jpeg")
        img_bottom = img_bottom.resize((1530,350),Image.ADAPTIVE)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        flb_1 = Label(self.root,image=self.photoimg_bottom)
        flb_1.place(x=0,y=440,width=1530,height=350)


        #-----------------------------------------------------
    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]
        
        for image in path:
            img=Image.open(image).convert('L') #gray scale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])


            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        #train classifier-------------------------------------------------
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        tkmb.showinfo("result","Training datasets completed!!")
               




if __name__ == "__main__":
    root = Tk()
    obj = Train_Data(root)
    root.mainloop()        