print("Vamos a crear un cuento juntos")
nombre = input("Primero dime tu nombre ")

print("De acuerdo " + nombre + " list@ para aterrarte? ")
print("Para saber que nivel de terror te puedo brindar necesito saber tu edad")

print("Presiona el número 1 si tienes +18")
print("Presiona el número 2 si tienes -18")
print("Presiona el número 3 si quieres salir")

opcion= int(input("¿Qué opcion escoges?"))

if opcion == 1:
    print("¿Cuánta cantidad de terror quieres?")
    print("El número 1_1 para leve")
    print("El número 2_2 para intermedio")
    print("El número 3_3 para fuerte")
    intensidad = input("¿Qué escoges? ")
    
    if intensidad == "1_1":
        print("Escogiste intensidad leve")
        objetos_malditos = ["mesa", "silla", "television"]
        maldicion = input("Escoge y escribe el nombre de alguno de estos objetos \n-" + " \n-" .join(objetos_malditos) + "-\n")
        
        if maldicion == "mesa":
            persona = input("Nombre de tu personaje principal: ")
            persona_1_1 = input ("Nombre de otro personaje: ")
            print("Vamos por el cuento\n\n")
            print("\nLa Mesa que Susurraba \nEn una antigua mansión, heredada de generación en generación, se encontraba una mesa de roble macizo. Era una pieza imponente, tallada con intrincados diseños que parecían cobrar vida a la luz de la luna. Los nuevos propietarios, una joven pareja " + persona + "y" + persona_1_1 +"habían quedado fascinados por su belleza y decidieron colocarla en el comedor. \nAl principio, todo parecía normal. La mesa servía de apoyo para comidas familiares, reuniones con amigos y juegos de mesa. Sin embargo, con el paso de los días, comenzaron a notar extraños sucesos. Los cubiertos se movían solos, las sillas crujían sin razón aparente y, a veces, creían escuchar susurros provenientes de la madera. \nUna noche, mientras cenaban a la luz de las velas, la mujer sintió una presencia fría en la nuca. Al volverse, vio que una de las sillas se había desplazado unos centímetros, como si alguien se hubiera levantado de ella. Su marido, tratando de tranquilizarla, le aseguró que solo era el viento. \nLos susurros se hicieron cada vez más frecuentes. Parecían palabras ininteligibles, como si la mesa intentara contar una historia antigua. La pareja consultó a un experto en lo paranormal, quien les explicó que la mesa podría estar vinculada a un suceso trágico ocurrido en esa misma habitación. Tal vez, alguien había sido asesinado allí, y la mesa había absorbido la energía negativa del lugar. \nDecididos a poner fin a las perturbaciones, los jóvenes propietarios decidieron llevar a cabo un ritual de limpieza espiritual. Encendieron velas, quemaron hierbas aromáticas y recitaron antiguas plegarias. Al finalizar el ritual, la atmósfera de la habitación se sintió más ligera. Los susurros cesaron y la mesa pareció recuperar su calma.\nSin embargo, la pareja nunca se olvidó de la extraña experiencia. A veces, al pasar por el comedor, tenían la sensación de que la mesa los observaba con ojos antiguos y sabios. Y aunque los sucesos paranormales habían cesado, no podían evitar preguntarse qué secretos ocultaba esa vieja mesa de roble.")
            
        elif maldicion == "silla":
            persona_1 = input("Nombre de tu personaje principal: ")
            persona_1_2 = input ("Nombre de otro personaje: ")
            print("Vamos por el cuento\n")
            print("La Silla que Observaba \n\nEn una pequeña casa de campo, rodeada de árboles centenarios, se encontraba una silla de madera tallada. Era una pieza antigua, heredada de generación en generación, con un respaldo alto y curvado que invitaba a la relajación. Los nuevos inquilinos, una pareja joven" + persona_1 + "y" + persona_1_2 +", quedaron encantados con su estilo rústico y la colocaron junto a la chimenea en la sala de estar. \nAl principio, la silla era simplemente un mueble más en la casa. Sin embargo, con el paso de los días, comenzaron a notar una sensación extraña cuando se sentaban en ella. Era como si la silla los estuviera observando, siguiendo sus movimientos con una mirada invisible. \nUna noche, mientras leían un libro, el hombre sintió un escalofrío recorrer su espalda. Al volverse, vio que la silla se había movido ligeramente, como si alguien se hubiera sentado en ella. Su mujer, tratando de tranquilizarlo, le aseguró que solo era el viento. \nLos sucesos extraños se repitieron en varias ocasiones. Las puertas se abrían y se cerraban solas, las luces parpadeaban sin razón aparente y, a veces, creían escuchar susurros provenientes de la silla. La pareja comenzó a investigar la historia de la casa y descubrieron que el antiguo propietario había pasado sus últimos años confinado a esa silla, debido a una enfermedad que lo dejó postrado. \Decididos a poner fin a las perturbaciones, los jóvenes inquilinos decidieron realizar un ritual de limpieza espiritual. Encendieron velas, quemaron hierbas aromáticas y recitaron antiguas plegarias. Al finalizar el ritual, la atmósfera de la casa se sintió más ligera. Los sucesos paranormales cesaron y la silla pareció recuperar su calma. \nSin embargo, la pareja nunca se olvidó de la extraña experiencia. A veces, al pasar por la sala de estar, tenían la sensación de que la silla los observaba con una mirada antigua y sabia. Y aunque los sucesos paranormales habían cesado, no podían evitar preguntarse qué secretos ocultaba esa vieja silla de madera.")
            
            
        elif maldicion == "televisión":
            persona_2 = input("Nombre de tu personaje principal: ")
            print("Vamos por el cuento\n\nLa Pantalla que Susurraba \nEn un pequeño apartamento, ubicado en el último piso de un antiguo edificio, vivía un joven escritor llamado " + persona_2 +". Pasaba largas horas frente a su computadora, escribiendo historias de terror. Para relajarse, solía encender una vieja televisión que había encontrado en un mercadillo. Era un modelo antiguo, con una pantalla de tubo y un sonido un poco distorsionado, pero tenía un encanto peculiar. \nAl principio, la televisión solo servía para poner música de fondo mientras trabajaba. Sin embargo, con el paso de las noches, " +persona_2, + "comenzó a notar cosas extrañas. A veces, cuando cambiaba de canal, la imagen se distorsionía y aparecían caras borrosas y sombras que se movían rápidamente. Otras veces, escuchaba susurros ininteligibles provenientes del altavoz, como si alguien estuviera hablando desde el otro lado de la pantalla. \n El trató de ignorar estos sucesos, pensando que eran solo producto de su imaginación. Pero las cosas empeoraron cuando comenzó a tener pesadillas recurrentes. En ellas, veía imágenes de la televisión, caras distorsionadas que lo perseguían por oscuros laberintos. \nUna noche, mientras estaba profundamente dormido, Daniel sintió una presencia en la habitación. Abrió los ojos y vio que la televisión estaba encendida, aunque no recordaba haberla dejado así. En la pantalla, aparecía una imagen estática de un rostro que lo miraba fijamente. Era una mujer joven, con los ojos vacíos y una expresión de dolor. El sintió un escalofrío recorrer su cuerpo y se tapó con las sábanas. \nAl día siguiente, decidido a descubrir el origen de las perturbaciones, el comenzó a investigar la historia de la televisión. Preguntó a los vecinos del edificio, pero nadie parecía saber nada al respecto. Frustrado, decidió consultar a un médium. \nLa médium le explicó que la televisión podría estar vinculada a un suceso trágico ocurrido en el pasado. Tal vez, alguien había muerto frente a ella o había sido utilizada para transmitir mensajes oscuros. Le recomendó que bendijera la televisión y la limpiara energéticamente. \El siguió el consejo de la médium y realizó un pequeño ritual. Encendió una vela blanca, roció la televisión con agua bendita y recitó una oración. Al finalizar el ritual, la sensación de inquietud desapareció. Las imágenes distorsionadas y los susurros cesaron por completo. \nSin embargo, el nunca se olvidó de la extraña experiencia. A veces, al pasar por la sala, tenía la sensación de que la televisión lo observaba con una mirada inquisitiva. Y aunque los sucesos paranormales habían cesado, no podía evitar preguntarse qué secretos ocultaba esa vieja pantalla.")
       
        else:
            print("Tu opción no es válida")
                
    elif intensidad == "2_2":
        print("Escogiste intensidad intermedia")
        objetos_malditos_1 = ["cuchillo", "dije", "muñeca"]
        ob_maldito=input("Escoge y escribe el nombre de alguno de estos objetos \n-" + " \n-" .join(objetos_malditos_1) + "-\n")
        
        
        if ob_maldito == "cuchillo":
            persona_3 = input("Nombre de tu personaje principal: ")
            print("Vamos por el cuento\n\nEl Cuchillo de la Abuela \nEn la pequeña localidad de San Lorenzo, rodeada de colinas y niebla, se transmitía de generación en generación la leyenda del cuchillo de la abuela. Se decía que aquella hoja, forjada en tiempos inmemoriales, estaba imbuida de una maldición ancestral, capaz de desatar la locura y la violencia en quien la empuñaba." + persona_3 +", una joven curiosa y escéptica, había escuchado estas historias desde niña. Sin embargo, nunca les había dado importancia hasta que encontró el cuchillo en el antiguo baúl de su abuela, durante una visita al pueblo. La hoja, de un óxido intenso, parecía susurrarle secretos oscuros. Con una mezcla de fascinación y temor, Lucía lo tomó entre sus manos. \nAl principio, el cuchillo era solo un objeto más. Ella lo utilizaba para cortar frutas, verduras, incluso para abrir cartas. Pero poco a poco, comenzó a notar cambios extraños. Sueños perturbadores la atormentaban cada noche, visiones de sangre y gritos desgarradores que la dejaban empapada en sudor. Durante el día, sentía una extraña atracción por el cuchillo, una necesidad imperiosa de tenerlo siempre cerca. \nSus amigos y familiares notaron un cambio radical en su comportamiento. Ella se volvía cada vez más irritable y violenta, sus ojos tenían un brillo extraño y sus palabras eran incoherentes. Sus pesadillas se hicieron realidad cuando, en un arranque de furia, hirió accidentalmente a su mejor amiga con el cuchillo. El miedo y la culpa la consumieron, comprendiendo por fin la terrible verdad que se escondía tras la leyenda. \nDecidida a romper la maldición, Lucía buscó la ayuda de un anciano curandero del pueblo. El hombre, con una mirada sabia y penetrante, la escuchó atentamente. Le habló de rituales ancestrales, de sacrificios y de la necesidad de enfrentar sus propios demonios. Ella, desesperada, aceptó someterse a cualquier prueba. \nDurante varios días, Ella se encerró en una habitación oscura, rodeada de velas y símbolos antiguos. El curandero la guió a través de un trance profundo, obligándola a confrontar los miedos más oscuros que se habían arraigado en su mente. Al final del ritual, ella sintió una liberación, como si una pesada carga hubiera sido levantada de sus hombros. \nCon una última mirada al cuchillo, ella lo arrojó al fuego. Mientras las llamas consumían la hoja maldita, sintió un profundo alivio. Las visiones y los impulsos violentos desaparecieron, dejando en su lugar una sensación de paz y tranquilidad. El cuchillo de la abuela había sido destruido, y con él, la maldición que había atormentado a su familia durante generaciones. \nSin embargo, Lucía sabía que el peligro nunca estaba completamente erradicado. La leyenda del cuchillo seguiría viva, una advertencia para aquellos que se atrevieran a jugar con fuerzas desconocidas. Y aunque había logrado escapar de su influencia, siempre llevaría consigo la marca de aquella experiencia, un recordatorio de que algunas historias son demasiado oscuras para ser ignoradas.")
            
        elif ob_maldito == "dije":
            persona_4 = input("Nombre de tu personaje principal: ")
            print("Vamos por el cuento \n\nEl Dije de Ópalo Negro \nEn el corazón de la antigua mansión Blackwood, heredada por la joven" + persona_4 + ", se encontraba un joyero ancestral. Entre sus tesoros, destacaba un dije de ópalo negro, una joya de familia que, según la leyenda, otorgaba una belleza sin igual a quien lo portaba, pero a costa de un terrible precio. Ella, atraída por la misteriosa belleza del dije, decidió usarlo en una importante gala. Esa noche, todos quedaron deslumbrados por su belleza, pero ella comenzó a sentir una sensación de frío intenso, como si una oscuridad se adentrara en su alma. Los días siguientes, extraños sucesos comenzaron a ocurrir en la mansión. Puertas se cerraban solas, sombras se deslizaban por los pasillos y sus pesadillas se volvieron cada vez más vívidas. Ella soñaba con una mujer vestida de negro, cuyos ojos de ópalo brillaban con una luz siniestra. \nConvencida de que el dije era la causa de sus problemas, Anya decidió consultarlo con un anciano médium. El hombre, con una mirada penetrante, le reveló que el ópalo negro estaba maldito y que estaba siendo consumida por una entidad oscura. Para liberarse de su influencia, debía realizar un ritual en la habitación donde había encontrado el dije. \nDurante el ritual, ella sintió una presencia maligna que la rodeaba. El ópalo negro comenzó a emitir una luz intensa, y la figura de la mujer de negro se materializó frente a ella. Una lucha sobrenatural se desató, llena de gritos y estallidos de energía. Al final, ella logró expulsar a la entidad, pero el dije se hizo añicos en sus manos. \nExhausta pero aliviada, ella salió de la habitación. La mansión parecía haber recuperado su calma, pero la experiencia la había marcado para siempre. A partir de ese día, ella se volvió más escéptica y desconfiada, temiendo que en cualquier momento otra fuerza oscura pudiera cruzar su camino. \nEllaAños más tarde, Anya decidió vender la mansión Blackwood. Antes de irse, regresó a la habitación donde había encontrado el dije. En un rincón olvidado, encontró un pequeño fragmento de ópalo negro. Lo tomó entre sus dedos, sintiendo un escalofrío recorrer su espalda. Sabía que, aunque había escapado de la maldición, una parte de ella siempre quedaría ligada a aquel misterioso dije.")
            
        elif ob_maldito == "muñeca":
            persona_5 = input("Nombre de tu personaje principal: ")
            print("Vamos por el cuento \n\nLa Muñeca de Porcelana \nEn una antigua mansión, heredada de generación en generación por la familia Blackwood, se encontraba una muñeca de porcelana en un rincón polvoriento de la habitación infantil. Sus ojos de cristal miraban fijamente a la nada, y una sonrisa macabra curvaba sus labios. Los rumores sobre la muñeca eran oscuros y persistentes: se decía que estaba poseída por un espíritu maligno que atormentaba a quien la poseía." + persona_5 + "la nieta mayor de la familia Blackwood, siempre había sentido una fascinación morbosa por la muñeca. A pesar de las advertencias de su abuela, un día decidió tomarla en sus manos. Al instante, sintió un escalofrío recorrer su espina dorsal y un extraño hormigueo en sus dedos. \nA partir de ese momento, extraños sucesos comenzaron a ocurrir en la mansión. Puertas se cerraban de golpe, sombras se deslizaban por los pasillos y la muñeca parecía moverse por sí sola. Ella comenzó a tener pesadillas recurrentes en las que la muñeca la observaba con ojos llenos de odio. \nConvencida de que la muñeca era la causa de todos sus males, Anya decidió deshacerse de ella. La llevó al bosque y la enterró profundamente. Sin embargo, sus problemas no habían terminado. Las pesadillas continuaron, y la sensación de ser observada la acompañaba a todas partes. \nUn día, mientras exploraba el ático, Anya encontró un viejo diario. Al leerlo, descubrió que la muñeca había sido un regalo de cumpleaños para la bisabuela de Anya, una niña solitaria y enfermiza. Se decía que la muñeca había cobrado vida durante la noche y había sido la mejor amiga de la niña. Pero cuando la niña falleció, la muñeca quedó encerrada en la habitación, sumida en una profunda tristeza. \nElla comprendió entonces que la muñeca no era un objeto maligno, sino una alma atormentada que buscaba compañía. Decidió llevar la muñeca de vuelta a la mansión y colocarla en su habitación. Esa noche, mientras dormía, sintió una presencia cálida a su lado. Al abrir los ojos, vio a la muñeca sonriendo suavemente.\nA partir de ese momento, Ella y la muñeca se convirtieron en inseparables. La muñeca ya no era una fuente de terror, sino una compañera fiel. Sin embargo, Ella sabía que el secreto de la muñeca debía permanecer oculto, ya que el mundo exterior nunca entendería su conexión especial.")
        
        else:
            print("Tu opción no es válida")
        
    elif intensidad == "3_3":
        print("Escogiste intensidad fuerte")
        objetos_malditos_2 = ["casa", "atico", "persona"]
        obj_maldito=input("Escoge y escribe el nombre de alguno de estos objetos \n-" + " \n-" .join(objetos_malditos_2) + "-\n")
        
        if obj_maldito == "casa":
            persona_6 = input("Apellido de la familia original: ")
            persona_6_1 = input("Apellido de los nuevos propietarios: ")
            print ("Vamos por el cuento \n\nLa Residencia de las Sombras \nEn las afueras de un pueblo sumido en una bruma constante, se erguía la mansión " + persona_6 + "Una construcción gótica que desafiaba el paso del tiempo, con ventanas oscuras que parecían mirar fijamente hacia el interior de las almas. Los lugareños la evitaban, susurrando leyendas de horrores inexplicables que habían ocurrido entre sus muros. \nLa familia " + persona_6 + "una dinastía adinerada y excéntrica, había habitado la mansión durante generaciones. Se decía que un antiguo ritual había corrompido la casa, atrayendo a entidades oscuras que se alimentaban del miedo y la desesperación de sus habitantes. \nCuando los nuevos propietarios, los hermanos " + persona_6_1 + ", se mudaron, ignoraron las advertencias. La casa era una ganga, y la vista desde las colinas era impresionante. Sin embargo, desde el primer momento, una sensación de inquietud los envolvió. Extraños ruidos resonaban en la noche, sombras se deslizaban por los pasillos, y la temperatura de las habitaciones fluctuaba de manera inexplicable. \nLos cuadros se volvían hacia las paredes, mostrando rostros distorsionados que parecían cambiar con cada mirada. Los espejos reflejaban figuras que no existían, y los muebles se movían solos. Los hermanos comenzaron a tener pesadillas recurrentes, donde eran perseguidos por entidades oscuras que surgían de las profundidades de la casa. \nCon el tiempo, la cordura de los hermanos empezó a deteriorarse. Aislados y aterrorizados, se volvieron paranoicos, acusándose mutuamente de intentar hacerles daño. Las peleas se volvieron cada vez más violentas, hasta que una noche, uno de ellos desapareció sin dejar rastro. \nLos vecinos, alertados por los gritos y los golpes, llamaron a la policía. Cuando los agentes entraron en la mansión, encontraron una escena dantesca. Los muebles estaban destrozados, los cuadros colgaban de las paredes como si hubieran sido arrancados con fuerza, y un olor a sangre impregnaba el aire. El hermano superviviente, enloquecido, deambulaba por los pasillos, murmurando palabras incoherentes. \nLa casa " + persona_6 + " fue sellada y abandonada. Se dice que aún hoy, en las noches sin luna, las ventanas de la mansión brillan con una luz fantasmal, y los gritos de los " + persona_6 + " resuenan entre los árboles, una macabra melodía que advierte a los incautos de no acercarse nunca a la residencia de las sombras.")
            
        elif obj_maldito == "atico":
            persona_7 = input("Apellido de la familia original: ")
            persona_7_1 = input("Apellido de los nuevos propietarios: ")
            print("Vamos por el cuento \n\nEL 'Atico Olvidado \nLa casa de los " + persona_7 + " era una antigua mansión victoriana que se erguía imponente en un barrio tranquilo. Su ático, un espacio polvoriento y lleno de telarañas, había permanecido cerrado durante décadas. Los rumores sobre lo que se ocultaba en su interior se habían convertido en leyendas entre los vecinos. \nLos nuevos propietarios, los hermanos " + persona_7_1 + ", atraídos por el encanto de la casa, decidieron explorar el ático. Al abrir la pesada puerta de madera, un hedor a humedad y descomposición los envolvió. El espacio era inmenso, con vigas de madera oscura y ventanas tapiadas que dejaban pasar una tenue luz. En el centro de la habitación, un viejo baúl de hierro oxidado parecía llamar su atención. \nIntrigados, los hermanos comenzaron a mover los muebles y a examinar los objetos que se encontraban amontonados en el ático. Entre ellos, encontraron un diario amarillento y un extraño pentagrama dibujado en la pared. Al leer el diario, descubrieron que el antiguo propietario de la casa había realizado rituales satánicos en el ático, invocando a entidades oscuras. \nA partir de ese momento, extraños sucesos comenzaron a ocurrir en la casa. Objetos se movían solos, las puertas se cerraban de golpe y las sombras cobraban vida en las paredes. Los hermanos empezaron a tener pesadillas recurrentes donde eran perseguidos por criaturas grotescas que surgían de las profundidades del ático. \nLa situación se volvió insostenible cuando uno de los hermanos desapareció misteriosamente. El otro, aterrorizado, decidió investigar a fondo el pasado de la casa. Descubrió que el baúl de hierro contenía un antiguo grimorio con instrucciones para realizar un exorcismo. Sin embargo, al intentar llevar a cabo el ritual, algo salió terriblemente mal. \nEl ático se convirtió en un portal hacia otra dimensión, y entidades demoníacas comenzaron a invadir la casa. Los hermanos Miller se vieron atrapados en una lucha desesperada por sobrevivir. El ático, ahora un epicentro de oscuridad, se había convertido en su peor pesadilla.")
            
        elif obj_maldito == "persona":
            persona_8 = input("Nombre de tu personaje principal (femenino): ")
            persona_8_1 = input("Apellido de la familia: ")
            print("Vamos por el cuento \n\nLa Sombra en los Ojos \nEl pequeño pueblo de Willow Creek siempre había sido un lugar tranquilo, hasta que llegaron los rumores sobre la familia " + persona_8_1 + ". Eran nuevos en la comunidad, una familia discreta que rara vez salía de su antigua mansión. Pero pronto, las extrañas luces que se veían en las ventanas durante la noche y los gritos agudos que resonaban en la madrugada comenzaron a despertar la inquietud de los vecinos. \nLa mayor de los " + persona_8_1 + ", una joven llamada " + persona_8 + ", era el centro de atención. Al principio, parecía una chica amable y tímida, pero con el paso del tiempo, su comportamiento se volvió cada vez más errático. Sus ojos, antes llenos de vida, ahora eran oscuros y vacíos, como si una sombra los hubiera consumido por completo. \nLos vecinos comenzaron a notar cambios extraños en ella. A veces, su voz se volvía profunda y masculina, y decía cosas que no tenían sentido. En otras ocasiones, se quedaba inmóvil durante horas, con una expresión de odio en su rostro. Los objetos se movían solos en su habitación, y las puertas se cerraban de golpe sin una explicación. \nUna noche, un grupo de adolescentes, atraídos por la morbosa curiosidad, se acercaron a la mansión. Al asomarse por una ventana, vieron a " + persona_8 + " de pie en el centro de la habitación, rodeada de velas negras. Sus ojos brillaban intensamente en la oscuridad, y sus labios se movían en una oración ininteligible. De repente, la ventana se estrelló, y ella desapareció. \nAterrorizados, los adolescentes huyeron del lugar. Al día siguiente, se encontró el cuerpo sin vida de uno de ellos en el bosque cercano. La policía investigó el caso, pero no encontraron ninguna evidencia que los llevara a los " + persona_8_1 + ". \nLos vecinos, cada vez más aterrorizados, comenzaron a sospechar que la joven estaba poseída por un demonio. Un anciano sacerdote, conocido por sus conocimientos en exorcismos, fue llamado para ayudar a la familia. Sin embargo, cuando intentó realizar el ritual, " + persona_8 + " se volvió más violenta que nunca. Sus ojos se pusieron completamente blancos, y su cuerpo se contorsionó de una manera que desafiaba las leyes de la naturaleza.")
             
        else:
            print("Tu opción no es válida")
          
