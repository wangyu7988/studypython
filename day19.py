from PIL import Image

imga = Image.open('a.jpg')
imgb = Image.open('b.jpg')

Image.blend(imga,imgb,0.5).show()


from PIL import Image

imga = Image.open('a.jpg')
imgb = Image.open('b.jpg')
mask = Image.open('c.jpg')

Image.composite(imga,imgb,mask).show()


def div2(v):
    return v//2
imga = Image.open('a.jpg')


Image.eval(imga,div2).show()


from PIL import Image
from PIL import ImageChops
imga = Image.open('a.jpg')
print('图像格式：',imga.format)
print('图像模式：',imga.mode)
print('图像尺寸：',imga.size)
print('图像通道列表：',imga.getbands())
# print('统计直方图列表：',imga.histogram())
imgb = imga.copy()

imgb.thumbnail((224,168))
imgb.show()

imgc = imga.copy()
region = imgb.crop((50,50,120,120))
imgc.paste(region,(130,130))
imgc.show()

img_output = Image.new('RGB',(448,168))
img_output.paste(imgb,(0,0))
img_output.show()
b = imgb.convert('CMYK')
img_output.paste(b,(224,0))
img_output.show()

flip = b.transpose(Image.FLIP_LEFT_RIGHT)
img_output.paste(flip,(224,0))
img_output.show()

b = imgb.convert('L')
img_output.paste(b,(224,0))
img_output.show()

b = ImageChops.offset(imgb,30)
#b = imgb.offset(30)
img_output.paste(b,(224,0))
img_output.show()

b = imgb.rotate(45)
img_output.paste(b,(224,0))
img_output.show()

chnls = imgb.split()
b = Image.merge('RGB',chnls[::-1])
img_output.paste(b,(224,0))
img_output.show()

from PIL import ImageFilter
b = imgb.filter(ImageFilter.GaussianBlur)
img_output.paste(b,(224,0))
img_output.show()

r,g,b = chnls
r_after = r.point(lambda i:i if i<100 else 255)
b = Image.merge("RGB",(r_after,g,b))
img_output.paste(b,(224,0))
img_output.show()

from PIL import Image
from PIL import ImageChops

imga = Image.open('a.jpg')
imgb = Image.open('b.jpg')

ImageChops.add(imga,imgb,1,0).show()
ImageChops.subtract(imga,imgb,1,0).show()
ImageChops.darker(imga,imgb).show()
ImageChops.lighter(imga,imgb).show()
ImageChops.multiply(imga,imgb).show()
ImageChops.screen(imga,imgb).show()
ImageChops.invert(imga).show()
ImageChops.difference(imga,imga).show()


from PIL import Image
from PIL import ImageEnhance

imga = Image.open('a.jpg')

w,h = imga.size
img_output = Image.new('RGB',(2*w,h))
img_output.paste(imga,(0,0))


nhc = ImageEnhance.Color(imga)
nhb = ImageEnhance.Brightness(imga)
for nh in [nhc,nhb]:
    for ratio in [0.6,1.8]:
        b = nh.enhance(ratio)
        img_output.paste(b,(w,0))
        img_output.show()
# ImageEnhance.Contrast(imga).show()
# ImageEnhance.Brightness(imga).show()
# ImageEnhance.Sharpness(imga).show()


from PIL import Image
from PIL import ImageFilter

imga = Image.open('a.jpg')

w,h = imga.size
img_output = Image.new('RGB',(2*w,h))
img_output.paste(imga,(0,0))

fltrs = []
fltrs.append(ImageFilter.EDGE_ENHANCE)
fltrs.append(ImageFilter.FIND_EDGES)
fltrs.append(ImageFilter.GaussianBlur(4))

for fltr in fltrs:
    r = imga.filter(fltr)
    img_output.paste(r,(w,0))
    img_output.show()


from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

