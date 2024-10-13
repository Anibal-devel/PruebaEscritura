import tkinter as tk
from tkinter import ttk
import utileria.util_ventana as util_ventana
import formularios.Inicio as inicio
import random as rn

caracteres ="1234567890()-"
list_caracteres= list(caracteres)

def open_window():
    def close():
        button1.destroy()
        entry.destroy()
    try:
        inicio.close_ventana_inicio()
    except:
        pass
    def comprobar(event):
        if entry.get() == frase:
           try:
               close()           
           except:
               pass
           open_window()

    

    # creamos fondos
    '''fondo_up = tk.Frame(inicio.ventana)
    fondo_down = tk.Frame(inicio.ventana)
    # ponemos color
    fondo_up.config(bg="#1f2229")
    fondo_down.config(bg="#2a3138")
    # damos ubicacion
    fondo_up.pack(side=tk.TOP, fill="both", expand=True)
    fondo_down.pack(side=tk.TOP, fill="both", expand=True)'''

    # imprimimos texto a escribir
    frase = comenzar_prueba()

    button1 = tk.Label(inicio.fondo, text = frase)
    button1.config(bg="#1f2229", fg="white",font=("Roboto",30), width=40, height=2)
    button1.pack(side=tk.LEFT, fill="both", expand=False)

    entry = ttk.Entry(inicio.ventana) # importar ttk + hacer focus_set() habilita que el entry al abrirse este seleccionado
    entry.config(font=("Segoe Ui Black",30))
    
    entry.pack(side="top",fill="both", expand=False, padx=200)       
    entry.bind("<Return>", comprobar)
    entry.focus_set() # al abrir la ventana queda seleccionado
    
    #inicio.ventana.mainloop()

    

def comenzar_prueba():
    frase_impresa = False
    while frase_impresa == False:
        # Abre el archivo y lee su contenido  
        with open('./txt/frases.txt', 'r') as file: 
            # muevo el curzor hasta el final del archivo para obtener longitud total
            file.seek(0, 2)
            # guardo la longitud total del archivo en longitud_archivo
            longitud_archivo = file.tell()        
            # elijo una posicion random para el curzor
            posicion_inicio_lectura = rn.randint(0,longitud_archivo)
            # leo desde la posicion random seleccionada
            file.seek(posicion_inicio_lectura)
            # solo leo 40 byts
            contenido = file.read(40)
            # Divide el contenido en palabras
            # frase = contenido.split()  
            # numero palabras 
            contador_palabras = len(contenido.split())
            # Selecciona 3 palabras consecutivas
            frase_random = " ".join(contenido.split()[1:4])
            # evitamos imprimir números, parentesis y guiones
            for letra in list_caracteres:            
                if letra in frase_random:
                    break
                elif letra == "-":
                    frase_impresa = True
                    return frase_random

def imprimir_frase(frase):
    '''# quitamos ventana anterior
    #ventana_juego.destroy()
    # creamos una nueva
    crear_ventana(frase)'''


    



    



