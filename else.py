nombre= input("Escribe tu nombre por favor ")
print(nombre+ " ¿mucho gusto que pelicula desea ver ?")
pelicula= input("tenemos 1_la de la noche del diablo y 2_coraline")
if pelicula<= "1_la noche con el diablo":
    print("Para entrar a verla necesito su edad")
if pelicula>= "2_coraline":
    print("Cuantos voletos quiere")
numero= float(input("¿Cuál es tu edad? "))
if numero>18:
    print("Eres mayor de edad puedes pasar")
if numero<10:
    print("Tenemos coraline para ti")
if numero>50:
    print("Igual le daremos descuento")