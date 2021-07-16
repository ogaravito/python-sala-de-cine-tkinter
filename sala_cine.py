from tkinter import *
from tkinter import messagebox

ventana = Tk()
ventana.title("SALA DE CINE")
filas = ['A','B','C','D','E','F','G','H']
sillas_reservadas=[]
lista_botones=[]

def reserva(silla):
    if silla in sillas_reservadas:
        messagebox.showerror("SILLA OCUPADA","La silla está reservada")
    else:
        respuesta = messagebox.askquestion("OK","¿Desea reservar?")
        if respuesta == 'yes':
            sillas_reservadas.append(silla)
            with open("data.txt", "a+") as f:
                txt_silla = silla+'\n'
                f.write(txt_silla)
            for j in lista_botones:
                if silla == j['text']:
                    j.configure(fg="red",bg="white")

with open('/home/ogaravito/python/olger/cine/data.txt', 'r') as f:
    for silla_reservada in f:
        sillas_reservadas.append(silla_reservada.strip('\n'))

for i in range(len(filas)):
    for j in range(1,11):
        silla = filas[i]+str(j)
        nombre = silla.lower()
        color_texto = 'red' if silla in sillas_reservadas else 'black'
        boton = Button(ventana, text=silla, command=lambda arg1=silla: reserva(arg1), fg=color_texto)
        boton.grid(row=1*i, column=1*j,)
        lista_botones.append(boton)

ventana.mainloop()