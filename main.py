import sys
import time

print("Bienvenido al Asistente 1Code")
time.sleep(0.5)
print("Para poder empezar a usar el programa necesito saber cual es tu nombre...")
time.sleep(0.5)
nombre = input()
time.sleep(0.5)
print("Bienvenido", nombre)
time.sleep(0.5)
if nombre=="1Code":
    time.sleep(0.5)
    print("Qué casualidad que nos llamemos igual!")
else:
    time.sleep(0.5)
    print("Me gusta tu nombre")
time.sleep(0.5)
print("¿Que edad tienes?")

edad = input()
 
if edad<="17":
    time.sleep(0.5)
    print("¡Todavía te queda mucha vida por delante!")

elif edad>"17":
    time.sleep(0.5)
    print("Se te acabaron las tonterias ehh")
    time.sleep(0.5)
    print("Ya tienes que comportarte como un adulto")
 
time.sleep(0.5)
print("Y...¿De dónde eres (ciudad de España) ?")

ciudad = input()
time.sleep(0.5)
if ciudad=="Madrid":
    time.sleep(0.5)
    print("Una pena no tener playa :(")
    time.sleep(0.5)
    print("Lo bueno es que hay mucho ocio y sitios para trabajar, incluso un pantano enooooorme!!")
    time.sleep(0.5)
    print("Siempre he querido visitar Madrid, pero... soy una maquina atrapada en 0 y 1 ")
     
elif ciudad=="Murcia":
    time.sleep(0.5)
    print(".....")
    time.sleep(0.5)
    print("Eso existe??")
elif ciudad=="Barcelona":
    time.sleep(0.5)
    print("Alaa, que guayy!!")
    time.sleep(0.5)
    print("Me encantaria ir a ver la sagrada familia")
elif ciudad=="Andalucia":
    time.sleep(0.5)
    print("Illo que guapo, no?")
time.sleep(0.5)
print("Por cierto, ¿cómo se llaman tus padres?")
 
time.sleep(0.5)
print("Nombre de la madre:")
madre = input()
time.sleep(0.5)
print("Nombre del padre:")
padre = input()
 
try:
    if madre == "Paula" or padre == "David":
        time.sleep(0.5)
        print("¡Qué nombres mas bonito!")

except:
    time.sleep(0.5)
    print("Qué nombres más raro")

time.sleep(0.5)
def espagueti():
    print("Aqui tienes, clicka el enlace de abajo")
    print("https://www.recetasdesbieta.com/wp-content/uploads/2020/07/espaguetis-rojos-destacada.jpg")
    menucomida()

time.sleep(0.5)
def chuleton():
    print("Aqui tienes, clicka el enlace de abajo")
    print(
        "https://www.hola.com/imagenes/cocina/recetas/20200611169948/chuleton-ternera-parrilla/0-834-955/chuletones-ternera-parrilla-m.jpg")
    menucomida()

time.sleep(0.5)
def paella():
    print("Aqui tienes, clicka el enlace de abajo")
    print("https://imag.bonviveur.es/articulos/paella-valenciana-tradicional.jpg")
    menucomida()
time.sleep(0.5)
def menu():
    print("\n****MENU****\n \n1) Calculadora\n \n2) Continuar hablando con el asistente\n \n0.- Salir")

    try:
        time.sleep(0.5)
        opcion = int(input("Elige una opcion de las siguientes:"))

        if (opcion == 1):
            calculadora()

        elif (opcion == 2):
            continuaramain()
            time.sleep(0.5)
            print("Perfecto, pues continuemos hablando !!")
            time.sleep(0.5)
            print("Oye, tienes hambre?")

            hambre = input()

            if hambre == "Si" or "si" or "bastante":
                time.sleep(0.5)
                print("Igual que yo jajajja")
                time.sleep(0.5)
                print("Ahora mismo me comeria unos microChips")
                time.sleep(0.5)
                print("Si tu tienes hambre te puedo ofrecer lo siguiente:")
                time.sleep(0.5)
                menucomida()

    except:
        time.sleep(0.5)
        print("")

def menucomida():
    time.sleep(0.5)
    print("1) Espaqueti \n 2) Chuleton \n 3) Paella \n 0) Salir")
    time.sleep(0.5)
    opcioncomida = int(input("Elige una opcion:"))
    try:
        if (opcioncomida == 1):
            espagueti()

        elif (opcioncomida == 2):
            chuleton()

        elif (opcioncomida == 3):
            paella()

        elif (opcioncomida == 0):
            time.sleep(0.5)
            print("Saliendo del programa....")
            time.sleep(0.5)
            print("¡Adios!")
            sys.exit(0)
    except:
        time.sleep(0.5)
        print("\nHas introducido letras en lugar de números. Por favor, inténtalo de nuevo.")
        menucomida()

