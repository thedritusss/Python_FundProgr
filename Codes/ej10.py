#ej10- Un alumno desea saber cuál será su calificación final en la materia de Algoritmos Dicha
#calificación se compone de los siguientes porcentajes:
#?55% del promedio de sus tres calificaciones parciales.
#?30% de la calificación del examen final.
#?15% de la calificación de un trabajo final.
#
#Entradas: Tres parciales, examen final, trabajo final.
#Salidas: Calificación final.
#Variables: Parcial1, Parcial2, Parcial3, Examen_fin, Trabajo_fin, Promedio, Nota_fin.


parcial1=float(input("Introduce la nota del primer parcial: ")) #A parcial1 se le asigna el valor introducido por el usuario
parcial2=float(input("Introduce la nota del segundo parcial: ")) #A parcial2 se le asigna el valor introducido por el usuario
parcial3=float(input("Introduce la nota del tercer parcial: ")) #A parcial3 se le asigna el valor introducido por el usuario

promedio=(parcial1+parcial2+parcial3)/3 #Calculo del promedio
promedio=promedio*0.55 #Calculo de la nota del primer parcial

examen_final=float(input("Introduce la nota del examen final: ")) #A examen_final se le asigna el valor introducido por el usuario
trabajo_final=float(input("Introduce la nota del trabajo final: ")) #A trabajo_final se le asigna el valor introducido por el usuario

examen_fin=examen_final*0.30 #Calculo de la nota del examen final
trabajo_fin=trabajo_final*0.15 #Calculo de la nota del trabajo final

nota_fin=promedio+examen_fin+trabajo_fin #Calculo de la nota final

print(f"Tu nota final es {nota_fin}")