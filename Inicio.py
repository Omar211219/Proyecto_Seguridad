
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askdirectory, askopenfilenames
from tkinter import messagebox as MessageBox
import pefile
from os import remove
import sys,os

from resultado import result

window = Tk()
folderPath = StringVar()

#Create a list of files with full path

filename=""
filename2=""

def btn_clicked():
    global filename
    global filename2
    file_list = []
    list_warning = {}

    if filename!="":
        for folder, subfolder, files in os.walk(filename):
            for f in files:
                full_path = os.path.join(folder, f)

                if f.endswith('.exe') or f.endswith('.dll') or f.endswith('.sys/.drv') or f.endswith('.ocx') or f.endswith('.cpl') or f.endswith('.scr'):
                    file=pefile.PE(full_path)
                    file_list.append(f)
                    if file.get_warnings() != []:
                        list_warning[full_path] = file.get_warnings()
                    file.close()
        filename=""
        folderPath.set(filename)
        result(file_list, list_warning)

    elif filename2!="":
        if filename2.endswith('.exe') or filename2.endswith('.dll') or filename2.endswith('.sys/.drv') or filename2.endswith('.ocx') or filename2.endswith('.cpl') or filename2.endswith('.scr'):
            file=pefile.PE(filename2)
            file_list.append(filename2)
            if file.get_warnings() != []:
                list_warning[filename2] = file.get_warnings()
            file.close()
        filename2=""
        folderPath.set(filename)
        result(file_list, list_warning)
    else:
        MessageBox.showwarning("Alerta", "Ruta para analisis vacia.")

def callbackDirectory():
    global filename
    filename = askdirectory()
    folderPath.set(filename)

def callbackFile():
    global filename2
    filename2 = askopenfilenames()[0]
    folderPath.set(filename2)

window.geometry("400x400")
window.configure(bg = "#dadada")
canvas = Canvas(
    window,
    bg = "#dadada",
    height = 400,
    width = 400,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    200.0, 200.0,
    image=background_img)

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    152.0, 204.5,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0,
    textvariable=folderPath)

entry0.place(
    x = 44.0, y = 187,
    width = 216.0,
    height = 33)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 104, y = 267,
    width = 96,
    height = 29)

img1 = PhotoImage(file = f"img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = callbackFile,
    relief = "flat")

b1.place(
    x = 342, y = 187,
    width = 40,
    height = 35)

img2 = PhotoImage(file = f"img2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = callbackDirectory,
    relief = "flat")

b2.place(
    x = 280, y = 187,
    width = 40,
    height = 35)

window.resizable(False, False)
window.mainloop()