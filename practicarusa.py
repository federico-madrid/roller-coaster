#Ejercicio de montaña rusa con condicional

#Preguntar al usuario su nombre y edad, si es mayor de 12 puede subirse a la montaña rusa, sino no puede.
#Si es hijo del dueño, puede subirse igual aunque sea menor de 12 años.

nombre = input("¿Como te llamas? ")
print("Hola " + nombre + " Bienvenido a la montaña rusa")

edad = int(input("¿Cuantos años tenes? "))

edadMayorA12 = edad >= 12
preguntarPadre = input("¿Sos hijo del dueño? ")
repuestaPadre = preguntarPadre == "si"
puedeSubirse = edadMayorA12 or repuestaPadre

if puedeSubirse:
    print("Podes Subirte a la montaña rusa!")
else:
    print("No podes subirte a la montaña rusa")
