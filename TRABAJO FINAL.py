
# Creación de Aplicaciones básicas en Python
from tkinter import *

root = tk()
root.title("FERRETERIA EL TORNILLO FELIZ")

miframe = frame(root)
miframe.pack()


          # etiqueta DNI

obtenerDNI =stringVar()
lDNI=Label(miframe, text="DNI: ")
lDNI.grid(row=0, columna=0, sticky="e", pady=5, padx=5)
tDni = Entry(miFrame,textvariable=obtenerDNI)
tDni.grid(row=0, column=1, pady=5, padx=5)


         # etiqueta apellidos

obtenerApellido=StringVar()
lApellido = Label(miFrame, text="Apellido:")
lApellido.grid(row=1, column=0, sticky="e", pady=5, padx=5)
tApellido = Entry(miFrame,textvariable=obtenerApellido)
tApellido.grid(row=1, column=1, pady=5, padx=5)


            # etiqueta nombre

obtenerNombre=StringVar()
lNombre = Label(miFrame, text="Nombre:")
lNombre.grid(row=1, column=2, sticky="e", pady=5, padx=5)
tNombre = Entry(miFrame,textvariable=obtenerNombre)
tNombre.grid(row=1, column=3, pady=5, padx=5)  

            # etiqueta direccion 

obtenerDir=StringVar()
lDireccion = Label(miFrame, text="Dirección:")
lDireccion.grid(row=2, column=0, sticky="e", pady=5, padx=5)
tDireccion = Entry(miFrame,textvariable=obtenerDir)
tDireccion.grid(row=2, column=1, columnspan=3, sticky="we",pady=5, padx=5)


             # etiqueta telefono


obtenerTel=StringVar()
lTel = Label(miFrame, text="Telefono:")
lTel.grid(row=3, column=0, sticky="e", pady=5, padx=5)
tTel = Entry(miFrame,textvariable=obtenerTel)
tTel.grid(row=3, column=1,columnspan=3, sticky="we", pady=5, padx=5)