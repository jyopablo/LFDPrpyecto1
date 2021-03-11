from analizador import *
def crear():
    crear=open(titulo[0].replace("\n","")+".html","w")
    crear.write("<html lang=\"es\">")
    crear.write("<head>")
    crear.write("<meta charset=\"ISO 8859-1\">")
    crear.write("<meta name=\"viewport\" content=\"width=, initial-scale=1.0\">")
    crear.write("<link rel=\"stylesheet\" href=\"https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css\" integrity=\"sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh\" crossorigin=\"anonymous\">")
    crear.write("<title>"+titulo[0]+"</title>")
    crear.write("</head>")
    crear.write("<body>")
    crear.write("<div class=\"container\"><div class=\"row justify-content-center\"><div class=\"col-4\"><h1>"+titulo[0]+"</h1></div></div>")
    x=len(datos)
    y=1
    for i in seccion:
        crear.write("<div class=\"row>\"><div class=\"col align-self-start\"><h3>"+i+"</h3></div></div><br>")
        for i in range(0,x):
            if cantidad[i]==y:
                crear.write("<div class=\"row>\"><div class=\"col align-self-start\"><h3>"+datos[i]+"</h3></div></div>")
                crear.write("<div class=\"row>\"><div class=\"col-md-9 offset-md-3\"><h4>"+descripcionProducto[i]+"</h4></div></div>")
        crear.write("<br>")
        crear.write("<hr>")
        y += 1
    crear.write("</div>")
    crear.write("<script src=\"https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js\" integrity=\"sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6\" crossorigin=\"anonymous\"></script>")
    crear.write("<script src=\"https://code.jquery.com/jquery-3.4.1.slim.min.js\" integrity=\"sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n\" crossorigin=\"anonymous\"></script>")
    crear.write("<script src=\"https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js\" integrity=\"sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo\" crossorigin=\"anonymous\"></script>")
    crear.write("</body>")
    crear.write("</html>")
    crear.close()
    print('archivo creado')
