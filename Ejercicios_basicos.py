"""
Los siguientes, son una serie de ejercicios que tienen como 
finalidad el que tu practiques los conocimientos adquiridos a 
lo largo de este segundo bloque.

"""

# Dado de los valores ingresados por el usuario (base, altura) 
# Calcular y mostrar en pantalla el área de un triángulo.
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
base = int(input("Ingresa la base\n"))
altura = int(input("Ingresa la altura\n"))

print("Resultado: ",(base*altura)/2)

# Convertir la cantidad de dólares ingresados por un usuario 
# A pesos colombianos y mostrar el resultado en pantalla.
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
cantidad = int(input("Cantidad a recibir en pesos?\n"))
PRECIO_DOLAR = 20

print("Conversion a dolares: ", cantidad/PRECIO_DOLAR)

# Convertir los grados centígrados ingresados por un 
# usuario a grados Fahrenheit y mostrar el resultado en pantalla.
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
temp1 = float(input("Ingresa temperatura en celsius\n"))
print("Grado F: ", (temp1*1.8)+32)

# Mostrar en pantalla la cantidad de segundos que tiene un lustro.

segundos =  5*(((60*60)*24)*365) 
print ("Segundos en un lustro: ",segundos)