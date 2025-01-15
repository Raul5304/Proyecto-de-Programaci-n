#! /C:\Users\Admin\AppData\Local\Microsoft\WindowsApps\python.exe

import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox

def mostrar_lista(event=None):
    # Obtener el contenido del campo de entrada y convertirlo en una lista
    lista_texto = entrada_lista.get()
    
    # Convertir el texto en una lista de elementos
    lista = lista_texto.split(",")
    
    # Mostrar la lista en la etiqueta de salida
    etiqueta_resultado.config(text=f"Lista ingresada: {lista}")
    
    # Guardar la lista en un atributo global para usarla luego
    global lista_guardada
    lista_guardada = lista

def guardar_lista():
    # Pedir al usuario el nombre del archivo
    nombre_archivo = simpledialog.askstring("Nombre del archivo", "Introduce el nombre del archivo (con extensión .txt):")
    
    if nombre_archivo:
        try:
            # Guardar la lista en el archivo especificado
            with open(nombre_archivo, 'w') as archivo:
                archivo.write(str(lista_guardada))
            etiqueta_resultado.config(text=f"Lista guardada en el archivo: {nombre_archivo}")
        except Exception as e:
            etiqueta_resultado.config(text=f"Error al guardar el archivo: {e}")

def cargar_lista():
    # Pedir al usuario el nombre del archivo para cargar
    nombre_archivo = simpledialog.askstring("Nombre del archivo", "Introduce el nombre del archivo para cargar (con extensión .txt):")
    
    if nombre_archivo:
        try:
            # Abrir el archivo y cargar su contenido
            with open(nombre_archivo, 'r') as archivo:
                contenido = archivo.read()
                # Convertir el contenido en una lista
                lista = eval(contenido)  # Usamos eval para convertir la cadena en una lista
                # Mostrar el contenido en el campo de entrada
                entrada_lista.delete(0, tk.END)  # Limpiar el campo de entrada
                entrada_lista.insert(0, ",".join(str(x) for x in lista))  # Insertar la lista como texto en el campo de entrada
                etiqueta_resultado.config(text=f"Lista cargada desde el archivo: {nombre_archivo}")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo cargar el archivo: {e}")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ingreso, Carga y Guardado de Lista")

# Configurar el comportamiento de la ventana para expandirse con el tamaño de la pantalla
ventana.grid_columnconfigure(0, weight=1)  # Hacer que la columna 0 sea flexible
ventana.grid_rowconfigure(0, weight=0)  # Fijar el tamaño de la primera fila
ventana.grid_rowconfigure(1, weight=0)  # Fijar el tamaño de la segunda fila
ventana.grid_rowconfigure(2, weight=1)  # Permitir que la tercera fila expanda si es necesario

# Crear un campo de entrada que ocupe todo el ancho disponible
entrada_lista = tk.Entry(ventana, width=40)
entrada_lista.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

# Asignar el evento de presionar 'Enter' para ejecutar la función de finalizar
entrada_lista.bind("<Return>", mostrar_lista)

# Crear un botón para mostrar la lista
boton_mostrar = tk.Button(ventana, text="Finalizar", command=mostrar_lista)
boton_mostrar.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

# Crear un botón para guardar la lista en un archivo
boton_guardar = tk.Button(ventana, text="Guardar Lista", command=guardar_lista)
boton_guardar.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

# Crear un botón para cargar la lista desde un archivo
boton_cargar = tk.Button(ventana, text="Cargar Lista", command=cargar_lista)
boton_cargar.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

# Crear una etiqueta para mostrar la lista ingresada
etiqueta_resultado = tk.Label(ventana, text="Lista ingresada:")
etiqueta_resultado.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

# Atributo global para almacenar la lista ingresada
lista_guardada = []

# Iniciar la interfaz gráfica
ventana.mainloop()