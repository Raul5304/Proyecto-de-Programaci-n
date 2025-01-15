# Logs de chat con IA

1. Hazme un codigo en Python en el que utilizando TKinter, me permita introducir una lista, y visualizarla al presionar un botón de finalización.

    ¡Claro! A continuación te dejo un ejemplo de código en Python usando Tkinter para crear una interfaz en la que puedes introducir una lista de elementos, y al presionar un botón, se visualizará la lista ingresada en la interfaz:

    import tkinter as tk

    def mostrar_lista():
        # Obtener el contenido del campo de entrada y convertirlo en una lista
        lista_texto = entrada_lista.get()

        # Convertir el texto en una lista de elementos
        lista = lista_texto.split(",")
        
        # Mostrar la lista en la etiqueta de salida
        etiqueta_resultado.config(text=f"Lista ingresada: {lista}")

   Crear la ventana principal

    ventana = tk.Tk()
    ventana.title("Ingreso de Lista")

   Crear un campo de entrada

    entrada_lista = tk.Entry(ventana, width=40)
    entrada_lista.grid(row=0, column=0, padx=10, pady=10)

   Crear un botón para mostrar la lista

    boton_mostrar = tk.Button(ventana, text="Finalizar", command=mostrar_lista)
    boton_mostrar.grid(row=1, column=0, padx=10, pady=10)

   Crear una etiqueta para mostrar la lista ingresada

    etiqueta_resultado = tk.Label(ventana, text="Lista ingresada:")
    etiqueta_resultado.grid(row=2, column=0, padx=10, pady=10)

   Iniciar la interfaz gráfica

    ventana.mainloop()
    Explicación del código:
    Ventana Principal: Usamos Tk() para crear la ventana principal de la interfaz gráfica.
    Campo de Entrada: Usamos tk.Entry() para crear un campo de texto donde el usuario podrá ingresar la lista como una cadena de texto separada por comas (ejemplo: "1,2,3,4").
    Botón de Finalización: Usamos tk.Button() para crear un botón que, al hacer clic, ejecutará la función mostrar_lista().
    Mostrar la Lista: Dentro de la función mostrar_lista(), tomamos el texto ingresado, lo dividimos en una lista usando el método split(",") y luego actualizamos la etiqueta etiqueta_resultado para mostrar la lista.
    Etiqueta de Resultado: Es una etiqueta donde se mostrará la lista ingresada.
    Ejemplo de uso:
    Si ingresas "1, 2, 3, 4" en el campo de texto y presionas el botón "Finalizar", la etiqueta mostrará: Lista ingresada: ['1', ' 2', ' 3', ' 4'].
    ¡Espero que esto te sea útil!

# -------------------------------------------------------------------------------------Fase 2-------------------------------------------------------------------------------------------------- #

1. Ahora modifica el código anterior para que al pulsar 'enter', ejecute la función de finalizar
    ¡Claro! Para que la función mostrar_lista() se ejecute al presionar la tecla Enter, podemos asociar el evento de presionar Enter al campo de entrada utilizando el método bind() de Tkinter.

    Aquí está el código modificado:

    import tkinter as tk

    def mostrar_lista(event=None):
        # Obtener el contenido del campo de entrada y convertirlo en una lista
        lista_texto = entrada_lista.get()
        
        # Convertir el texto en una lista de elementos
        lista = lista_texto.split(",")
        
        # Mostrar la lista en la etiqueta de salida
        etiqueta_resultado.config(text=f"Lista ingresada: {lista}")

    Crear la ventana principal
    ventana = tk.Tk()
    ventana.title("Ingreso de Lista")

    Crear un campo de entrada
    entrada_lista = tk.Entry(ventana, width=40)
    entrada_lista.grid(row=0, column=0, padx=10, pady=10)

    Asignar el evento de presionar 'Enter' para ejecutar la función de finalizar
    entrada_lista.bind("<Return>", mostrar_lista)

    Crear un botón para mostrar la lista (opcional, pero puedes dejarlo si lo prefieres)
    boton_mostrar = tk.Button(ventana, text="Finalizar", command=mostrar_lista)
    boton_mostrar.grid(row=1, column=0, padx=10, pady=10)

    Crear una etiqueta para mostrar la lista ingresada
    etiqueta_resultado = tk.Label(ventana, text="Lista ingresada:")
    etiqueta_resultado.grid(row=2, column=0, padx=10, pady=10)

    Iniciar la interfaz gráfica
    ventana.mainloop()
    Cambios realizados:
    bind("<Return>", mostrar_lista): Esta línea asocia el evento de presionar la tecla Enter (representada como "<Return>") con la función mostrar_lista. Cuando presiones Enter mientras el campo de entrada está activo, la función se ejecutará.
    Argumento event en mostrar_lista: El argumento event es necesario cuando se usa el evento de tecla (bind()), aunque no lo utilizamos en la función, debe ser incluido en la definición para que funcione correctamente.
    Ahora, al presionar Enter mientras el campo de texto está activo, la lista se mostrará sin necesidad de hacer clic en el botón. También puedes seguir usando el botón si lo prefieres. ¡Espero que esto sea lo que buscabas!

