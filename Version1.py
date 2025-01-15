#! /C:\Users\Admin\AppData\Local\Microsoft\WindowsApps\python.exe

import tkinter as tk

def mostrar_lista():
    # Obtener el contenido del campo de entrada y convertirlo en una lista
    lista_texto = entrada_lista.get()
    
    # Convertir el texto en una lista de elementos
    lista = lista_texto.split(",")
    
    # Mostrar la lista en la etiqueta de salida
    etiqueta_resultado.config(text=f"Lista ingresada: {lista}")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ingreso de Lista")

# Crear un campo de entrada
entrada_lista = tk.Entry(ventana, width=40)
entrada_lista.grid(row=0, column=0, padx=10, pady=10)

# Crear un botón para mostrar la lista
boton_mostrar = tk.Button(ventana, text="Finalizar", command=mostrar_lista)
boton_mostrar.grid(row=1, column=0, padx=10, pady=10)

# Crear una etiqueta para mostrar la lista ingresada
etiqueta_resultado = tk.Label(ventana, text="Lista ingresada:")
etiqueta_resultado.grid(row=2, column=0, padx=10, pady=10)

# Iniciar la interfaz gráfica
ventana.mainloop()