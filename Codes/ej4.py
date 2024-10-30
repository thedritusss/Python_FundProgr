#ej4.- Suma, resta, multiplicación, división de 2 números;
#Entradas: 2 Numeros;
#Salidas: Resultado de suma, resta, multiplicación, división;
#Variables: Num1, Num2, Result_suma, Result_resta, Result_multiplicacion, Result_Division

result_suma = 0
result_resta = 0
result_multiplicacion = 0
result_division = 0

num1 = int(input("Introduce el primer numero: ")) #A num1 se le asigna el valor introducido por el usuario
num2 = int(input("Introduce el segundo numero: ")) #A num2 se le asigna el valor introducido por el usuario

result_suma = num1 + num2
result_resta = num1 - num2
result_multiplicacion = num1 * num2
result_division = num1 / num2

print(f"La suma es {result_suma}")
print(f"La resta es {result_resta}")
print(f"La multiplicacion es {result_multiplicacion}")
print(f"La division es {result_division}")