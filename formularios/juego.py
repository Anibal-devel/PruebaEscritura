import tkinter as tk
import utileria.util_ventana as util_ventana
import formularios.Inicio as inicio
import random as rn

caracteres ="1234567890()-"
list_caracteres= list(caracteres)

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
                    print("######### ", contenido,"##########")
                    print("**********",frase_random)
                    print("Palabras totales:", contador_palabras)

def open_window():
    # ---cremos ventana_juego--- 
    ventana_juego = tk.Tk()
    # cerramos ventana inicio
    inicio.close_ventana_inicio()
    # centramos y damos tamaño    
    util_ventana.centrar_ventana(ventana_juego, 890, 200)
    # titulo
    ventana_juego.title("PRUEBA DE ESCRITURA")
    # color de fondo
    ventana_juego.config(bg="#2a3138")
    # agregar icono
    ventana_juego.iconbitmap("./imagenes/logo.ico")

    # creamos fondos
    fondo_up = tk.Frame(ventana_juego)
    fondo_down = tk.Frame(ventana_juego)
    # ponemos color
    fondo_up.config(bg="#1f2229")
    fondo_down.config(bg="#2a3138")
    # damos ubicacion
    fondo_up.pack(side=tk.TOP, fill="both", expand=True)
    fondo_down.pack(side=tk.TOP, fill="both", expand=True)

    button1 = tk.Button(fondo_up, text="Para comenzar haga")
    button1.config(bg="#1f2229", fg="white",font=("Roboto",30), width=40, height=2, command=comenzar_prueba)
    button1.pack(side=tk.LEFT, fill="both", expand=False)

    button2 = tk.Button(fondo_down, text="clic sobre la pantalla")
    button2.config(bg="white", fg="black",font=("Segoe Ui Black",30), width=40, height=2, command=comenzar_prueba)
    button2.pack(side=tk.LEFT, fill="both", expand=True)



    ventana_juego.mainloop()



