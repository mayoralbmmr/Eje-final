productos = {
    1: {"nombre": "Laptop", "precio": 15000},
    2: {"nombre": "Smartphone", "precio": 8000},
    3: {"nombre": "TV", "precio": 12000},
    4: {"nombre": "Refrigerador", "precio": 18000},
    5: {"nombre": "Lavadora", "precio": 10000}
}

def calcular_interes(meses, es_bbva):
    if es_bbva:
        return 0
    elif meses in [3, 6, 9]:
        return 0.05     
    elif meses in [12, 18]:
        return 0.10
    else:
        return 0

def mostrar_productos():
    print("\nProductos disponibles:")
    for id, producto in productos.items():
        print(f"{id}. {producto['nombre']} - ${producto['precio']}")

def comprar():
    total = 0
    carrito = {}
    
    while True:
        mostrar_productos()
        seleccion = input("\nSeleccione un producto (1-5) o 'f' para finalizar: ")
        
        if seleccion.lower() == 'f':
            break
        
        if seleccion.isdigit() and 1 <= int(seleccion) <= 5:
            producto = productos[int(seleccion)]
            cantidad = int(input(f"Cantidad de {producto['nombre']} a comprar: "))
            carrito[producto['nombre']] = cantidad
            total += producto['precio'] * cantidad
        else:
            print("Selección inválida. Intente de nuevo.")
    
    if total == 0:
        print("No se seleccionaron productos. Gracias por su visita.")
        return
    
    print(f"\nTotal de la compra: ${total}")
    
    metodo_pago = input("Método de pago (BBVA/Otro): ").upper()
    es_bbva = metodo_pago == "BBVA"
    
    opciones_msi = [3, 6, 9, 12, 18]
    print("\nOpciones de pago:")
    print("0. Pago de contado")
    for meses in opciones_msi:
        interes = calcular_interes(meses, es_bbva)
        total_con_interes = total * (1 + interes)
        mensualidad = total_con_interes / meses
        print(f"{meses}. {meses} meses sin intereses: ${mensualidad:.2f} por mes (Total: ${total_con_interes:.2f})")
    
    opcion = int(input("\nSeleccione una opción de pago: "))
    
    if opcion == 0:
        print(f"Pago de contado seleccionado. Total a pagar: ${total}")
    elif opcion in opciones_msi:
        interes = calcular_interes(opcion, es_bbva)
        total_con_interes = total * (1 + interes)
        mensualidad = total_con_interes / opcion
        print(f"Pago a {opcion} meses seleccionado.")
        print(f"Mensualidad: ${mensualidad:.2f}")
        print(f"Total a pagar: ${total_con_interes:.2f}")
    else:
        print("Opción inválida.")
        return
    
    abono = float(input("\n¿Desea realizar un abono inicial? Ingrese la cantidad (0 para no abonar): "))
    if abono > 0:
        if abono >= total_con_interes:
            print("El abono cubre el total de la compra. Gracias por su pago.")
        else:
            restante = total_con_interes - abono
            print(f"Abono de ${abono} aplicado. Monto restante: ${restante:.2f}")
    
    print("\nGracias por su compra!")

if __name__ == "__main__":
    comprar()