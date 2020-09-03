texto = "curso de python 3"
# Cambia a mayusculas la primer letra del String
print(texto.capitalize())
# Cambia las letras min a mayus y viceversa del String
print(texto.swapcase())
# Todas las letras a mayusculas
print(texto.upper())
# Todas las letras en min
print(texto.lower())
# Saber si un string esta con mayusculas o minusculas
print(texto.isupper())
print(texto.islower())
# Generar un formato con estilo de titulo
print(texto.title())
# Reemplazar valores del String -> Primer param : Palabra a reemplazar, Segundo param : Texto nuevo
# Nota: Todos los strings que hagan match seran remplazados..
# Nota: Podemos agregar un 3 valor entero para definir cuantas veces puede reemplazar el string seleccionado
texto2 = "curso de python 3 python"
print(texto2.replace("python","JAVA",3))
# El metodo strip elimina todos los espacios al inicio y final
texto3 = "       texto       "
print(texto3.strip())

# Imprimir variables desde el texto
curso = 'Python'
version = '3'
resultado = 'Curso de %s %s' %(curso, version)
resultado2 = 'Curso de {} {}'.format(curso, version)
# Podemos nombrar a nuestros valores para tener un mejor control
# Aqui ya no se manejan por posicion, sino por asignacion.
resultado3 = 'Curso de {a} {b}'.format(a=curso, b=version)
print(resultado)
print(resultado2)
print(resultado3)