import tkinter
root = tkinter.Tk()
label = tkinter.Label(root,text="hello world")
label.pack()

button1 = tkinter.Button(root,
			anchor = tkinter.E,
			text = 'Button1',
			width = 40,
			height = 5)
button1.pack()
button2 = tkinter.Button(root,
			text = 'Button2',
			bg = 'blue')
button2.pack()
button3 = tkinter.Button(root,
			text = 'Button3',
			width = 14,
			height = 1)
button3.pack()
button4 = tkinter.Button(root,
			text = 'Button4',
			width = 60,
			height = 5,
			state = tkinter.DISABLED)
button4.pack()


entry1 = tkinter.Entry(root,
			show = '*',)
entry1.pack()
entry2 = tkinter.Entry(root,
			show = '#',
			width = 50)
entry2.pack()
entry3 = tkinter.Entry(root,
			bg = 'red',
			fg = 'blue')
entry3.pack()
entry4 = tkinter.Entry(root,
			selectbackground = 'red',
			selectforeground = 'gray')
entry4.pack()
entry5 = tkinter.Entry(root,
			state = tkinter.DISABLED)
entry5.pack()
edit1 = tkinter.Text(root,
			selectbackground = 'red',
            height = 5,
			selectforeground = 'gray')
edit1.pack()


label1 = tkinter.Label(root,
			anchor = tkinter.E,
			bg = 'blue',
			fg = 'red',
			text = 'Python',
			width = 30,
			height = 5)
label1.pack()
label2 = tkinter.Label(root,
			text = 'Python GUI\ntkinter',
			justify = tkinter.LEFT,
			width = 30,
			height = 5)
label2.pack()
label3 = tkinter.Label(root,
			text = 'Python GUI\ntkinter',
			justify = tkinter.RIGHT,
			width = 30,
			height = 1)
label3.pack()
label4 = tkinter.Label(root,
			text = 'Python GUI\ntkinter',
			justify = tkinter.CENTER,
			width = 30,
			height = 1)
label4.pack()


menu = tkinter.Menu(root)
submenu = tkinter.Menu(menu, tearoff=0)
submenu.add_command(label="Open")
submenu.add_command(label="Save")
submenu.add_command(label="Close")
menu.add_cascade(label="File", menu=submenu)
submenu = tkinter.Menu(menu, tearoff=0)
submenu.add_command(label="Copy")
submenu.add_command(label="Paste")
submenu.add_separator()
submenu.add_command(label="Cut")
menu.add_cascade(label="Edit", menu=submenu)
submenu = tkinter.Menu(menu, tearoff=0)
submenu.add_command(label="About")
menu.add_cascade(label="Help", menu=submenu)


def popupmenu(event):
    menu.post(event.x_root, event.y_root)
root.bind("<Button-3>", popupmenu)

import os
canvas = tkinter.Canvas(root,
                        width=600,
                        height=480,
                        bg='white')
im = tkinter.PhotoImage(file='python.gif')
canvas.create_image(300, 50, image=im)
canvas.create_text(302, 77,
                   text='Use Canvas'
                   , fill='gray')
canvas.create_text(300, 75,
                   text='Use Canvas',
                   fill='blue')
canvas.create_polygon(290, 114, 316, 114,
                      330, 130, 310, 146, 284, 146, 270, 130)
canvas.create_oval(280, 120, 320, 140,
                   fill='white')
canvas.create_line(250, 130, 350, 130)
canvas.create_line(300, 100, 300, 160)
canvas.create_rectangle(90, 190, 510, 410,
                        width=5)
canvas.create_arc(100, 200, 500, 400,
                  start=0, extent=240,
                  fill="pink")
canvas.create_arc(103, 203, 500, 400,
                  start=241, extent=118,
                  fill="red")
canvas.pack()

root.config(menu=menu)
root.mainloop()


