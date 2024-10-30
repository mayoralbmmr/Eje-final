# Bienvenido al cajero automático

# Establecemos el NIP
nip = ""

# Pedimos al usuario que ingrese su NIP
def establecer_NIP():
    global nip
    while True:
        nip_nuevo = input("Por favor, establezca su nip de 4 digitos: ")
        if len(nip_nuevo) == 4 and nip_nuevo.isdigit():
            nip = nip_nuevo
            print("NIP establecido correctamente")
            break
        else:
            print("El NIP debe de ser de cuatro dígitos, intentalo de nuevo ")

# Verificamos el NIP
def verificar_nip():
    intentos = 3
    while intentos > 0:
        nip_ingresado = input("Ingrese su NIP de 4 digitos")
        if nip_ingresado == nip:
            return True
        else:
            intentos -= 1
            print("NIP incorrecto, vuelve a intentarlo")
    print("Ha excedido el numero de intentos disponibles, por favor contacte a su banco")
    return False

# Inicializamos el saldo
saldo = 0

# Pedimos al usuario que ingrese su saldo inicial
def inicializar_saldo():
    global saldo
    while True:
        try:
            saldo = float(input("Por favor, ingrese su saldo inicial: $"))
            if saldo < 0:
                print("El saldo inicial no puede ser negativo. \nIntentelo de nuevo")
            else:
                print("Su saldo inicial es $" , saldo)
                break
        except ValueError:
            print("Por favor, ingrese un número válido.")

# Mostramos el menú
def mostrar_menu():
    print("""
        Menu del cajero Automatico
        (1)Depositar
        (2)Transferir
        (3)Retirar
        (4)Retiro sin tarjeta
        (5)Abono
        (6)Consultar saldo
        """)

# Funciones para realizar operaciones
def Depositar():
    global saldo
    cantidad = float(input("Ingrese la cantidad a depositar: $"))
    if cantidad > 0:
        saldo += cantidad
        print("Depósito realizado con éxito. Su nuevo saldo es: $", saldo)
    else:
        print("La cantidad a depositar no puede ser negativa.")

def Transferir():
    global saldo
    cantidad = float(input("Ingrese la cantidad a transferir: $"))
    if cantidad > 0 and cantidad <= saldo:
        saldo -= cantidad
        print("Transferencia realizada con éxito. Su nuevo saldo es: $", saldo)
    else:
        print("La cantidad a transferir no puede ser negativa o superior a su saldo.")

def Retirar():
    global saldo
    cantidad = float(input("Ingrese la cantidad a retirar: $"))
    if cantidad > 0 and cantidad <= saldo:
        saldo -= cantidad
        print("Retiro realizado con éxito. Su nuevo saldo es: $", saldo)
    if cantidad < 8000:
        print("Lo maximo que se puede retirar son $8000")
    else:
        print("La cantidad a retirar no puede ser negativa o superior a su saldo.")

def Retiro_sin_tarjeta():
    global saldo
    cantidad = float(input("Ingrese la cantidad a retirar sin tarjeta: $"))
    if cantidad > 0 and cantidad <= saldo:
        saldo -= cantidad
        print("Retiro sin tarjeta realizado con éxito. Su nuevo saldo es: $", saldo)
    else:
        print("La cantidad a retirar no puede ser negativa o superior a su saldo.")

def Abono():
    global saldo
    cantidad = float(input("Ingrese la cantidad a abonar: $"))
    if cantidad > 0:
        saldo += cantidad
        print("Abono realizado con éxito. Su nuevo saldo es: $", saldo)
    else:
        print("La cantidad a abonar no puede ser negativa.")

def Consultar_saldo():
    print("Su saldo actual es: $", saldo)

# Función principal
def main():
    establecer_NIP()
    inicializar_saldo()
    while True:
        mostrar_menu()
        opcion = input("Ingrese la opción: ")
        if opcion == "1":
            Depositar()
        elif opcion == "2":
            Transferir()
        elif opcion == "3":
            Retirar()
        elif opcion == "4":
            Retiro_sin_tarjeta()
        elif opcion == "5":
            Abono()
        elif opcion == "6":
            Consultar_saldo()
        else:
            print("Opción inválida. Por favor, intente de nuevo.")
if __name__ == "__main__":
    main()