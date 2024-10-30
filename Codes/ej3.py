#ej3 Calcular hipotenusa dados sus catetos
#Entradas: Catetos
#Salida: Hipotenusa
#Variables: cateteto1, cateto2, hipotenusa.


import math
 
cateto1 = float(input("Introduce el primer cateto: ")) #A cateto1 se le asigna el valor introducido por el usuario
cateto2 = float(input("Introduce el segundo cateto: ")) #A cateto2 se le asigna el valor introducido por el usuario

hipotenusa = math.sqrt(cateto1**2 + cateto2**2) #Calculo de la hipotenusa

print(f"La hipotenusa es {hipotenusa}")