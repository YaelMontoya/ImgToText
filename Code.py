import os
from tkinter import *
from PIL import Image
from pytesseract import *
from tkinter import filedialog



pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Ruta de la carpeta
ruta = ""

# Función que se ejecutará al presionar el botón
def convertir_imagen():
    imagen_encontrada = False
    try:
        x=os.listdir(ruta)
    except:
        texto.insert(INSERT, "Error: No se encontró la ruta especificada.")
        
    for file in os.listdir(ruta):
        if file.endswith(".png"):
            ##print(os.path.join(ruta, file)) Esto es para imprimir la ruta de la imagen encontrada
            img = Image.open(os.path.join(ruta, file))
            resultado = pytesseract.image_to_string(img , lang='spa' )
            texto.insert(INSERT, resultado)
            # Eliminamos el archivo
            os.remove(os.path.join(ruta, file))
            imagen_encontrada = True
    if not imagen_encontrada:
        texto.insert(INSERT, "Error: No se encontró ninguna imagen.")

# Función que se ejecutará al presionar el botón de copiar al portapapeles
def copiar_portapapeles():
    # Copia el contenido del Text
    ventana.clipboard_clear()
    ventana.clipboard_append(texto.get("1.0",END))
    ventana.update()

# Función que se ejecutará al presionar el botón de borrar
def borrar_texto():
    texto.delete("1.0",END)

# Función que se ejecutará al presionar el botón de cambiar la ruta
def cambiar_ruta():
    global ruta
    ruta = filedialog.askdirectory()
    label_ruta.config(text="Ruta actual: " + ruta)
    ventana.update()

def guardar_texto():
    try:
        archivo = filedialog.asksaveasfile(mode="w", defaultextension=".txt", filetypes=[("Todos los archivos", "*.*"), ("Archivos de texto", "*.txt")])
        if archivo is not None:
            archivo.write(texto.get("1.0", END))
            archivo.close()
    except:
        texto.insert(INSERT, "Error: Se produjo un error al guardar el archivo.")




# Crear ventana
ventana = Tk()
ventana.title("Convertidor de Imagen a Texto")
ventana.geometry("400x700")

# Crear un Frame
frame = Frame(ventana)
frame.pack()

# Crear un label
label = Label(frame, text="Convertidor de Imagen a Texto", font=("Arial", 18))
label.pack(pady=30)
# Crear label para mostrar la ruta actual
label_ruta = Label(frame, text="Ruta actual: " + ruta, font=("Arial", 12))
label_ruta.pack(pady=15)

# Crear un botón
boton = Button(frame, text="Convertir", command=convertir_imagen, font=("Arial", 14))
boton.pack(pady=15)

# Crear un botón para cambiar la ruta
boton_ruta = Button(frame, text="Cambiar ruta", command=cambiar_ruta, font=("Arial", 14))
boton_ruta.pack(pady=15)

# Crear un text
texto = Text(frame, width=40, height=10, font=("Arial", 12))
texto.pack(pady=15)

# Crear un botón para copiar al portapapeles
boton_copiar = Button(frame, text="Copiar al portapapeles", command=copiar_portapapeles, font=("Arial", 14))
boton_copiar.pack(pady=15)

# Crear un botón para borrar texto
boton_borrar = Button(frame, text="Borrar texto", command=borrar_texto, font=("Arial", 14))
boton_borrar.pack(pady=15)

# Crear un botón para guardar el texto
boton_guardar = Button(frame, text="Guardar texto", command=guardar_texto, font=("Arial", 14))
boton_guardar.pack(pady=15)

ventana.mainloop()
