from tkinter import Tk,Label,Button,filedialog
import os
import shutil


root = Tk()
root.title("File Organiser")
root.geometry('400x300')
root.resizable(False, False)

#front level
lvl = Label(root,text='Welcome to File Orgsniser',background='#717fad',font=2)
lvl.pack()
root.config(background='#717fad')



def openFile(): # Function
    global filepath
    filepath = filedialog.askdirectory()
    global files
    files = os.listdir(filepath)
    lvl1 = Label(root,text = filepath)
    lvl1.place(x=60,y=100)
    lvl2 = Label(root,text = "Ready To Start!")
    lvl2.place(x=160,y=130)

def startmanaging():
    for file in files:
        filename, extension = os.path.splitext(file)
        extension = extension[1:]

        if os.path.exists(filepath + '/' + extension):
            shutil.move(filepath + '/' + file, filepath + '/' + extension + '/' + file)
            lvl3 = Label(root,text = "Done!")
            lvl3.place(x=180,y=130)
        else:
            os.makedirs(filepath + '/' + extension)
            shutil.move(filepath + '/' + file, filepath + '/' + extension + '/' + file)


#button type 1
btn1 = Button(root,text="Browse",background='#cad5fa',command=openFile)
btn1.place(x=170,y=70)

#button type 2
btn = Button(root,text="start",background='#cad5fa',command = startmanaging)
btn.place(x=170,y=200)

root.mainloop()
