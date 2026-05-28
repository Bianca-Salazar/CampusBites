```python
# ==========================================
# CAMPUS BITES - Sistema en Consola
# Proyecto sencillo en Python
# ==========================================

lugares = [
    {
        "nombre": "Comedor Don Pepe",
        "ubicacion": "Frente a la universidad",
        "precio": 3.50,
        "tipo": "Almuerzos"
    },
    {
        "nombre": "Pizza Express",
        "ubicacion": "Calle Principal",
        "precio": 2.00,
        "tipo": "Pizzas"
    },
    {
        "nombre": "Burger House",
        "ubicacion": "Centro Comercial",
        "precio": 4.00,
        "tipo": "Hamburguesas"
    }
]


def mostrar_menu():
    print("\n========== CAMPUS BITES ==========")
    print("1. Ver lugares de comida")
    print("2. Buscar lugares económicos")
    print("3. Agregar nuevo lugar")
    print("4. Salir")
    print("==================================")


def ver_lugares():
    print("\n--- LISTA DE LUGARES ---")

    if len(lugares) == 0:
        print("No hay lugares registrados.")
    else:
        for i, lugar in enumerate(lugares, start=1):
            print(f"\nLugar #{i}")
            print(f"Nombre: {lugar['nombre']}")
            print(f"Ubicación: {lugar['ubicacion']}")
            print(f"Tipo de comida: {lugar['tipo']}")
            print(f"Precio promedio: ${lugar['precio']}")


def buscar_economicos():
    print("\n--- LUGARES ECONÓMICOS ---")

    limite = float(input("Mostrar lugares con precio menor o igual a: $"))

    encontrados = False

    for lugar in lugares:
        if lugar["precio"] <= limite:
            print(f"\n{lugar['nombre']}")
            print(f"Ubicación: {lugar['ubicacion']}")
            print(f"Tipo: {lugar['tipo']}")
            print(f"Precio: ${lugar['precio']}")
            encontrados = True

    if not encontrados:
        print("No se encontraron lugares económicos.")


def agregar_lugar():
    print("\n--- AGREGAR NUEVO LUGAR ---")

    nombre = input("Nombre del lugar: ")
    ubicacion = input("Ubicación: ")
    tipo = input("Tipo de comida: ")
    precio = float(input("Precio promedio: $"))

    nuevo_lugar = {
        "nombre": nombre,
        "ubicacion": ubicacion,
        "precio": precio,
        "tipo": tipo
    }

    lugares.append(nuevo_lugar)

    print("Lugar agregado correctamente.")


# Programa principal
while True:
    mostrar_menu()

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        ver_lugares()

    elif opcion == "2":
        buscar_economicos()

    elif opcion == "3":
        agregar_lugar()

    elif opcion == "4":
        print("\nGracias por usar Campus Bites.")
        break

    else:
        print("Opción inválida. Intente nuevamente.")
```
