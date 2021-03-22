from analizador_orden import*
from analizador import*
from analizar_token import*
import os
import datetime
ahora=datetime.datetime.now()

def crear(Factura):
    crear=open("Factura#"+str(Factura)+".html","w")
    crear.write("<html lang=\"es\">")
    crear.write("<html lang=\"es\" dir=\"ltr\"><head><meta charset=\"ISO-8859-1\"><link href=\"https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/css/bootstrap.min.css\" rel=\"stylesheet\" integrity=\"sha384-BmbxuPwQa2lc/FVzBcNJ7UAyJxM6wuqIj61tLrc4wSX0szH/Ev+nYRRuWlolflfl\" crossorigin=\"anonymous\">")
    crear.write("<title>Factura#"+str(Factura)+"</title></head><style>body{background:#8ba987 url('https://cronica.com.gt/wp-content/uploads/2019/09/1.jpg') no-repeat center center;background-size:100% 100%;}</style><body class=\"img-fluid\"><div class=\"container\"><div class=\"row justify-content-center  align-items-center vh-100\"><div class=\"card shadow p-3\" style=\"width: 50rem;\"><div class=\"card-body\"><h3 class=\"card-title\"><div class=\"row justify-content-center\">"+titulo[0]+"</div></h3>")
    crear.write("<h5 class=\"card-title\"><div class=\"row justify-content-center\">Factura No."+str(Factura)+"</div></h5>")
    crear.write("<h5 class=\"card-title\"><div class=\"row justify-content-center\">Fecha: "+str(ahora)+"</div></h5>")
    crear.write("<h5 class=\"card-subtitle mb-2 text-muted\">Datos Cliente</h5><h5 class=\"card-subtitle mb-2 text-muted\">Nombre: "+nombre_cliente[0]+"</h5><h5 class=\"card-subtitle mb-2 text-muted\">Nit: "+nit_cliente[0]+"</h5>")
    crear.write("<h5 class=\"card-subtitle mb-2 text-muted\"> Direccion: "+direccion_cliente[0]+"</h5><br><h5 class=\"card-subtitle mb-2 text-muted\">Descripcion</h5><table class=\"table\"><thead><tr>")
    crear.write("<th scope=\"col\">Cantidad</th><th scope=\"col\">Concepto</th><th scope=\"col\">Precio</th><th scope=\"col\">Total</th></tr></thead><tbody>")
    SUBTOTAL=0
    TOTAL=0
    x=len(identificador_id)
    y=len(cantidad_comprada)
    for i in range(0,y):
        crear.write("<tr><th scope=\"row\">"+str(cantidad_comprada[i])+"</th>")
        j=identificador_id.index(identificador_comprado[i].replace("\n",""))
        crear.write("<td>"+nombreProducto[j]+"</td>")
        crear.write("<td>"+str("{:.2f}".format(precioProducto[j]))+"</td>")
        TotalComprado=(precioProducto[j]*cantidad_comprada[i])
        crear.write("<td>"+str("{:.2f}".format(TotalComprado))+"</td></tr>")
        SUBTOTAL=SUBTOTAL+TotalComprado

    crear.write("</tbody><thead><tr><td scope=\"row\" colspan=\"3\">Sub total</td>")
    crear.write("<td scope=\"row\" colspan=\"2\">Q "+str("{:.2f}".format(SUBTOTAL))+"</td>")
    crear.write("<tr><td scope=\"row\" colspan=\"3\">Propina("+propina_cliente[0]+"%)</td>")
    propina=(propina_clienteInt[0]/100)*SUBTOTAL
    crear.write("<td scope=\"row\" colspan=\"1\">Q "+str("{:.2f}".format(propina))+"</td></tr></thead>")
    TOTAL=propina+SUBTOTAL
    crear.write("<thead><tr><th scope=\"col\" colspan=\"3\">Total</th>")
    crear.write("<th scope=\"col\" colspan=\"1\">"+str("{:.2f}".format(TOTAL))+"</th></tr></thead>")
    crear.write("</table></div></div></div></div></body></html>")
    crear.close()
    os.system("Factura#"+str(Factura)+".html")
    print('archivo creado')
