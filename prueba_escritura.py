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

# ---creando ventana---
ventana = tk.Tk()
# titulo
ventana.title("PRUEBA DE ESCRITURA")
# tamaño 
ventana.geometry("890x200+500+400")
# color de fondo
ventana.configure(bg="black")

# etiquetas
etiqueta = tk.Label(ventana)
etiqueta.config(bg="black")
etiqueta.grid(row=0)
etiqueta1 = tk.Label(etiqueta, text="PRUEBA DE ESCRITURA")
etiqueta1.config(bg="blue", fg="white",font=("Colonna MT",30), width=40, height=2)
etiqueta1.grid(row=0)

# button
button = tk.Button(ventana, text="start", width=40, height=2, font=("Arial Black", 20))
button.grid(row=1, column=0)



ventana.mainloop()
