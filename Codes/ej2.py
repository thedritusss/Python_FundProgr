#Ej2.- Calculo perímetro y área de un rectángulo 
#Entradas: Base, Altura
#Salidas: Perímetro, Área
#Variables: Base, Altura, Perímetro, Área


base = float(input("Introduce la base: ")) #A base se le asigna el valor introducido por el usuario
aluta = float (input("Introduce la altura: ")) #A altura se le asigna el valor introducido por el usuario

perimetro = 2*(base+aluta) #Calculo del perimetro
area = base*aluta #Calculo del area

print(f"El perimetro es {perimetro} y el area es {area}")
