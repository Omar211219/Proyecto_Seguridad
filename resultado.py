from tkinter import *
from tkinter import messagebox as MessageBox
from os import remove

def result(file_list, list_warning):
    def btn_clicked1():
        window2.destroy()

    window2 = Toplevel() 

    window2.geometry("400x400")
    window2.configure(bg = "#dadada")
    canvas2 = Canvas(
        window2,
        bg = "#dadada",
        height = 400,
        width = 400,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas2.place(x = 0, y = 0)

    background_img2 = PhotoImage(file = f"backgroundResultado.png")
    background2 = canvas2.create_image(200.0, 200.0,image=background_img2)

    entry0_img2 = PhotoImage(file = f"img_textBox0Resultado.png")
    entry0_bg2 = canvas2.create_image(199.5, 200.0,image = entry0_img2)

    entry02 = Text(
        window2,
        bd = 0,
        bg = "#ffffff",
        highlightthickness = 0,
        height=5,
        width=50)

    entry02.place(
        x = 33.0, y = 70,
        width = 333.0,
        height = 258)

    img02 = PhotoImage(file = f"img0Resultado.png")
    b02 = Button(
        window2,
        image = img02,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_clicked1,
        relief = "flat")

    b02.place(
        x = 152, y = 350,
        width = 96,
        height = 29)

    texto="*** Archivos Analizados ***\n\n"
    if file_list!=[]:
        for n in file_list:
            texto+=n+"\n"

        texto+="\n*** Archivos Infectados ***\n\n"

        if list_warning!={}:
            for k in list_warning.keys() :
                texto+=k+"  :  "+" ".join(map(str, list_warning[k]))+"\n\n"
        else:
            texto+="No se detectaron amenazas"
    else:
        texto+="No se analizo ningun archivo porque ninguno termina en:\n.exe o .dll o .sys/.drv o .ocx o .cpl o .scr"
    entry02.insert(INSERT, texto)

    if list_warning != {}:
        MessageBox.showerror("Virus", "Se ha detectado una amenaza.")
        resultado = MessageBox.askquestion("Eliminar", "¿Desea eliminar el\los documento\s infectado\s?")
        if resultado == "yes":
            for k in list_warning.keys():
                remove(k)

    window2.resizable(False, False)
    window2.mainloop()  