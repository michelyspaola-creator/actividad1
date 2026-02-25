nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad_mayor = int(input("Ingrese edad del hermano mayor: "))
edad_menor = int(input("Ingrese edad del hermano menor: "))

diferencia = edad_mayor - edad_menor

print(f"Nombre completo: {nombre} {apellido}")
print(f"La diferencia de edad es: {diferencia} años")