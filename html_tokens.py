from analizar_token import*
import os
def crear(Tokens):
    crear=open("TokensMenu#"+str(Tokens)+".html","w")
    crear.write("<html lang=\"es\">")
    crear.write("<head><meta charset=\"ISO-8859-1\"><link href=\"https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/css/bootstrap.min.css\" rel=\"stylesheet\" integrity=\"sha384-BmbxuPwQa2lc/FVzBcNJ7UAyJxM6wuqIj61tLrc4wSX0szH/Ev+nYRRuWlolflfl\" crossorigin=\"anonymous\"><title>Tokens#"+str(Tokens)+"</title></head><body>")
    crear.write("<div class=\"container\"><div class=\"row justify-content-center\"><div class=\"col-4\"><h1>Tabla Tokens# "+str(Tokens)+"</h1></div></div>")
    crear.write("<table class=\"table\"><thead><tr class=\"table-dark\"><th scope=\"col\">No</th><th scope=\"col\">Fila</th><th scope=\"col\">Columna</th><th scope=\"col\">Carácter</th><th scope=\"col\">Descripcion</th></tr></thead><tbody>")
    x=len(No)
    for i in range(0,x):
        crear.write("<tr><th scope=\"row\">"+No[i]+"</th><td>"+lexema[i]+"</td><td>"+filas[i]+"</td><td>"+columnas[i]+"</td><td>"+Total_tokens[i]+"</td></tr>")

    crear.write("</table></div></body></html>")
    crear.close()
    os.system("TokensMenu#"+str(Tokens)+".html")
    print('archivo creado')
