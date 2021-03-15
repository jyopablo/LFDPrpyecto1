from tkinter import *
from analizador import *
from tkinter import filedialog
from analizar_token import *
import analizador as analizador
import analizador_orden as analizador_orden
import analizar_token as analizar_token
import html_menu as html_menu

ruta1="Hola"
ruta2="Hola"
def menu():
    while True:
        print('1. Cargar menu')
        print('2. Cargar o rden')
        print('3. Generar menu')
        print('4. Generar factura')
        print('5. Generar árbol')
        print('6. Salir')
        opcion=int(input('ELIJA UNA OPCION'))
        if opcion==1:
            cargar_menu()

        elif opcion ==2:
            cargar_orden()

        elif opcion==3:
            generar_menu()

        elif opcion==4:
            generar_factura()

        elif opcion==5:
            generar_arbol()

        elif opcion==6:
               break


def cargar_menu():
    global ruta1
    try:
        ruta1=filedialog.askopenfilename(title="abrir")
        print('Datos de menu cargados')
    except Exception as e:
        print('No se eligio archivo')

def cargar_orden():
    global ruta2
    try:
        ruta2=filedialog.askopenfilename(title="abrir")
        print('Datos de orden cargados')
    except Exception as e:
        print('No se eligio archivo')

def generar_menu():
    Validacion_Tokens()
    contador=0
    archivo=open(ruta1,encoding="utf8")
    for linea in archivo.readlines():
        archivo_sin_espacios=linea.replace("  ","")
        analizador.analizar(archivo_sin_espacios,contador)
        contador +=1
    archivo.close()
    html_menu.crear()

def generar_factura():
    contador=0
    archivo_orden=open(ruta2,encoding="utf8")
    for linea in archivo_orden.readlines():
        archivo_sin_espacios=linea.replace("  ","")
        analizador_orden.analizar_orden(archivo_sin_espacios,contador)
        contador +=1
    archivo_orden.close()

def generar_arbol():
    print('Hola')

def limite_precio():
    opcion=int(input('Desea poner un limite de precio'))
    print('1. Si')
    print('2. No')
    if opcion==1:
        precio=int(input('Limite de presio'))
    else:
        pass

def Validacion_Tokens():
    try:
        contador=0
        archivo=open(ruta1,encoding="utf8")
        for linea in archivo.readlines():
            archivo_sin_espacios=linea.replace("  ","")
            analizar_token.analizar(archivo_sin_espacios,contador)
            contador +=1
        archivo.close()
        print('Datos Cargados')
    except Exception as e:
        pass

    for i in tokens:
        print(i)

    for j in errores:
        print(j)



menu()
