"""
las listas pueden contener cualquier tipo de dato almacenadas(boolean,int,float or string)
Inician en la posicion 0 y pueden ser de cualquier tama;o, puede incrementar o decrementar
"""
cursos = ["python","django","flask"]
#Para acceder a posicion utilizamos nombrelista[posicion]
print(cursos[1])
# Para recorrer la lista de manera inversa -> nombreLitas[-posicion]
print(cursos[-1])

nombres = ["Mauricio","Diego","Marie","Clau"]
# Nomeclatura -> [Desde : Hasta-1],
print(nombres[0:3])

# Otra forma de solicitar que el rango inicia desde cero, 
# podemos omitir escribir nuestra posición "desde" de la siguiente manera:
print(nombres[:3])

# Generar una sublista iniciando desde una posicion especifica hasta el final
print(nombres[2:])

# Si no se agregan valores en [:] obtendremos toda la lista sin modificaciones.
print(nombres[:])

# Obtener los valores con saltos, ejemplo: obtener elementos de cada 2 posiciones en un intervalo
print(nombres[0:3:2])

# Obtener el inverso de toda nuestra lista
print(nombres[::-1])
