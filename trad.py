
nombre = input("Escribe tu nombre: ")
print("Bienvenid@ al progama de traducción" ,nombre )

print(nombre + " presiona en, es, fr, fr_es, al para seleccionar el idioma al que quieres traducir \nin: de español a ingles \nes: de ingles a españos \nfr: de español a frances \nfr_es: de frances a español \nal: de español a aleman")

opcion = input("selecciona tu opcion: ")
en = "en"
es = "es"
fr = "fr"
fr_es = "fr_es"
al= "al"

if opcion == en:
    print("Español --> Ingles")
    opcion_en = input("¿Que verbo deseas traducir?: ")
    if opcion_en == "dormir":
        print ("La traducción es -sleep-")
    elif opcion_en == "jugar":
        print ("La traducción es -play-")
    elif opcion_en == "comer":
        print ("La traducción es -eat-")
    elif opcion_en == "mandar":
        print ("La traducción es -sent-")
    elif opcion_en == "elegir":
        print ("La traducción es -choose-")
    elif opcion_en == "cruzar":
        print ("La traducción es -cross-")
    elif opcion_en == "llorar":
        print ("La traducción es -cry-")
    elif opcion_en == "saltar":
        print ("La traducción es -jump-")
    elif opcion_en == "perder":
        print ("La traducción es -lose-")
    elif opcion_en == "hablar":
        print ("La traducción es -talk-")
    else:
        print ("No se encontro la palabra -The word is not founded-")
        

elif opcion == es:
    print("Ingles --> Español")
    opcion_es = input("¿Que nombre de animales deceas traducir?")
    if opcion_es == "dog":
        print ("The traduccion is -perro-")
    elif opcion_es == "gato":
        print ("The traduccion is -cat-")
    elif opcion_es == "otter":
        print ("The traduccion is -nutria-")
    elif opcion_es == "fox":
        print ("The traduccion is -zorro-")
    elif opcion_es == "butterfly":
        print ("The traduccion is -mariposa-")
    elif opcion_es == "lion":
        print ("The traduccion is -leon-")
    elif opcion_es == "snake":
        print ("The traduccion is -serpiente-")
    elif opcion_es == "dolphin":
        print ("The traduccion is -delfin-")
    elif opcion_es == "turtle":
        print ("The traduccion is -tortuga-")
    elif opcion_es == "turkey":
        print ("The traduccion is -pavo-")
    else:
        print( "The word is not founded -La palabra no fue encontrada-")
        
elif opcion == fr:
    print("Español --> Frances")
    opcion_es = input("¿Que número con letras deceas traducir?")
    if opcion_es == "uno":
        print ("La traduction est -un-")
    elif opcion_es == "dos":
        print ("La traduction est -deux-")
    elif opcion_es == "tres":
        print ("La traduction est -trois-")
    elif opcion_es == "cuatro":
        print ("La traduction est -quatre-")
    elif opcion_es == "cinco":
        print ("La traduction est -cinq-")
    elif opcion_es == "seis":
        print ("La traduction est -six-")
    elif opcion_es == "siete":
        print ("La traduction est -sept-")
    elif opcion_es == "ocho":
        print ("La traduction est -huit-")
    elif opcion_es == "nueve":
        print ("La traduction est -neuf-")
    elif opcion_es == "diez":
        print ("La traduction est -dix-")
    else:
        print( "La palabra no fue encontrada -Le mont n'a pas été trouvé-")

elif opcion == fr_es:
    print("Frances --> Español")
    opcion_es = input("¿Que nombre de lugares de la casa deceas traducir?")
    if opcion_es == "la tete":
        print ("La traducción es -la cabeza-")
    elif opcion_es == "les yeux":
        print ("La traducción es -los ojos-")
    elif opcion_es == "le bras":
        print ("La traducción es -el brazo-")
    elif opcion_es == "la langue":
        print ("La traducción es -la lengua-")
    elif opcion_es == "le coeur":
        print ("La traducción es -el corazón-")
    elif opcion_es == "le bouche":
        print ("La traducción es -la boca-")
    elif opcion_es == "la main":
        print ("La traducción es -la mano-")
    elif opcion_es == "le corps":
        print ("La traducción es -el cuerpo-")
    elif opcion_es == "l'oreille":
        print ("La traducción es -la oreja-")
    elif opcion_es == "le nez":
        print ("La traducción es -la nariz-")
    else:
        print( "Le mont n'a pas été trouvé -La palabra no fue encontrada-")
        
elif opcion == al:
    print("Español --> Aleman")
    opcion_es = input("¿Que palabras deceas traducir?")
    if opcion_es == "si":
        print ("Die Übersetzung lautet -ja-")
    elif opcion_es == "no":
        print ("Die Übersetzung lautet -nein-")
    elif opcion_es == "hola":
        print ("Die Übersetzung lautet -hallo-")
    elif opcion_es == "adiós":
        print ("Die Übersetzung lautet -auf wiedersehen-")
    elif opcion_es == "buenos días":
        print ("Die Übersetzung lautet -guten tag-")
    elif opcion_es == "buenas tardes":
        print ("Die Übersetzung lautet -guten abend-")
    elif opcion_es == "buenas noches":
        print ("Die Übersetzung lautet -guten nacht-")
    elif opcion_es == "por favor":
        print ("Die Übersetzung lautet -bitte-")
    elif opcion_es == "perdón":
        print ("Die Übersetzung lautet -verzeihung-")
    elif opcion_es == "hoy":
        print ("Die Übersetzung lautet -heute-")
    else:
        print( "Das Wort wurde nicht gefunden -La palabra no fue encontrada-")