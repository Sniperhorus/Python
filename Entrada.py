print("Cual es tu nombre?")
nombre = input()

print("Cual es tu edad?")
edad = int (input())

print("Cual es tu peso?")
peso = float(input())

print("--------------++++-----+++")
print(nombre,edad,peso)

# Otra forma de pedir la entrada de datos
# Si no agregamos el salto del linea al final \n del string el cursor se posicionara
# En el mismo renglon de la etrada
nombre1 = input("Cual es tu nombre?\n")
edad2 = int(input("Cual es tu edad?\n"))
peso3 = float(input("Cual es tu peso?\n"))
print(nombre1,edad2,peso3)