2. Modifica el código anterior para que ahora haya otro botón en el que al pulsarlo, se almacene la lista en un archivo externo, en el que tú tengas que introducir el nombre del archivo.
    ¡Claro! Vamos a modificar el código para agregar un segundo botón que permita almacenar la lista en un archivo externo. Para ello, se pedirá al usuario que ingrese el nombre del archivo y luego guardaremos la lista en ese archivo.

    Aquí tienes el código modificado:

    python
    Copiar código
    import tkinter as tk
    from tkinter import simpledialog

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

    Crear la ventana principal
    ventana = tk.Tk()
    ventana.title("Ingreso y Guardado de Lista")

    Crear un campo de entrada
    entrada_lista = tk.Entry(ventana, width=40)
    entrada_lista.grid(row=0, column=0, padx=10, pady=10)

    Asignar el evento de presionar 'Enter' para ejecutar la función de finalizar
    entrada_lista.bind("<Return>", mostrar_lista)

    Crear un botón para mostrar la lista
    boton_mostrar = tk.Button(ventana, text="Finalizar", command=mostrar_lista)
    boton_mostrar.grid(row=1, column=0, padx=10, pady=10)

    Crear un botón para guardar la lista en un archivo
    boton_guardar = tk.Button(ventana, text="Guardar Lista", command=guardar_lista)
    boton_guardar.grid(row=1, column=1, padx=10, pady=10)

    Crear una etiqueta para mostrar la lista ingresada
    etiqueta_resultado = tk.Label(ventana, text="Lista ingresada:")
    etiqueta_resultado.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    Atributo global para almacenar la lista ingresada
    lista_guardada = []

    Iniciar la interfaz gráfica
    ventana.mainloop()
    Cambios realizados:
    guardar_lista(): Esta nueva función se activa cuando presionas el botón "Guardar Lista". Pide al usuario que ingrese el nombre del archivo mediante un cuadro de diálogo simpledialog.askstring(). Luego, guarda la lista en ese archivo con la extensión .txt (o la que el usuario ingrese).

    simpledialog.askstring(): Este método muestra una ventana emergente en la que el usuario puede introducir el nombre del archivo.

    Atributo global lista_guardada: La lista ingresada se guarda en la variable global lista_guardada para que pueda ser utilizada más tarde cuando el usuario quiera guardar la lista en un archivo.

    Botón "Guardar Lista": Se agrega este botón que, al presionarlo, guarda la lista en el archivo proporcionado por el usuario.

    Flujo:
    El usuario ingresa una lista en el campo de texto y presiona Enter o hace clic en "Finalizar". La lista se muestra en la interfaz.
    Al presionar "Guardar Lista", se le pide al usuario que ingrese el nombre del archivo. La lista se guarda en ese archivo en formato de texto.
    Ejemplo de uso:
    Si ingresas "1, 2, 3, 4" y luego presionas el botón "Guardar Lista", se abrirá un cuadro de entrada donde podrás escribir el nombre del archivo, como "mi_lista.txt". Luego, el contenido de la lista se guardará en ese archivo.
    Espero que este código cumpla con tus expectativas. ¡Déjame saber si necesitas más ajustes!

