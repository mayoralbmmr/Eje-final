def mostrar_menu_principal():
    print("\n=== ENTRADAS MORAT ===")
    print("""
    (1) 27 noviembre (Monterrey)
    (2) 28 noviembre (Monterrey)
    (3) 2 diciembre (Zapopan, Jalisco)
    (4) 3 diciembre (Zapopan, Jalisco)
    (5) 8 diciembre (Merida)
    (6) 13 diciembre (Ciudad de México)
    (7) 14 diciembre (Ciudad de México)
    (8) Salir
    """)
    
def mostrar_menu_asientos():
    print("""
    === SELECCIÓN ZONA === 
    (1) PIT
    (2) Grada Oriente
    (3) General B
    (4) Grada Poniente
    (5) Boxes
    (6) Grada
    (7) A1 - A6
    (8) B1 - B9
    (9) C1 - C4  
    """)
    
def preguntar_cantidad_de_entradas():
    while True:
        try:
            cantidad = int(input("¿Cuántas entradas desea comprar? "))
            if cantidad > 0:
                return cantidad
            else:
                print("Por favor, ingrese un número mayor a 0")
        except ValueError:
            print("Por favor, ingrese un número valido")
       
def preguntar_asientos_juntos():
    while True:
        respuesta = input("¿Desean estar juntos? (si/no) ").lower()
        if respuesta == "si":
            print("Te localizaremos las mejores entradas que esten disponibles según los criterios de búsqueda ")
            return True
        elif respuesta == "no":
            print("No es necesario la localizacion de los asientos juntos ")
            return False
        else:
            print("No es valida esa opción. Por favor responda 'si' o 'no'")
        
def procesar_compra(fecha):
    print(f"\nProsesando compra para el {fecha}")
    
    cantidad = preguntar_cantidad_de_entradas()
    
    if cantidad >= 2:
        preguntar_asientos_juntos()
        
    mostrar_menu_asientos()
    
    while True:
        try:
            zona = int(input("Seleccione la zona deseada (1-9): "))
            if 1 <= zona <= 9:
                print(f"\nHa seleccionado la zona {zona}")
                print("\n==== Resumen de compra =====")
                print(f"Fecha: {fecha}")
                print(f"Cantidad de asientos: {cantidad}")
                print(f"Zona seleccionada: {zona}")
                break
            else:
                print("Por favor, seleccione una zona válida (1-9)")
                
        except ValueError:
            print("Por favor, ingrese un número válido")

def main():
    fechas = {
        "1": "27 noviembre (Monterrey)",
        "2": "28 noviembre (Monterrey)",
        "3": "2 diciembre (Zapopan, Jalisco)",
        "4": "3 diciembre (Zapopan, Jalisco)",
        "5": "8 diciembre (Merida)",
        "6": "13 diciembre (Ciudad de México)",
        "7": "14 diciembre (Ciudad de México)"
    }
                      
    while True:
        mostrar_menu_principal()
        respuesta = input("Ingrese el número de opción (1-8): ")
        
        if respuesta == "8":
            print("¡Gracias por usar nuestro sistema!")
            break
        elif respuesta in fechas:
            procesar_compra(fechas[respuesta])
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 8")

if __name__ == "__main__":
    main()