titulo=[]
seccion=[]
datos=[]
total_datos=[]
descripcionProducto=[]
cantidad=[]
precioProducto=[]
nombreProducto=[]
cantidadProductos=0
def analizar(cadena,contador):
    if contador==0:
        Titulo(cadena)

    inicial=cadena[0]
    if inicial=="'":
        global cantidadProductos
        cantidadProductos += 1
        Nombre_seccion(cadena)

    if inicial=="[":
        Opcion_menu(cadena)
        cantidad.append(cantidadProductos)


def Titulo(cadena):
    contador=0
    paso1=True
    paso2=False
    cajon=""
    cajon2=""
    error1=""
    for i in cadena:
        caracter=i
        if paso1==True:
            if caracter=="=":
                if cajon=="restaurante" or cajon=="RESTAURANTE" or cajon=="Restaurante":
                    paso1=False
                    paso2=True
                    cajon="Nombre restaurante = "
                else:
                    error1=("No existepalabra restaurante")
            else:
                cajon=cajon+caracter
        elif paso2==True:
            if caracter=="'":
                contador +=1
                if contador==2:
                    pass
                else:
                    error1=error1+"no contiene comillas"
            else:
                cajon2=cajon2+caracter
    titulo.append(cajon2)



def Nombre_seccion(cadena):
    contador=0
    cajon=""
    cajon2=""
    paso1=True
    paso2=False
    error2=""
    for i in cadena:
        caracter=i
        if paso1==True:
            if caracter=="'":
                contador += 1
                if contador==2:
                    paso1=False
                    paso2=True
            else:
                cajon=cajon+caracter
        elif paso2==True:
            if caracter==":" :
                cajon2="Nombre Seccion = "
            else:
                error2="No existe el caracter :"
    seccion.append(cajon)

def Opcion_menu(cadena):
    contador=0
    contador2=0
    paso1=False
    paso2=False
    paso3=False
    paso4=False
    paso5=False
    ultimo=""
    id=""
    nombre=""
    precio=""
    descripcion=""
    for i in cadena:
        caracter=i
        if caracter=="[":
             contador += 1
             paso1=True
        elif paso1==True:
            if caracter==";":
                paso1=False
                paso2=True
            else:
                id=id+caracter
        elif paso2==True:
            if caracter==";":
                paso2=False
                paso3=True
            else:
                if caracter=="'":
                    pass
                else:
                    nombre=nombre+caracter
        elif paso3==True:
            if caracter==";":
                x= "." in precio
                if ultimo==".":
                    precio=precio+"00"
                    paso3=False
                    paso4=True
                elif x==False:
                    precio=precio+".00"
                    paso3=False
                    paso4=True
                else:
                    paso3=False
                    paso4=True
            else:
                if caracter==" ":
                    pass
                else:
                    ultimo=caracter
                    precio=precio+caracter
        elif paso4==True:
            if caracter=="]":
                contador += 1
            else:
                if caracter=="'":
                    pass
                else:
                    descripcion=descripcion+caracter

    nombreProducto.append(nombre)
    precioProducto.append(float(precio))
    datos.append(nombre+"    Q"+precio)
    total_datos.append(nombre+"    Q"+precio+"\n"+descripcion)
    descripcionProducto.append(descripcion)