3. Modifica el código anterior para que el campo de entrada esté alineado con la anchura de la ventana, independientemente de sus dimensiones.
    ¡Por supuesto! Para hacer que el campo de entrada se ajuste automáticamente al ancho de la ventana, podemos usar el método columnspan y configurar la propiedad sticky de los widgets en el grid para que el campo de entrada ocupe todo el espacio disponible en la ventana.

    Aquí te dejo el código modificado para que el campo de entrada esté alineado con el ancho de la ventana:

    import tkinter as tk
    from tkinter import simpledialog

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

    Crear la ventana principal
    ventana = tk.Tk()
    ventana.title("Ingreso y Guardado de Lista")

    Configurar el comportamiento de la ventana para expandirse con el tamaño de la pantalla
    ventana.grid_columnconfigure(0, weight=1)  # Hacer que la columna 0 sea flexible
    ventana.grid_rowconfigure(0, weight=0)  # Fijar el tamaño de la primera fila
    ventana.grid_rowconfigure(1, weight=0)  # Fijar el tamaño de la segunda fila
    ventana.grid_rowconfigure(2, weight=1)  # Permitir que la tercera fila expanda si es necesario

    Crear un campo de entrada que ocupe todo el ancho disponible
    entrada_lista = tk.Entry(ventana, width=40)
    entrada_lista.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

    Asignar el evento de presionar 'Enter' para ejecutar la función de finalizar
    entrada_lista.bind("<Return>", mostrar_lista)

    Crear un botón para mostrar la lista
    boton_mostrar = tk.Button(ventana, text="Finalizar", command=mostrar_lista)
    boton_mostrar.grid(row=1, column=0, padx=10, pady=10)

    Crear un botón para guardar la lista en un archivo
    boton_guardar = tk.Button(ventana, text="Guardar Lista", command=guardar_lista)
    boton_guardar.grid(row=1, column=1, padx=10, pady=10)

    Crear una etiqueta para mostrar la lista ingresada
    etiqueta_resultado = tk.Label(ventana, text="Lista ingresada:")
    etiqueta_resultado.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

    Atributo global para almacenar la lista ingresada
    lista_guardada = []

    Iniciar la interfaz gráfica
    ventana.mainloop()
    Cambios realizados:
    ventana.grid_columnconfigure(0, weight=1): Esto hace que la primera columna (donde está el campo de entrada) sea flexible, lo que significa que se expandirá para llenar el espacio disponible en la ventana.

    sticky="ew": Se ha añadido la propiedad sticky="ew" en el campo de entrada y en la etiqueta de resultado. Esto indica que el widget debe expandirse en ambas direcciones horizontales (este y oeste), haciendo que ocupe todo el ancho disponible de la ventana.

    ventana.grid_rowconfigure(): Se ha configurado la fila 0 y 1 con weight=0 para que su tamaño no cambie con la ventana, mientras que la fila 2 tiene weight=1 para que se expanda si es necesario (especialmente útil para la etiqueta de resultado).

    Resultado:
    El campo de entrada ahora se ajustará automáticamente al ancho de la ventana, independientemente de las dimensiones de la ventana, y también la etiqueta de resultado ocupará todo el ancho disponible. De esta manera, el diseño será más flexible y adaptable a cambios en el tamaño de la ventana.

    ¡Espero que esto te funcione como deseas! Si tienes alguna otra consulta o ajuste, no dudes en preguntar.

