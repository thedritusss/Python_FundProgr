#ej7.- minutos a horas y minutos
#Entrada: Minutos totales;
#Salida: Horas y minutos;
#Variables: horas, minutos;

minutos_resto = 0
horas = 0

minutos = int(input("Introduce los minutos: ")) #A minutos se le asigna el valor introducido por el usuario

minutos_resto = minutos % 60
horas = (minutos - minutos_resto) / 60

print(f"{horas} horas y {minutos_resto} minutos")