import re
tokens=[]
errores=[]
identificador_id=[]
columnas=[]
filas=[]
Total_tokens=[]
lexema=[]
No=[]
contador_filas=0
cantidad_tokens=0
cantidad_errores=0
def analizar(cadena,contador):
    global contador_filas
    global cantidad_tokens
    if contador==0:
        contador_filas += 1
        Titulo(cadena)

    inicial=cadena[0]

    if inicial=="'":
        contador_filas += 1
        Nombre_seccion(cadena)

    if inicial=="[":
        contador_filas += 1
        Opcion_menu(cadena)


def Titulo(cadena):
    global contador_filas
    global cantidad_tokens
    global cantidad_errores
    contador_columnas=0
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
                    cantidad_tokens += 1
                    No.append(str(cantidad_tokens))
                    lexema.append("restaurante")
                    filas.append(str(contador_filas))
                    columnas.append(str(contador_columnas))
                    Total_tokens.append("Palabra Reservada")
                    tokens.append("No = "+str(cantidad_tokens)+", Lexema = restaurante, Fila = "+str(contador_filas)+", Columna = "+str(contador_columnas+1)+", Token = Palabra Reservada")
                    contador_columnas += 1
                else:
                    error1=("No existepalabra restaurante")
            else:
                if caracter=="r" or caracter=="e" or caracter=="s" or caracter=="t" or caracter=="a" or caracter=="u" or caracter=="n" or caracter=="t":
                     cajon=cajon+caracter
                     contador_columnas += 1
                elif caracter=="'":
                    contador_columnas += 1
                    cantidad_errores +=1
                    errores.append("No = "+str(cantidad_errores)+", Fila = "+str(contador_filas)+", Columna = "+str(contador_columnas)+", Caracter = '=', Descripcion = Caracter no Encontrado")
                    paso1=False
                    paso2=True
                    contador +=1
                    cajon2=cajon2+caracter
                else:
                    contador_columnas += 1
                    cantidad_errores +=1
                    errores.append("No = "+str(cantidad_errores)+", Fila = "+str(contador_filas)+", Columna = "+str(contador_columnas)+", Caracter = "+caracter+", Descripcion = Caracter Desconocido")
        elif paso2==True:
            if caracter=="'":
                contador +=1
                contador_columnas += 1
                cajon2=cajon2+caracter
                if contador==2:
                    cantidad_tokens += 1
                    No.append(str(cantidad_tokens))
                    lexema.append(cajon2)
                    filas.append(str(contador_filas))
                    columnas.append(str(contador_columnas))
                    Total_tokens.append("Cadena")
                    tokens.append("No = "+str(cantidad_tokens)+", Lexema = "+cajon2+", Fila = "+str(contador_filas)+", Columna = "+str(contador_columnas+1)+", Token = Cadena")
                    cajon2=""
                elif contador==3:
                    cantidad_errores += 1
                    errores.append("No = "+str(cantidad_errores)+", Fila = "+str(contador_filas)+", Columna = "+str(contador_columnas)+", Caracter = "+caracter+", Descripcion = Caracter Desconocido")
                else:
                    error1=error1+"no contiene comillas"
            elif contador == 1:
                cajon2=cajon2+caracter
                contador_columnas += 1
            elif contador == 0:
                contador_columnas += 1
                cantidad_errores += 1
                errores.append("No = "+str(cantidad_errores)+", Fila = "+str(contador_filas)+", Columna = "+str(contador_columnas)+", Caracter = ', Descripcion = Caracter no Encontrado")
                contador += 1


def Nombre_seccion(cadena):
    global contador_filas
    global cantidad_tokens
    contador_columnas=0
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
                contador_columnas += 1
                cajon=cajon+caracter
                if contador==2:
                    paso1=False
                    paso2=True
                    cantidad_tokens += 1
            else:
                contador_columnas += 1
                cajon=cajon+caracter
        elif paso2==True:
            if caracter==":" :
                contador_columnas += 1
                No.append(str(cantidad_tokens))
                lexema.append(cajon)
                filas.append(str(contador_filas))
                columnas.append(str(contador_columnas))
                Total_tokens.append("Cadena")
                tokens.append("No = "+str(cantidad_tokens)+", Lexema = "+cajon+", Fila = "+str(contador_filas)+", Columna = "+str(contador_columnas)+", Token = Cadena")
            else:
                error2="No existe el caracter :"


def Opcion_menu(cadena):
    global contador_filas
    global cantidad_tokens
    contador_columnas=0
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
             contador_columnas += 1
             contador += 1
             paso1=True
        elif paso1==True:
            if caracter==";":
                paso1=False
                paso2=True
                cantidad_tokens += 1
                contador_columnas += 1
                id=id.strip()
                tamaño_id=len(id)
                contador_columnas =contador_columnas+tamaño_id
                No.append(str(cantidad_tokens))
                lexema.append(id)
                filas.append(str(contador_filas))
                columnas.append(str(contador_columnas))
                Total_tokens.append("Identificador")
                tokens.append("No = "+str(cantidad_tokens)+", Lexema = "+id+", Fila = "+str(contador_filas)+", Columna = "+str(contador_columnas)+", Token = Identificador")
                identificador_id.append(id)
            else:
                id=id+caracter
        elif paso2==True:
            if caracter==";":
                paso2=False
                paso3=True
                cantidad_tokens += 1
                contador_columnas += 1
                nombre=nombre.strip()
                tamaño_nombre=len(nombre)
                contador_columnas =contador_columnas+tamaño_nombre
                No.append(str(cantidad_tokens))
                lexema.append(nombre)
                filas.append(str(contador_filas))
                columnas.append(str(contador_columnas))
                Total_tokens.append("Cadena")
                tokens.append("No = "+str(cantidad_tokens)+", Lexema = "+nombre+", Fila = "+str(contador_filas)+", Columna = "+str(contador_columnas)+", Token = Cadena")
            else:
                nombre=nombre+caracter
        elif paso3==True:
            if caracter==";":
                paso3=False
                paso4=True
                contador_columnas += 1
                cantidad_tokens += 1
                precio=precio.strip()
                tamaño_precio=len(precio)
                contador_columnas =contador_columnas+tamaño_precio
                No.append(str(cantidad_tokens))
                lexema.append(precio)
                filas.append(str(contador_filas))
                columnas.append(str(contador_columnas))
                Total_tokens.append("Numero")
                tokens.append("No = "+str(cantidad_tokens)+", Lexema = "+precio+", Fila = "+str(contador_filas)+", Columna = "+str(contador_columnas)+", Token = Numero")
            else:
                precio=precio+caracter
        elif paso4==True:
            if caracter=="]":
                contador += 1
                contador_columnas += 1
                cantidad_tokens += 1
                descripcion=descripcion.strip()
                tamaño_descripcion=len(precio)
                contador_columnas =contador_columnas+tamaño_descripcion
                No.append(str(cantidad_tokens))
                lexema.append(descripcion)
                filas.append(str(contador_filas))
                columnas.append(str(contador_columnas))
                Total_tokens.append("Cadena")
                tokens.append("No = "+str(cantidad_tokens)+", Lexema = "+descripcion+", Fila = "+str(contador_filas)+", Columna = "+str(contador_columnas)+", Token = Cadena")
            else:
                if caracter=="'":
                    contador_columnas += 1
                    descripcion=descripcion+caracter
                else:
                    descripcion=descripcion+caracter
