
from tkinter import*
import tkinter.messagebox as tkmb
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
import mysql.connector
from time import strftime
from datetime import datetime
import os
import datetime
import numpy as np
import cv2



class Face_Detection:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #----------------------------------------------
        title_lb1 = Label(self.root,text="Face Recognition",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lb1.place(x=0,y=0,width=1530,height=60)

        #first image-----------------------------------
        img_left = Image.open(r"C:\Users\shiva\Desktop\advanced attendence system\images\image36.png")
        img_left = img_left.resize((765,730),Image.ADAPTIVE)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        flb_1 = Label(self.root,image=self.photoimg_left)
        flb_1.place(x=0,y=60,width=765,height=730)

        #second image------------------------------------
        img_right = Image.open(r"C:\Users\shiva\Desktop\advanced attendence system\images\image39.jpg")
        img_right = img_right.resize((765,730),Image.ADAPTIVE)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        flb_1 = Label(self.root,image=self.photoimg_right)
        flb_1.place(x=765,y=60,width=765,height=730)

        #button----------------------------------------------------
        face_button=Button(flb_1,text="FACE RECOGNITION",command=self.face_recog,cursor="hand2",font=("times new roman",20,"bold"),bg="darkgreen",fg="white")
        face_button.place(x=235,y=650,width=295,height=60)
    #mark attendence------------------------------------
    def mark_attendance(self,i,r,n,d):
        with open("attendence.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now=datetime.datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")
                 






    #face recognition---------------------------------
    def face_recog(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn = mysql.connector.connect(host="localhost",username="root",password="#shiva@#465#",database="face_recognizer")
                my_cursor = conn.cursor()



                my_cursor.execute("select Name from student where Student_id="+str(id))
                n=my_cursor.fetchone()
                #try:
                     #n = "+".join(n)
                #except Exception as e:
                     #pass
                n="+".join(n)
                #n=str(n)

                my_cursor.execute("select Roll from student where Student_id="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)
                #r=str(r)

                my_cursor.execute("select Dep from student where Student_id="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)
                #d=str(d)

                my_cursor.execute("select Student_id from student where Student_id="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)
                #i=str(i)


                #if n == "None" or r == "None" or d == "None" or i == "None":
                    #cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    #cv2.putText(img,"Unknown Face",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                if confidence>77:
                    cv2.putText(img,f"ID:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(i,r,n,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)    
                    
                coord=[x,y,w,y]

            return coord
            
        def recognize(img,clf,faceCascade):
            coord=draw_boundray(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
            

        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret ,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome To Face Recognition",img)


            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()



if __name__ == "__main__":
    root = Tk()
    obj = Face_Detection(root)
    root.mainloop()         