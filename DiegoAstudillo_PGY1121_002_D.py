import os
os.system("cls")

def op1():
    cantidad = int(input("Ingrese la cantidad de entradas a comprar (1-3): "))
    while cantidad < 1 or cantidad > 3:
        cantidad = int(input("Cantidad inválida. Ingrese la cantidad de entradas a comprar (1-3): "))

    print("Ubicaciones disponibles:")
    for i in range(1, 101):
        if i <= 20:
            tipo = "Platinum"
        elif i <= 50:
            tipo = "Gold"
        else:
            tipo = "Silver"

        if i in asientos_vendidos:
            print(f"Asiento {i} ({tipo}): X", end="    ")
        else:
            print(f"Asiento {i} ({tipo}): {i}", end="    ")

        if i % 10 == 0:
            print("\n")

    for _ in range(cantidad):
        asiento = int(input("Ingrese el número de asiento a comprar: "))
        while asiento in asientos_vendidos:
            print("Ubicación no disponible. Por favor, elija otro asiento.")
            asiento = int(input("Ingrese el número de asiento a comprar: "))

        asientos_vendidos.append(asiento)
        run = input("Ingrese el RUN del asistente (sin puntos ni guiones): ")
        while not run.isdigit() or len(run) != 8:
            print("RUN inválido. Por favor, ingrese solo números (8 dígitos).")
            run = input("Ingrese el RUN del asistente (sin puntos ni guiones): ")

        ListaAsist.append((run, asiento))

    print("Operación realizada correctamente.")


def op2():
    print("Ubicaciones disponibles:")
    for i in range(1, 101):
        if i <= 20:
            tipo = "Platinum"
        elif i <= 50:
            tipo = "Gold"
        else:
            tipo = "Silver"

        if i in asientos_vendidos:
            print(f"Asiento  ({tipo}): X", end="    ")
        else:
            print(f"Asiento  ({tipo}): {i}", end="    ")

        if i % 10 == 0:
            print("\n")


def op3():
    ListaAsist.sort(key=lambda x: int(x[0]))
    print("Listado de asistentes:")
    for asistente in ListaAsist:
        print(f"RUN: {asistente[0]}, Asiento: {asistente[1]}")


def op4():
    precios = {"Platinum": 120000, "Gold": 80000, "Silver": 50000}
    total = 0
    print("Tipo     |    Entrada  |  Cantidad  |    Total")
    print("-" * 48)
    for tipo, precio in precios.items():
        cantidad = asientos_vendidos.count(tipo)
        subtotal = cantidad * precio
        print(f"{tipo:<13} {precio:>8,} {cantidad:>8} {subtotal:>11,}")
        total += subtotal
    print(f"{'TOTAL':<13} {'':>8} {len(asientos_vendidos):>8} {total:>11,}")


def op5():
    import datetime
    fecha_actual = datetime.datetime.now()
    print("Saliendo del sistema...")
    print("Nombre: [Tu nombre aquí]")
    print("Fecha: ", fecha_actual.strftime("%Y-%m-%d %H:%M:%S"))


asientos_vendidos = [14,15,16,33,45]
ListaAsist = []

while True:
    print("\n--- Menú ---")
    print("1. Comprar entradas")
    print("2. Mostrar ubicaciones disponibles")
    print("3. Ver listado de asistentes")
    print("4. Mostrar ganancias totales")
    print("5. Salir")

    try:
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            op1()
        elif opcion == 2:
            op2()
        elif opcion == 3:
            op3()
        elif opcion == 4:
            op4()
        elif opcion == 5:
            op5()
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")
    except ValueError:
        print("Opción inválida. Por favor, seleccione una opción válida.")