from random import choice 

palabras= ["panadero","dinosaurio","helipuerto","tiburon"]
letras_correctas=[]
letras_incorrectas=[]
intentos=6
aciertos=0
Juego_terminado = False

def elegir_palabra(lista):
    palabra_elegida= choice(lista)
    letras_unicas = len(set(palabra_elegida))
    return palabra_elegida, letras_unicas

def pedir_letra():
    letra_elegida =''
    es_valida = False 
    abecedario='abcdefghijklmnñopqrstuvwxyz'
    while not es_valida:
       letra_elegida = input("Elige una letra: ").lower()
       if letra_elegida in abecedario and len(letra_elegida)== 1:
           es_valida = True 
       else:
           print("No has elegido una letra válida")
    return letra_elegida

def mostrar_nuevo_tablero(Palabra_elegida):
    lista_oculta= []

    for i in Palabra_elegida:
        if i in letras_correctas:
            lista_oculta.append(i)
        else:
            lista_oculta.append('-')
    print(' '.join(lista_oculta))

def chequear(letra_elegida,palabra_oculta, vida , coincidencias,):
    
    fin = False

    if letra_elegida in palabra_oculta and letra_elegida not in letras_correctas:
        letras_correctas.append(letra_elegida)
        coincidencias += 1
    elif letra_elegida in palabra_oculta and letra_elegida in letras_correctas:
        print("Ya has encontrado la palabra, intenta otra ")
    else:
        letras_incorrectas.append(letra_elegida)
        vida -=1

    if vida == 0:
        fin =perder()
    elif coincidencias == cantidad_letras:
        fin = ganar(palabra_oculta)
    
    return vida, fin , coincidencias

def perder():
    print("Te has quedado sin vidas")
    print("La palabra oculta era: " + palabra)
    return True

def ganar(palabra_descubierta):
    mostrar_nuevo_tablero(palabra_descubierta)
    print("Felcitaciones has descubierto la palabra!!!!")

    return True

palabra, cantidad_letras = elegir_palabra(palabras)

while not Juego_terminado:
    print("\n" + "*"*20 + '\n')
    mostrar_nuevo_tablero(palabra)
    print('\n')
    print("Letras incorrectas: "+ "-".join(letras_incorrectas))
    print(f"Vidas:{intentos}")
    print("\n" + "*"*20 + '\n')
    letra =pedir_letra()
    intentos, terminado, aciertos = chequear(letra,palabra,intentos,aciertos)

    Juego_terminado= terminado