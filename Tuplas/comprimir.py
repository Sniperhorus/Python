tupla = (1,2,3,4,5)

# Cada variable obtendra un valor de la tupla la variable a igualar debe ser la misma donde
# Se definio la tupla, de lo contrario arroja error que no esta definida.

# Aniadir el simbolo * antes de una variable toma el rango requerido para
# Asignar los valores que no tiene una variable. 
a, *b, c = tupla
print(b)


tupla_nom = ('Mauricio', 'Pedro', 'Diego')
tupla_ap = ('Carrillo', 'Picapiedra', 'Lozoya')
# La funcion zip comprime n cantidad de listas o tuplas y genera un objeto 
# para despues pasarle la funcion list o tuple y esta haga el cambio segun se requeira.


print(list(zip(tupla_nom, tupla_ap)))