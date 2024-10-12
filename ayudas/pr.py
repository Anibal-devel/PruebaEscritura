import random  

frase = "Esta es una frase de ejemplo para seleccionar palabras."  
palabras = frase.split()  # Divide la frase en palabras  
numero_palabras = 3  # Número de palabras a seleccionar  
palabras_seleccionadas = random.sample(palabras, numero_palabras)  

print(palabras_seleccionadas)

texto = "Este es un texto de ejemplo."  
contador_palabras = len(texto.split())  
print(contador_palabras)


texto = "Esta es una cadena de texto con varias palabras"  
palabras_limitadas = " ".join(texto.split()[:3])  
print(palabras_limitadas)  # Salida: "Esta es una"