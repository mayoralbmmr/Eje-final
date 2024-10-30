print("\nBienvenid@ a tu cajero virtual")
saldo= input("\n¿Cuál es tu saldo? \n")

while True:
    print("""
    (1)Depositar
    (2)Transferir
    (3)Retirar
    """)

    respuesta= input("¿Qué desea hacer?: ")
    if respuesta == "1":
        cant=input("¿Qué cantidad desea depositar?: ")
        print("\nDepositado $",cant, "\nDeposito exitoso")
    elif respuesta == "2":
        Num=int(input("Ingresa el número de cuenta: "))
        trans=input("¿Qué cantidad desea transferir? $")
        if trans <= saldo:
            print("transfiriendo a ",Num, " $",trans)
        if trans > saldo:
            print("Saldo insuficiente")
    elif respuesta == "3":
        retiro=input("¿Qué cantidad desea retirar?")
        if retiro > saldo:
            print("Saldo insuficiente")
        if retiro <= saldo:
            print("Retirando", retiro, "\nRetiro exitoso")
    else:
            print("ERROR\nGracias por usar nuetro cajero virtual")
    print("\nGracias por usar nuestro cajero virtual\n")
    