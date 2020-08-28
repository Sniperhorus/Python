num_1 = 10
num_2 = 10
test1= "mauricio"
test2="maurici"

mayor = num_1 > num_2
menor = num_1 < num_2
mayor_igual = num_1 >= num_2
menor_igual = num_1 <= num_2
igual = num_1 == num_2
# para validar que dos valores son iguales puedes utiliza == o is -> funciona con strings? si
igual_is = test1 is test2
diferente = num_1 != num_2


print(mayor)
print(menor)
print(mayor_igual)
print(menor_igual)
print(igual)
print(igual_is)
print(diferente)

# Todas las condiciones se deben cumplir
resultado = True and True and diferente
print("////////////////////")
print(resultado)
print("////////////////////")
# Al menos una condicion se debe cumplir
resultado2 = True or True or igual
print(resultado2)
print("////////////////////")
# Not para negar la condicion o valor. not False = True --- not True = False
resultado3 = not False
print (resultado3)