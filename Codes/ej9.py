#ej9.- Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber
#cuánto deberá pagar finalmente por su compra.
#Entrada: Total de la compra
#Salida: Total de la compra con el descuento
#Variables: Compra, Compra_descuento

total_compra=float(input("Introduce el total de la compra: ")) #A total_compra se le asigna el valor introducido por el usuario
compra_con_descuento = total_compra - (total_compra*0.15) #Calculo del descuento

print(f"El total de la compra con descuento es de {compra_con_descuento}")