#Operaciones con listas:
lista=[8.17,90,1,5,44,1.32]
print(lista)
#para conseguir el valor de la longitud de la lista se usa el len(nombre_lista)
longitud=len(lista)
print(longitud)
#sort se usa para ordenar las listas de forma ascendente
lista.sort()
print(lista)
#sort(reverse=True) se usa para ordenar la lista de forma descendente
lista.sort(reverse=True)
print(lista)

# para conseguir el numero menor y mayor en la lista, una vez que han sido ordenados podemos imprimirlos 
# dentro de una variable e indicar el primer y ultimo valor en la lista. 
mayor=lista[0]
print(mayor)
menor=lista[-1]
print(menor)
# Funciones  min/max para obtener el maximo y minimo de una lista
menor1=min(lista)
print(menor1)
mayor1=max(lista)
print(mayor1)

#buscar algun valor en la lista se puede usar el in
resultado=8 in lista
print(resultado)

#Usando nombre_lista.index podemos encontrar el indice en el que se encuentra un valor en la lista. 
#indice=lista.index(valor)
indice=lista.index(44)
print(indice)

#Usando el nombre_lista.count(valor) podemos ver cuantas veces se encuentra ese valor dentro de una lista.
contador=lista.count(5)
print(contador)
