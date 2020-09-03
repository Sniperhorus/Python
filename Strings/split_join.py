# la funcion split tiene predefinido el separador en espacio en blanco
# Esta funcion retorna una lista con los valores obtenidos

lenguajes = 'Python, Java, Perl, JS'
print(lenguajes.split(","))

# Tomar en cuenta que los espacios en las cadenas tambien interfieren en el metodo split 
# Resultado -> ['Python', ' Java', ' Perl', ' JS']
# Agregando espacios al split
# Resultado -> ['Python', 'Java', 'Perl', 'JS']

lenguajes = 'Python, Java, Perl, JS'
print(lenguajes.split(", "))

# Join
# Genera strings a partir de listas
# El primer valor de join puede ser utilizado para configurar con que queremos separarlo
# podemos usar espacios en blanco, algun simbolo e incluso strings
#
#

check = lenguajes.split(",")
nuevo = " Curso ".join(check)
print(nuevo)

# Regresar al estado origianl nuestro string
# Utilizando el separador con el que dividimos el string.
nuevo_str = ", ".join(check)
print(nuevo_str)

# Metodo a utilizar cuando nuestro string tenga saltos de linea

texto = """esto es un 
string con 
saltos

de linea """

texto_join = texto.splitlines()
print(texto_join)