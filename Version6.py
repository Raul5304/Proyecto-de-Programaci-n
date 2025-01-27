#! /C:\Users\Admin\AppData\Local\Microsoft\WindowsApps\python.exe

import tkinter as tk
from tkinter import simpledialog, messagebox
from tkinter import ttk
import os
import random
import string

def mostrar_lista(event=None):
    lista_texto = entrada_lista.get()
    lista = lista_texto.split(",")
    etiqueta_resultado.config(text=f"Lista ingresada: {lista}")
    global lista_guardada
    lista_guardada = lista

def guardar_lista():
    nombre_archivo = simpledialog.askstring("Nombre del archivo", "Introduce el nombre del archivo (con extensión .txt):")
    if nombre_archivo:
        try:
            with open(nombre_archivo, 'w') as archivo:
                archivo.write(str(lista_guardada))
            etiqueta_resultado.config(text=f"Lista guardada en el archivo: {nombre_archivo}")
        except Exception as e:
            etiqueta_resultado.config(text=f"Error al guardar el archivo: {e}")

def cargar_lista():
    nombre_archivo = simpledialog.askstring("Nombre del archivo", "Introduce el nombre del archivo para cargar (con extensión .txt):")
    if nombre_archivo:
        try:
            with open(nombre_archivo, 'r') as archivo:
                contenido = archivo.read()
                lista = eval(contenido)
                entrada_lista.delete(0, tk.END)
                entrada_lista.insert(0, ",".join(str(x) for x in lista))
                etiqueta_resultado.config(text=f"Lista cargada desde el archivo: {nombre_archivo}")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo cargar el archivo: {e}")

def eliminar_archivo():
    nombre_archivo = simpledialog.askstring("Eliminar archivo", "Introduce el nombre del archivo para eliminar (con extensión .txt):")
    if nombre_archivo:
        try:
            if os.path.exists(nombre_archivo):
                os.remove(nombre_archivo)
                etiqueta_resultado.config(text=f"Archivo '{nombre_archivo}' eliminado correctamente.")
            else:
                messagebox.showerror("Error", f"El archivo '{nombre_archivo}' no existe.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo eliminar el archivo: {e}")

def mostrar_ayuda():
    # Crear un mensaje que explique la funcionalidad de cada botón
    mensaje_ayuda = (
        "Funcionalidades del programa:\n\n"
        "1. 'Finalizar': Ingresa una lista separada por comas, la cual se muestra en la etiqueta.\n"
        "2. 'Guardar Lista': Guarda la lista ingresada en un archivo de texto.\n"
        "3. 'Cargar Lista': Carga una lista desde un archivo de texto y la muestra en el campo de entrada.\n"
        "4. 'Eliminar Archivo': Elimina un archivo de texto especificado por el usuario.\n"
        "5. 'Generar Lista Aleatoria': Genera una lista con palabras aleatorias."
    )
    messagebox.showinfo("Ayuda", mensaje_ayuda)

def generar_lista_aleatoria():
    # Pedir al usuario el número de palabras
    num_palabras = simpledialog.askinteger("Número de palabras", "Introduce el número de palabras a generar:")
    if num_palabras:
        # Generar palabras aleatorias
        lista_aleatoria = [''.join(random.choices(string.ascii_lowercase, k=5)) for _ in range(num_palabras)]
        # Mostrar la lista generada en la etiqueta
        etiqueta_resultado.config(text=f"Lista aleatoria generada: {lista_aleatoria}")
        global lista_guardada
        lista_guardada = lista_aleatoria

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ingreso, Carga, Guardado y Eliminación de Lista")
ventana.geometry("600x550")  # Aumentar el ancho de la ventana para el botón adicional
ventana.config(bg="#f0f0f0")  # Fondo gris claro para una apariencia más moderna

# Usar un diseño grid más limpio
ventana.grid_columnconfigure(0, weight=1)
ventana.grid_columnconfigure(1, weight=1)  # Configuramos una segunda columna para los botones

# Crear un campo de entrada con estilo moderno
entrada_lista = ttk.Entry(ventana, font=("Helvetica", 12))
entrada_lista.grid(row=0, column=0, padx=20, pady=10, sticky="ew", columnspan=2)

# Crear un botón con estilo moderno
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 12), padding=10, relief="flat", background="#4CAF50", foreground="black")
style.map("TButton", background=[('active', '#45a049')])

# Crear botones con el estilo configurado
boton_mostrar = ttk.Button(ventana, text="Finalizar", command=mostrar_lista)
boton_mostrar.grid(row=1, column=0, padx=20, pady=10, sticky="ew")

# Botón para generar lista aleatoria (al lado del botón 'Finalizar')
boton_generar_aleatoria = ttk.Button(ventana, text="Generar Lista Aleatoria", command=generar_lista_aleatoria)
boton_generar_aleatoria.grid(row=1, column=1, padx=20, pady=10, sticky="ew")

boton_guardar = ttk.Button(ventana, text="Guardar Lista", command=guardar_lista)
boton_guardar.grid(row=2, column=0, padx=20, pady=10, sticky="ew", columnspan=2)

boton_cargar = ttk.Button(ventana, text="Cargar Lista", command=cargar_lista)
boton_cargar.grid(row=3, column=0, padx=20, pady=10, sticky="ew", columnspan=2)

boton_eliminar = ttk.Button(ventana, text="Eliminar Archivo", command=eliminar_archivo)
boton_eliminar.grid(row=4, column=0, padx=20, pady=10, sticky="ew", columnspan=2)

# Crear un botón de ayuda
boton_ayuda = ttk.Button(ventana, text="Ayuda", command=mostrar_ayuda)
boton_ayuda.grid(row=5, column=0, padx=20, pady=10, sticky="ew", columnspan=2)

# Crear una etiqueta con un estilo moderno
etiqueta_resultado = tk.Label(ventana, text="Lista ingresada:", font=("Helvetica", 12), bg="#f0f0f0")
etiqueta_resultado.grid(row=6, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

# Atributo global para almacenar la lista ingresada
lista_guardada = []

# Iniciar la interfaz gráfica
ventana.mainloop()
