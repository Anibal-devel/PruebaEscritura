import tkinter as tk
from tkinter import ttk
import utileria.util_ventana as util_ventana
import formularios.Inicio as inicio
import random as rn
import time as tm

caracteres ="1234567890()-"
list_caracteres= list(caracteres)

def open_window():

        
    # al iniciar una nueva prueba de frase borramos label con frase y entry anterior
    def close():
        button1.destroy()
        entry.destroy()
    # al crear la nueva ventana borramos button start y label "prueba escritura"
    try: # evitamos el crash al ya estar borrada anteriormente con (try)
        inicio.close_ventana_inicio()
    except:
        pass
    def comprobar(event):
        '''comprueba que los datos de entrada ingresados en el entry por el 
        usuario sean iguales a la frase propuesta a ecribir'''
        if entry.get() == frase:
           try:
               close()           
           except:
               pass
           # tomamos tiempo final
           end_time = tm.time()
           resultado_time = end_time - start_time
           imprimir_tiempo(resultado_time) 

    # imprimimos texto a escribir
    frase = crear_frase()
    
    # imprime en pantalla la frase creada
    button1 = tk.Label(inicio.fondo, text = frase)
    button1.config(bg="#1f2229", fg="white",font=("Roboto",30), width=40, height=2)
    button1.pack(side=tk.LEFT, fill="both", expand=False)
    
    # creamos entry donde escribira el usuario
    entry = ttk.Entry(inicio.ventana) # importar ttk + hacer focus_set() habilita que el entry al abrirse este seleccionado
    entry.config(font=("Segoe Ui Black",30))
    entry.pack(side="top",fill="both", expand=False, padx=200)    
    # tomamos el tiemo de inicio   
    start_time = tm.time()
    entry.bind("<Return>", comprobar)
    entry.focus_set() # al abrir la ventana queda seleccionado
    
    #inicio.ventana.mainloop()
 
def crear_frase():
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

def imprimir_tiempo(resultado_time):
    
    def borrar_time_button():
        button1.destroy()
        button.destroy()
        open_window()

    # imprimimos frase en el label
    button1 = tk.Label(inicio.fondo, text = f"Time: {round(resultado_time, 2)} segundos")
    button1.config(bg="#1f2229", fg="white",font=("Roboto",30), width=40, height=2)
    button1.pack(side=tk.LEFT, fill="both", expand=False)

    # button start
    button = tk.Button(inicio.ventana, text="start", width=40, height=2, 
           font=("Arial Black", 20), command = borrar_time_button)
    button.pack(side=tk.LEFT, fill="both", expand=True)

    
    



    



