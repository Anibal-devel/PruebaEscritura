'''La idea de este proyecto es crear un programa que evalúe cuan rápido puedes escribir una
oración de manera precisa.
Este programa puede requerir crear una interfaz gráfica de usuario (GUI) mediante el módulo
tkinter. Si eres nuevo en las GUI, este ejemplo es una buena introducción, ya que tan solo
necesitas crear una serie de etiquetas simples, botones y campos de entrada para crear una
ventana. 

Puedes usar el módulo timeit de Python para manejar el aspecto de temporización
de nuestra prueba de escritura, y el módulo random para seleccionar aleatoriamente una frase
de prueba.'''
# crear ventana y sus componentes
import tkinter as tk
# centrado de ventana
import utileria.util_ventana as util_ventana
import formularios.juego as juego

def close_ventana_inicio():
    button.destroy()
    etiqueta1.destroy()
    #fondo.destroy()


# ---creando ventana---
ventana = tk.Tk()
    
# titulo
ventana.title("PRUEBA DE ESCRITURA")
# tamaño 
# ventana.geometry("890x200+500+400")
# color de fondo
ventana.configure(bg="#2a3138")
# agregamos icono
ventana.iconbitmap("./imagenes/logo.ico")
# centrar ventana
util_ventana.centrar_ventana(ventana, 890, 200)

# etiquetas
fondo = tk.Frame(ventana)
fondo.config(bg="#2a3138")
fondo.pack(side=tk.TOP, fill="both")
etiqueta1 = tk.Label(fondo, text="PRUEBA DE ESCRITURA")
etiqueta1.config(bg="#1f2229", fg="white",font=("Roboto",30), width=40, height=2)
etiqueta1.pack(side=tk.LEFT, fill="both", expand=True)

# button
button = tk.Button(ventana, text="start", width=40, height=2, 
                    font=("Arial Black", 20), command = juego.open_window)
button.pack(side=tk.LEFT, fill="both", expand=True)



ventana.mainloop()