4. Ahora modifica el código anterior para que los botones estén alineados verticalmente uno encima del otro.
    ¡Claro! Para alinear los botones verticalmente uno encima del otro, podemos modificar la disposición en el grid y ajustar las posiciones de los botones para que se encuentren en la misma columna, pero en filas diferentes.

    Aquí tienes el código modificado:

    import tkinter as tk
    from tkinter import simpledialog

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

    Crear la ventana principal
    ventana = tk.Tk()
    ventana.title("Ingreso y Guardado de Lista")

    Configurar el comportamiento de la ventana para expandirse con el tamaño de la pantalla
    ventana.grid_columnconfigure(0, weight=1)  # Hacer que la columna 0 sea flexible
    ventana.grid_rowconfigure(0, weight=0)  # Fijar el tamaño de la primera fila
    ventana.grid_rowconfigure(1, weight=0)  # Fijar el tamaño de la segunda fila
    ventana.grid_rowconfigure(2, weight=1)  # Permitir que la tercera fila expanda si es necesario

    Crear un campo de entrada que ocupe todo el ancho disponible
    entrada_lista = tk.Entry(ventana, width=40)
    entrada_lista.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

    Asignar el evento de presionar 'Enter' para ejecutar la función de finalizar
    entrada_lista.bind("<Return>", mostrar_lista)

    Crear un botón para mostrar la lista
    boton_mostrar = tk.Button(ventana, text="Finalizar", command=mostrar_lista)
    boton_mostrar.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

    Crear un botón para guardar la lista en un archivo
    boton_guardar = tk.Button(ventana, text="Guardar Lista", command=guardar_lista)
    boton_guardar.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

    Crear una etiqueta para mostrar la lista ingresada
    etiqueta_resultado = tk.Label(ventana, text="Lista ingresada:")
    etiqueta_resultado.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

    Atributo global para almacenar la lista ingresada
    lista_guardada = []

    Iniciar la interfaz gráfica
    ventana.mainloop()
    Cambios realizados:
    Alineación vertical de los botones: Los botones "Finalizar" y "Guardar Lista" ahora están alineados en la misma columna (columna 0) pero en filas diferentes (row=1 y row=2 respectivamente). Esto hace que los botones se apilen verticalmente uno encima del otro.

    Ajuste de la propiedad sticky: La propiedad sticky="ew" de los botones asegura que estos se expandan a lo largo del eje horizontal (este-oeste), ocupando todo el ancho disponible de la ventana.

    Resultado:
    El campo de entrada ocupa todo el ancho de la ventana.
    Los botones "Finalizar" y "Guardar Lista" están alineados verticalmente, uno encima del otro, ocupando también todo el ancho disponible.
    La etiqueta de resultado sigue ocupando todo el ancho disponible en la parte inferior.
    Este ajuste debería hacer que la interfaz sea más clara y que los botones estén organizados de manera más coherente. ¡Espero que ahora funcione como deseas! Si tienes más preguntas o necesitas más modificaciones, ¡avísame!

# ------------------------------------------------------------------------------------Fase 3----------------------------------------------------------------------------------------------------#

