# Pedimos la edad
edad = int(input("Introduce tu edad: "))

# Pedimos el nivel físico y validamos que esté entre 1 y 10
while True:
    nivel_fisico = int(input("Introduce tu nivel físico (1 a 10): "))
    if 1 <= nivel_fisico <= 10:
        break

    else:
        print("El nivel físico debe estar entre 1 y 10. Inténtalo de nuevo.")

# Evaluamos condiciones
if edad < 18:
    print("Debes ser mayor de edad.")
elif nivel_fisico < 5:
    print("Debes estar en mejor forma.")
else:
    print("¡Listo para despegar!")


