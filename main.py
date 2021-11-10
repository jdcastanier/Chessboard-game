import random

from graphics import *

#INICIA EL PROGRAMA PRINCIPAL
def main():
    #CREA UN MENÚ INICIAL PARA ELEGIR EL JUEGO (AUNQUE ES UNO SOLO)
    def menu():
        print(f'''
BIENVENIDO AL PROGRAMA DE JUEGOS PARA DESARROLLAR 
NUESTRAS HABILIDADES COGNITIVAS. POR FAVOR ESCOJA UNA
DE LAS SIGUIENTES OPCIONES:
    
1. IMPOSSIBLE ESCAPE: TECLEE "1".
    
EN CUALQUIER MOMENTO DURANTE EL JUEGO TECLEE "SALIR"
PARA TERMINAR EL JUEGO Y REGRESAR AL MENÚ PRINCIPAL.

    ''')

        opcion = input()
        if opcion == "1":
            impossible_escape()
        else:
            opcion_1 = opcion.upper()
            if opcion_1 != "SALIR":
                print ('INPUT INCORRECTO')
            menu()

    #INICIA EL JUEGO
    def impossible_escape():
        
        #CREA LAS MONEDAS EN LA VENTANA CUANDO SE JUEGA
        def monedas_real(ventana_tablero_expo, letras, numeros):
            matriz_circulos = []
            for col in range(65, 416, 50):
                for ren in range(65, 416, 50):
                    lista = []
                    circulo = Circle(Point(ren, col), 23)
                    color_num = random.randint(0, 1)
                    if color_num == 0:
                        circulo.setFill(color_rgb(247, 198, 86))
                        color = "amarillo"
                        lista.append(ren)
                        lista.append(col)
                        lista.append(color)
                    else:
                        circulo.setFill(color_rgb(129, 95, 18))
                        color = "cafe"
                        lista.append(ren)
                        lista.append(col)
                        lista.append(color)
                    circulo.draw(ventana_tablero_expo)
                    matriz_circulos.append(lista)
            print(f'''


- CARCELERO: Tienes derecho a cambiar la configuración de una sola moneda. 

INGRESA LA UBICACIÓN DE LA MONEDA QUE QUIERES CAMBIAR. HAZLO DE LA FORMA: A, 1
NOTARÁS QUE LA MONEDA EN LA POSICIÓN QUE ELEGISTE CAMBIA SU CONFIGURACIÓN.
''')
            # matriz = [[ren, col, color]]
            moneda = input()
            moneda_1 = moneda.upper()
            if moneda_1 == "SALIR":
                menu()

            lista_coord = moneda.split(", ")
            num_trad = [0,1,2,3,4,5,6,7] 

            if (lista_coord[0] not in "ABCDEFGH") \
            or (lista_coord[1] not in "12345678") :
                print ('INPUT INCORRECTO')      
                menu()      

            for ren in range(len(letras)):
                if lista_coord [0] == letras [ren]:
                    for col in range(len(numeros)):
                        if lista_coord [1] == numeros [col]:
                            coord_trad_1 = [num_trad[ren], num_trad[col]]
                            coord_trad_2 =(num_trad[ren]) +(num_trad[col]*8)
                            break

            circulo_cambio = Circle(Point(matriz_circulos[coord_trad_2][0],\
            matriz_circulos[coord_trad_2][1]), 23)

            if matriz_circulos [coord_trad_2][2] == "cafe":
                circulo_cambio.setFill(color_rgb(247, 198, 86))
                matriz_circulos [coord_trad_2][2] = "amarillo"
            elif matriz_circulos [coord_trad_2][2] == "amarillo":
                circulo_cambio.setFill(color_rgb(129, 95, 18))
                matriz_circulos [coord_trad_2][2] = "cafe"

            circulo_cambio.draw(ventana_tablero_expo)
            return(None)

        #TRADUCE LA POSICION DE FORMATO "A, 1" A PIXELES Y LLAMA A LA FUNCION QUE DIBUJA EL CUADRO ROJO
        def buscar_rojo_real(ventana_tablero_expo, posicion_rojo, letras, numeros, coordenadas_llaves):
            buscador_a = input()
            buscador_1 = buscador_a.upper()
            if buscador_1 == "SALIR":
                menu()

            
            buscador_list = buscador_a.split(", ")
            num_trad = [0,1,2,3,4,5,6,7] 
            
            if (buscador_list[0] not in "ABCDEFGH") \
            or (buscador_list[1] not in "12345678") :
                print ('INPUT INCORRECTO')
                menu()


            for ren in range(len(letras)):
                if buscador_list [0] == letras [ren]:
                    for col in range(len(numeros)):
                        if buscador_list [1] == numeros [col]:
                            coord_trad_3 = [(num_trad[ren]*50 + 40),(num_trad[col]*50 + 40)]
                            break

            cosa = rectangulo_rojo(ventana_tablero_expo, coordenadas_llaves, letras, numeros)
            if posicion_rojo[0] == coord_trad_3[0] \
            and posicion_rojo[1] == coord_trad_3[1]:
                print('''
                
                



- CARCELERO: ¡Felicitaciones! Han logrado descifrar la posición de las llaves. Quedan libres. ''')
            else:
                print('''
                
                



- CARCELERO: JAJAJAJAJA no pudieron descifrar la ubicación de las llaves, serán ejecutados.''')

        #CREA LA VENTANA CUANDO SE JUEGA
        def crear_ventana_real():
            ventana_tablero_real = GraphWin('Tablero', 450, 450)
            negro = Rectangle(Point(40, 40), Point(440, 440))
            negro.setOutline(color_rgb(0, 50, 255))
            negro.setWidth(3)
            negro.setFill(color_rgb(0, 0, 0))
            negro.draw(ventana_tablero_real)
            for ren in range(40, 441, 50):
                for col in range(40, 441, 50):
                    if ren == 40 or ren == 140 or ren == 240 or ren == 340:
                        if col == 90 or col == 190 or col == 290 or col == 390:
                            blancos(ren, col, ventana_tablero_real)
                    elif ren == 90 or ren == 190 or ren == 290 or ren == 390:
                        if col == 40 or col == 140 or col == 240 or col == 340:
                            blancos(ren, col, ventana_tablero_real)
            letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
            numeros = ['1', '2', '3', '4', '5', '6', '7', '8']
            indices(letras, numeros, ventana_tablero_real)
            posicion_llaves_ren = random.randint(0, 7)
            posicion_llaves_col = random.randint(0, 7)
            coordenadas_llaves = [posicion_llaves_ren, posicion_llaves_col]

            posicion_rojo = rectangulo_rojo(ventana_tablero_real, coordenadas_llaves, letras, numeros)
            

            ventana_tablero_real.getMouse()
            regresa_rectangulo(ventana_tablero_real, posicion_rojo)
            monedas_real(ventana_tablero_real, letras, numeros)                    
            print('''
            
            
            
            
            
- CARCELERO: Ahora puede venir el segundo prisionero para intentar adivinar en dónde se encuentran las llaves. Los prisioneros deben recordar que no pueden comunicarse.
            
EL SEGUNDO JUGADOR DEBE INGRESAR LA POSICIÓN EN LA QUE CREE QUE ESTÁN LAS LLAVES. LO DEBE HACER EN EL FORMATO A, 1''')
            buscar_rojo_real(ventana_tablero_real, posicion_rojo, letras, numeros, coordenadas_llaves)
            print (f'''
        
        
        
GRACIAS POR JUGAR IMPOSSIBLE ESCAPE, SI QUIERES INTENTARLO DE NUEVO, VUELVE A CORRER EL PROGRAMA.

LA SOLUCIÓN SE ENCUENTRA DISPONIBLE EN: http://datagenetics.com/blog/december12014/index.html

PROGRAMA REALIZADO POR JUAN DANIEL CASTANIER RIVAS.
TEC DE MONTERREY.''')
            ventana_tablero_real.getMouse()
            ventana_tablero_real.close()
            return(None)

        #FUNCION QUE DIBUJA EL RECUADRO ROJO AL AZAR
        def rectangulo_rojo(ventana_tablero_expo, coordenadas_llaves, letras, numeros):
            rectangulo_rojo = Rectangle( Point(40 +(50 * coordenadas_llaves[0]),\
            40 +(50 * coordenadas_llaves[1])), \
            Point(90 +(50 * coordenadas_llaves[0]), \
            90 +(50 * coordenadas_llaves[1])))
            rectangulo_rojo.setFill(color_rgb(255, 0, 0))
            rectangulo_rojo.draw(ventana_tablero_expo)
            posicion_rojo = [40 +(50 * coordenadas_llaves[0]), \
            40 +(50 * coordenadas_llaves[1]), \
            90 +(50 * coordenadas_llaves[0]), \
            90 +(50 * coordenadas_llaves[1])]
            letra = letras [coordenadas_llaves[0]]
            numero = numeros [coordenadas_llaves[1]]
            print(f'''


Las llaves son asignadas a la posición {letra}, {numero}.
            
DALE CLICK AL TABLERO PARA CONTINUAR''')
            return(posicion_rojo)
            
        #TRADUCE LA POSICION DE FORMATO "A, 1" A PIXELES Y LLAMA A LA FUNCION QUE DIBUJA EL CUADRO ROJO, A DIFERENCIA DE BUSCAR_ROJO_REAL TIENE EL PRINT DEL TUTORIAL.
        def buscar_rojo(ventana_tablero_expo, posicion_rojo, letras, numeros, coordenadas_llaves):
            buscador = input()
            buscador_2 = buscador.upper()
            if buscador_2 == "SALIR":
                menu()

            buscador_list = buscador.split(", ")
            num_trad = [0,1,2,3,4,5,6,7] 
            
            if (buscador_list[0] not in "ABCDEFGH") \
            or (buscador_list[1] not in "12345678") :
              print ('INPUT INCORRECTO')
              menu()

            for ren in range(len(letras)):
                if buscador_list [0] == letras [ren]:
                    for col in range(len(numeros)):
                        if buscador_list [1] == numeros [col]:
                            coord_trad_3 = [(num_trad[ren]*50 + 40),(num_trad[col]*50 + 40)]
                            break
            cosa = rectangulo_rojo(ventana_tablero_expo, \
            coordenadas_llaves, letras, numeros)
            if posicion_rojo[0] == coord_trad_3[0] \
            and posicion_rojo[1] == coord_trad_3[1]:
                print('''
                
                



- CARCELERO: Una vez el que el segundo prisionero haya escogido el casillero en donde cree que se asignaron las llaves, se le revelará la posición real de las llaves, y en caso de haberlo logrado los dos quedarán salvados, caso contrario, ambos serán ejecutados.''')
            else:
                print('''
                
                



- CARCELERO: Una vez el que el segundo prisionero haya escogido el casillero en donde cree que se asignaron las llaves, se le revelará la posición real y en caso de haberlo logrado los dos quedarán salvados, caso contrario, ambos serán ejecutados.''')

        #DEVUELVE EL COLOR ORIGINAL AL RECUADRO ROJO
        def regresa_rectangulo(ventana_tablero_expo, posicion_rojo):
            rentangulo_cambio = Rectangle(Point(posicion_rojo [0], posicion_rojo[1]), \
            Point(posicion_rojo[2], posicion_rojo [3]))
            if posicion_rojo [0] == 40 \
            or posicion_rojo [0] == 140 \
            or posicion_rojo [0] == 240 \
            or posicion_rojo [0] == 340:
                if posicion_rojo [1] == 90 \
                or posicion_rojo [1] == 190 \
                or posicion_rojo [1] == 290 \
                or posicion_rojo [1] == 390:
                    rentangulo_cambio.setFill(color_rgb(255,255,255))
                else:
                    rentangulo_cambio.setFill(color_rgb(0,0,0))
            else:
                if posicion_rojo [1] == 40 \
                or posicion_rojo [1] == 140 \
                or posicion_rojo [1] == 240 \
                or posicion_rojo [1] == 340:
                    rentangulo_cambio.setFill(color_rgb(255,255,255))
                else:
                    rentangulo_cambio.setFill(color_rgb(0,0,0))
            rentangulo_cambio.draw(ventana_tablero_expo)

        #COLOCA LAS MONEDAS EN LA VENTANA, A DIFERENCIA DE MONEDAS_REAL TIENE EL PRINT DEL TUTORIAL
        def monedas_expo(ventana_tablero_expo, letras, numeros):
            matriz_circulos = []
            for col in range(65, 416, 50):
                for ren in range(65, 416, 50):
                    lista = []
                    circulo = Circle(Point(ren, col), 23)
                    color_num = random.randint(0, 1)
                    if color_num == 0:
                        circulo.setFill(color_rgb(247, 198, 86))
                        color = "amarillo"
                        lista.append(ren)
                        lista.append(col)
                        lista.append(color)
                    else:
                        circulo.setFill(color_rgb(129, 95, 18))
                        color = "cafe"
                        lista.append(ren)
                        lista.append(col)
                        lista.append(color)
                    circulo.draw(ventana_tablero_expo)
                    matriz_circulos.append(lista)
            print(f'''




- CARCELERO: Luego de asignar la llave a un casillero, colocaré una moneda en cada casillero. 
La configuración de cada moneda(cara o cruz) será totalmente mi decisión. Puede ser al azar o puede ser un orden malvado apropósito con el fin de hacerlo más difícil, es mi problema.
Entonces le dejaré a quien se quedó conmigo cambiar la configuración de una sola moneda. 

INGRESA LA UBICACIÓN DE LA MONEDA QUE QUIERES CAMBIAR. HAZLO DE LA FORMA: A, 1
NOTARÁS QUE LA MONEDA EN LA POSICIÓN QUE ELEGISTE CAMBIA SU CONFIGURACIÓN.
''')
            # matriz = [[ren, col, color]]
            moneda = input()
            moneda_2 = moneda.upper()
            if moneda_2 == "SALIR":
                menu()

            lista_coord = moneda.split(", ")
            num_trad = [0,1,2,3,4,5,6,7]
            
            if (lista_coord[0] not in "ABCDEFGH") \
            or (lista_coord[1] not in "12345678") :
              print ('INPUT INCORRECTO') 
              menu()

            for ren in range(len(letras)):
                if lista_coord [0] == letras [ren]:
                    for col in range(len(numeros)):
                        if lista_coord [1] == numeros [col]:
                            coord_trad_1 = [num_trad[ren], num_trad[col]]
                            coord_trad_2 =(num_trad[ren]) +(num_trad[col]*8)
                            break

            circulo_cambio = Circle(Point(matriz_circulos[coord_trad_2][0],\
            matriz_circulos[coord_trad_2][1]), 23)

            if matriz_circulos [coord_trad_2][2] == "cafe":
                circulo_cambio.setFill(color_rgb(247, 198, 86))
                matriz_circulos [coord_trad_2][2] = "amarillo"
            elif matriz_circulos [coord_trad_2][2] == "amarillo":
                circulo_cambio.setFill(color_rgb(129, 95, 18))
                matriz_circulos [coord_trad_2][2] = "cafe"

            circulo_cambio.draw(ventana_tablero_expo)
            return(None)

        #CREA LA VENTANA DEL TUTORIAL, A DIFERENCIA DE CREAR_VENTANA_REAL TIENE LOS PRINTS DEL TUTORIAL
        def crear_ventana_expo():
            ventana_tablero_expo = GraphWin('Tablero', 450, 450)
            negro = Rectangle(Point(40, 40), Point(440, 440))
            negro.setOutline(color_rgb(0, 50, 255))
            negro.setWidth(3)
            negro.setFill(color_rgb(0, 0, 0))
            negro.draw(ventana_tablero_expo)
            for ren in range(40, 441, 50):
                for col in range(40, 441, 50):
                    if ren == 40 or ren == 140 or ren == 240 or ren == 340:
                        if col == 90 or col == 190 or col == 290 or col == 390:
                            blancos(ren, col, ventana_tablero_expo)
                    elif ren == 90 or ren == 190 or ren == 290 or ren == 390:
                        if col == 40 or col == 140 or col == 240 or col == 340:
                            blancos(ren, col, ventana_tablero_expo)
            letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
            numeros = ['1', '2', '3', '4', '5', '6', '7', '8']
            indices(letras, numeros, ventana_tablero_expo)
            posicion_llaves_ren = random.randint(0, 7)
            posicion_llaves_col = random.randint(0, 7)
            coordenadas_llaves = [posicion_llaves_ren, posicion_llaves_col]

            posicion_rojo = rectangulo_rojo(ventana_tablero_expo, coordenadas_llaves, letras, numeros)
            

            ventana_tablero_expo.getMouse()
            regresa_rectangulo(ventana_tablero_expo, posicion_rojo)
            monedas_expo(ventana_tablero_expo, letras, numeros)                    
            print('''
            
            
            
            
            
- CARCELERO: Cuando intenten el reto de verdad, será en este momento en el que regresará el segundo prisionero; quien, sin comunicarse con el primer prisionero, sin saber cuál fue la configuración inicial del tablero, y sin saber cuál fue la moneda que modificó su compañero, deberá determinar a qué casillero se asignaron las llaves(cuadro rojo del comienzo).
            
EL SEGUNDO JUGADOR DEBE INGRESAR LA POSICIÓN EN LA QUE CREE QUE ESTÁN LAS LLAVES. LO DEBE HACER EN EL FORMATO A, 1''')
            buscar_rojo(ventana_tablero_expo, posicion_rojo, letras, numeros, coordenadas_llaves)
            return(ventana_tablero_expo)

        #DIBUJA LOS RECUADROS BLANCOS EN EL TABLERO
        def blancos(ren, col, ventana_tablero):
            blanco = Rectangle(Point(col, ren), Point(col + 50, ren + 50))
            blanco.setFill(color_rgb(255, 255, 255))
            blanco.draw(ventana_tablero)
            return(None)

        #CREA LOS INDICES ALFANUMERICOS DEL TABLERO
        def indices(lista_letras, lista_num, ventana_tablero):
            i = 0
            for lugar in range(65, 465, 50):
                text = Text(Point(lugar, 25), lista_letras[i])
                text.setTextColor(color_rgb(0, 0, 0))
                text.setSize(25)
                text.draw(ventana_tablero)
                i += 1
            i = 0
            for lugar_b in range(65, 465, 50):
                text_b = Text(Point(25, lugar_b), lista_num[i])
                text_b.setTextColor(color_rgb(0, 0, 0))
                text_b.setSize(25)
                text_b.draw(ventana_tablero)
                i += 1
            return(None)

        #CREA LA PRIMERA VENTANA DEL JUEGO Y DEL TUTORIAL, SIN LLAMAR A LA FUNCION DL RECUADRO ROJO
        def crear_ventana():
            ventana_tablero = GraphWin('Tablero', 450, 450)
            negro = Rectangle(Point(40, 40), Point(440, 440))
            negro.setOutline(color_rgb(0, 50, 255))
            negro.setWidth(3)
            negro.setFill(color_rgb(0, 0, 0))
            negro.draw(ventana_tablero)
            for ren in range(40, 441, 50):
                for col in range(40, 441, 50):
                    if ren == 40 or ren == 140 or ren == 240 or ren == 340:
                        if col == 90 or col == 190 or col == 290 or col == 390:
                            blancos(ren, col, ventana_tablero)
                    elif ren == 90 or ren == 190 or ren == 290 or ren == 390:
                        if col == 40 or col == 140 or col == 240 or col == 340:
                            blancos(ren, col, ventana_tablero)
            letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
            numeros = ['1', '2', '3', '4', '5', '6', '7', '8']
            indices(letras, numeros, ventana_tablero)
            ventana_tablero.getMouse()
            ventana_tablero.close()
            return (None)
