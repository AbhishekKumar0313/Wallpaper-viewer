from tkinter import *
from PIL import Image,ImageTk
import os

def next_img():
    global counter
    img_label.config(image=images[counter%len(images)])
    counter+=1
counter=1
root=Tk()
root.iconbitmap('favicon.ico')
root.title('Wallpaper viewer')
root.geometry('1000x1550')
root.configure(background='black')

files=os.listdir('Images')
# print(type(files))
images=[]
for img in files:
    img=Image.open(os.path.join('Images',img))
    resize_img=img.resize((800,600))
    images.append(ImageTk.PhotoImage(resize_img))

img_label=Label(root,image=images[0])
img_label.pack(pady=(35,10))
next=Button(root,text='Next',command=next_img)
next.pack(pady=20)
next.config(font=('Verdana',15,'bold'))

root.mainloop()