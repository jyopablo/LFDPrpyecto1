from analizador import *
from graphviz import Digraph
import os
letras=['B','C','D','E','F','G','H','I','J','K','L','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z']
seccion2=[]
def crear(graphviz):
    os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'
    dot=Digraph(comment='Restaurante')
    dot.node('A', titulo[0])
    contador=0
    x=len(total_datos)
    y=1
    for i in seccion:
        contador += 1
        posicion=contador
        dot.node(letras[contador] , i)
        dot.edges(['A'+letras[contador]])
        for i in range(0,x):
            if cantidad[i]==y:
                contador += 1
                dot.node(letras[contador] , total_datos[i])
                dot.edges([letras[posicion]+letras[contador]])
        y += 1


    dot.render('Graficos/Grafico'+str(graphviz)+'.pdf', view=True)
