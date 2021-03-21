nombre_cliente=[]
nit_cliente=[]
direccion_cliente=[]
propina_cliente=[]
propina_clienteInt=[]
cantidad_comprada=[]
identificador_comprado=[]

def analizar_orden(cadena,contador):
    if contador==0:
        DatosPersonales(cadena)
    else:
        Pedidos(cadena)

def DatosPersonales(cadena):
    paso1=True
    contador=0
    contador2=0
    nombre=""
    nit=""
    direccion=""
    porcentaje=""
    porcentaje_int=0
    for i in cadena:
        caracter=i
        if paso1==True:
            if caracter=="'":
                contador += 1
            elif caracter==",":
                contador2 += 1
            else:
                if contador==1:
                    nombre=nombre+caracter
                elif contador==3:
                    nit=nit+caracter
                elif contador==5:
                    direccion=direccion+caracter
                elif contador2==3:
                    if caracter=="%":
                        porcentaje_int=int(porcentaje)
                    else:
                        if caracter==" ":
                            pass
                        else:
                            porcentaje=porcentaje+caracter
    nombre_cliente.append(nombre)
    nit_cliente.append(nit)
    direccion_cliente.append(direccion)
    propina_cliente.append(porcentaje)
    propina_clienteInt.append(porcentaje_int)


def Pedidos(cadena):
    global posicion_contador
    paso1=True
    paso2=False
    cantidad=""
    identificador=""
    for i in cadena:
        caracter=i
        if paso1==True:
            if caracter == ",":
                cantidad_int=int(cantidad)
                paso1=False
                paso2=True
            else:
                if caracter==" ":
                    pass
                else:
                    cantidad=cantidad+caracter
        elif paso2==True:
            if caracter==" ":
                pass
            else:
                identificador=identificador+caracter

    cantidad_comprada.append(cantidad_int)
    identificador_comprado.append(identificador)
