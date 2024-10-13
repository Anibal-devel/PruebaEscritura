import tkinter as tk  
from tkinter import ttk  

root = tk.Tk()  

entrada = ttk.Entry(root)  
entrada.pack()  

# Hacer que el Entry esté activo al abrir la ventana  
entrada.focus_set()  

root.mainloop()