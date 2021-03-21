from token_factura import*
def crear(Tokens):
    crear=open("TokensFactura#"+str(Tokens)+".html","w")
    crear.write("<html lang=\"es\">")
    crear.write("<head><meta charset=\"ISO-8859-1\"><link href=\"https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/css/bootstrap.min.css\" rel=\"stylesheet\" integrity=\"sha384-BmbxuPwQa2lc/FVzBcNJ7UAyJxM6wuqIj61tLrc4wSX0szH/Ev+nYRRuWlolflfl\" crossorigin=\"anonymous\"><title>Tokens#"+str(Tokens)+"</title></head><body>")
    crear.write("<div class=\"container\"><div class=\"row justify-content-center\"><div class=\"col-4\"><h1>Tabla Tokens# "+str(Tokens)+"</h1></div></div>")
    crear.write("<table class=\"table\"><thead><tr class=\"table-dark\"><th scope=\"col\">No</th><th scope=\"col\">Fila</th><th scope=\"col\">Columna</th><th scope=\"col\">Carácter</th><th scope=\"col\">Descripcion</th></tr></thead><tbody>")
    x=len(No_factura)
    for i in range(0,x):
        crear.write("<tr><th scope=\"row\">"+No_factura[i]+"</th><td>"+Lexema_factura[i]+"</td><td>"+fila_factura[i]+"</td><td>"+columna_factura[i]+"</td><td>"+tokensfactura[i]+"</td></tr>")
    crear.write("</table></div></body></html>")
    crear.close()
    print('archivo creado')
