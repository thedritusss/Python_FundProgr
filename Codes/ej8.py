#ej8.- Un vendedor recibe un sueldo base más un 10% extra por comisión de sus ventas, el vendedor
# desea saber cuánto dinero obtendrá por concepto de comisiones por las tres ventas que reaiza
# en el mes y el total que recibirá en el mes tomando en cuenta su sueldo base y comisiones.#
#Entrada:
#Salida:
#Variables:

venta1=float(input("Introduce la venta 1: ")) #A venta1 se le asigna el valor introducido por el usuario
venta2=float(input("Introduce la venta 2: ")) #A venta2 se le asigna el valor introducido por el usuario
venta3=float(input("Introduce la venta 3: ")) #A venta3 se le asigna el valor introducido por el usuario

sueldo_base = float(input("Introduce tu sueldo base: ")) #A base se le asigna el valor introducido por el usuario
comision = (venta1+venta2+venta3)*0.10 #Calculo de las comisiones

print(f"Tu sueldo base es {sueldo_base} y tus comisiones son {comision}, por lo tanto tu sueldo total es {sueldo_base+comision}")