1. Modifica el código anterior para que ahora haya un botón que te permita cargar una lista mediante el nombre del archivo.
    ¡Por supuesto! Vamos a modificar el código para añadir un nuevo botón que permita cargar una lista desde un archivo. Este botón abrirá un cuadro de diálogo donde podrás ingresar el nombre del archivo, y luego cargará el contenido de ese archivo, actualizando el campo de entrada con la lista almacenada en el archivo.

    Aquí tienes el código modificado:

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

    Crear la ventana principal
    ventana = tk.Tk()
    ventana.title("Ingreso, Carga y Guardado de Lista")

    Configurar el comportamiento de la ventana para expandirse con el tamaño de la pantalla
    ventana.grid_columnconfigure(0, weight=1)  # Hacer que la columna 0 sea flexible
    ventana.grid_rowconfigure(0, weight=0)  # Fijar el tamaño de la primera fila
    ventana.grid_rowconfigure(1, weight=0)  # Fijar el tamaño de la segunda fila
    ventana.grid_rowconfigure(2, weight=1)  # Permitir que la tercera fila expanda si es necesario

    Crear un campo de entrada que ocupe todo el ancho disponible
    entrada_lista = tk.Entry(ventana, width=40)
    entrada_lista.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

    Asignar el evento de presionar 'Enter' para ejecutar la función de finalizar
    entrada_lista.bind("<Return>", mostrar_lista)

    Crear un botón para mostrar la lista
    boton_mostrar = tk.Button(ventana, text="Finalizar", command=mostrar_lista)
    boton_mostrar.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

    Crear un botón para guardar la lista en un archivo
    boton_guardar = tk.Button(ventana, text="Guardar Lista", command=guardar_lista)
    boton_guardar.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

    Crear un botón para cargar la lista desde un archivo
    boton_cargar = tk.Button(ventana, text="Cargar Lista", command=cargar_lista)
    boton_cargar.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

    Crear una etiqueta para mostrar la lista ingresada
    etiqueta_resultado = tk.Label(ventana, text="Lista ingresada:")
    etiqueta_resultado.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

    Atributo global para almacenar la lista ingresada
    lista_guardada = []

    Iniciar la interfaz gráfica
    ventana.mainloop()
    Cambios realizados:
    Nuevo botón "Cargar Lista":

    Se agregó un botón que, al ser presionado, abre un cuadro de diálogo para pedir el nombre del archivo que se desea cargar.
    Si el archivo existe, se lee su contenido y se convierte en una lista. Esta lista se muestra luego en el campo de entrada.
    Función cargar_lista():

    Esta función pide al usuario que ingrese el nombre del archivo para cargar.
    Se usa eval() para convertir el contenido del archivo (que se espera que sea una representación de una lista en formato de cadena) de nuevo en una lista. Nota: eval() es útil cuando confiamos en el contenido del archivo, pero debe ser usado con precaución, ya que puede ejecutar código no deseado si el archivo es manipulado maliciosamente. Si no confías en el contenido del archivo, podrías considerar usar otras técnicas de deserialización como json.
    Manejo de errores:

    Si el archivo no existe o hay algún problema al leerlo, se mostrará un cuadro de mensaje de error usando messagebox.showerror().
    Flujo:
    El usuario puede ingresar una lista en el campo de texto y presionar el botón "Finalizar" o la tecla Enter para mostrar la lista.
    Puede guardar la lista ingresada en un archivo usando el botón "Guardar Lista".
    Puede cargar una lista desde un archivo utilizando el botón "Cargar Lista". Esto reemplazará el contenido del campo de entrada con la lista cargada.

    Ejemplo de archivo:
    El archivo debe tener una representación de lista en formato de texto, como por ejemplo:

    [1, 2, 3, 4]
    ¡Espero que esta modificación te sea útil! Si necesitas más cambios o tienes alguna duda, no dudes en preguntar.

# --------------------------------------------------------------------------------------Fase 4--------------------------------------------------------------------------------------------------#

