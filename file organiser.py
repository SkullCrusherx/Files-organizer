from tkinter import Tk,Label,Button,filedialog,Entry,Frame
import os
import shutil

root = Tk()
root.title("File Organiser")
root.geometry('250x170')
root.resizable(False, False)

#front level
lvl = Label(root,text='Welcome to File Orgsniser',background='#a87c03',font=("arial",13,'bold'))
lvl.pack()
root.config(background='#a87c03')

def open_File(): # Function
    global filepath
    filepath = filedialog.askdirectory()
    global files
    global lvl2
    files = os.listdir(filepath)
    lvl1 = Entry(root,background='#523d05',width=35,foreground="white")
    lvl1.insert(0, filepath)
    lvl1.place(x=25,y=73)

    lvl2 = Label(root,text = "Ready To Start!",background='#a87c03',font="arial")
    lvl2.place(x=80,y=135)

def start_managing():
    for file in files:
        filename, extension = os.path.splitext(file)
        extension = extension[1:]

        if os.path.exists(filepath + '/' + extension):
            shutil.move(filepath + '/' + file, filepath + '/' + extension + '/' + file)
            lvl2.config(text='Done')

        else:
            os.makedirs(filepath + '/' + extension)
            shutil.move(filepath + '/' + file, filepath + '/' + extension + '/' + file)
#button type 1
btn1 = Button(root,text="BROWSE",background='#691706',command=open_File,font=("arial",10,"bold"),foreground="white")
btn1.place(x=100,y=40)

#button type 2
btn = Button(root,text="START",background='#691706',command = start_managing,font=("arial",10,"bold"),width=7,fg="white")
btn.place(x=100,y=105)
print('help')

root.mainloop()


