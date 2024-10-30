#ej5.- Calcula la media de tres números;
#Entradas: 3 numeros 
#salida: Media de los números
#variables: num1, num2, num3, result_media

result_media = 0

num1 = int(input("Introduce el primer numero: ")) #A num1 se le asigna el valor introducido por el usuario
num2 = int(input("Introduce el segundo numero: ")) #A num2 se le asigna el valor introducido por el usuario
num3 = int(input("Introduce el tercer numero: ")) #A num3 se le asigna el valor introducido por el usuario

result_media = (num1 + num2 + num3) / 3

print(f"La media es {result_media}")