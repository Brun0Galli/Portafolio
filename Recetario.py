#menu
import os
from pathlib import Path
from os import system

ruta= Path("C:\\Users\\bruni\\OneDrive\\Desktop\\Python Total","Recetas")
abecedario= 'zxcvbnmasdfghjklñqwertyuiopZXCVBNMASDFGHJKLÑQWERTYUIOP'

def contar_recetas(ruta):
    contador = 0
    for txt in Path(ruta).glob("**/*.txt"):
        contador +=1
    return contador

def inicio():
    system("cls")
    print("-"*20)
    print("Bienvenido al admin de recetas")
    print("-" * 20)
    print(f"Las recetas se encuentran en {ruta} ")
    print(f"Total de recetas: {contar_recetas(ruta)}")
    Menu()
def Menu():
    finalizar =False
    while not finalizar:
        print('''
        Elige una opción para continuar 
        [1] - Leer receta
        [2] - Crear nueva receta
        [3] - Crear Categoria nueva
        [4] - Elimina receta 
        [5] - Eliminar categoría
        [6] - Salir del programa
        
        ''')
        validacion=False
        while not validacion:
            user_input = input("Ingresa un numero del 1-6: ")
            if user_input.isdigit():
                menu = int(user_input)
                if menu in range(1,7):
                    break
                else:
                    print("Escóge el valor indicado")
            else:
                print("Escoge un valor válido")

        if menu == 1:
          mis_categorias =  mostrar_categoria(ruta)
          mi_categoria= elegir_categoria(mis_categorias)
          mis_recetas= mostrar_recetas(mi_categoria)
          receta =elegir_recetas(mis_recetas)
          leer_receta(receta)

        elif menu == 2:
            mis_categorias = mostrar_categoria(ruta)
            mi_categoria = elegir_categoria(mis_categorias)
            crear_receta(mi_categoria)
            volver_inicio()


        elif menu == 3:
            crear_categoria(ruta)
            volver_inicio()


        elif menu == 4:
            mis_categorias = mostrar_categoria(ruta)
            mi_categoria = elegir_categoria(mis_categorias)
            mis_recetas = mostrar_recetas(mi_categoria)
            receta =elegir_recetas(mis_recetas)
            eliminar_receta(receta)
            volver_inicio()


        elif menu == 5:
            mis_categorias = mostrar_categoria(ruta)
            mi_categoria = elegir_categoria(mis_categorias)
            eliminar_categoria(mi_categoria)
            volver_inicio()

        elif menu == 6:
            finalizar = True


def mostrar_categoria(ruta):
    print('Categorias: ')
    ruta_categorias = Path(ruta)
    lista_categorias= []
    contador = 1

    for carpeta in ruta_categorias.iterdir():
        carpeta_str= str(carpeta.name)
        print(f"[{contador}]- {carpeta_str}")
        lista_categorias.append(carpeta)
        contador +=1

    return lista_categorias
def elegir_categoria(lista):
    eleccion_correcta = 'x'

    while not eleccion_correcta.isnumeric() or int(eleccion_correcta) not in range(1,len(lista)+1):
        eleccion_correcta = input("\nElige una categoria: ")

    return lista[int(eleccion_correcta)-1]
def mostrar_recetas(ruta):
    print('Recetas: ')
    ruta_recetas= Path(ruta)
    lista_recetas =[]
    contador = 1
    for receta in ruta_recetas.glob('*.txt'):
        receta_str = str(receta.name)
        print(f'[{contador}] - {receta_str}')
        lista_recetas.append((receta))
        contador +=1
    return lista_recetas

def elegir_recetas(lista):
    eleccion = 'x'
    while not eleccion.isnumeric() or int(eleccion) not in range(1, len(lista)+1):
        eleccion = input("\nElige una receta: ")
    return lista[int(eleccion)-1]
def leer_receta(receta):
    print(Path.read_text(receta))
def crear_receta(ruta):
    existe =False
    while not existe:
        print("Escribe el nombre de tu receta: ")
        nombre_receta= input() + '.txt'
        print("Escribe tu nueva receta: ")
        contenido= input()
        ruta_nueva= Path(ruta, nombre_receta)
        if not os.path.exist(ruta_nueva):
            Path.write_text(ruta_nueva,contenido)
            print(f"Tu receta {nombre_receta} ha sida creada")
            existe =True
        else:
            print("Esa receta ya existe ")

def crear_categoria(ruta):
    existe =False
    while not existe:
        print("Escribe el nombre de tu categoria nueva: ")
        nombre_categoria= input()

        ruta_nueva= Path(ruta, nombre_categoria)
        if not os.path.exist(ruta_nueva):
            Path.mkdir(ruta_nueva)
            print(f"Tu categoria {nombre_categoria} ha sida creada")
            existe =True
        else:
            print("Esa categoria ya existe ")

def eliminar_receta(receta):
    Path(receta).unlink()
    print(f"La receta {receta.name} ha sido eliminada")

def eliminar_categoria(categoria):
    Path(categoria.rmdir())
    print(f"La categoria {categoria.name} ha sido eliminada")

def volver_inicio():
    eleccion ='x'
    while eleccion.lower() !='v':
        eleccion= input("\nPresione V para volver al inicio")

inicio()