1. Ahora modifica el código para que tenga un botón de 'eliminar' el cual te permita eliminar un archivo de listas introduciendo el nombre del archivo
    ¡Claro! Vamos a agregar un nuevo botón de "Eliminar", que permitirá al usuario eliminar un archivo de listas al introducir el nombre del archivo. Si el archivo existe, se eliminará; si no, se mostrará un mensaje de error.

    Aquí tienes el código modificado:

    python
    Copiar código
    import tkinter as tk
    from tkinter import simpledialog
    from tkinter import messagebox
    import os

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

    def eliminar_archivo():
        # Pedir al usuario el nombre del archivo a eliminar
        nombre_archivo = simpledialog.askstring("Eliminar archivo", "Introduce el nombre del archivo para eliminar (con extensión .txt):")
        
        if nombre_archivo:
            try:
                # Verificar si el archivo existe y eliminarlo
                if os.path.exists(nombre_archivo):
                    os.remove(nombre_archivo)
                    etiqueta_resultado.config(text=f"Archivo '{nombre_archivo}' eliminado correctamente.")
                else:
                    messagebox.showerror("Error", f"El archivo '{nombre_archivo}' no existe.")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo eliminar el archivo: {e}")

    Crear la ventana principal
    ventana = tk.Tk()
    ventana.title("Ingreso, Carga, Guardado y Eliminación de Lista")

    Configurar el comportamiento de la ventana para expandirse con el tamaño de la pantalla
    ventana.grid_columnconfigure(0, weight=1)  # Hacer que la columna 0 sea flexible
    ventana.grid_rowconfigure(0, weight=0)  # Fijar el tamaño de la primera fila
    ventana.grid_rowconfigure(1, weight=0)  # Fijar el tamaño de la segunda fila
    ventana.grid_rowconfigure(2, weight=1)  # Permitir que la tercera fila expanda si es necesario

    Crear un campo de entrada que ocupe todo el ancho disponible
    entrada_lista = tk.Entry(ventana, width=40)
    entrada_lista.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

    Asignar el evento de presionar 'Enter' para ejecutar la función de finalizar
    entrada_lista.bind("<Return>", mostrar_lista)

    Crear un botón para mostrar la lista
    boton_mostrar = tk.Button(ventana, text="Finalizar", command=mostrar_lista)
    boton_mostrar.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

    Crear un botón para guardar la lista en un archivo
    boton_guardar = tk.Button(ventana, text="Guardar Lista", command=guardar_lista)
    boton_guardar.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

    Crear un botón para cargar la lista desde un archivo
    boton_cargar = tk.Button(ventana, text="Cargar Lista", command=cargar_lista)
    boton_cargar.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

    Crear un botón para eliminar un archivo de lista
    boton_eliminar = tk.Button(ventana, text="Eliminar Archivo", command=eliminar_archivo)
    boton_eliminar.grid(row=4, column=0, padx=10, pady=10, sticky="ew")

    Crear una etiqueta para mostrar la lista ingresada
    etiqueta_resultado = tk.Label(ventana, text="Lista ingresada:")
    etiqueta_resultado.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

    Atributo global para almacenar la lista ingresada
    lista_guardada = []

    Iniciar la interfaz gráfica
    ventana.mainloop()
    Cambios realizados:
    Nuevo botón "Eliminar Archivo":
    Este botón se ha añadido para permitir la eliminación de un archivo especificando su nombre.
    Función eliminar_archivo():
    Esta función pide al usuario que ingrese el nombre del archivo que desea eliminar.
    Si el archivo existe, lo elimina usando os.remove().
    Si el archivo no existe, se muestra un mensaje de error usando messagebox.showerror().

    Manejo de errores:
    Si ocurre algún error al intentar eliminar el archivo (por ejemplo, permisos insuficientes), se muestra un mensaje de error adecuado.

    Flujo de la interfaz:
    El usuario puede ingresar una lista en el campo de texto y presionar el botón "Finalizar" o la tecla Enter para mostrar la lista.
    El usuario puede guardar la lista en un archivo usando el botón "Guardar Lista".
    El usuario puede cargar una lista desde un archivo utilizando el botón "Cargar Lista".
    El usuario puede eliminar un archivo existente usando el botón "Eliminar Archivo". Si el archivo no existe, se muestra un error.

    Ejemplo de uso:
    Si el archivo "mi_lista.txt" existe, al presionar el botón "Eliminar Archivo", este se eliminará.
    Si el archivo no existe, se mostrará un mensaje de error indicando que no se encontró el archivo.
    ¡Espero que esta funcionalidad te sea útil! Si tienes alguna otra solicitud o pregunta, no dudes en comentarlo.