a = Image.new('RGB',(200,200),'white')
drw = ImageDraw.Draw(a)
drw.rectangle((50,50,150,150),outline='red')
drw.text((60,60),'My First Draw',fill='green')
a.show()
# -*- coding:utf-8 -*-
# file: pyImageConv.py
#
import os                                       # 导入模块
from PIL import Image
import tkinter
import tkinter.filedialog
import tkinter.messagebox
class Window:                                       # 创建窗口
    def __init__(self):
        self.root = root = tkinter.Tk()                     # 创建组件
        label = tkinter.Label(root, text = '选择目录')
        label.place(x = 5, y = 5)
        self.entry = tkinter.Entry(root)
        self.entry.place(x=60, y = 5)
        self.buttonBrowser = tkinter.Button(root, text = '浏览',
                command = self.Browser)
        self.buttonBrowser.place(x=210, y = 5)
        frameF = tkinter.Frame(root)
        frameF.place(x = 5, y = 30)
        frameT = tkinter.Frame(root)
        frameT.place(x = 100, y = 30)
        self.fImage = tkinter.StringVar()                   # 生成关联变量
        self.tImage = tkinter.StringVar()
        self.status = tkinter.StringVar()
        self.fImage.set('.bmp')
        self.tImage.set('.bmp')
        labelFrom = tkinter.Label(frameF, text = 'From')
        labelFrom.pack(anchor='w')
        labelTo = tkinter.Label(frameT, text = 'To')
        labelTo.pack(anchor='w')
        frBmp = tkinter.Radiobutton(frameF, variable = self.fImage,
                value = '.bmp', text = 'BMP' )
        frBmp.pack(anchor='w')
        frJpg = tkinter.Radiobutton(frameF, variable = self.fImage,
                value = '.jpg', text = 'JPG' )
        frJpg.pack(anchor='w')
        frGif = tkinter.Radiobutton(frameF, variable = self.fImage,
                value = '.gif', text = 'GIF' )
        frGif.pack(anchor='w')
        frPng = tkinter.Radiobutton(frameF, variable = self.fImage,
                value = '.png', text = 'PNG' )
        frPng.pack(anchor='w')
        trBmp = tkinter.Radiobutton(frameT, variable = self.tImage,
                value = '.bmp', text = 'BMP' )
        trBmp.pack(anchor='w')
        trJpg = tkinter.Radiobutton(frameT, variable = self.tImage,
                value = '.jpg', text = 'JPG' )
        trJpg.pack(anchor='w')
        trGif = tkinter.Radiobutton(frameT, variable = self.tImage,
                value = '.gif', text = 'GIF' )
        trGif.pack(anchor='w')
        trPng = tkinter.Radiobutton(frameT, variable = self.tImage,
                value = '.png', text = 'PNG' )
        trPng.pack(anchor='w')
        self.buttonConv = tkinter.Button(root, text = '转换',
                command = self.Conv)
        self.buttonConv.place(x=80, y = 160)
        self.labelStatus = tkinter.Label(root,textvariable=self.status)
        self.labelStatus.place(x=50, y = 195)
    def MainLoop(self):                                 # 进入消息循环
        self.root.minsize(250,220)
        self.root.maxsize(250,220)
        self.root.mainloop()
    def Browser(self):                                  # 浏览目录
        directory = tkinter.filedialog.askdirectory(title='Python')
        if directory:
            self.entry.delete(0, tkinter.END)
            self.entry.insert(tkinter.END, directory)
    def Conv(self):                                     # 转换文件格式
        n = 0
        t = self.tImage.get()
        f = self.fImage.get()
        path = self.entry.get()
        if path == '':
            tkinter.messagebox.showerror('Python tkinter','请输入路径')
            return
        filenames = os.listdir(path)
        os.mkdir(path + '/' + t[-3:])
        for filename in filenames:
            if filename[-4:] == f:
                Image.open(path + '/' +filename).save(path +
                        '/' + t[-3:] + '/' + filename[:-4] + t)
                n = n + 1
        self.status.set('成功转换%d张图片' % n)
window = Window()
window.MainLoop()
# -*- coding:utf-8 -*-
# file: pyImageThumb.py
#
import os                                       # 导入模块
from PIL import Image
import tkinter
import tkinter.filedialog
import tkinter.messagebox