##
        print(f'''







BIENVENIDOS A IMPOSSIBLE ESCAPE, EL RETO MATEMÁTICO. ESTE JUEGO ESTÁ DISEÑADO
PARA DOS PERSONAS. ¡ASÍ QUE CONSIGUE UN COMPAÑERO! UNA VEZ LISTOS COMENCEMOS EL TUTORIAL...(ESCRIBE "LISTOS" PARA CONTINUAR)

''')
        salir = True
        while salir == True:
            respuesta = input()
            res_may = respuesta.upper()
            if res_may == 'LISTOS':
                print()
                print(''' 



-CARCELERO: Jejeje. Hola par de prisioneros, yo seré su carcelero. Ustedes dos han sido condenados a muerte; sin embargo, estoy dispuesto a darles una oportunidad de salir en libertad. La explicaré antes de ponerlos a prueba...

DALE CLICK AL TABLERO PARA CONTINUAR''')
                salir = not(salir)
                crear_ventana()
            elif res_may == "SALIR":
                menu()
            else:
                print(
'''PALABRA INCORRECTA. ESCRIBE "LISTOS" PARA CONTINUAR''')

        print('''




-CARCELERO:    ¿Ven este tablero de ajedrez? Los separaré de modo que SÓLO UNO DE USTEDES PUEDA VER LA PANTALLA y asignaré la llave de las celdas a uno de los casilleros del tablero, mostrándole a quien se quedó conmigo la posición.

''')

        ventana_tablero_expo = crear_ventana_expo()
        print(''' 



¿Están listos para intentarlo? A partir de este momento tienen todo el tiempo que deseen para desarrollar su estrategia. Una vez listos DENLE CLICK AL TABLERO PARA EMPEZAR.''')
        ventana_tablero_expo.getMouse()
        ventana_tablero_expo.close()
        print ('''
        
        
        
        
        
-CARCELERO: Hola de nuevo prisioneros, en este momento uno de ustedes debe dejar la sala, de modo que no pueda ver la pantalla.
        
CUANDO ESTÉS LISTO DALE CLICK AL TABLERO PARA CONTINUAR.''')
        crear_ventana()
        crear_ventana_real()
        

    menu()


main()
