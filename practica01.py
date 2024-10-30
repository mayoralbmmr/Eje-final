#ciclo

x = int(input("Escriba un número entero menor a 20000"))
while x < 20000:
    print("Este es tu número", x , "y es menor a 20000 le voy a sumar uno hasta llegar a la meta")
    x += 1

if x == 20000:
    print("Felicidades no sabes seguir instrucciones")

else:
    print("No se hizo nada ya que escribiste un número mayor")  