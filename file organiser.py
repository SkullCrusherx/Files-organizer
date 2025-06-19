from tkinter import Tk,Label,Button,filedialog,Entry
import os
import shutil

root = Tk()
root.title("File Organiser")
root.geometry('250x170')
root.resizable(False, False)

#front level
lvl = Label(root,text='Welcome to File Orgsniser',background='#717fad',font=("arial",13,'bold'))
lvl.pack()
root.config(background='#717fad')


def openFile(): # Function
    global filepath
    filepath = filedialog.askdirectory()
    global files
    global lvl2
    files = os.listdir(filepath)
    lvl1 = Entry(root,text = filepath,background='#717fad')
    lvl1.place(x=100,y=70)
    
    lvl2 = Label(root,text = "Ready To Start!",background='#717fad')
    lvl2.place(x=100,y=130)

def startmanaging():
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
btn1 = Button(root,text="Browse",background='#cad5fa',command=openFile)
btn1.place(x=100,y=40)

#button type 2
btn = Button(root,text="start",background='#cad5fa',command = startmanaging)
btn.place(x=100,y=100)

root.mainloop()
