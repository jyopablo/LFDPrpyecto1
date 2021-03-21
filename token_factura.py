contadorfilas_factura=0
tokensfactura=[]
cantidadtokens_factura=0
No_factura=[]
Lexema_factura=[]
fila_factura=[]
columna_factura=[]
def analizar_orden(cadena,contador):
    global contadorfilas_factura
    global contadorcolumnas_factura

    if contador==0:
        contadorfilas_factura +=1
        DatosPersonales(cadena)
    else:
        contadorfilas_factura +=1
        Pedidos(cadena)

def DatosPersonales(cadena):
    global cantidadtokens_factura
    global contadorfilas_factura
    contadorcolumnas_factura=0
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
                contadorcolumnas_factura += 1
                if contador==1:
                    nombre=nombre+caracter
                elif contador==2:
                    nombre=nombre+caracter
                    contadorcolumnas_factura += 1
                    cantidadtokens_factura += 1
                    No_factura.append(str(cantidadtokens_factura))
                    Lexema_factura.append(nombre)
                    fila_factura.append(str(contadorfilas_factura))
                    columna_factura.append(str(contadorcolumnas_factura))
                    tokensfactura.append("cadena")
                elif contador==3:
                    nit=nit+caracter
                elif contador==4:
                    nit=nit+caracter
                    contadorcolumnas_factura += 1
                    cantidadtokens_factura += 1
                    No_factura.append(str(cantidadtokens_factura))
                    Lexema_factura.append(nit)
                    fila_factura.append(str(contadorfilas_factura))
                    columna_factura.append(str(contadorcolumnas_factura))
                    tokensfactura.append("cadena")
                elif contador==5:
                    direccion=direccion+caracter
                elif contador==6:
                    direccion=direccion+caracter
                    contadorcolumnas_factura += 1
                    cantidadtokens_factura += 1
                    No_factura.append(str(cantidadtokens_factura))
                    Lexema_factura.append(direccion)
                    fila_factura.append(str(contadorfilas_factura))
                    columna_factura.append(str(contadorcolumnas_factura))
                    tokensfactura.append("numero")
            elif caracter==",":
                contador2 += 1
                contadorcolumnas_factura += 1
            else:
                if contador==1:
                    if caracter==" ":
                        pass
                    else:
                        contadorcolumnas_factura += 1
                        nombre=nombre+caracter
                elif contador==3:
                    if caracter==" ":
                        pass
                    else:
                        contadorcolumnas_factura += 1
                        nit=nit+caracter
                elif contador==5:
                    if caracter==" ":
                        pass
                    else:
                        contadorcolumnas_factura += 1
                        direccion=direccion+caracter
                elif contador2==3:
                    if caracter=="%":
                        porcentaje=porcentaje+caracter
                        contadorcolumnas_factura += 1
                        cantidadtokens_factura += 1
                        No_factura.append(str(cantidadtokens_factura))
                        Lexema_factura.append(porcentaje)
                        fila_factura.append(str(contadorfilas_factura))
                        columna_factura.append(str(contadorcolumnas_factura))
                        tokensfactura.append("numero")
                    else:
                        if caracter== " ":
                            pass
                        else:
                            contadorcolumnas_factura += 1
                            porcentaje=porcentaje+caracter




def Pedidos(cadena):
    global cantidadtokens_factura
    global contadorfilas_factura
    contadorcolumnas_factura=0
    paso1=True
    paso2=False
    cantidad=""
    identificador=""
    x=len(cadena)
    total=x-1
    for i in cadena:
        caracter=i
        if paso1==True:
            if caracter == ",":
                contadorcolumnas_factura += 1
                paso1=False
                paso2=True
                cantidadtokens_factura += 1
                No_factura.append(str(cantidadtokens_factura))
                Lexema_factura.append(cantidad)
                fila_factura.append(str(contadorfilas_factura))
                columna_factura.append(str(contadorcolumnas_factura))
                tokensfactura.append("numero")
            else:
                if caracter==" ":
                    pass
                else:
                    contadorcolumnas_factura += 1
                    cantidad=cantidad+caracter
        elif paso2==True:
            if caracter==" ":
                pass
            elif contadorcolumnas_factura==total:
                contadorcolumnas_factura += 1
                cantidadtokens_factura += 1
                No_factura.append(str(cantidadtokens_factura))
                Lexema_factura.append(identificador)
                fila_factura.append(str(contadorfilas_factura))
                columna_factura.append(str(contadorcolumnas_factura))
                tokensfactura.append("identificador")
            else:
                contadorcolumnas_factura += 1
                identificador=identificador+caracter