class Window:
    def __init__(self):
        self.root = root = tkinter.Tk()                     # 创建窗口
        self.Image = tkinter.StringVar()
        self.status = tkinter.StringVar()
        self.mstatus = tkinter.IntVar()
        self.fstatus = tkinter.IntVar()
        self.Image.set('bmp')
        self.mstatus.set(0)
        self.fstatus.set(0)
        label = tkinter.Label(root, text = '输入百分比')
        label.place(x = 5, y = 5)
        self.entryNew = tkinter.Entry(root)
        self.entryNew.place(x = 70, y = 5)
        self.checkM = tkinter.Checkbutton(root, text ='批量转换',
                command = self.OnCheckM,
                variable = self.mstatus,
                onvalue = 1,
                offvalue = 0)
        self.checkM.place(x = 5, y = 30)
        label = tkinter.Label(root, text = '选择文件')
        label.place(x = 5, y = 55)
        self.entryFile = tkinter.Entry(root)
        self.entryFile.place(x=60, y = 55)
        self.buttonBrowserFile = tkinter.Button(root, text = '浏览',
                command = self.BrowserFile)
        self.buttonBrowserFile.place(x=200, y = 55)
        label = tkinter.Label(root, text = '选择目录')
        label.place(x = 5, y = 80)
        self.entryDir = tkinter.Entry(root,
                state = tkinter.DISABLED)
        self.entryDir.place(x=60, y = 80)
        self.buttonBrowserDir = tkinter.Button(root, text = '浏览',
                command = self.BrowserDir,
                state = tkinter.DISABLED)
        self.buttonBrowserDir.place(x=200, y = 80)

        self.checkF = tkinter.Checkbutton(root, text ='改变文件格式',
                command = self.OnCheckF,
                variable = self.fstatus,
                onvalue = 1,
                offvalue = 0)
        self.checkF.place(x = 5, y = 110)
        frame = tkinter.Frame(root)
        frame.place(x = 10, y = 130)
        labelTo = tkinter.Label(frame, text = 'To')
        labelTo.pack(anchor='w')
        self.rBmp = tkinter.Radiobutton(frame, variable = self.Image,
                value = 'bmp', text = 'BMP',
                state = tkinter.DISABLED)
        self.rBmp.pack(anchor='w')
        self.rJpg = tkinter.Radiobutton(frame, variable = self.Image,
                value = 'jpg', text = 'JPG',
                state = tkinter.DISABLED)
        self.rJpg.pack(anchor='w')
        self.rGif = tkinter.Radiobutton(frame, variable = self.Image,
                value = 'gif', text = 'GIF',
                state = tkinter.DISABLED)
        self.rGif.pack(anchor='w')
        self.rPng = tkinter.Radiobutton(frame, variable = self.Image,
                value = 'png', text = 'PNG',
                state = tkinter.DISABLED)
        self.rPng.pack(anchor='w')
        self.buttonConv = tkinter.Button(root, text = '转换',
                command = self.Conv)
        self.buttonConv.place(x=100, y = 175)
        self.labelStatus = tkinter.Label(root,textvariable=self.status)
        self.labelStatus.place(x=80, y = 205)
    def MainLoop(self):                                 # 进入消息循环
        self.root.minsize(250,270)
        self.root.maxsize(250,250)
        self.root.mainloop()
    def BrowserDir(self):                                   # 选择路径
        directory = tkinter.filedialog.askdirectory(title='Python')
        if directory:
            self.entryDir.delete(0, tkinter.END)
            self.entryDir.insert(tkinter.END, directory)
    def BrowserFile(self):                                  # 选择文件
        file = tkinter.filedialog.askopenfilename(title = 'Python Music Player',
            filetypes=[('JPG', '*.jpg'), ('BMP', '*.bmp'),
                ('GIF', '*.gif'), ('PNG', '*.png')])
        if file:
            self.entryFile.delete(0, tkinter.END)
            self.entryFile.insert(tkinter.END, file)
    def OnCheckM(self):                                 # 设置组件状态
        if not self.mstatus.get():
            self.entryDir.config(state = tkinter.DISABLED)
            self.entryFile.config(state = tkinter.NORMAL)
            self.buttonBrowserDir.config(state = tkinter.DISABLED)
            self.buttonBrowserFile.config(state = tkinter.NORMAL)
        else:
            self.entryDir.config(state = tkinter.NORMAL)
            self.entryFile.config(state = tkinter.DISABLED)
            self.buttonBrowserDir.config(state = tkinter.NORMAL)
            self.buttonBrowserFile.config(state = tkinter.DISABLED)
    def OnCheckF(self):                                 # 设置组件状态
        if not self.fstatus.get():
            self.rBmp.config(state = tkinter.DISABLED)
            self.rJpg.config(state = tkinter.DISABLED)
            self.rGif.config(state = tkinter.DISABLED)
            self.rPng.config(state = tkinter.DISABLED)
        else:
            self.rBmp.config(state = tkinter.NORMAL)
            self.rJpg.config(state = tkinter.NORMAL)
            self.rGif.config(state = tkinter.NORMAL)
            self.rPng.config(state = tkinter.NORMAL)
    def Conv(self):                                     # 转换图片
        n = 0
        if self.mstatus.get():
            path = self.entryDir.get()
            if path == '':
                tkinter.messagebox.showerror('Python tkinter','请输入路径')
                return
            filenames = os.listdir(path)
            if self.fstatus.get():
                f = self.Image.get()
                for filename in filenames:
                    if filename[-3:] in ('bmp','jpg','gif','png'):
                        self.make(path + '/' + filename, f)
                        n = n + 1
            else:
                for filename in filenames:
                    if filename[-3:] in ('bmp','jpg','gif','png'):
                        self.make(path + '/' + filename)
                        n = n + 1
        else:
            file = self.entryFile.get()
            if file == '':
                tkinter.messagebox.showerror('Python tkinter','请选择文件')
                return
            if self.fstatus.get():
                f = self.Image.get()
                self.make(file, f)
                n = n + 1
            else:
                self.make(file)
                n = n + 1
        self.status.set('成功转换%d图片' % n)
    def make(self, file, format = None):                            # 生成缩略图
        im = Image.open(file)
        mode = im.mode
        if mode not in ('L', 'RGB'):
            im = im.convert('RGB')
        width, height = im.size
        s = self.entryNew.get()
        if s == '':
            tkMessageBox.showerror('Python tkinter','请输入百分比')
            return
        else:
            n = int(s)
        nwidth = int(width * n / 100)
        nheight = int(height * n / 100)
        thumb = im.resize((nwidth,nheight), Image.ANTIALIAS)
        if format:
            thumb.save(file[:(len(file) - 4)] + '_thumb.' + format)
        else:
            thumb.save(file[:(len(file) - 4)] + '_thumb' + file[-4:])