def calculadora():

        def menucalculadora():
            print("\n****MENU****\n \n1.- Sumar\n \n11.-Suma Decimales\n \n2.- Restar\n \n22.-Resta Decimales\n \n3.- Multiplicar\n \n33.-Multiplicar Decimales\n \n4.- Dividir \n \n5.- Raiz 2\n\n6.- Raiz 3\n \n7.- Raiz 4 \n")

            try:
                time.sleep(0.5)
                opcion = int(input("\nElige una opcion de las siguientes:"))

                if (opcion == 1):
                    sumar()

                elif (opcion == 11):
                    sumardecimales()

                elif (opcion == 2):
                    restar()

                elif (opcion == 22):
                    restardecimales()

                elif (opcion == 3):
                    multiplicar()

                elif (opcion == 33):
                    multiplicardecimales()


                elif (opcion == 4):
                    dividir()

                elif (opcion == 5):
                    raiz()

                elif (opcion == 6):
                    raiz2()

                elif (opcion == 7):
                  raiz3()

            except:
                time.sleep(0.5)
                print("\nHas escrito un caracter en lugar de un número. Inténtalo de nuevo, por favor")
                calculadora()

        def sumar():
            ###SUMA##
            time.sleep(0.5)
            sumando1 = int(input("Numero 1:"))
            time.sleep(0.5)
            sumando2 = int(input("Numero 2:"))
            time.sleep(0.5)
            resultado = sumando1 + sumando2
            time.sleep(0.5)
            print("Resultado final:", resultado)
            menucalculadora()

        def sumardecimales():
            ###SUMA DECIMALES##
            time.sleep(0.5)
            sumandodec1 = float(input("Numero 1:"))
            time.sleep(0.5)
            sumandodec2 = float(input("Numero 2:"))

            resultado = sumandodec1 + sumandodec2
            time.sleep(0.5)
            print("Resultado final:", resultado)
            time.sleep(0.5)
            menucalculadora()

        def restar():
            ###RESTA###
            time.sleep(0.5)
            restando1 = int(input("Numero 1:"))
            time.sleep(0.5)
            restando2 = int(input("Numero 2:"))
            resultado = restando1 + restando2
            time.sleep(0.5)
            menucalculadora()

        def restardecimales():
            ###RESTA DECIMALES###
            time.sleep(0.5)
            restandodec1 = float(input("Numero 1:"))
            time.sleep(0.5)
            restandodec2 = float(input("Numero 2:"))
            time.sleep(0.5)

            resultado = restandodec1 - restandodec2
            time.sleep(0.5)
            print("Resultado final:", resultado)
            time.sleep(0.5)
            menucalculadora()

        def multiplicardecimales():
            ###MULTIPLICACIÓN DECIMALES###
            time.sleep(0.5)
            multidec1 = float(input("Numero 1:"))
            time.sleep(0.5)
            multidec2 = float(input("Numero 2:"))
            time.sleep(0.5)

            resultado = multidec1 * multidec2
            time.sleep(0.5)
            print("Resultado final:", resultado)
            time.sleep(0.5)
            menucalculadora()

        def multiplicar():
            ###MULTIPLICACIÓN###
            time.sleep(0.5)
            multi1 = int(input("Numero 1:"))
            time.sleep(0.5)
            multi2 = int(input("Numero 2:"))
            time.sleep(0.5)

            resultado = multi1 * multi2
            time.sleep(0.5)
            print("Resultado final:", resultado)
            time.sleep(0.5)
            menucalculadora()

        def dividir():
            ###DIVISIÓN###
            time.sleep(0.5)
            divisor1 = int(input("Numero 1:"))
            time.sleep(0.5)
            divisor2 = int(input("Numero 2:"))
            time.sleep(0.5)

            resultado = divisor1 / divisor2
            time.sleep(0.5)
            print("Resultado final:", resultado)
            time.sleep(0.5)
            menucalculadora()

        def raiz():
            ###RAIZ CUADRADA##
            time.sleep(0.5)
            numeroraiz = int(input("Numero:"))
            time.sleep(0.5)

            resultado = numeroraiz ** 0.5
            time.sleep(0.5)
            print("Resultado final:", resultado)
            time.sleep(0.5)
            menucalculadora()

        def raiz2():
            ###RAIZ CUBICA###
            time.sleep(0.5)
            numeroraiz2 = int(input("Numero:"))
            time.sleep(0.5)

            resultado = numeroraiz2 ** (1 / 3)
            time.sleep(0.5)
            print("Resultado final:", resultado)
            time.sleep(0.5)
            menucalculadora()

        def raiz3():
            ###RAIZ CUARTA###
            time.sleep(0.5)
            numeroraiz3 = int(input("Numero:"))
            time.sleep(0.5)

            resultado = numeroraiz3 ** (1 / 4)
            time.sleep(0.5)
            print("Resultado final:", resultado)
            time.sleep(0.5)
            menucalculadora()

        menucalculadora()

def continuaramain():
    time.sleep(0.5)
    print("Continua con el Asistente 1Code")

menu()
time.sleep(0.5)
print("CONTINUARA......")