if opcion == 2:
    print("¿Cuánta cantidad de terror quieres?")
    print("El número 1 para leve")
    print("El número 2 para intermedio")
    cantidad = int(input("¿Qué escoges? "))
    
    if cantidad == 1:
        print("Escogiste intensidad leve")
        objetos_malditos_3 = ["pluma", "lampara", "cuadro"]
        obje_maldicion = input("Escoge y escribe el nombre de alguno de estos objetos \n-" + " \n-" .join(objetos_malditos_3) + "-\n")
        
        if obje_maldicion == "pluma":
            persona_9 = input("Nombre de tu personaje principal: ")
            print("Vamos por el cuento \n\nLa Pluma Mágica \nEn un pequeño pueblo rodeado de bosques, vivía un niño llamado " + persona_9 + ". Era un niño muy curioso y le encantaba explorar los rincones de su casa. Un día, mientras rebuscaba en el ático polvoriento de su abuela, encontró una pluma antigua y muy bonita. Era de un color azul intenso y tenía unas plumas suaves como el terciopelo. \nUn día se llevó la pluma a su habitación y comenzó a dibujar con ella. Para su sorpresa, los dibujos cobraban vida. Dibujó un pequeño pájaro y este salió volando por la ventana. Dibujó un castillo y se encontró explorándolo en sus sueños. \nAl principio, " + persona_9 + "  estaba encantado con su nueva pluma mágica. Pero pronto comenzó a notar cosas extrañas. Los dibujos que hacía no siempre obedecían sus órdenes. Una vez, dibujó un dragón, pero en lugar de ser amigable, el dragón empezó a rugir y a echar fuego. " + persona_9 + " tuvo que borrarlo rápidamente para que desapareciera. \nUna noche, mientras dormía, soñó que la pluma lo llevaba a un lugar oscuro y misterioso. Allí, vio a una bruja anciana que le advirtió que la pluma tenía un gran poder y que debía usarla con cuidado. Si dibujaba algo malo, podría traer consecuencias terribles. \nAl despertar, decidió que sería mejor guardar la pluma en un lugar seguro. La envolvió en un paño suave y la escondió en el fondo de su cajón. Desde entonces, nunca volvió a dibujar con ella, pero siempre recordaría la aventura que había vivido con la pluma mágica.")
        
        elif obje_maldicion == "lampara":
            persona_10 = input("Nombre de tu personaje principal: ")
            print("Vamos por el cuento \n\nLa Lámpara que Susurraba en la Noche \nEn una casa antigua y llena de rincones oscuros vivía un niño llamado " + persona_10 + ". Su habitación era su lugar favorito, lleno de juguetes y libros. Pero había algo en esa habitación que le daba un poco de miedo: una vieja lámpara que había pertenecido a su bisabuelo. \nLa lámpara era muy extraña. Tenía dibujos raros y una luz tenue que parpadeaba como si estuviera viva. Por las noches, cuando intentaba dormir, escuchaba unos susurros que venían de la lámpara. Al principio, pensó que eran solo los ruidos de la casa vieja, pero los susurros se volvían cada vez más claros. \nUna noche, no pudo más. Se levantó de la cama y se acercó a la lámpara. Los susurros se intensificaron y vio cómo la luz parpadeaba más rápido. De repente, la lámpara comenzó a girar sola y los dibujos se movieron como si estuvieran vivos. Se asustó tanto que salió corriendo de la habitación y se metió en la cama de sus padres. \nAl día siguiente, le contó a su mamá lo que había pasado. Su mamá lo abrazó y le dijo que no se preocupara, que solo eran sus imaginaciones. Pero Martín seguía sintiendo miedo. \nUn día, mientras limpiaba su habitación, encontró un viejo libro debajo de la cama. Era un diario de su bisabuelo. Al leerlo, descubrió que la lámpara tenía una historia muy extraña. Según el diario, la lámpara había sido un regalo de un mago. Pero el mago le había advertido a su bisabuelo que la lámpara solo debía usarse en ocasiones especiales, ya que tenía un poder misterioso. \nSe dio cuenta de que los susurros que escuchaba eran las historias que la lámpara guardaba en su interior. Decidió que lo mejor era dejar de escucharla y taparla con una sábana. A partir de ese momento, dejó de tener miedo y la lámpara se quedó en silencio, guardando sus secretos en la oscuridad.")
        
        elif obje_maldicion == "cuadro":
            persona_11 = input("Nombre de tu personaje principal (femenino): ")
            print("Vamos por el cuento \n\nEl Retrato que Observaba \nEn una casa antigua y llena de pasillos oscuros, vivía una niña llamada " + persona_11 + ". Su habitación era su rincón favorito, lleno de juguetes y libros. Pero había algo en esa habitación que a ella le daba un poco de miedo: un viejo retrato que colgaba en la pared. \nEl retrato era de una mujer muy hermosa, pero tenía una mirada extraña, como si estuviera observando todo el tiempo. Por las noches, cuando ella intentaba dormir, sentía que los ojos de la mujer del retrato la seguían. Al principio, pensó que eran solo sus imaginaciones, pero la sensación se volvía cada vez más fuerte. \nUna noche, no pudo más. Se levantó de la cama y se acercó al retrato. La mujer del cuadro parecía sonreírle levemente. Ella se asustó tanto que salió corriendo de la habitación y se metió en la cama de sus padres. \nAl día siguiente, le contó a su mamá lo que había pasado. Su mamá la abrazó y le dijo que no se preocupara, que solo eran sus imaginaciones. Pero seguía sintiendo miedo. \nUn día, mientras limpiaba su habitación, encontró un viejo libro debajo de la cama. Era un diario de su bisabuela. Al leerlo, descubrió que el retrato tenía una historia muy extraña. Según el diario, el retrato había sido pintado por un artista muy famoso, pero se decía que la mujer del cuadro estaba maldita. \nSe dio cuenta de que la sensación de ser observada era real. Decidió que lo mejor era tapar el retrato con una sábana. A partir de ese momento, dejó de tener miedo y el retrato quedó oculto a la vista, guardando su secreto en la oscuridad.")
        
        else:
            print("Tu opción no es válida")
        
    elif cantidad == 2:
        objetos_malditos_4 = ["cable", "peluche", "sombrero"]
        objet_maldicion = input("Escoge y escribe el nombre de alguno de estos objetos \n-" + " \n-" .join(objetos_malditos_4) + "-\n")
        
        if objet_maldicion == "cable":
            persona_12 = input("Nombre de tu personaje principal (masculino): ")
            print("Vamos por el cuento \n\nEl Cable que Chillaba en la Noche \nEn una casa antigua y llena de pasillos oscuros, vivía un niño llamado " + persona_12 + ". Su habitación era su refugio, un lugar lleno de juguetes y libros. Pero había algo en esa habitación que a el le daba un poco de miedo: un viejo cable que colgaba del techo y se conectaba a una lámpara. \nEl cable era muy extraño. Tenía un aspecto desgastado y parecía demasiado largo para la lámpara. Por las noches, cuando intentaba dormir, escuchaba unos chillidos agudos que venían del cable. Al principio, pensó que eran solo los ruidos de la casa vieja, pero los chillidos se volvían cada vez más fuertes. \nUna noche, no pudo más. Se levantó de la cama y se acercó al cable. Los chillidos se intensificaron y vio cómo el cable se movía solo, como si estuviera vivo. Lucas se asustó tanto que salió corriendo de la habitación y se metió en la cama de sus padres. \nAl día siguiente, le contó a su mamá lo que había pasado. Su mamá lo abrazó y le dijo que no se preocupara, que solo eran sus imaginaciones. Pero seguía sintiendo miedo. \nUn día, mientras exploraba el ático, encontró un viejo diario de su abuelo. Al leerlo, descubrió que el cable tenía una historia muy extraña. Según el diario, el cable había pertenecido a un inventor que había tratado de crear un robot. Pero el experimento había salido mal y el robot se había vuelto loco, atrapando al inventor dentro de la casa. \nEl se dio cuenta de que los chillidos del cable eran los gritos de ayuda del inventor atrapado. Decidió que tenía que hacer algo para liberarlo. Con mucho cuidado, comenzó a desenredar el cable. A medida que lo hacía, los chillidos se volvían más fuertes. De repente, el cable se soltó y cayó al suelo. En ese momento, se escuchó un ruido extraño y la lámpara comenzó a parpadear. \nEl se asustó, pero no se dio por vencido. Siguió tirando del cable hasta que de repente, se detuvo. Lucas miró hacia arriba y vio una pequeña puerta oculta en el techo. Con mucho esfuerzo, logró abrir la puerta y se encontró con una habitación secreta. \nDentro de la habitación, encontró una caja de metal. Al abrirla, encontró un pequeño robot oxidado. Lucas lo tomó en sus manos y lo llevó a su habitación. El robot estaba muy dañado, pero Lucas sabía que tenía que ayudarlo. \nCon la ayuda de su papá, repararón al robot. Cuando el robot se encendió, los chillidos del cable cesaron por completo. Se dio cuenta de que había logrado liberar al inventor y salvar a su casa de la maldición.")
            
        elif objet_maldicion == "peluche":
            persona_13 = input("Nombre de tu personaje principal (masculino): ")
            print("Vamos por el cuento \n\nEl Osito que Susurraba en la Noche \nEn una habitación llena de juguetes, vivía un niño llamado " + persona_13 + ". Su osito de peluche, Pelusa, era su mejor amigo. Era suave, esponjoso y tenía una sonrisa que parecía tan real como la de Mateo. Pero Pelusa guardaba un secreto oscuro. \nPor las noches, cuando el se quedaba dormido, escuchaba una voz suave que susurraba su nombre. Al principio, pensó que era su imaginación, pero los susurros se volvían cada vez más claros. Era la voz de Pelusa. \nUna noche, se despertó sobresaltado. Pelusa lo estaba mirando fijamente, y sus ojos, que antes eran de botones negros, ahora brillaban como dos luciernagas. Pelusa se levantó y comenzó a caminar por la habitación, susurrando palabras que el niño no entendía. \nAterrorizado, salió corriendo de su habitación y se escondió debajo de las sábanas de sus padres. Al día siguiente, le contó a su mamá lo que había pasado. Su mamá lo abrazó y le dijo que no se preocupara, que solo era una pesadilla. Pero el sabía que lo que había visto era real. \nCon el paso de los días, los susurros se hicieron más frecuentes y extraños. Pelusa comenzó a moverse solo y a cambiar de forma. A veces, parecía más grande y amenazador, y otras veces, se hacía más pequeño y más escurridizo. \nUn día, encontró un viejo libro en el ático. Era un diario que pertenecía a su abuela. Al leerlo, descubrió que Pelusa tenía una historia muy extraña. Según el diario, Pelusa había sido un regalo de una bruja. La bruja había puesto un hechizo en el osito, para que pudiera susurrar los secretos más oscuros de las personas. \nEL se dio cuenta de que Pelusa estaba tratando de hacerle daño. Decidió que tenía que deshacerse del osito maldito. Con mucho miedo, lo llevó al jardín y lo enterró bajo un árbol. \nAl día siguiente, cuando se despertó, se sintió mucho más tranquilo. Los susurros habían desaparecido por completo. Y aunque extrañaba a su viejo amigo, sabía que había hecho lo correcto.")
            
        elif objet_maldicion == "sombrero":
            persona_14 = input("Nombre de tu personaje principal (femenino): ")
            print("Vamos por el cuento \n\nEl Sombrero que Susurraba Secretos \nEn una antigua mansión, llena de rincones oscuros y polvorientos, vivía una niña llamada " + persona_14 + ". Su habitación era su refugio, un lugar lleno de juguetes y libros. Pero había algo en esa habitación que a ella le daba un poco de miedo: un viejo sombrero que colgaba de una percha. \nEl sombrero era muy extraño. Era de un color negro intenso y tenía una forma puntiaguda. Por las noches, cuando intentaba dormir, escuchaba una voz susurrante que parecía venir del sombrero. Al principio, pensó que era el viento que se colaba por la ventana, pero los susurros se volvían cada vez más claros y siniestros. \nUna noche, ella no pudo más. Se levantó de la cama y se acercó al sombrero. Los susurros se intensificaron y sintió un escalofrío recorrer su espalda. El sombrero parecía moverse solo, como si estuviera vivo. Ella se asustó tanto que salió corriendo de la habitación y se metió en la cama de sus padres. \nAl día siguiente, ella le contó a su abuela lo que había pasado. Su abuela, una mujer sabia y misteriosa, la escuchó con atención. Le dijo que ese sombrero tenía una larga historia y que era mejor que lo dejara en paz. \nIntrigada, ella decidió investigar sobre el sombrero. Encontró un viejo diario en el ático que pertenecía a su bisabuelo. Según el diario, el sombrero había pertenecido a un mago que había realizado un hechizo oscuro. El mago había encerrado sus secretos más terribles dentro del sombrero, y ahora, esos secretos buscaban salir a la luz. \nElla se dio cuenta de que los susurros que escuchaba eran los secretos oscuros del mago. Decidió que tenía que deshacerse del sombrero antes de que fuera demasiado tarde. Con mucho cuidado, lo envolvió en una tela y lo llevó al jardín. Allí, lo enterró bajo un árbol viejo y seco. \nAl día siguiente, cuando Ana volvió a su habitación, sintió una gran sensación de alivio. Los susurros habían desaparecido por completo y el sombrero ya no la asustaba.")
        else:
            print("Tu opción no es válida")
        
elif opcion == 3:
    print("Mucho gusto " + nombre + " hasta luego")

else:
    print("Tu opción no es válida")