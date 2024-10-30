#ej5.- Paso de Fahrenheit a Celsius
#Entradas: Fahrenheit;
#Salidas: Celsisus;
#Variables: Farenheit, Celsius;

farenheit = float(input("Introduce los grados en Farenheit: ")) #A farenheit se le asigna el valor introducido por el usuario

celsius = (farenheit - 32) * 5/9 #Calculo del celsius

print(f"{farenheit} grados Farenheit son {celsius} grados Celsius")