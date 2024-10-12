import tkinter as tk
import utileria.util_ventana as util_ventana
import formularios.Inicio as inicio

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



    ventana_juego.mainloop()