window = Window()
window.MainLoop()



# -*- coding:utf-8 -*-
# file: pyImageAddLogo.py
#
import os                                       # 导入模块
from PIL import Image
import tkinter
import tkinter.filedialog
import tkinter.messagebox

class Window:
    def __init__(self):
        self.root = root = tkinter.Tk()                     # 创建窗口
        self.Image = tkinter.StringVar()
        self.status = tkinter.StringVar()
        self.mstatus = tkinter.IntVar()
        self.fstatus = tkinter.IntVar()
        self.pstatus = tkinter.IntVar()
        self.Image.set('bmp')
        self.mstatus.set(0)
        self.fstatus.set(0)
        self.pstatus.set(0)
        label = tkinter.Label(root, text = 'Logo')
        label.place(x = 5, y = 5)
        self.entryLogo = tkinter.Entry(root)
        self.entryLogo.place(x = 50, y = 5)
        self.buttonBrowserLogo = tkinter.Button(root, text = '浏览',
                command = self.BrowserLogo)
        self.buttonBrowserLogo.place(x = 200, y = 5)
        self.checkM = tkinter.Checkbutton(root, text ='批量转换',
                command = self.OnCheckM,
                variable = self.mstatus,
                onvalue = 1,
                offvalue = 0)
        self.checkM.place(x = 5, y = 30)
        label = tkinter.Label(root, text = '选择文件')
        label.place(x = 5, y = 55)
        self.entryFile = tkinter.Entry(root)
        self.entryFile.place(x = 60, y = 55)
        self.buttonBrowserFile = tkinter.Button(root, text = '浏览',
                command = self.BrowserFile)
        self.buttonBrowserFile.place(x=200, y = 55)
        label = tkinter.Label(root, text = '选择目录')
        label.place(x = 5, y = 80)
        self.entryDir = tkinter.Entry(root,
                state = tkinter.DISABLED)
        self.entryDir.place(x=60, y = 80)
        self.buttonBrowserDir = tkinter.Button(root, text = '浏览',
                command = self.BrowserDir,
                state = tkinter.DISABLED)
        self.buttonBrowserDir.place(x=200, y = 80)

        self.checkF = tkinter.Checkbutton(root, text ='改变文件格式',
                command = self.OnCheckF,
                variable = self.fstatus,
                onvalue = 1,
                offvalue = 0)
        self.checkF.place(x = 5, y = 110)
        frame = tkinter.Frame(root)
        frame.place(x = 10, y = 130)
        labelTo = tkinter.Label(frame, text = '格式')
        labelTo.pack(anchor='w')
        self.rBmp = tkinter.Radiobutton(frame, variable = self.Image,
                value = 'bmp', text = 'BMP',
                state = tkinter.DISABLED)
        self.rBmp.pack(anchor='w')
        self.rJpg = tkinter.Radiobutton(frame, variable = self.Image,
                value = 'jpg', text = 'JPG',
                state = tkinter.DISABLED)
        self.rJpg.pack(anchor='w')
        self.rGif = tkinter.Radiobutton(frame, variable = self.Image,
                value = 'gif', text = 'GIF',
                state = tkinter.DISABLED)
        self.rGif.pack(anchor='w')
        self.rPng = tkinter.Radiobutton(frame, variable = self.Image,
                value = 'png', text = 'PNG',
                state = tkinter.DISABLED)
        self.rPng.pack(anchor='w')
        pframe = tkinter.Frame(root)
        pframe.place(x = 70, y = 130)
        labelPos = tkinter.Label(pframe, text = '位置')
        labelPos.pack(anchor = 'w')
        self.rLT = tkinter.Radiobutton(pframe, variable = self.pstatus,
                value = 0, text = '左上角')
        self.rLT.pack(anchor = 'w')
        self.rRT = tkinter.Radiobutton(pframe, variable = self.pstatus,
                value = 1, text = '右上角')
        self.rRT.pack(anchor = 'w')
        self.rLB = tkinter.Radiobutton(pframe, variable = self.pstatus,
                value = 2, text = '左下角')
        self.rLB.pack(anchor = 'w')
        self.rRB = tkinter.Radiobutton(pframe, variable = self.pstatus,
                value = 3, text = '右下角')
        self.rRB.pack(anchor = 'w')
        self.buttonAdd = tkinter.Button(root, text = '添加',
                command = self.Add)
        self.buttonAdd.place(x=180, y = 175)
        self.labelStatus = tkinter.Label(root,textvariable=self.status)
        self.labelStatus.place(x=150, y = 205)
    def MainLoop(self):                                 # 进入消息循环
        self.root.minsize(250,270)
        self.root.maxsize(250,270)
        self.root.mainloop()
    def BrowserLogo(self):
        file = tkinter.filedialog.askopenfilename(title = 'Python Music Player',
            filetypes=[('JPG', '*.jpg'), ('BMP', '*.bmp'),
                ('GIF', '*.gif'), ('PNG', '*.png')])
        if file:
            self.entryLogo.delete(0, tkinter.END)
            self.entryLogo.insert(tkinter.END, file)
    def BrowserDir(self):                                   # 选择路径
        directory = tkinter.filedialog.askdirectory(title='Python')
        if directory:
            self.entryDir.delete(0, tkinter.END)
            self.entryDir.insert(tkinter.END, directory)
    def BrowserFile(self):                                  # 选择文件
        file = tkinter.filedialog.askopenfilename(title = 'Python Music Player',
            filetypes=[('JPG', '*.jpg'), ('BMP', '*.bmp'),
                ('GIF', '*.gif'), ('PNG', '*.png')])
        if file:
            self.entryFile.delete(0, tkinter.END)
            self.entryFile.insert(tkinter.END, file)
    def OnCheckM(self):                                 # 设置组件状态
        if not self.mstatus.get():
            self.entryDir.config(state = tkinter.DISABLED)
            self.entryFile.config(state = tkinter.NORMAL)
            self.buttonBrowserDir.config(state = tkinter.DISABLED)
            self.buttonBrowserFile.config(state = tkinter.NORMAL)
        else:
            self.entryDir.config(state = tkinter.NORMAL)
            self.entryFile.config(state = tkinter.DISABLED)
            self.buttonBrowserDir.config(state = tkinter.NORMAL)
            self.buttonBrowserFile.config(state = tkinter.DISABLED)
    def OnCheckF(self):                                 # 设置组件状态
        if not self.fstatus.get():
            self.rBmp.config(state = tkinter.DISABLED)
            self.rJpg.config(state = tkinter.DISABLED)
            self.rGif.config(state = tkinter.DISABLED)
            self.rPng.config(state = tkinter.DISABLED)
        else:
            self.rBmp.config(state = tkinter.NORMAL)
            self.rJpg.config(state = tkinter.NORMAL)
            self.rGif.config(state = tkinter.NORMAL)
            self.rPng.config(state = tkinter.NORMAL)
    def Add(self):                                      # 处理图片
        n = 0
        if self.mstatus.get():
            path = self.entryDir.get()
            if path == '':
                tkinter.messagebox.showerror('Python tkinter','请输入路径')
                return
            filenames = os.listdir(path)
            if self.fstatus.get():
                f = self.Image.get()
                for filename in filenames:
                    if filename[-3:] in ('bmp','jpg','gif','png'):
                        self.addlogo(path + '/' + filename, f)
                        n = n + 1
            else:
                for filename in filenames:
                    if filename[-3:] in ('bmp','jpg','gif','png'):
                        self.addlogo(path + '/' + filename)
                        n = n + 1
        else:
            file = self.entryFile.get()
            if file == '':
                tkinter.messagebox.showerror('Python tkinter','请选择文件')
                return
            if self.fstatus.get():
                f = self.Image.get()
                self.addlogo(file, f)
                n = n + 1
            else:
                self.addlogo(file)
                n = n + 1
        self.status.set('成功添加%d张图片' % n)
    def addlogo(self, file, format = None):                         # 向图片添加Logo
        logo = self.entryLogo.get()
        if logo == '':
            tkinter.messagebox.showerror('Python tkinter','请选择Logo')
            return
        im = Image.open(file)
        lo = Image.open(logo)
        imwidth = im.size[0]
        imheight = im.size[1]
        lowidth = lo.size[0]
        loheight = lo.size[1]
        pos = self.pstatus.get()
        if pos == 0:
            left = 0
            top = 0
            right = lowidth
            bottom = loheight
        elif pos == 1:
            left = imwidth - lowidth
            top = 0
            right = imwidth
            bottom = loheight
        elif pos == 2:
            left = 0
            top = imheight - loheight
            right = lowidth
            bottom = imheight
        else:
            left = imwidth - lowidth
            top = imheight - loheight
            right = imwidth
            bottom = imheight
        im.paste(lo, (left, top, right, bottom))
        if format:
            im.save(file[:(len(file) - 4)] + '_logo.' + format)
        else:
            im.save(file[:(len(file) - 4)] + '_logo' + file[-4:])
window = Window()
window.MainLoop()