2. Modifica el código anterior para que los botones estén a la misma distancia entre ellos, independientemente de la altura de la ventana

    Para lograr que los botones estén distribuidos a la misma distancia entre ellos, independientemente de la altura de la ventana, podemos utilizar el método grid_rowconfigure y configurar el weight de las filas. Esto permitirá que las filas entre los botones se ajusten de forma proporcional, manteniendo la distancia uniforme.

    Aquí te dejo el código modificado para que los botones estén espaciados uniformemente:

    import tkinter as tk
    from tkinter import simpledialog
    from tkinter import messagebox
    import os

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

    def eliminar_archivo():
        # Pedir al usuario el nombre del archivo a eliminar
        nombre_archivo = simpledialog.askstring("Eliminar archivo", "Introduce el nombre del archivo para eliminar (con extensión .txt):")
        
        if nombre_archivo:
            try:
                # Verificar si el archivo existe y eliminarlo
                if os.path.exists(nombre_archivo):
                    os.remove(nombre_archivo)
                    etiqueta_resultado.config(text=f"Archivo '{nombre_archivo}' eliminado correctamente.")
                else:
                    messagebox.showerror("Error", f"El archivo '{nombre_archivo}' no existe.")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo eliminar el archivo: {e}")

    Crear la ventana principal
    ventana = tk.Tk()
    ventana.title("Ingreso, Carga, Guardado y Eliminación de Lista")

    Configurar el comportamiento de la ventana para expandirse con el tamaño de la pantalla
    ventana.grid_columnconfigure(0, weight=1)  # Hacer que la columna 0 sea flexible
    ventana.grid_rowconfigure(0, weight=0)  # Fijar el tamaño de la primera fila
    ventana.grid_rowconfigure(1, weight=0)  # Fijar el tamaño de la segunda fila
    ventana.grid_rowconfigure(2, weight=1)  # Permitir que la tercera fila expanda si es necesario
    ventana.grid_rowconfigure(3, weight=1)  # Permitir que la cuarta fila expanda si es necesario
    ventana.grid_rowconfigure(4, weight=1)  # Permitir que la quinta fila expanda si es necesario
    ventana.grid_rowconfigure(5, weight=1)  # Permitir que la sexta fila expanda si es necesario

    Crear un campo de entrada que ocupe todo el ancho disponible
    entrada_lista = tk.Entry(ventana, width=40)
    entrada_lista.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

    Asignar el evento de presionar 'Enter' para ejecutar la función de finalizar
    entrada_lista.bind("<Return>", mostrar_lista)

    Crear un botón para mostrar la lista
    boton_mostrar = tk.Button(ventana, text="Finalizar", command=mostrar_lista)
    boton_mostrar.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

    Crear un botón para guardar la lista en un archivo
    boton_guardar = tk.Button(ventana, text="Guardar Lista", command=guardar_lista)
    boton_guardar.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

    Crear un botón para cargar la lista desde un archivo
    boton_cargar = tk.Button(ventana, text="Cargar Lista", command=cargar_lista)
    boton_cargar.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

    Crear un botón para eliminar un archivo de lista
    boton_eliminar = tk.Button(ventana, text="Eliminar Archivo", command=eliminar_archivo)
    boton_eliminar.grid(row=4, column=0, padx=10, pady=10, sticky="ew")

    Crear una etiqueta para mostrar la lista ingresada
    etiqueta_resultado = tk.Label(ventana, text="Lista ingresada:")
    etiqueta_resultado.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

    Atributo global para almacenar la lista ingresada
    lista_guardada = []

    Iniciar la interfaz gráfica
    ventana.mainloop()
    Cambios realizados:
    Configuración de las filas en el grid:

    Se han añadido varias llamadas a ventana.grid_rowconfigure() para que las filas de los botones se distribuyan de manera proporcional a la altura de la ventana.
    Por ejemplo, hemos agregado las filas 1 a 5 con weight=1, lo que hace que se distribuyan proporcionalmente y mantengan una distancia uniforme entre ellas cuando la ventana cambia de tamaño.
    Distribución uniforme de los botones:

    Ahora los botones están alineados en la misma columna (columna 0), pero las filas intermedias entre los botones tienen un weight=1 para que el espacio entre los botones se distribuya de forma igualitaria.
    Resultado:
    Con estos cambios, los botones tendrán una distribución uniforme, sin importar la altura de la ventana. A medida que la ventana cambie de tamaño, los botones se ajustarán para mantener una separación proporcional entre ellos.

    Si tienes alguna otra duda o necesitas más cambios, no dudes en comentarlo. ¡Estoy aquí para ayudar!
