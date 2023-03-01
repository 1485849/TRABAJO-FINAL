
# Creación de Aplicaciones básicas en Python
from tkinter import *

root = tk()
root.title("FERRETERIA EL TORNILLO FELIZ")

miframe = frame(root)
miframe.pack()

obtenerDNI =stringVar()
lDNI=Label(miframe, text="DNI: ")
lDNI.grid(row=0, columna=0, sticky="e", pady=5, padx=5)
