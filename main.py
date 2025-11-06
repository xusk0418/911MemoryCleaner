from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import pyautogui
from time import sleep
import sys
st=0
def win():
    global rt
    rt=Toplevel(root)
    m1=Label(rt,image=imge)
    m2=Label(rt,image=imge)
    rt.attributes('-topmost',1)
    rt.resizable(0,0)
    rt.overrideredirect(True)
    rt.geometry(f'200x541+{root.weight-200}+{root.ny-100}')
    m1.place(x=0,y=0)
    m2.place(x=72,y=0)
class ImgTk(Tk):
    def __init__(self,img,**kw):
        super().__init__(**kw)
        imgsize=Image.open(img,mode='r')
        self.w,self.h=imgsize.size
        self.weight,self.height=pyautogui.size()
        wy=self.height-self.height%1000
        self.ny=wy
        self.wy=int(wy)
        self.geometry(str(self.w)+'x'+str(self.h)+'+-120+'+str(self.wy))
        self.img=img
        imgtk=ImageTk.PhotoImage(Image.open(img))
        img_back=Label(self,image=imgtk)
        img_back.image=imgtk
        img_back.place(x=0,y=0,relwidth=1,relheight=1)
        img_back['bg']='#f0f0f1'
        self.attributes('-transparent','#f0f0f1')
        self.overrideredirect(True)
        self.img_back=img_back
    def move(self,y):
        self.geometry(str(self.w)+'x'+str(self.h)+'+0+'+str(y))
root=ImgTk('pl.png')
#root.iconphoto(True,PhotoImage(file="icon.png"))
root.iconbitmap(sys.executable)
def move(event):
    if not st:
        print('move')
        x,root.ny=pyautogui.position()
        if root.ny<root.wy:
            root.ny=root.ny-root.height//1000*30
        else:
            root.ny=root.wy
        root.move(root.ny)
def focusin(event):
    root.geometry(str(root.w)+'x'+str(root.h)+'+0+'+str(root.ny))
def focusout(event):
    root.geometry(str(root.w)+'x'+str(root.h)+'+-120+'+str(root.ny))
def cm(event):
    global st
    sleep(0.3)
    if st==0:
        st=1
        win()
        print(1)
        i=0
        while i<(root.weight-100-root.w):
            root.geometry(str(root.w)+'x'+str(root.h)+f'+{i}+'+str(root.ny))
            root.update()
            sleep(0.001)
            i+=15
        sleep(2)
        focusout(0)
        rt.destroy()
        st=0
def tc(event):
    st=2
    print(2)
    if messagebox.askyesno("911内存释放工具","是否要退出"):
        sys.exit()
imge=ImageTk.PhotoImage(Image.open('m.png'))
root.bind('<ButtonRelease-1>',move)
root.bind('<Double-Button-1>',cm)
root.bind('<Button-3>',tc)
root.bind('<Enter>',focusin)
root.bind('<Leave>',focusout)
root.attributes('-topmost',1)
root.mainloop()