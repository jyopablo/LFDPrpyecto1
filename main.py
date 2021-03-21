from tkinter import *
from analizador import *
from tkinter import filedialog
from analizar_token import *
from analizador_orden import*
from token_factura import*
import analizador as analizador
import analizador_orden as analizador_orden
import analizar_token as analizar_token
import html_menu as html_menu
import html_factura as html_factura
import html_tokens as html_tokens
import token_factura as token_factura
import html_token_factura as html_token_factura
import Graphviz as Graphviz

Factura=0
numero=0
numero2=0
graphviz=0
factura_lista=[0]
ruta1=""
ruta2=""
def menu():
    print('Lenguajes Formales de Programacion seccion')
    print('Juan Pablo Gonzalez Leal')
    print('Carne: 201901374')
    while True:
        print('1. Cargar menu')
        print('2. Cargar orden')
        print('3. Generar menu')
        print('4. Generar factura')
        print('5. Generar árbol')
        print('6. Salir')
        opcion=int(input('ELIJA UNA OPCION'))
        if opcion==1:
            cargar_menu()
            titulo.clear()
            seccion.clear()
            datos.clear()
            total_datos.clear()
            descripcionProducto.clear()
            cantidad.clear()
            precioProducto.clear()
            nombreProducto.clear()
            cantidadProductos=0

            tokens.clear()
            errores.clear()
            identificador_id.clear()
            columnas.clear()
            filas.clear()
            Total_tokens.clear()
            lexema.clear()
            No.clear()
            contador_filas=0
            cantidad_tokens=0
            cantidad_errores=0

        elif opcion ==2:
            cargar_orden()
            nombre_cliente.clear()
            nit_cliente.clear()
            direccion_cliente.clear()
            propina_cliente.clear()
            propina_clienteInt.clear()
            cantidad_comprada.clear()
            identificador_comprado.clear()

            No_factura.clear()
            Lexema_factura.clear()
            fila_factura.clear()
            columna_factura.clear()
            tokensfactura.clear()
            cantidadtokens_factura=0
            contadorfilas_factura=0

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
    global Factura
    Validacion_Tokens_Factura()
    contador=0
    archivo_orden=open(ruta2,encoding="utf8")
    for linea in archivo_orden.readlines():
        archivo_sin_espacios=linea.replace("  ","")
        analizador_orden.analizar_orden(archivo_sin_espacios,contador)
        contador +=1
    archivo_orden.close()
    Factura += 1
    html_factura.crear(Factura)

def generar_arbol():
    global graphviz
    graphviz += 1
    Graphviz.crear(graphviz)


def Validacion_Tokens():
    global numero
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

    numero += 1
    html_tokens.crear(numero)


def Validacion_Tokens_Factura():
    global numero2
    try:
        contador=0
        archivo=open(ruta2,encoding="utf8")
        for linea in archivo.readlines():
            archivo_sin_espacios=linea.replace("  ","")
            token_factura.analizar_orden(archivo_sin_espacios,contador)
            contador +=1
        archivo.close()
        print('Datos Cargados')
    except Exception as e:
        pass

    numero2 += 1
    html_token_factura.crear(numero2)
menu()
