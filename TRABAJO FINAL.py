
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

miFrame1 = Frame(root)
miFrame1.pack()


          # etiqueta de codigo de prodecto


lCodigo = Label(miFrame1, text="Cod_Prod")
lCodigo.grid(row=4, column=0,sticky="e", pady=5, padx=5)
tCodigo1 = Entry(miFrame1, width=7)
tCodigo1.grid(row=5, column=0, pady=5, padx=5)
tCodigo2 = Entry(miFrame1, width=7)
tCodigo2.grid(row=6, column=0, pady=5, padx=5)
tCodigo3 = Entry(miFrame1, width=7)
tCodigo3.grid(row=7, column=0, pady=5, padx=5)


            # etiqueta descripcion 


lDes = Label(miFrame1, text="Descripción")
lDes.grid(row=4, column=1,sticky="ew", pady=5, padx=5)
tDes1 = Entry(miFrame1, width=7, state="readonly")
tDes1.grid(row=5, column=1, pady=5, padx=5)
tDes2 = Entry(miFrame1, width=7, state="readonly")
tDes2.grid(row=6, column=1, pady=5, padx=5)
tDes3 = Entry(miFrame1, width=7, state="readonly")
tDes3.grid(row=7, column=1, pady=5, padx=5)

           # etiqueta unidad


lUni = Label(miFrame1, text="Unidad")
lUni.grid(row=4, column=2,sticky="ew", pady=5, padx=5)
tUni1 = Entry(miFrame1, width=7, state="readonly")
tUni1.grid(row=5, column=2, pady=5, padx=5)
tUni2 = Entry(miFrame1, width=7, state="readonly")
tUni2.grid(row=6, column=2, pady=5, padx=5)
tUni3 = Entry(miFrame1, width=7, state="readonly")
tUni3.grid(row=7, column=2, pady=5, padx=5)