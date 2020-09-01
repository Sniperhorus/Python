lista_nom = ['Mauricio', 'Pedro', 'Diego']
tupla_ap = ('Carrillo', 'Picapiedra', 'Lozoya')

# Funciones para convertir a tuplas o listas segun se requiera.
nueva_tupla = tuple(lista_nom)
nuevla_lista = list (tupla_ap)

print(nueva_tupla)
print(nuevla_lista)
# Tambien se puede convertir strings a tuplas o listas
mensaje = 'Hola Mauricio'

tupla_uno = tuple(mensaje)
lista_dos = list(mensaje)

print(tupla_uno)
print(lista_dos)